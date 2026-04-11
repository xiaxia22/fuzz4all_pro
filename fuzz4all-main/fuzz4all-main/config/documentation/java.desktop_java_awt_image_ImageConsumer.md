# Interface ImageConsumer

**Source:** `java.desktop\java\awt\image\ImageConsumer.html`

### Class Description

```java
public interface
ImageConsumer
```

The interface for objects expressing interest in image data through
the ImageProducer interfaces. When a consumer is added to an image
producer, the producer delivers all of the data about the image
using the method calls defined in this interface.

**All Known Implementing Classes:** AreaAveragingScaleFilter

,

BufferedImageFilter

,

CropImageFilter

,

GrayFilter

,

ImageFilter

,

PixelGrabber

,

ReplicateScaleFilter

,

RGBImageFilter

---

### Field Details

#### static final int RANDOMPIXELORDER

The pixels will be delivered in a random order. This tells the
ImageConsumer not to use any optimizations that depend on the
order of pixel delivery, which should be the default assumption
in the absence of any call to the setHints method.

**See Also:**
- setHints(int)

,

Constant Field Values

---

#### static final int TOPDOWNLEFTRIGHT

The pixels will be delivered in top-down, left-to-right order.

**See Also:**
- setHints(int)

,

Constant Field Values

---

#### static final int COMPLETESCANLINES

The pixels will be delivered in (multiples of) complete scanlines
at a time.

**See Also:**
- setHints(int)

,

Constant Field Values

---

#### static final int SINGLEPASS

The pixels will be delivered in a single pass. Each pixel will
appear in only one call to any of the setPixels methods. An
example of an image format which does not meet this criterion
is a progressive JPEG image which defines pixels in multiple
passes, each more refined than the previous.

**See Also:**
- setHints(int)

,

Constant Field Values

---

#### static final int SINGLEFRAME

The image contain a single static image. The pixels will be defined
in calls to the setPixels methods and then the imageComplete method
will be called with the STATICIMAGEDONE flag after which no more
image data will be delivered. An example of an image type which
would not meet these criteria would be the output of a video feed,
or the representation of a 3D rendering being manipulated
by the user. The end of each frame in those types of images will
be indicated by calling imageComplete with the SINGLEFRAMEDONE flag.

**See Also:**
- setHints(int)

,

imageComplete(int)

,

Constant Field Values

---

#### static final int IMAGEERROR

An error was encountered while producing the image.

**See Also:**
- imageComplete(int)

,

Constant Field Values

---

#### static final int SINGLEFRAMEDONE

One frame of the image is complete but there are more frames
to be delivered.

**See Also:**
- imageComplete(int)

,

Constant Field Values

---

#### static final int STATICIMAGEDONE

The image is complete and there are no more pixels or frames
to be delivered.

**See Also:**
- imageComplete(int)

,

Constant Field Values

---

#### static final int IMAGEABORTED

The image creation process was deliberately aborted.

**See Also:**
- imageComplete(int)

,

Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### void setDimensions​(int width,
int height)

The dimensions of the source image are reported using the
setDimensions method call.

**Parameters:**
- width

- the width of the source image
- height

- the height of the source image

---

#### void setProperties​(
Hashtable
<?,​?> props)

Sets the extensible list of properties associated with this image.

**Parameters:**
- props

- the list of properties to be associated with this
image

---

#### void setColorModel​(
ColorModel
model)

Sets the ColorModel object used for the majority of
the pixels reported using the setPixels method
calls. Note that each set of pixels delivered using setPixels
contains its own ColorModel object, so no assumption should
be made that this model will be the only one used in delivering
pixel values. A notable case where multiple ColorModel objects
may be seen is a filtered image when for each set of pixels
that it filters, the filter
determines whether the
pixels can be sent on untouched, using the original ColorModel,
or whether the pixels should be modified (filtered) and passed
on using a ColorModel more convenient for the filtering process.

**Parameters:**
- model

- the specified

ColorModel

**See Also:**
- ColorModel

---

#### void setHints​(int hintflags)

