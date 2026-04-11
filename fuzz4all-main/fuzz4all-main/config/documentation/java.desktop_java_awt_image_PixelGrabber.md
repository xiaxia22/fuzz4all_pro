# Class PixelGrabber

**Source:** `java.desktop\java\awt\image\PixelGrabber.html`

### Class Description

```java
public class
PixelGrabber

extends
Object

implements
ImageConsumer
```

The PixelGrabber class implements an ImageConsumer which can be attached
to an Image or ImageProducer object to retrieve a subset of the pixels
in that image. Here is an example:

```java
public void handlesinglepixel(int x, int y, int pixel) {
int alpha = (pixel >> 24) & 0xff;
int red = (pixel >> 16) & 0xff;
int green = (pixel >> 8) & 0xff;
int blue = (pixel ) & 0xff;
// Deal with the pixel as necessary...
}

public void handlepixels(Image img, int x, int y, int w, int h) {
int[] pixels = new int[w * h];
PixelGrabber pg = new PixelGrabber(img, x, y, w, h, pixels, 0, w);
try {
pg.grabPixels();
} catch (InterruptedException e) {
System.err.println("interrupted waiting for pixels!");
return;
}
if ((pg.getStatus() & ImageObserver.ABORT) != 0) {
System.err.println("image fetch aborted or errored");
return;
}
for (int j = 0; j < h; j++) {
for (int i = 0; i < w; i++) {
handlesinglepixel(x+i, y+j, pixels[j * w + i]);
}
}
}
```

**All Implemented Interfaces:** ImageConsumer

---

### Field Details

*No entries found.*

### Constructor Details

#### public PixelGrabber​(
Image
img,
int x,
int y,
int w,
int h,
int[] pix,
int off,
int scansize)

Create a PixelGrabber object to grab the (x, y, w, h) rectangular
section of pixels from the specified image into the given array.
The pixels are stored into the array in the default RGB ColorModel.
The RGB data for pixel (i, j) where (i, j) is inside the rectangle
(x, y, w, h) is stored in the array at

pix[(j - y) * scansize + (i - x) + off]

.

**Parameters:**
- img

- the image to retrieve pixels from
- x

- the x coordinate of the upper left corner of the rectangle
of pixels to retrieve from the image, relative to the default
(unscaled) size of the image
- y

- the y coordinate of the upper left corner of the rectangle
of pixels to retrieve from the image
- w

- the width of the rectangle of pixels to retrieve
- h

- the height of the rectangle of pixels to retrieve
- pix

- the array of integers which are to be used to hold the
RGB pixels retrieved from the image
- off

- the offset into the array of where to store the first pixel
- scansize

- the distance from one row of pixels to the next in
the array

**See Also:**
- ColorModel.getRGBdefault()

---

#### public PixelGrabber​(
ImageProducer
ip,
int x,
int y,
int w,
int h,
int[] pix,
int off,
int scansize)

Create a PixelGrabber object to grab the (x, y, w, h) rectangular
section of pixels from the image produced by the specified
ImageProducer into the given array.
The pixels are stored into the array in the default RGB ColorModel.
The RGB data for pixel (i, j) where (i, j) is inside the rectangle
(x, y, w, h) is stored in the array at

pix[(j - y) * scansize + (i - x) + off]

.

**Parameters:**
- ip

- the

ImageProducer

that produces the
image from which to retrieve pixels
- x

- the x coordinate of the upper left corner of the rectangle
of pixels to retrieve from the image, relative to the default
(unscaled) size of the image
- y

- the y coordinate of the upper left corner of the rectangle
of pixels to retrieve from the image
- w

- the width of the rectangle of pixels to retrieve
- h

- the height of the rectangle of pixels to retrieve
- pix

- the array of integers which are to be used to hold the
RGB pixels retrieved from the image
- off

- the offset into the array of where to store the first pixel
- scansize

- the distance from one row of pixels to the next in
the array

**See Also:**
- ColorModel.getRGBdefault()

---

#### public PixelGrabber​(
Image
img,
int x,
int y,
int w,
int h,
boolean forceRGB)

Create a PixelGrabber object to grab the (x, y, w, h) rectangular
section of pixels from the specified image. The pixels are
accumulated in the original ColorModel if the same ColorModel
is used for every call to setPixels, otherwise the pixels are
accumulated in the default RGB ColorModel. If the forceRGB
parameter is true, then the pixels will be accumulated in the
default RGB ColorModel anyway. A buffer is allocated by the
PixelGrabber to hold the pixels in either case. If

(w < 0)

or

(h < 0)

, then they will default to the remaining width and
height of the source data when that information is delivered.

**Parameters:**
- img

- the image to retrieve the image data from
- x

- the x coordinate of the upper left corner of the rectangle
of pixels to retrieve from the image, relative to the default
(unscaled) size of the image
- y

- the y coordinate of the upper left corner of the rectangle
of pixels to retrieve from the image
- w

- the width of the rectangle of pixels to retrieve
- h

- the height of the rectangle of pixels to retrieve
- forceRGB

- true if the pixels should always be converted to
the default RGB ColorModel

---

### Method Details

#### public void startGrabbing()

Request the PixelGrabber to start fetching the pixels.

---

#### public void abortGrabbing()

Request the PixelGrabber to abort the image fetch.

---

#### public boolean grabPixels()
throws
InterruptedException

Request the Image or ImageProducer to start delivering pixels and
wait for all of the pixels in the rectangle of interest to be
delivered.

**Returns:**
- true if the pixels were successfully grabbed, false on
abort, error or timeout

**Throws:**
- InterruptedException

- Another thread has interrupted this thread.

---

#### public boolean grabPixels​(long ms)
throws
InterruptedException

Request the Image or ImageProducer to start delivering pixels and
wait for all of the pixels in the rectangle of interest to be
delivered or until the specified timeout has elapsed. This method
behaves in the following ways, depending on the value of

ms

:

- If

ms == 0

, waits until all pixels are delivered

If

ms > 0

, waits until all pixels are delivered
as timeout expires.

If

ms < 0

, returns

true

if all pixels
are grabbed,

false

otherwise and does not wait.

**Parameters:**
- ms

- the number of milliseconds to wait for the image pixels
to arrive before timing out

**Returns:**
- true if the pixels were successfully grabbed, false on
abort, error or timeout

**Throws:**
- InterruptedException

- Another thread has interrupted this thread.

---

#### public int getStatus()

Return the status of the pixels. The ImageObserver flags
representing the available pixel information are returned.

**Returns:**
- the bitwise OR of all relevant ImageObserver flags

**See Also:**
- ImageObserver

---

#### public int getWidth()

Get the width of the pixel buffer (after adjusting for image width).
If no width was specified for the rectangle of pixels to grab then
then this information will only be available after the image has
delivered the dimensions.

**Returns:**
- the final width used for the pixel buffer or -1 if the width
is not yet known

**See Also:**
- getStatus()

---

#### public int getHeight()

Get the height of the pixel buffer (after adjusting for image height).
If no width was specified for the rectangle of pixels to grab then
then this information will only be available after the image has
delivered the dimensions.

**Returns:**
- the final height used for the pixel buffer or -1 if the height
is not yet known

**See Also:**
- getStatus()

---

#### public
Object
getPixels()

Get the pixel buffer. If the PixelGrabber was not constructed
with an explicit pixel buffer to hold the pixels then this method
will return null until the size and format of the image data is
known.
Since the PixelGrabber may fall back on accumulating the data
in the default RGB ColorModel at any time if the source image
uses more than one ColorModel to deliver the data, the array
object returned by this method may change over time until the
image grab is complete.