Sets the hints that the ImageConsumer uses to process the
pixels delivered by the ImageProducer.
The ImageProducer can deliver the pixels in any order, but
the ImageConsumer may be able to scale or convert the pixels
to the destination ColorModel more efficiently or with higher
quality if it knows some information about how the pixels will
be delivered up front. The setHints method should be called
before any calls to any of the setPixels methods with a bit mask
of hints about the manner in which the pixels will be delivered.
If the ImageProducer does not follow the guidelines for the
indicated hint, the results are undefined.

**Parameters:**
- hintflags

- a set of hints that the ImageConsumer uses to
process the pixels

---

#### void setPixels​(int x,
int y,
int w,
int h,

ColorModel
model,
byte[] pixels,
int off,
int scansize)

Delivers the pixels of the image with one or more calls
to this method. Each call specifies the location and
size of the rectangle of source pixels that are contained in
the array of pixels. The specified ColorModel object should
be used to convert the pixels into their corresponding color
and alpha components. Pixel (m,n) is stored in the pixels array
at index (n * scansize + m + off). The pixels delivered using
this method are all stored as bytes.

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
- ColorModel

---

#### void setPixels​(int x,
int y,
int w,
int h,

ColorModel
model,
int[] pixels,
int off,
int scansize)

The pixels of the image are delivered using one or more calls
to the setPixels method. Each call specifies the location and
size of the rectangle of source pixels that are contained in
the array of pixels. The specified ColorModel object should
be used to convert the pixels into their corresponding color
and alpha components. Pixel (m,n) is stored in the pixels array
at index (n * scansize + m + off). The pixels delivered using
this method are all stored as ints.
this method are all stored as ints.

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
- ColorModel

---

#### void imageComplete​(int status)

The imageComplete method is called when the ImageProducer is
finished delivering all of the pixels that the source image
contains, or when a single frame of a multi-frame animation has
been completed, or when an error in loading or producing the
image has occurred. The ImageConsumer should remove itself from the
list of consumers registered with the ImageProducer at this time,
unless it is interested in successive frames.

**Parameters:**
- status

- the status of image loading

**See Also:**
- ImageProducer.removeConsumer(java.awt.image.ImageConsumer)

---

### Additional Sections

#### Interface ImageConsumer

**All Known Implementing Classes:** AreaAveragingScaleFilter

,

BufferedImageFilter

,

CropImageFilter

,

GrayFilter

,

ImageFilter

,

PixelGrabber

,

ReplicateScaleFilter

,

RGBImageFilter

```java
public interface
ImageConsumer
```

The interface for objects expressing interest in image data through
the ImageProducer interfaces. When a consumer is added to an image
producer, the producer delivers all of the data about the image
using the method calls defined in this interface.

**See Also:** ImageProducer

public interface

ImageConsumer

The interface for objects expressing interest in image data through
the ImageProducer interfaces. When a consumer is added to an image
producer, the producer delivers all of the data about the image
using the method calls defined in this interface.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

COMPLETESCANLINES

The pixels will be delivered in (multiples of) complete scanlines
at a time.

static int

IMAGEABORTED

The image creation process was deliberately aborted.

static int

IMAGEERROR

An error was encountered while producing the image.

static int

RANDOMPIXELORDER

The pixels will be delivered in a random order.

static int

SINGLEFRAME

The image contain a single static image.

static int

SINGLEFRAMEDONE

One frame of the image is complete but there are more frames
to be delivered.

static int

SINGLEPASS

The pixels will be delivered in a single pass.

static int

STATICIMAGEDONE

The image is complete and there are no more pixels or frames
to be delivered.

static int

TOPDOWNLEFTRIGHT

The pixels will be delivered in top-down, left-to-right order.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

imageComplete

​(int status)

The imageComplete method is called when the ImageProducer is
finished delivering all of the pixels that the source image
contains, or when a single frame of a multi-frame animation has
been completed, or when an error in loading or producing the
image has occurred.

void

setColorModel

​(

ColorModel

model)

Sets the ColorModel object used for the majority of
the pixels reported using the setPixels method
calls.

void

setDimensions

​(int width,
int height)

The dimensions of the source image are reported using the
setDimensions method call.

void

setHints

​(int hintflags)

Sets the hints that the ImageConsumer uses to process the
pixels delivered by the ImageProducer.

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

Delivers the pixels of the image with one or more calls
to this method.

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