**Returns:**
- either a byte array or an int array

**See Also:**
- getStatus()

,

setPixels(int, int, int, int, ColorModel, byte[], int, int)

,

setPixels(int, int, int, int, ColorModel, int[], int, int)

---

#### public
ColorModel
getColorModel()

Get the ColorModel for the pixels stored in the array. If the
PixelGrabber was constructed with an explicit pixel buffer then
this method will always return the default RGB ColorModel,
otherwise it may return null until the ColorModel used by the
ImageProducer is known.
Since the PixelGrabber may fall back on accumulating the data
in the default RGB ColorModel at any time if the source image
uses more than one ColorModel to deliver the data, the ColorModel
object returned by this method may change over time until the
image grab is complete and may not reflect any of the ColorModel
objects that was used by the ImageProducer to deliver the pixels.

**Returns:**
- the ColorModel object used for storing the pixels

**See Also:**
- getStatus()

,

ColorModel.getRGBdefault()

,

setColorModel(ColorModel)

---

#### public void setDimensions​(int width,
int height)

The setDimensions method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being grabbed. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

**Specified by:**
- setDimensions

in interface

ImageConsumer

**Parameters:**
- width

- the width of the dimension
- height

- the height of the dimension

---

#### public void setHints​(int hints)

The setHints method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being grabbed. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

**Specified by:**
- setHints

in interface

ImageConsumer

**Parameters:**
- hints

- a set of hints used to process the pixels

---

#### public void setProperties​(
Hashtable
<?,​?> props)

The setProperties method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being grabbed. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

**Specified by:**
- setProperties

in interface

ImageConsumer

**Parameters:**
- props

- the list of properties

---

#### public void setColorModel​(
ColorModel
model)

The setColorModel method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being grabbed. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

**Specified by:**
- setColorModel

in interface

ImageConsumer

**Parameters:**
- model

- the specified

ColorModel

**See Also:**
- getColorModel()

---

#### public void setPixels​(int srcX,
int srcY,
int srcW,
int srcH,

ColorModel
model,
byte[] pixels,
int srcOff,
int srcScan)

The setPixels method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being grabbed. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

**Specified by:**
- setPixels

in interface

ImageConsumer

**Parameters:**
- srcX

- the X coordinate of the upper-left corner
of the area of pixels to be set
- srcY

- the Y coordinate of the upper-left corner
of the area of pixels to be set
- srcW

- the width of the area of pixels
- srcH

- the height of the area of pixels
- model

- the specified

ColorModel
- pixels

- the array of pixels
- srcOff

- the offset into the pixels array
- srcScan

- the distance from one row of pixels to the next
in the pixels array

**See Also:**
- getPixels()

---

#### public void setPixels​(int srcX,
int srcY,
int srcW,
int srcH,

ColorModel
model,
int[] pixels,
int srcOff,
int srcScan)

The setPixels method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being grabbed. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

**Specified by:**
- setPixels

in interface

ImageConsumer

**Parameters:**
- srcX

- the X coordinate of the upper-left corner
of the area of pixels to be set
- srcY

- the Y coordinate of the upper-left corner
of the area of pixels to be set
- srcW

- the width of the area of pixels
- srcH

- the height of the area of pixels
- model

- the specified

ColorModel
- pixels

- the array of pixels
- srcOff

- the offset into the pixels array
- srcScan

- the distance from one row of pixels to the next
in the pixels array

**See Also:**
- getPixels()

---

#### public void imageComplete​(int status)

The imageComplete method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being grabbed. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

**Specified by:**
- imageComplete

in interface

ImageConsumer

**Parameters:**
- status

- the status of image loading

**See Also:**
- ImageProducer.removeConsumer(java.awt.image.ImageConsumer)

---

#### public int status()

Returns the status of the pixels. The ImageObserver flags
representing the available pixel information are returned.
This method and

getStatus

have the
same implementation, but

getStatus

is the
preferred method because it conforms to the convention of
naming information-retrieval methods with the form
"getXXX".

**Returns:**
- the bitwise OR of all relevant ImageObserver flags

**See Also:**
- ImageObserver

,

getStatus()

---

### Additional Sections

#### Class PixelGrabber

java.lang.Object

- java.awt.image.PixelGrabber

java.awt.image.PixelGrabber

**All Implemented Interfaces:** ImageConsumer

```java
public class
PixelGrabber

extends
Object

implements
ImageConsumer
```

The PixelGrabber class implements an ImageConsumer which can be attached
to an Image or ImageProducer object to retrieve a subset of the pixels
in that image. Here is an example:

```java
public void handlesinglepixel(int x, int y, int pixel) {
int alpha = (pixel >> 24) & 0xff;
int red = (pixel >> 16) & 0xff;
int green = (pixel >> 8) & 0xff;
int blue = (pixel ) & 0xff;
// Deal with the pixel as necessary...
}

public void handlepixels(Image img, int x, int y, int w, int h) {
int[] pixels = new int[w * h];
PixelGrabber pg = new PixelGrabber(img, x, y, w, h, pixels, 0, w);
try {
pg.grabPixels();
} catch (InterruptedException e) {
System.err.println("interrupted waiting for pixels!");
return;
}
if ((pg.getStatus() & ImageObserver.ABORT) != 0) {
System.err.println("image fetch aborted or errored");
return;
}
for (int j = 0; j < h; j++) {
for (int i = 0; i < w; i++) {
handlesinglepixel(x+i, y+j, pixels[j * w + i]);
}
}
}
```

**See Also:** ColorModel.getRGBdefault()

public class

PixelGrabber

extends

Object

implements

ImageConsumer

The PixelGrabber class implements an ImageConsumer which can be attached
to an Image or ImageProducer object to retrieve a subset of the pixels
in that image. Here is an example:

```java
public void handlesinglepixel(int x, int y, int pixel) {
int alpha = (pixel >> 24) & 0xff;
int red = (pixel >> 16) & 0xff;
int green = (pixel >> 8) & 0xff;
int blue = (pixel ) & 0xff;
// Deal with the pixel as necessary...
}

public void handlepixels(Image img, int x, int y, int w, int h) {
int[] pixels = new int[w * h];
PixelGrabber pg = new PixelGrabber(img, x, y, w, h, pixels, 0, w);
try {
pg.grabPixels();
} catch (InterruptedException e) {
System.err.println("interrupted waiting for pixels!");
return;
}
if ((pg.getStatus() & ImageObserver.ABORT) != 0) {
System.err.println("image fetch aborted or errored");
return;
}
for (int j = 0; j < h; j++) {
for (int i = 0; i < w; i++) {
handlesinglepixel(x+i, y+j, pixels[j * w + i]);
}
}
}
```

public void handlesinglepixel(int x, int y, int pixel) {
int alpha = (pixel >> 24) & 0xff;
int red = (pixel >> 16) & 0xff;
int green = (pixel >> 8) & 0xff;
int blue = (pixel ) & 0xff;
// Deal with the pixel as necessary...
}