The pixels of the image are delivered using one or more calls
to the setPixels method.

void

setProperties

​(

Hashtable

<?,​?> props)

Sets the extensible list of properties associated with this image.

Field Summary

Fields

Modifier and Type

Field

Description

static int

COMPLETESCANLINES

The pixels will be delivered in (multiples of) complete scanlines
at a time.

static int

IMAGEABORTED

The image creation process was deliberately aborted.

static int

IMAGEERROR

An error was encountered while producing the image.

static int

RANDOMPIXELORDER

The pixels will be delivered in a random order.

static int

SINGLEFRAME

The image contain a single static image.

static int

SINGLEFRAMEDONE

One frame of the image is complete but there are more frames
to be delivered.

static int

SINGLEPASS

The pixels will be delivered in a single pass.

static int

STATICIMAGEDONE

The image is complete and there are no more pixels or frames
to be delivered.

static int

TOPDOWNLEFTRIGHT

The pixels will be delivered in top-down, left-to-right order.

---

#### Field Summary

The pixels will be delivered in (multiples of) complete scanlines
at a time.

The image creation process was deliberately aborted.

An error was encountered while producing the image.

The pixels will be delivered in a random order.

The image contain a single static image.

One frame of the image is complete but there are more frames
to be delivered.

The pixels will be delivered in a single pass.

The image is complete and there are no more pixels or frames
to be delivered.

The pixels will be delivered in top-down, left-to-right order.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

imageComplete

​(int status)

The imageComplete method is called when the ImageProducer is
finished delivering all of the pixels that the source image
contains, or when a single frame of a multi-frame animation has
been completed, or when an error in loading or producing the
image has occurred.

void

setColorModel

​(

ColorModel

model)

Sets the ColorModel object used for the majority of
the pixels reported using the setPixels method
calls.

void

setDimensions

​(int width,
int height)

The dimensions of the source image are reported using the
setDimensions method call.

void

setHints

​(int hintflags)

Sets the hints that the ImageConsumer uses to process the
pixels delivered by the ImageProducer.

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

Delivers the pixels of the image with one or more calls
to this method.

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

The pixels of the image are delivered using one or more calls
to the setPixels method.

void

setProperties

​(

Hashtable

<?,​?> props)

Sets the extensible list of properties associated with this image.

---

#### Method Summary

The imageComplete method is called when the ImageProducer is
finished delivering all of the pixels that the source image
contains, or when a single frame of a multi-frame animation has
been completed, or when an error in loading or producing the
image has occurred.

Sets the ColorModel object used for the majority of
the pixels reported using the setPixels method
calls.

The dimensions of the source image are reported using the
setDimensions method call.

Sets the hints that the ImageConsumer uses to process the
pixels delivered by the ImageProducer.

Delivers the pixels of the image with one or more calls
to this method.

The pixels of the image are delivered using one or more calls
to the setPixels method.

Sets the extensible list of properties associated with this image.

============ FIELD DETAIL ===========

- Field Detail

- RANDOMPIXELORDER

```java
static final int RANDOMPIXELORDER
```

The pixels will be delivered in a random order. This tells the
ImageConsumer not to use any optimizations that depend on the
order of pixel delivery, which should be the default assumption
in the absence of any call to the setHints method.

**See Also:** setHints(int)

,

Constant Field Values

- TOPDOWNLEFTRIGHT

```java
static final int TOPDOWNLEFTRIGHT
```

The pixels will be delivered in top-down, left-to-right order.

**See Also:** setHints(int)

,

Constant Field Values

- COMPLETESCANLINES

```java
static final int COMPLETESCANLINES
```

The pixels will be delivered in (multiples of) complete scanlines
at a time.

**See Also:** setHints(int)

,

Constant Field Values

- SINGLEPASS

```java
static final int SINGLEPASS
```

The pixels will be delivered in a single pass. Each pixel will
appear in only one call to any of the setPixels methods. An
example of an image format which does not meet this criterion
is a progressive JPEG image which defines pixels in multiple
passes, each more refined than the previous.

**See Also:** setHints(int)

,

Constant Field Values

- SINGLEFRAME

```java
static final int SINGLEFRAME
```

The image contain a single static image. The pixels will be defined
in calls to the setPixels methods and then the imageComplete method
will be called with the STATICIMAGEDONE flag after which no more
image data will be delivered. An example of an image type which
would not meet these criteria would be the output of a video feed,
or the representation of a 3D rendering being manipulated
by the user. The end of each frame in those types of images will
be indicated by calling imageComplete with the SINGLEFRAMEDONE flag.

**See Also:** setHints(int)

,

imageComplete(int)

,

Constant Field Values

- IMAGEERROR

```java
static final int IMAGEERROR
```

An error was encountered while producing the image.

**See Also:** imageComplete(int)

,

Constant Field Values

- SINGLEFRAMEDONE

```java
static final int SINGLEFRAMEDONE
```

One frame of the image is complete but there are more frames
to be delivered.

**See Also:** imageComplete(int)

,

Constant Field Values

- STATICIMAGEDONE

```java
static final int STATICIMAGEDONE
```

The image is complete and there are no more pixels or frames
to be delivered.

**See Also:** imageComplete(int)

,

Constant Field Values

- IMAGEABORTED

```java
static final int IMAGEABORTED
```

The image creation process was deliberately aborted.

**See Also:** imageComplete(int)

,

Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- setDimensions

```java
void setDimensions​(int width,
int height)
```

The dimensions of the source image are reported using the
setDimensions method call.

**Parameters:** width

- the width of the source image
**Parameters:** height

- the height of the source image

- setProperties

```java
void setProperties​(
Hashtable
<?,​?> props)
```

Sets the extensible list of properties associated with this image.

**Parameters:** props

- the list of properties to be associated with this
image

- setColorModel

```java
void setColorModel​(
ColorModel
model)
```

Sets the ColorModel object used for the majority of
the pixels reported using the setPixels method
calls. Note that each set of pixels delivered using setPixels
contains its own ColorModel object, so no assumption should
be made that this model will be the only one used in delivering
pixel values. A notable case where multiple ColorModel objects
may be seen is a filtered image when for each set of pixels
that it filters, the filter
determines whether the
pixels can be sent on untouched, using the original ColorModel,
or whether the pixels should be modified (filtered) and passed
on using a ColorModel more convenient for the filtering process.

**Parameters:** model

- the specified

ColorModel
**See Also:** ColorModel

- setHints

```java
void setHints​(int hintflags)
```

Sets the hints that the ImageConsumer uses to process the
pixels delivered by the ImageProducer.
The ImageProducer can deliver the pixels in any order, but
the ImageConsumer may be able to scale or convert the pixels
to the destination ColorModel more efficiently or with higher
quality if it knows some information about how the pixels will
be delivered up front. The setHints method should be called
before any calls to any of the setPixels methods with a bit mask
of hints about the manner in which the pixels will be delivered.
If the ImageProducer does not follow the guidelines for the
indicated hint, the results are undefined.

**Parameters:** hintflags

- a set of hints that the ImageConsumer uses to
process the pixels

- setPixels

```java
void setPixels​(int x,
int y,
int w,
int h,

ColorModel
model,
byte[] pixels,
int off,
int scansize)
```

Delivers the pixels of the image with one or more calls
to this method. Each call specifies the location and
size of the rectangle of source pixels that are contained in
the array of pixels. The specified ColorModel object should
be used to convert the pixels into their corresponding color
and alpha components. Pixel (m,n) is stored in the pixels array
at index (n * scansize + m + off). The pixels delivered using
this method are all stored as bytes.

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
**See Also:** ColorModel

- setPixels

```java
void setPixels​(int x,
int y,
int w,
int h,

ColorModel
model,
int[] pixels,
int off,
int scansize)
```

The pixels of the image are delivered using one or more calls
to the setPixels method. Each call specifies the location and
size of the rectangle of source pixels that are contained in
the array of pixels. The specified ColorModel object should
be used to convert the pixels into their corresponding color
and alpha components. Pixel (m,n) is stored in the pixels array
at index (n * scansize + m + off). The pixels delivered using
this method are all stored as ints.
this method are all stored as ints.

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
**See Also:** ColorModel

- imageComplete

```java
void imageComplete​(int status)
```