public void handlepixels(Image img, int x, int y, int w, int h) {
int[] pixels = new int[w * h];
PixelGrabber pg = new PixelGrabber(img, x, y, w, h, pixels, 0, w);
try {
pg.grabPixels();
} catch (InterruptedException e) {
System.err.println("interrupted waiting for pixels!");
return;
}
if ((pg.getStatus() & ImageObserver.ABORT) != 0) {
System.err.println("image fetch aborted or errored");
return;
}
for (int j = 0; j < h; j++) {
for (int i = 0; i < w; i++) {
handlesinglepixel(x+i, y+j, pixels[j * w + i]);
}
}
}

=========== FIELD SUMMARY ===========

- Field Summary

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

PixelGrabber

​(

ImageProducer

ip,
int x,
int y,
int w,
int h,
int[] pix,
int off,
int scansize)

Create a PixelGrabber object to grab the (x, y, w, h) rectangular
section of pixels from the image produced by the specified
ImageProducer into the given array.

PixelGrabber

​(

Image

img,
int x,
int y,
int w,
int h,
boolean forceRGB)

Create a PixelGrabber object to grab the (x, y, w, h) rectangular
section of pixels from the specified image.

PixelGrabber

​(

Image

img,
int x,
int y,
int w,
int h,
int[] pix,
int off,
int scansize)

Create a PixelGrabber object to grab the (x, y, w, h) rectangular
section of pixels from the specified image into the given array.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

abortGrabbing

()

Request the PixelGrabber to abort the image fetch.

ColorModel

getColorModel

()

Get the ColorModel for the pixels stored in the array.

int

getHeight

()

Get the height of the pixel buffer (after adjusting for image height).

Object

getPixels

()

Get the pixel buffer.

int

getStatus

()

Return the status of the pixels.

int

getWidth

()

Get the width of the pixel buffer (after adjusting for image width).

boolean

grabPixels

()

Request the Image or ImageProducer to start delivering pixels and
wait for all of the pixels in the rectangle of interest to be
delivered.

boolean

grabPixels

​(long ms)

Request the Image or ImageProducer to start delivering pixels and
wait for all of the pixels in the rectangle of interest to be
delivered or until the specified timeout has elapsed.

void

imageComplete

​(int status)

The imageComplete method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

void

setColorModel

​(

ColorModel

model)

The setColorModel method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

void

setDimensions

​(int width,
int height)

The setDimensions method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

void

setHints

​(int hints)

The setHints method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

void

setPixels

​(int srcX,
int srcY,
int srcW,
int srcH,

ColorModel

model,
byte[] pixels,
int srcOff,
int srcScan)

The setPixels method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

void

setPixels

​(int srcX,
int srcY,
int srcW,
int srcH,

ColorModel

model,
int[] pixels,
int srcOff,
int srcScan)

The setPixels method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

void

setProperties

​(

Hashtable

<?,​?> props)

The setProperties method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

void

startGrabbing

()

Request the PixelGrabber to start fetching the pixels.

int

status

()

Returns the status of the pixels.

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

PixelGrabber

​(

ImageProducer

ip,
int x,
int y,
int w,
int h,
int[] pix,
int off,
int scansize)

Create a PixelGrabber object to grab the (x, y, w, h) rectangular
section of pixels from the image produced by the specified
ImageProducer into the given array.

PixelGrabber

​(

Image

img,
int x,
int y,
int w,
int h,
boolean forceRGB)

Create a PixelGrabber object to grab the (x, y, w, h) rectangular
section of pixels from the specified image.

PixelGrabber

​(

Image

img,
int x,
int y,
int w,
int h,
int[] pix,
int off,
int scansize)

Create a PixelGrabber object to grab the (x, y, w, h) rectangular
section of pixels from the specified image into the given array.

---

#### Constructor Summary

Create a PixelGrabber object to grab the (x, y, w, h) rectangular
section of pixels from the image produced by the specified
ImageProducer into the given array.

Create a PixelGrabber object to grab the (x, y, w, h) rectangular
section of pixels from the specified image.

Create a PixelGrabber object to grab the (x, y, w, h) rectangular
section of pixels from the specified image into the given array.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

abortGrabbing

()

Request the PixelGrabber to abort the image fetch.

ColorModel

getColorModel

()

Get the ColorModel for the pixels stored in the array.

int

getHeight

()

Get the height of the pixel buffer (after adjusting for image height).

Object

getPixels

()

Get the pixel buffer.

int

getStatus

()

Return the status of the pixels.

int

getWidth

()

Get the width of the pixel buffer (after adjusting for image width).

boolean

grabPixels

()

Request the Image or ImageProducer to start delivering pixels and
wait for all of the pixels in the rectangle of interest to be
delivered.

boolean

grabPixels

​(long ms)

Request the Image or ImageProducer to start delivering pixels and
wait for all of the pixels in the rectangle of interest to be
delivered or until the specified timeout has elapsed.

void

imageComplete

​(int status)

The imageComplete method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

void

setColorModel

​(

ColorModel

model)

The setColorModel method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

void

setDimensions

​(int width,
int height)

The setDimensions method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

void

setHints

​(int hints)

The setHints method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

void

setPixels

​(int srcX,
int srcY,
int srcW,
int srcH,

ColorModel

model,
byte[] pixels,
int srcOff,
int srcScan)

The setPixels method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

void

setPixels

​(int srcX,
int srcY,
int srcW,
int srcH,

ColorModel

model,
int[] pixels,
int srcOff,
int srcScan)

The setPixels method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

void

setProperties

​(

Hashtable

<?,​?> props)

The setProperties method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

void

startGrabbing

()

Request the PixelGrabber to start fetching the pixels.

int

status

()

Returns the status of the pixels.

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

Request the PixelGrabber to abort the image fetch.

Get the ColorModel for the pixels stored in the array.

Get the height of the pixel buffer (after adjusting for image height).

Get the pixel buffer.

Return the status of the pixels.

Get the width of the pixel buffer (after adjusting for image width).

Request the Image or ImageProducer to start delivering pixels and
wait for all of the pixels in the rectangle of interest to be
delivered.

Request the Image or ImageProducer to start delivering pixels and
wait for all of the pixels in the rectangle of interest to be
delivered or until the specified timeout has elapsed.

The imageComplete method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

The setColorModel method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

The setDimensions method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

The setHints method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

The setPixels method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

The setProperties method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

Request the PixelGrabber to start fetching the pixels.

Returns the status of the pixels.

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

- PixelGrabber

```java
public PixelGrabber​(
Image
img,
int x,
int y,
int w,
int h,
int[] pix,
int off,
int scansize)
```

Create a PixelGrabber object to grab the (x, y, w, h) rectangular
section of pixels from the specified image into the given array.
The pixels are stored into the array in the default RGB ColorModel.
The RGB data for pixel (i, j) where (i, j) is inside the rectangle
(x, y, w, h) is stored in the array at

pix[(j - y) * scansize + (i - x) + off]

.

**Parameters:** img

- the image to retrieve pixels from
**Parameters:** x

- the x coordinate of the upper left corner of the rectangle
of pixels to retrieve from the image, relative to the default
(unscaled) size of the image
**Parameters:** y

- the y coordinate of the upper left corner of the rectangle
of pixels to retrieve from the image
**Parameters:** w

- the width of the rectangle of pixels to retrieve
**Parameters:** h

- the height of the rectangle of pixels to retrieve
**Parameters:** pix

- the array of integers which are to be used to hold the
RGB pixels retrieved from the image
**Parameters:** off

- the offset into the array of where to store the first pixel
**Parameters:** scansize

- the distance from one row of pixels to the next in
the array
**See Also:** ColorModel.getRGBdefault()

- PixelGrabber

```java
public PixelGrabber​(
ImageProducer
ip,
int x,
int y,
int w,
int h,
int[] pix,
int off,
int scansize)
```

Create a PixelGrabber object to grab the (x, y, w, h) rectangular
section of pixels from the image produced by the specified
ImageProducer into the given array.
The pixels are stored into the array in the default RGB ColorModel.
The RGB data for pixel (i, j) where (i, j) is inside the rectangle
(x, y, w, h) is stored in the array at

pix[(j - y) * scansize + (i - x) + off]

.

**Parameters:** ip

- the

ImageProducer

that produces the
image from which to retrieve pixels
**Parameters:** x

- the x coordinate of the upper left corner of the rectangle
of pixels to retrieve from the image, relative to the default
(unscaled) size of the image
**Parameters:** y

- the y coordinate of the upper left corner of the rectangle
of pixels to retrieve from the image
**Parameters:** w

- the width of the rectangle of pixels to retrieve
**Parameters:** h

- the height of the rectangle of pixels to retrieve
**Parameters:** pix

- the array of integers which are to be used to hold the
RGB pixels retrieved from the image
**Parameters:** off

- the offset into the array of where to store the first pixel
**Parameters:** scansize

- the distance from one row of pixels to the next in
the array
**See Also:** ColorModel.getRGBdefault()

- PixelGrabber

```java
public PixelGrabber​(
Image
img,
int x,
int y,
int w,
int h,
boolean forceRGB)
```

Create a PixelGrabber object to grab the (x, y, w, h) rectangular
section of pixels from the specified image. The pixels are
accumulated in the original ColorModel if the same ColorModel
is used for every call to setPixels, otherwise the pixels are
accumulated in the default RGB ColorModel. If the forceRGB
parameter is true, then the pixels will be accumulated in the
default RGB ColorModel anyway. A buffer is allocated by the
PixelGrabber to hold the pixels in either case. If

(w < 0)

or

(h < 0)

, then they will default to the remaining width and
height of the source data when that information is delivered.

**Parameters:** img

- the image to retrieve the image data from
**Parameters:** x

- the x coordinate of the upper left corner of the rectangle
of pixels to retrieve from the image, relative to the default
(unscaled) size of the image
**Parameters:** y

- the y coordinate of the upper left corner of the rectangle
of pixels to retrieve from the image
**Parameters:** w

- the width of the rectangle of pixels to retrieve
**Parameters:** h

- the height of the rectangle of pixels to retrieve
**Parameters:** forceRGB

- true if the pixels should always be converted to
the default RGB ColorModel

============ METHOD DETAIL ==========

- Method Detail

- startGrabbing

```java
public void startGrabbing()
```

Request the PixelGrabber to start fetching the pixels.

- abortGrabbing

```java
public void abortGrabbing()
```

Request the PixelGrabber to abort the image fetch.

- grabPixels

```java
public boolean grabPixels()
throws
InterruptedException
```

Request the Image or ImageProducer to start delivering pixels and
wait for all of the pixels in the rectangle of interest to be
delivered.

**Returns:** true if the pixels were successfully grabbed, false on
abort, error or timeout
**Throws:** InterruptedException

- Another thread has interrupted this thread.

- grabPixels

```java
public boolean grabPixels​(long ms)
throws
InterruptedException
```

Request the Image or ImageProducer to start delivering pixels and
wait for all of the pixels in the rectangle of interest to be
delivered or until the specified timeout has elapsed. This method
behaves in the following ways, depending on the value of

ms

:

- If

ms == 0

, waits until all pixels are delivered

If

ms > 0

, waits until all pixels are delivered
as timeout expires.

If

ms < 0

, returns

true

if all pixels
are grabbed,

false

otherwise and does not wait.

**Parameters:** ms

- the number of milliseconds to wait for the image pixels
to arrive before timing out
**Returns:** true if the pixels were successfully grabbed, false on
abort, error or timeout
**Throws:** InterruptedException

- Another thread has interrupted this thread.

- getStatus

```java
public int getStatus()
```

Return the status of the pixels. The ImageObserver flags
representing the available pixel information are returned.

**Returns:** the bitwise OR of all relevant ImageObserver flags
**See Also:** ImageObserver

- getWidth

```java
public int getWidth()
```

Get the width of the pixel buffer (after adjusting for image width).
If no width was specified for the rectangle of pixels to grab then
then this information will only be available after the image has
delivered the dimensions.

**Returns:** the final width used for the pixel buffer or -1 if the width
is not yet known
**See Also:** getStatus()

- getHeight

```java
public int getHeight()
```

Get the height of the pixel buffer (after adjusting for image height).
If no width was specified for the rectangle of pixels to grab then
then this information will only be available after the image has
delivered the dimensions.

**Returns:** the final height used for the pixel buffer or -1 if the height
is not yet known
**See Also:** getStatus()

- getPixels

```java
public
Object
getPixels()
```

Get the pixel buffer. If the PixelGrabber was not constructed
with an explicit pixel buffer to hold the pixels then this method
will return null until the size and format of the image data is
known.
Since the PixelGrabber may fall back on accumulating the data
in the default RGB ColorModel at any time if the source image
uses more than one ColorModel to deliver the data, the array
object returned by this method may change over time until the
image grab is complete.

**Returns:** either a byte array or an int array
**See Also:** getStatus()

,

setPixels(int, int, int, int, ColorModel, byte[], int, int)

,

setPixels(int, int, int, int, ColorModel, int[], int, int)

- getColorModel

```java
public
ColorModel
getColorModel()
```

Get the ColorModel for the pixels stored in the array. If the
PixelGrabber was constructed with an explicit pixel buffer then
this method will always return the default RGB ColorModel,
otherwise it may return null until the ColorModel used by the
ImageProducer is known.
Since the PixelGrabber may fall back on accumulating the data
in the default RGB ColorModel at any time if the source image
uses more than one ColorModel to deliver the data, the ColorModel
object returned by this method may change over time until the
image grab is complete and may not reflect any of the ColorModel
objects that was used by the ImageProducer to deliver the pixels.

**Returns:** the ColorModel object used for storing the pixels
**See Also:** getStatus()

,

ColorModel.getRGBdefault()

,

setColorModel(ColorModel)

- setDimensions

```java
public void setDimensions​(int width,
int height)
```

The setDimensions method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being grabbed. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

**Specified by:** setDimensions

in interface

ImageConsumer
**Parameters:** width

- the width of the dimension
**Parameters:** height

- the height of the dimension

- setHints

```java
public void setHints​(int hints)
```

The setHints method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being grabbed. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

**Specified by:** setHints

in interface

ImageConsumer
**Parameters:** hints

- a set of hints used to process the pixels

- setProperties

```java
public void setProperties​(
Hashtable
<?,​?> props)
```

The setProperties method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being grabbed. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

**Specified by:** setProperties

in interface

ImageConsumer
**Parameters:** props

- the list of properties

- setColorModel

```java
public void setColorModel​(
ColorModel
model)
```

The setColorModel method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being grabbed. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

**Specified by:** setColorModel

in interface

ImageConsumer
**Parameters:** model

- the specified

ColorModel
**See Also:** getColorModel()

- setPixels

```java
public void setPixels​(int srcX,
int srcY,
int srcW,
int srcH,

ColorModel
model,
byte[] pixels,
int srcOff,
int srcScan)
```

The setPixels method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being grabbed. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

**Specified by:** setPixels

in interface

ImageConsumer
**Parameters:** srcX