The imageComplete method is called when the ImageProducer is
finished delivering all of the pixels that the source image
contains, or when a single frame of a multi-frame animation has
been completed, or when an error in loading or producing the
image has occurred. The ImageConsumer should remove itself from the
list of consumers registered with the ImageProducer at this time,
unless it is interested in successive frames.

**Parameters:** status

- the status of image loading
**See Also:** ImageProducer.removeConsumer(java.awt.image.ImageConsumer)

Field Detail

- RANDOMPIXELORDER

```java
static final int RANDOMPIXELORDER
```

The pixels will be delivered in a random order. This tells the
ImageConsumer not to use any optimizations that depend on the
order of pixel delivery, which should be the default assumption
in the absence of any call to the setHints method.

**See Also:** setHints(int)

,

Constant Field Values

- TOPDOWNLEFTRIGHT

```java
static final int TOPDOWNLEFTRIGHT
```

The pixels will be delivered in top-down, left-to-right order.

**See Also:** setHints(int)

,

Constant Field Values

- COMPLETESCANLINES

```java
static final int COMPLETESCANLINES
```

The pixels will be delivered in (multiples of) complete scanlines
at a time.

**See Also:** setHints(int)

,

Constant Field Values

- SINGLEPASS

```java
static final int SINGLEPASS
```

The pixels will be delivered in a single pass. Each pixel will
appear in only one call to any of the setPixels methods. An
example of an image format which does not meet this criterion
is a progressive JPEG image which defines pixels in multiple
passes, each more refined than the previous.

**See Also:** setHints(int)

,

Constant Field Values

- SINGLEFRAME

```java
static final int SINGLEFRAME
```

The image contain a single static image. The pixels will be defined
in calls to the setPixels methods and then the imageComplete method
will be called with the STATICIMAGEDONE flag after which no more
image data will be delivered. An example of an image type which
would not meet these criteria would be the output of a video feed,
or the representation of a 3D rendering being manipulated
by the user. The end of each frame in those types of images will
be indicated by calling imageComplete with the SINGLEFRAMEDONE flag.

**See Also:** setHints(int)

,

imageComplete(int)

,

Constant Field Values

- IMAGEERROR

```java
static final int IMAGEERROR
```

An error was encountered while producing the image.

**See Also:** imageComplete(int)

,

Constant Field Values

- SINGLEFRAMEDONE

```java
static final int SINGLEFRAMEDONE
```

One frame of the image is complete but there are more frames
to be delivered.

**See Also:** imageComplete(int)

,

Constant Field Values

- STATICIMAGEDONE

```java
static final int STATICIMAGEDONE
```

The image is complete and there are no more pixels or frames
to be delivered.

**See Also:** imageComplete(int)

,

Constant Field Values

- IMAGEABORTED

```java
static final int IMAGEABORTED
```

The image creation process was deliberately aborted.

**See Also:** imageComplete(int)

,

Constant Field Values

---

#### Field Detail

RANDOMPIXELORDER

```java
static final int RANDOMPIXELORDER
```

The pixels will be delivered in a random order. This tells the
ImageConsumer not to use any optimizations that depend on the
order of pixel delivery, which should be the default assumption
in the absence of any call to the setHints method.

**See Also:** setHints(int)

,

Constant Field Values

---

#### RANDOMPIXELORDER

static final int RANDOMPIXELORDER

The pixels will be delivered in a random order. This tells the
ImageConsumer not to use any optimizations that depend on the
order of pixel delivery, which should be the default assumption
in the absence of any call to the setHints method.

TOPDOWNLEFTRIGHT

```java
static final int TOPDOWNLEFTRIGHT
```

The pixels will be delivered in top-down, left-to-right order.

**See Also:** setHints(int)

,

Constant Field Values

---

#### TOPDOWNLEFTRIGHT

static final int TOPDOWNLEFTRIGHT

The pixels will be delivered in top-down, left-to-right order.

COMPLETESCANLINES

```java
static final int COMPLETESCANLINES
```

The pixels will be delivered in (multiples of) complete scanlines
at a time.

**See Also:** setHints(int)

,

Constant Field Values

---

#### COMPLETESCANLINES

static final int COMPLETESCANLINES

The pixels will be delivered in (multiples of) complete scanlines
at a time.