- the X coordinate of the upper-left corner
of the area of pixels to be set
**Parameters:** srcY

- the Y coordinate of the upper-left corner
of the area of pixels to be set
**Parameters:** srcW

- the width of the area of pixels
**Parameters:** srcH

- the height of the area of pixels
**Parameters:** model

- the specified

ColorModel
**Parameters:** pixels

- the array of pixels
**Parameters:** srcOff

- the offset into the pixels array
**Parameters:** srcScan

- the distance from one row of pixels to the next
in the pixels array
**See Also:** getPixels()

- setPixels

```java
public void setPixels​(int srcX,
int srcY,
int srcW,
int srcH,

ColorModel
model,
int[] pixels,
int srcOff,
int srcScan)
```

The setPixels method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being grabbed. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

**Specified by:** setPixels

in interface

ImageConsumer
**Parameters:** srcX

- the X coordinate of the upper-left corner
of the area of pixels to be set
**Parameters:** srcY

- the Y coordinate of the upper-left corner
of the area of pixels to be set
**Parameters:** srcW

- the width of the area of pixels
**Parameters:** srcH

- the height of the area of pixels
**Parameters:** model

- the specified

ColorModel
**Parameters:** pixels

- the array of pixels
**Parameters:** srcOff

- the offset into the pixels array
**Parameters:** srcScan

- the distance from one row of pixels to the next
in the pixels array
**See Also:** getPixels()

- imageComplete

```java
public void imageComplete​(int status)
```

The imageComplete method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being grabbed. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

**Specified by:** imageComplete

in interface

ImageConsumer
**Parameters:** status

- the status of image loading
**See Also:** ImageProducer.removeConsumer(java.awt.image.ImageConsumer)

- status

```java
public int status()
```

Returns the status of the pixels. The ImageObserver flags
representing the available pixel information are returned.
This method and

getStatus

have the
same implementation, but

getStatus

is the
preferred method because it conforms to the convention of
naming information-retrieval methods with the form
"getXXX".

**Returns:** the bitwise OR of all relevant ImageObserver flags
**See Also:** ImageObserver

,

getStatus()

Constructor Detail

- PixelGrabber

```java
public PixelGrabber​(
Image
img,
int x,
int y,
int w,
int h,
int[] pix,
int off,
int scansize)
```

Create a PixelGrabber object to grab the (x, y, w, h) rectangular
section of pixels from the specified image into the given array.
The pixels are stored into the array in the default RGB ColorModel.
The RGB data for pixel (i, j) where (i, j) is inside the rectangle
(x, y, w, h) is stored in the array at

pix[(j - y) * scansize + (i - x) + off]

.

**Parameters:** img

- the image to retrieve pixels from
**Parameters:** x

- the x coordinate of the upper left corner of the rectangle
of pixels to retrieve from the image, relative to the default
(unscaled) size of the image
**Parameters:** y

- the y coordinate of the upper left corner of the rectangle
of pixels to retrieve from the image
**Parameters:** w

- the width of the rectangle of pixels to retrieve
**Parameters:** h

- the height of the rectangle of pixels to retrieve
**Parameters:** pix

- the array of integers which are to be used to hold the
RGB pixels retrieved from the image
**Parameters:** off

- the offset into the array of where to store the first pixel
**Parameters:** scansize

- the distance from one row of pixels to the next in
the array
**See Also:** ColorModel.getRGBdefault()

- PixelGrabber

```java
public PixelGrabber​(
ImageProducer
ip,
int x,
int y,
int w,
int h,
int[] pix,
int off,
int scansize)
```

Create a PixelGrabber object to grab the (x, y, w, h) rectangular
section of pixels from the image produced by the specified
ImageProducer into the given array.
The pixels are stored into the array in the default RGB ColorModel.
The RGB data for pixel (i, j) where (i, j) is inside the rectangle
(x, y, w, h) is stored in the array at

pix[(j - y) * scansize + (i - x) + off]

.

**Parameters:** ip

- the

ImageProducer

that produces the
image from which to retrieve pixels
**Parameters:** x

- the x coordinate of the upper left corner of the rectangle
of pixels to retrieve from the image, relative to the default
(unscaled) size of the image
**Parameters:** y

- the y coordinate of the upper left corner of the rectangle
of pixels to retrieve from the image
**Parameters:** w

- the width of the rectangle of pixels to retrieve
**Parameters:** h

- the height of the rectangle of pixels to retrieve
**Parameters:** pix

- the array of integers which are to be used to hold the
RGB pixels retrieved from the image
**Parameters:** off

- the offset into the array of where to store the first pixel
**Parameters:** scansize

- the distance from one row of pixels to the next in
the array
**See Also:** ColorModel.getRGBdefault()

- PixelGrabber

```java
public PixelGrabber​(
Image
img,
int x,
int y,
int w,
int h,
boolean forceRGB)
```

Create a PixelGrabber object to grab the (x, y, w, h) rectangular
section of pixels from the specified image. The pixels are
accumulated in the original ColorModel if the same ColorModel
is used for every call to setPixels, otherwise the pixels are
accumulated in the default RGB ColorModel. If the forceRGB
parameter is true, then the pixels will be accumulated in the
default RGB ColorModel anyway. A buffer is allocated by the
PixelGrabber to hold the pixels in either case. If

(w < 0)

or

(h < 0)

, then they will default to the remaining width and
height of the source data when that information is delivered.

**Parameters:** img

- the image to retrieve the image data from
**Parameters:** x

- the x coordinate of the upper left corner of the rectangle
of pixels to retrieve from the image, relative to the default
(unscaled) size of the image
**Parameters:** y

- the y coordinate of the upper left corner of the rectangle
of pixels to retrieve from the image
**Parameters:** w

- the width of the rectangle of pixels to retrieve
**Parameters:** h

- the height of the rectangle of pixels to retrieve
**Parameters:** forceRGB

- true if the pixels should always be converted to
the default RGB ColorModel

---

#### Constructor Detail

PixelGrabber

```java
public PixelGrabber​(
Image
img,
int x,
int y,
int w,
int h,
int[] pix,
int off,
int scansize)
```

Create a PixelGrabber object to grab the (x, y, w, h) rectangular
section of pixels from the specified image into the given array.
The pixels are stored into the array in the default RGB ColorModel.
The RGB data for pixel (i, j) where (i, j) is inside the rectangle
(x, y, w, h) is stored in the array at

pix[(j - y) * scansize + (i - x) + off]

.

**Parameters:** img

- the image to retrieve pixels from
**Parameters:** x

- the x coordinate of the upper left corner of the rectangle
of pixels to retrieve from the image, relative to the default
(unscaled) size of the image
**Parameters:** y

- the y coordinate of the upper left corner of the rectangle
of pixels to retrieve from the image
**Parameters:** w

- the width of the rectangle of pixels to retrieve
**Parameters:** h

- the height of the rectangle of pixels to retrieve
**Parameters:** pix

- the array of integers which are to be used to hold the
RGB pixels retrieved from the image
**Parameters:** off

- the offset into the array of where to store the first pixel
**Parameters:** scansize

- the distance from one row of pixels to the next in
the array
**See Also:** ColorModel.getRGBdefault()

---

#### PixelGrabber

public PixelGrabber​(

Image

img,
int x,
int y,
int w,
int h,
int[] pix,
int off,
int scansize)