SINGLEPASS

```java
static final int SINGLEPASS
```

The pixels will be delivered in a single pass. Each pixel will
appear in only one call to any of the setPixels methods. An
example of an image format which does not meet this criterion
is a progressive JPEG image which defines pixels in multiple
passes, each more refined than the previous.

**See Also:** setHints(int)

,

Constant Field Values

---

#### SINGLEPASS

static final int SINGLEPASS

The pixels will be delivered in a single pass. Each pixel will
appear in only one call to any of the setPixels methods. An
example of an image format which does not meet this criterion
is a progressive JPEG image which defines pixels in multiple
passes, each more refined than the previous.

SINGLEFRAME

```java
static final int SINGLEFRAME
```

The image contain a single static image. The pixels will be defined
in calls to the setPixels methods and then the imageComplete method
will be called with the STATICIMAGEDONE flag after which no more
image data will be delivered. An example of an image type which
would not meet these criteria would be the output of a video feed,
or the representation of a 3D rendering being manipulated
by the user. The end of each frame in those types of images will
be indicated by calling imageComplete with the SINGLEFRAMEDONE flag.

**See Also:** setHints(int)

,

imageComplete(int)

,

Constant Field Values

---

#### SINGLEFRAME

static final int SINGLEFRAME

The image contain a single static image. The pixels will be defined
in calls to the setPixels methods and then the imageComplete method
will be called with the STATICIMAGEDONE flag after which no more
image data will be delivered. An example of an image type which
would not meet these criteria would be the output of a video feed,
or the representation of a 3D rendering being manipulated
by the user. The end of each frame in those types of images will
be indicated by calling imageComplete with the SINGLEFRAMEDONE flag.

IMAGEERROR

```java
static final int IMAGEERROR
```

An error was encountered while producing the image.

**See Also:** imageComplete(int)

,

Constant Field Values

---

#### IMAGEERROR

static final int IMAGEERROR

An error was encountered while producing the image.

SINGLEFRAMEDONE

```java
static final int SINGLEFRAMEDONE
```

One frame of the image is complete but there are more frames
to be delivered.

**See Also:** imageComplete(int)

,

Constant Field Values

---

#### SINGLEFRAMEDONE

static final int SINGLEFRAMEDONE

One frame of the image is complete but there are more frames
to be delivered.

STATICIMAGEDONE

```java
static final int STATICIMAGEDONE
```

The image is complete and there are no more pixels or frames
to be delivered.

**See Also:** imageComplete(int)

,

Constant Field Values

---

#### STATICIMAGEDONE

static final int STATICIMAGEDONE

The image is complete and there are no more pixels or frames
to be delivered.

IMAGEABORTED

```java
static final int IMAGEABORTED
```

The image creation process was deliberately aborted.

**See Also:** imageComplete(int)

,

Constant Field Values

---

#### IMAGEABORTED

static final int IMAGEABORTED

The image creation process was deliberately aborted.

Method Detail

- setDimensions

```java
void setDimensions​(int width,
int height)
```

The dimensions of the source image are reported using the
setDimensions method call.

**Parameters:** width

- the width of the source image
**Parameters:** height

- the height of the source image

- setProperties

```java
void setProperties​(
Hashtable
<?,​?> props)
```

Sets the extensible list of properties associated with this image.

**Parameters:** props

- the list of properties to be associated with this
image

- setColorModel

```java
void setColorModel​(
ColorModel
model)
```

Sets the ColorModel object used for the majority of
the pixels reported using the setPixels method
calls. Note that each set of pixels delivered using setPixels
contains its own ColorModel object, so no assumption should
be made that this model will be the only one used in delivering
pixel values. A notable case where multiple ColorModel objects
may be seen is a filtered image when for each set of pixels
that it filters, the filter
determines whether the
pixels can be sent on untouched, using the original ColorModel,
or whether the pixels should be modified (filtered) and passed
on using a ColorModel more convenient for the filtering process.

**Parameters:** model

- the specified

ColorModel
**See Also:** ColorModel

- setHints

```java
void setHints​(int hintflags)
```

Sets the hints that the ImageConsumer uses to process the
pixels delivered by the ImageProducer.
The ImageProducer can deliver the pixels in any order, but
the ImageConsumer may be able to scale or convert the pixels
to the destination ColorModel more efficiently or with higher
quality if it knows some information about how the pixels will
be delivered up front. The setHints method should be called
before any calls to any of the setPixels methods with a bit mask
of hints about the manner in which the pixels will be delivered.
If the ImageProducer does not follow the guidelines for the
indicated hint, the results are undefined.

**Parameters:** hintflags

- a set of hints that the ImageConsumer uses to
process the pixels

- setPixels

```java
void setPixels​(int x,
int y,
int w,
int h,

ColorModel
model,
byte[] pixels,
int off,
int scansize)
```

Delivers the pixels of the image with one or more calls
to this method. Each call specifies the location and
size of the rectangle of source pixels that are contained in
the array of pixels. The specified ColorModel object should
be used to convert the pixels into their corresponding color
and alpha components. Pixel (m,n) is stored in the pixels array
at index (n * scansize + m + off). The pixels delivered using
this method are all stored as bytes.

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
**See Also:** ColorModel

- setPixels

```java
void setPixels​(int x,
int y,
int w,
int h,

ColorModel
model,
int[] pixels,
int off,
int scansize)
```

The pixels of the image are delivered using one or more calls
to the setPixels method. Each call specifies the location and
size of the rectangle of source pixels that are contained in
the array of pixels. The specified ColorModel object should
be used to convert the pixels into their corresponding color
and alpha components. Pixel (m,n) is stored in the pixels array
at index (n * scansize + m + off). The pixels delivered using
this method are all stored as ints.
this method are all stored as ints.

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
**See Also:** ColorModel

- imageComplete

```java
void imageComplete​(int status)
```

The imageComplete method is called when the ImageProducer is
finished delivering all of the pixels that the source image
contains, or when a single frame of a multi-frame animation has
been completed, or when an error in loading or producing the
image has occurred. The ImageConsumer should remove itself from the
list of consumers registered with the ImageProducer at this time,
unless it is interested in successive frames.

**Parameters:** status

- the status of image loading
**See Also:** ImageProducer.removeConsumer(java.awt.image.ImageConsumer)

---

#### Method Detail

setDimensions

```java
void setDimensions​(int width,
int height)
```

The dimensions of the source image are reported using the
setDimensions method call.

**Parameters:** width

- the width of the source image
**Parameters:** height

- the height of the source image

---

#### setDimensions

void setDimensions​(int width,
int height)

The dimensions of the source image are reported using the
setDimensions method call.

setProperties

```java
void setProperties​(
Hashtable
<?,​?> props)
```

Sets the extensible list of properties associated with this image.

**Parameters:** props

- the list of properties to be associated with this
image

---

#### setProperties

void setProperties​(

Hashtable

<?,​?> props)

Sets the extensible list of properties associated with this image.

setColorModel

```java
void setColorModel​(
ColorModel
model)
```

Sets the ColorModel object used for the majority of
the pixels reported using the setPixels method
calls. Note that each set of pixels delivered using setPixels
contains its own ColorModel object, so no assumption should
be made that this model will be the only one used in delivering
pixel values. A notable case where multiple ColorModel objects
may be seen is a filtered image when for each set of pixels
that it filters, the filter
determines whether the
pixels can be sent on untouched, using the original ColorModel,
or whether the pixels should be modified (filtered) and passed
on using a ColorModel more convenient for the filtering process.

**Parameters:** model

- the specified

ColorModel
**See Also:** ColorModel

---

#### setColorModel

void setColorModel​(

ColorModel

model)

Sets the ColorModel object used for the majority of
the pixels reported using the setPixels method
calls. Note that each set of pixels delivered using setPixels
contains its own ColorModel object, so no assumption should
be made that this model will be the only one used in delivering
pixel values. A notable case where multiple ColorModel objects
may be seen is a filtered image when for each set of pixels
that it filters, the filter
determines whether the
pixels can be sent on untouched, using the original ColorModel,
or whether the pixels should be modified (filtered) and passed
on using a ColorModel more convenient for the filtering process.

setHints

```java
void setHints​(int hintflags)
```