Create a PixelGrabber object to grab the (x, y, w, h) rectangular
section of pixels from the specified image into the given array.
The pixels are stored into the array in the default RGB ColorModel.
The RGB data for pixel (i, j) where (i, j) is inside the rectangle
(x, y, w, h) is stored in the array at

pix[(j - y) * scansize + (i - x) + off]

.

PixelGrabber

```java
public PixelGrabber​(
ImageProducer
ip,
int x,
int y,
int w,
int h,
int[] pix,
int off,
int scansize)
```

Create a PixelGrabber object to grab the (x, y, w, h) rectangular
section of pixels from the image produced by the specified
ImageProducer into the given array.
The pixels are stored into the array in the default RGB ColorModel.
The RGB data for pixel (i, j) where (i, j) is inside the rectangle
(x, y, w, h) is stored in the array at

pix[(j - y) * scansize + (i - x) + off]

.

**Parameters:** ip

- the

ImageProducer

that produces the
image from which to retrieve pixels
**Parameters:** x

- the x coordinate of the upper left corner of the rectangle
of pixels to retrieve from the image, relative to the default
(unscaled) size of the image
**Parameters:** y

- the y coordinate of the upper left corner of the rectangle
of pixels to retrieve from the image
**Parameters:** w

- the width of the rectangle of pixels to retrieve
**Parameters:** h

- the height of the rectangle of pixels to retrieve
**Parameters:** pix

- the array of integers which are to be used to hold the
RGB pixels retrieved from the image
**Parameters:** off

- the offset into the array of where to store the first pixel
**Parameters:** scansize

- the distance from one row of pixels to the next in
the array
**See Also:** ColorModel.getRGBdefault()

---

#### PixelGrabber

public PixelGrabber​(

ImageProducer

ip,
int x,
int y,
int w,
int h,
int[] pix,
int off,
int scansize)

Create a PixelGrabber object to grab the (x, y, w, h) rectangular
section of pixels from the image produced by the specified
ImageProducer into the given array.
The pixels are stored into the array in the default RGB ColorModel.
The RGB data for pixel (i, j) where (i, j) is inside the rectangle
(x, y, w, h) is stored in the array at

pix[(j - y) * scansize + (i - x) + off]

.

PixelGrabber

```java
public PixelGrabber​(
Image
img,
int x,
int y,
int w,
int h,
boolean forceRGB)
```

Create a PixelGrabber object to grab the (x, y, w, h) rectangular
section of pixels from the specified image. The pixels are
accumulated in the original ColorModel if the same ColorModel
is used for every call to setPixels, otherwise the pixels are
accumulated in the default RGB ColorModel. If the forceRGB
parameter is true, then the pixels will be accumulated in the
default RGB ColorModel anyway. A buffer is allocated by the
PixelGrabber to hold the pixels in either case. If

(w < 0)

or

(h < 0)

, then they will default to the remaining width and
height of the source data when that information is delivered.

**Parameters:** img

- the image to retrieve the image data from
**Parameters:** x

- the x coordinate of the upper left corner of the rectangle
of pixels to retrieve from the image, relative to the default
(unscaled) size of the image
**Parameters:** y

- the y coordinate of the upper left corner of the rectangle
of pixels to retrieve from the image
**Parameters:** w

- the width of the rectangle of pixels to retrieve
**Parameters:** h

- the height of the rectangle of pixels to retrieve
**Parameters:** forceRGB

- true if the pixels should always be converted to
the default RGB ColorModel

---

#### PixelGrabber

public PixelGrabber​(

Image

img,
int x,
int y,
int w,
int h,
boolean forceRGB)

Create a PixelGrabber object to grab the (x, y, w, h) rectangular
section of pixels from the specified image. The pixels are
accumulated in the original ColorModel if the same ColorModel
is used for every call to setPixels, otherwise the pixels are
accumulated in the default RGB ColorModel. If the forceRGB
parameter is true, then the pixels will be accumulated in the
default RGB ColorModel anyway. A buffer is allocated by the
PixelGrabber to hold the pixels in either case. If

(w < 0)

or

(h < 0)

, then they will default to the remaining width and
height of the source data when that information is delivered.

Method Detail

- startGrabbing

```java
public void startGrabbing()
```

Request the PixelGrabber to start fetching the pixels.

- abortGrabbing

```java
public void abortGrabbing()
```

Request the PixelGrabber to abort the image fetch.

- grabPixels

```java
public boolean grabPixels()
throws
InterruptedException
```

Request the Image or ImageProducer to start delivering pixels and
wait for all of the pixels in the rectangle of interest to be
delivered.

**Returns:** true if the pixels were successfully grabbed, false on
abort, error or timeout
**Throws:** InterruptedException

- Another thread has interrupted this thread.

- grabPixels

```java
public boolean grabPixels​(long ms)
throws
InterruptedException
```

Request the Image or ImageProducer to start delivering pixels and
wait for all of the pixels in the rectangle of interest to be
delivered or until the specified timeout has elapsed. This method
behaves in the following ways, depending on the value of

ms

:

- If

ms == 0

, waits until all pixels are delivered

If

ms > 0

, waits until all pixels are delivered
as timeout expires.

If

ms < 0

, returns

true

if all pixels
are grabbed,

false

otherwise and does not wait.

**Parameters:** ms

- the number of milliseconds to wait for the image pixels
to arrive before timing out
**Returns:** true if the pixels were successfully grabbed, false on
abort, error or timeout
**Throws:** InterruptedException

- Another thread has interrupted this thread.

- getStatus

```java
public int getStatus()
```

Return the status of the pixels. The ImageObserver flags
representing the available pixel information are returned.

**Returns:** the bitwise OR of all relevant ImageObserver flags
**See Also:** ImageObserver

- getWidth

```java
public int getWidth()
```

Get the width of the pixel buffer (after adjusting for image width).
If no width was specified for the rectangle of pixels to grab then
then this information will only be available after the image has
delivered the dimensions.

**Returns:** the final width used for the pixel buffer or -1 if the width
is not yet known
**See Also:** getStatus()

- getHeight

```java
public int getHeight()
```

Get the height of the pixel buffer (after adjusting for image height).
If no width was specified for the rectangle of pixels to grab then
then this information will only be available after the image has
delivered the dimensions.

**Returns:** the final height used for the pixel buffer or -1 if the height
is not yet known
**See Also:** getStatus()

- getPixels

```java
public
Object
getPixels()
```

Get the pixel buffer. If the PixelGrabber was not constructed
with an explicit pixel buffer to hold the pixels then this method
will return null until the size and format of the image data is
known.
Since the PixelGrabber may fall back on accumulating the data
in the default RGB ColorModel at any time if the source image
uses more than one ColorModel to deliver the data, the array
object returned by this method may change over time until the
image grab is complete.

**Returns:** either a byte array or an int array
**See Also:** getStatus()

,

setPixels(int, int, int, int, ColorModel, byte[], int, int)

,

setPixels(int, int, int, int, ColorModel, int[], int, int)

- getColorModel

```java
public
ColorModel
getColorModel()
```

Get the ColorModel for the pixels stored in the array. If the
PixelGrabber was constructed with an explicit pixel buffer then
this method will always return the default RGB ColorModel,
otherwise it may return null until the ColorModel used by the
ImageProducer is known.
Since the PixelGrabber may fall back on accumulating the data
in the default RGB ColorModel at any time if the source image
uses more than one ColorModel to deliver the data, the ColorModel
object returned by this method may change over time until the
image grab is complete and may not reflect any of the ColorModel
objects that was used by the ImageProducer to deliver the pixels.

**Returns:** the ColorModel object used for storing the pixels
**See Also:** getStatus()

,

ColorModel.getRGBdefault()

,

setColorModel(ColorModel)

- setDimensions

```java
public void setDimensions​(int width,
int height)
```

The setDimensions method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being grabbed. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

**Specified by:** setDimensions

in interface

ImageConsumer
**Parameters:** width

- the width of the dimension
**Parameters:** height

- the height of the dimension

- setHints

```java
public void setHints​(int hints)
```

The setHints method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being grabbed. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

**Specified by:** setHints

in interface

ImageConsumer
**Parameters:** hints

- a set of hints used to process the pixels

- setProperties

```java
public void setProperties​(
Hashtable
<?,​?> props)
```

The setProperties method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being grabbed. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

**Specified by:** setProperties

in interface

ImageConsumer
**Parameters:** props

- the list of properties

- setColorModel

```java
public void setColorModel​(
ColorModel
model)
```

The setColorModel method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being grabbed. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

**Specified by:** setColorModel

in interface

ImageConsumer
**Parameters:** model

- the specified

ColorModel
**See Also:** getColorModel()

- setPixels

```java
public void setPixels​(int srcX,
int srcY,
int srcW,
int srcH,

ColorModel
model,
byte[] pixels,
int srcOff,
int srcScan)
```

The setPixels method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being grabbed. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

**Specified by:** setPixels

in interface

ImageConsumer
**Parameters:** srcX

- the X coordinate of the upper-left corner
of the area of pixels to be set
**Parameters:** srcY

- the Y coordinate of the upper-left corner
of the area of pixels to be set
**Parameters:** srcW

- the width of the area of pixels
**Parameters:** srcH

- the height of the area of pixels
**Parameters:** model

- the specified

ColorModel
**Parameters:** pixels

- the array of pixels
**Parameters:** srcOff

- the offset into the pixels array
**Parameters:** srcScan

- the distance from one row of pixels to the next
in the pixels array
**See Also:** getPixels()

- setPixels

```java
public void setPixels​(int srcX,
int srcY,
int srcW,
int srcH,

ColorModel
model,
int[] pixels,
int srcOff,
int srcScan)
```

The setPixels method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being grabbed. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

**Specified by:** setPixels

in interface

ImageConsumer
**Parameters:** srcX

- the X coordinate of the upper-left corner
of the area of pixels to be set
**Parameters:** srcY

- the Y coordinate of the upper-left corner
of the area of pixels to be set
**Parameters:** srcW

- the width of the area of pixels
**Parameters:** srcH

- the height of the area of pixels
**Parameters:** model

- the specified

ColorModel
**Parameters:** pixels

- the array of pixels
**Parameters:** srcOff

- the offset into the pixels array
**Parameters:** srcScan

- the distance from one row of pixels to the next
in the pixels array
**See Also:** getPixels()

- imageComplete

```java
public void imageComplete​(int status)
```

The imageComplete method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being grabbed. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

**Specified by:** imageComplete

in interface

ImageConsumer
**Parameters:** status

- the status of image loading
**See Also:** ImageProducer.removeConsumer(java.awt.image.ImageConsumer)

- status

```java
public int status()
```

Returns the status of the pixels. The ImageObserver flags
representing the available pixel information are returned.
This method and

getStatus

have the
same implementation, but

getStatus

is the
preferred method because it conforms to the convention of
naming information-retrieval methods with the form
"getXXX".

**Returns:** the bitwise OR of all relevant ImageObserver flags
**See Also:** ImageObserver

,

getStatus()

---

#### Method Detail

startGrabbing

```java
public void startGrabbing()
```

Request the PixelGrabber to start fetching the pixels.

---

#### startGrabbing

public void startGrabbing()

Request the PixelGrabber to start fetching the pixels.

abortGrabbing

```java
public void abortGrabbing()
```

Request the PixelGrabber to abort the image fetch.

---

#### abortGrabbing

public void abortGrabbing()

Request the PixelGrabber to abort the image fetch.

grabPixels

```java
public boolean grabPixels()
throws
InterruptedException
```

Request the Image or ImageProducer to start delivering pixels and
wait for all of the pixels in the rectangle of interest to be
delivered.

**Returns:** true if the pixels were successfully grabbed, false on
abort, error or timeout
**Throws:** InterruptedException

- Another thread has interrupted this thread.

---

#### grabPixels

public boolean grabPixels()
throws

InterruptedException

Request the Image or ImageProducer to start delivering pixels and
wait for all of the pixels in the rectangle of interest to be
delivered.

grabPixels

```java
public boolean grabPixels​(long ms)
throws
InterruptedException
```

Request the Image or ImageProducer to start delivering pixels and
wait for all of the pixels in the rectangle of interest to be
delivered or until the specified timeout has elapsed. This method
behaves in the following ways, depending on the value of

ms

:

- If

ms == 0

, waits until all pixels are delivered

If

ms > 0

, waits until all pixels are delivered
as timeout expires.

If

ms < 0

, returns

true

if all pixels
are grabbed,

false

otherwise and does not wait.

**Parameters:** ms

- the number of milliseconds to wait for the image pixels
to arrive before timing out
**Returns:** true if the pixels were successfully grabbed, false on
abort, error or timeout
**Throws:** InterruptedException

- Another thread has interrupted this thread.

---

#### grabPixels

public boolean grabPixels​(long ms)
throws

InterruptedException

Request the Image or ImageProducer to start delivering pixels and
wait for all of the pixels in the rectangle of interest to be
delivered or until the specified timeout has elapsed. This method
behaves in the following ways, depending on the value of

ms

:

- If

ms == 0

, waits until all pixels are delivered

If

ms > 0

, waits until all pixels are delivered
as timeout expires.

If

ms < 0

, returns

true

if all pixels
are grabbed,

false

otherwise and does not wait.

If

ms == 0

, waits until all pixels are delivered

If

ms > 0

, waits until all pixels are delivered
as timeout expires.

If

ms < 0

, returns

true

if all pixels
are grabbed,

false

otherwise and does not wait.

getStatus

```java
public int getStatus()
```

Return the status of the pixels. The ImageObserver flags
representing the available pixel information are returned.

**Returns:** the bitwise OR of all relevant ImageObserver flags
**See Also:** ImageObserver

---

#### getStatus

public int getStatus()

Return the status of the pixels. The ImageObserver flags
representing the available pixel information are returned.

getWidth

```java
public int getWidth()
```

Get the width of the pixel buffer (after adjusting for image width).
If no width was specified for the rectangle of pixels to grab then
then this information will only be available after the image has
delivered the dimensions.

**Returns:** the final width used for the pixel buffer or -1 if the width
is not yet known
**See Also:** getStatus()

---

#### getWidth

public int getWidth()

Get the width of the pixel buffer (after adjusting for image width).
If no width was specified for the rectangle of pixels to grab then
then this information will only be available after the image has
delivered the dimensions.

getHeight

```java
public int getHeight()
```

Get the height of the pixel buffer (after adjusting for image height).
If no width was specified for the rectangle of pixels to grab then
then this information will only be available after the image has
delivered the dimensions.

**Returns:** the final height used for the pixel buffer or -1 if the height
is not yet known
**See Also:** getStatus()

---

#### getHeight

public int getHeight()

Get the height of the pixel buffer (after adjusting for image height).
If no width was specified for the rectangle of pixels to grab then
then this information will only be available after the image has
delivered the dimensions.