Sets the hints that the ImageConsumer uses to process the
pixels delivered by the ImageProducer.
The ImageProducer can deliver the pixels in any order, but
the ImageConsumer may be able to scale or convert the pixels
to the destination ColorModel more efficiently or with higher
quality if it knows some information about how the pixels will
be delivered up front. The setHints method should be called
before any calls to any of the setPixels methods with a bit mask
of hints about the manner in which the pixels will be delivered.
If the ImageProducer does not follow the guidelines for the
indicated hint, the results are undefined.

**Parameters:** hintflags

- a set of hints that the ImageConsumer uses to
process the pixels

---

#### setHints

void setHints​(int hintflags)

Sets the hints that the ImageConsumer uses to process the
pixels delivered by the ImageProducer.
The ImageProducer can deliver the pixels in any order, but
the ImageConsumer may be able to scale or convert the pixels
to the destination ColorModel more efficiently or with higher
quality if it knows some information about how the pixels will
be delivered up front. The setHints method should be called
before any calls to any of the setPixels methods with a bit mask
of hints about the manner in which the pixels will be delivered.
If the ImageProducer does not follow the guidelines for the
indicated hint, the results are undefined.

setPixels

```java
void setPixels​(int x,
int y,
int w,
int h,

ColorModel
model,
byte[] pixels,
int off,
int scansize)
```

Delivers the pixels of the image with one or more calls
to this method. Each call specifies the location and
size of the rectangle of source pixels that are contained in
the array of pixels. The specified ColorModel object should
be used to convert the pixels into their corresponding color
and alpha components. Pixel (m,n) is stored in the pixels array
at index (n * scansize + m + off). The pixels delivered using
this method are all stored as bytes.

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
**See Also:** ColorModel

---

#### setPixels

void setPixels​(int x,
int y,
int w,
int h,

ColorModel

model,
byte[] pixels,
int off,
int scansize)

Delivers the pixels of the image with one or more calls
to this method. Each call specifies the location and
size of the rectangle of source pixels that are contained in
the array of pixels. The specified ColorModel object should
be used to convert the pixels into their corresponding color
and alpha components. Pixel (m,n) is stored in the pixels array
at index (n * scansize + m + off). The pixels delivered using
this method are all stored as bytes.

setPixels

```java
void setPixels​(int x,
int y,
int w,
int h,

ColorModel
model,
int[] pixels,
int off,
int scansize)
```

The pixels of the image are delivered using one or more calls
to the setPixels method. Each call specifies the location and
size of the rectangle of source pixels that are contained in
the array of pixels. The specified ColorModel object should
be used to convert the pixels into their corresponding color
and alpha components. Pixel (m,n) is stored in the pixels array
at index (n * scansize + m + off). The pixels delivered using
this method are all stored as ints.
this method are all stored as ints.

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
**See Also:** ColorModel

---

#### setPixels

void setPixels​(int x,
int y,
int w,
int h,

ColorModel

model,
int[] pixels,
int off,
int scansize)

The pixels of the image are delivered using one or more calls
to the setPixels method. Each call specifies the location and
size of the rectangle of source pixels that are contained in
the array of pixels. The specified ColorModel object should
be used to convert the pixels into their corresponding color
and alpha components. Pixel (m,n) is stored in the pixels array
at index (n * scansize + m + off). The pixels delivered using
this method are all stored as ints.
this method are all stored as ints.

imageComplete

```java
void imageComplete​(int status)
```

The imageComplete method is called when the ImageProducer is
finished delivering all of the pixels that the source image
contains, or when a single frame of a multi-frame animation has
been completed, or when an error in loading or producing the
image has occurred. The ImageConsumer should remove itself from the
list of consumers registered with the ImageProducer at this time,
unless it is interested in successive frames.

**Parameters:** status

- the status of image loading
**See Also:** ImageProducer.removeConsumer(java.awt.image.ImageConsumer)

---

#### imageComplete

void imageComplete​(int status)

The imageComplete method is called when the ImageProducer is
finished delivering all of the pixels that the source image
contains, or when a single frame of a multi-frame animation has
been completed, or when an error in loading or producing the
image has occurred. The ImageConsumer should remove itself from the
list of consumers registered with the ImageProducer at this time,
unless it is interested in successive frames.

---