getPixels

```java
public
Object
getPixels()
```

Get the pixel buffer. If the PixelGrabber was not constructed
with an explicit pixel buffer to hold the pixels then this method
will return null until the size and format of the image data is
known.
Since the PixelGrabber may fall back on accumulating the data
in the default RGB ColorModel at any time if the source image
uses more than one ColorModel to deliver the data, the array
object returned by this method may change over time until the
image grab is complete.

**Returns:** either a byte array or an int array
**See Also:** getStatus()

,

setPixels(int, int, int, int, ColorModel, byte[], int, int)

,

setPixels(int, int, int, int, ColorModel, int[], int, int)

---

#### getPixels

public

Object

getPixels()

Get the pixel buffer. If the PixelGrabber was not constructed
with an explicit pixel buffer to hold the pixels then this method
will return null until the size and format of the image data is
known.
Since the PixelGrabber may fall back on accumulating the data
in the default RGB ColorModel at any time if the source image
uses more than one ColorModel to deliver the data, the array
object returned by this method may change over time until the
image grab is complete.

getColorModel

```java
public
ColorModel
getColorModel()
```

Get the ColorModel for the pixels stored in the array. If the
PixelGrabber was constructed with an explicit pixel buffer then
this method will always return the default RGB ColorModel,
otherwise it may return null until the ColorModel used by the
ImageProducer is known.
Since the PixelGrabber may fall back on accumulating the data
in the default RGB ColorModel at any time if the source image
uses more than one ColorModel to deliver the data, the ColorModel
object returned by this method may change over time until the
image grab is complete and may not reflect any of the ColorModel
objects that was used by the ImageProducer to deliver the pixels.

**Returns:** the ColorModel object used for storing the pixels
**See Also:** getStatus()

,

ColorModel.getRGBdefault()

,

setColorModel(ColorModel)

---

#### getColorModel

public

ColorModel

getColorModel()

Get the ColorModel for the pixels stored in the array. If the
PixelGrabber was constructed with an explicit pixel buffer then
this method will always return the default RGB ColorModel,
otherwise it may return null until the ColorModel used by the
ImageProducer is known.
Since the PixelGrabber may fall back on accumulating the data
in the default RGB ColorModel at any time if the source image
uses more than one ColorModel to deliver the data, the ColorModel
object returned by this method may change over time until the
image grab is complete and may not reflect any of the ColorModel
objects that was used by the ImageProducer to deliver the pixels.

setDimensions

```java
public void setDimensions​(int width,
int height)
```

The setDimensions method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being grabbed. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

**Specified by:** setDimensions

in interface

ImageConsumer
**Parameters:** width

- the width of the dimension
**Parameters:** height

- the height of the dimension

---

#### setDimensions

public void setDimensions​(int width,
int height)

The setDimensions method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being grabbed. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being grabbed. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

setHints

```java
public void setHints​(int hints)
```

The setHints method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being grabbed. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

**Specified by:** setHints

in interface

ImageConsumer
**Parameters:** hints

- a set of hints used to process the pixels

---

#### setHints

public void setHints​(int hints)

The setHints method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being grabbed. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being grabbed. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

setProperties

```java
public void setProperties​(
Hashtable
<?,​?> props)
```

The setProperties method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being grabbed. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

**Specified by:** setProperties

in interface

ImageConsumer
**Parameters:** props

- the list of properties

---

#### setProperties

public void setProperties​(

Hashtable

<?,​?> props)

The setProperties method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being grabbed. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being grabbed. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

setColorModel

```java
public void setColorModel​(
ColorModel
model)
```

The setColorModel method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being grabbed. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

**Specified by:** setColorModel

in interface

ImageConsumer
**Parameters:** model

- the specified

ColorModel
**See Also:** getColorModel()

---

#### setColorModel

public void setColorModel​(

ColorModel

model)

The setColorModel method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being grabbed. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being grabbed. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

setPixels

```java
public void setPixels​(int srcX,
int srcY,
int srcW,
int srcH,

ColorModel
model,
byte[] pixels,
int srcOff,
int srcScan)
```

The setPixels method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being grabbed. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

**Specified by:** setPixels

in interface

ImageConsumer
**Parameters:** srcX

- the X coordinate of the upper-left corner
of the area of pixels to be set
**Parameters:** srcY

- the Y coordinate of the upper-left corner
of the area of pixels to be set
**Parameters:** srcW

- the width of the area of pixels
**Parameters:** srcH

- the height of the area of pixels
**Parameters:** model

- the specified

ColorModel
**Parameters:** pixels

- the array of pixels
**Parameters:** srcOff

- the offset into the pixels array
**Parameters:** srcScan

- the distance from one row of pixels to the next
in the pixels array
**See Also:** getPixels()

---

#### setPixels

public void setPixels​(int srcX,
int srcY,
int srcW,
int srcH,

ColorModel

model,
byte[] pixels,
int srcOff,
int srcScan)

The setPixels method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being grabbed. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being grabbed. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

setPixels

```java
public void setPixels​(int srcX,
int srcY,
int srcW,
int srcH,

ColorModel
model,
int[] pixels,
int srcOff,
int srcScan)
```

The setPixels method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being grabbed. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

**Specified by:** setPixels

in interface

ImageConsumer
**Parameters:** srcX

- the X coordinate of the upper-left corner
of the area of pixels to be set
**Parameters:** srcY

- the Y coordinate of the upper-left corner
of the area of pixels to be set
**Parameters:** srcW

- the width of the area of pixels
**Parameters:** srcH

- the height of the area of pixels
**Parameters:** model

- the specified

ColorModel
**Parameters:** pixels

- the array of pixels
**Parameters:** srcOff

- the offset into the pixels array
**Parameters:** srcScan

- the distance from one row of pixels to the next
in the pixels array
**See Also:** getPixels()

---

#### setPixels

public void setPixels​(int srcX,
int srcY,
int srcW,
int srcH,

ColorModel

model,
int[] pixels,
int srcOff,
int srcScan)

The setPixels method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being grabbed. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being grabbed. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

imageComplete

```java
public void imageComplete​(int status)
```

The imageComplete method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being grabbed. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

**Specified by:** imageComplete

in interface

ImageConsumer
**Parameters:** status

- the status of image loading
**See Also:** ImageProducer.removeConsumer(java.awt.image.ImageConsumer)

---

#### imageComplete

public void imageComplete​(int status)

The imageComplete method is part of the ImageConsumer API which
this class must implement to retrieve the pixels.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being grabbed. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

Note: This method is intended to be called by the ImageProducer
of the Image whose pixels are being grabbed. Developers using
this class to retrieve pixels from an image should avoid calling
this method directly since that operation could result in problems
with retrieving the requested pixels.

status

```java
public int status()
```

Returns the status of the pixels. The ImageObserver flags
representing the available pixel information are returned.
This method and

getStatus

have the
same implementation, but

getStatus

is the
preferred method because it conforms to the convention of
naming information-retrieval methods with the form
"getXXX".

**Returns:** the bitwise OR of all relevant ImageObserver flags
**See Also:** ImageObserver

,

getStatus()

---

#### status

public int status()

Returns the status of the pixels. The ImageObserver flags
representing the available pixel information are returned.
This method and

getStatus

have the
same implementation, but

getStatus

is the
preferred method because it conforms to the convention of
naming information-retrieval methods with the form
"getXXX".

---

