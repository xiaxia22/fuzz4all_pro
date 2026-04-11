# Class MemoryImageSource

**Source:** `java.desktop\java\awt\image\MemoryImageSource.html`

### Class Description

```java
public class
MemoryImageSource

extends
Object

implements
ImageProducer
```

This class is an implementation of the ImageProducer interface which
uses an array to produce pixel values for an Image. Here is an example
which calculates a 100x100 image representing a fade from black to blue
along the X axis and a fade from black to red along the Y axis:

```java
int w = 100;
int h = 100;
int pix[] = new int[w * h];
int index = 0;
for (int y = 0; y < h; y++) {
int red = (y * 255) / (h - 1);
for (int x = 0; x < w; x++) {
int blue = (x * 255) / (w - 1);
pix[index++] = (255 << 24) | (red << 16) | blue;
}
}
Image img = createImage(new MemoryImageSource(w, h, pix, 0, w));
```

The MemoryImageSource is also capable of managing a memory image which
varies over time to allow animation or custom rendering. Here is an
example showing how to set up the animation source and signal changes
in the data (adapted from the MemoryAnimationSourceDemo by Garth Dickie):

```java
int pixels[];
MemoryImageSource source;

public void init() {
int width = 50;
int height = 50;
int size = width * height;
pixels = new int[size];

int value = getBackground().getRGB();
for (int i = 0; i < size; i++) {
pixels[i] = value;
}

source = new MemoryImageSource(width, height, pixels, 0, width);
source.setAnimated(true);
image = createImage(source);
}

public void run() {
Thread me = Thread.currentThread( );
me.setPriority(Thread.MIN_PRIORITY);

while (true) {
try {
Thread.sleep(10);
} catch( InterruptedException e ) {
return;
}

// Modify the values in the pixels array at (x, y, w, h)

// Send the new data to the interested ImageConsumers
source.newPixels(x, y, w, h);
}
}
```

**All Implemented Interfaces:** ImageProducer

---

### Field Details

*No entries found.*

### Constructor Details

#### public MemoryImageSource​(int w,
int h,

ColorModel
cm,
byte[] pix,
int off,
int scan)

Constructs an ImageProducer object which uses an array of bytes
to produce data for an Image object.

**Parameters:**
- w

- the width of the rectangle of pixels
- h

- the height of the rectangle of pixels
- cm

- the specified

ColorModel
- pix

- an array of pixels
- off

- the offset into the array of where to store the
first pixel
- scan

- the distance from one row of pixels to the next in
the array

**See Also:**
- Component.createImage(java.awt.image.ImageProducer)

---

#### public MemoryImageSource​(int w,
int h,

ColorModel
cm,
byte[] pix,
int off,
int scan,

Hashtable
<?,​?> props)

Constructs an ImageProducer object which uses an array of bytes
to produce data for an Image object.

**Parameters:**
- w

- the width of the rectangle of pixels
- h

- the height of the rectangle of pixels
- cm

- the specified

ColorModel
- pix

- an array of pixels
- off

- the offset into the array of where to store the
first pixel
- scan

- the distance from one row of pixels to the next in
the array
- props

- a list of properties that the

ImageProducer

uses to process an image

**See Also:**
- Component.createImage(java.awt.image.ImageProducer)

---

#### public MemoryImageSource​(int w,
int h,

ColorModel
cm,
int[] pix,
int off,
int scan)

Constructs an ImageProducer object which uses an array of integers
to produce data for an Image object.

**Parameters:**
- w

- the width of the rectangle of pixels
- h

- the height of the rectangle of pixels
- cm

- the specified

ColorModel
- pix

- an array of pixels
- off

- the offset into the array of where to store the
first pixel
- scan

- the distance from one row of pixels to the next in
the array

**See Also:**
- Component.createImage(java.awt.image.ImageProducer)

---

#### public MemoryImageSource​(int w,
int h,

ColorModel
cm,
int[] pix,
int off,
int scan,

Hashtable
<?,​?> props)

Constructs an ImageProducer object which uses an array of integers
to produce data for an Image object.

**Parameters:**
- w

- the width of the rectangle of pixels
- h

- the height of the rectangle of pixels
- cm

- the specified

ColorModel
- pix

- an array of pixels
- off

- the offset into the array of where to store the
first pixel
- scan

- the distance from one row of pixels to the next in
the array
- props

- a list of properties that the

ImageProducer

uses to process an image

**See Also:**
- Component.createImage(java.awt.image.ImageProducer)

---

#### public MemoryImageSource​(int w,
int h,
int[] pix,
int off,
int scan)

Constructs an ImageProducer object which uses an array of integers
in the default RGB ColorModel to produce data for an Image object.

**Parameters:**
- w

- the width of the rectangle of pixels
- h

- the height of the rectangle of pixels
- pix

- an array of pixels
- off

- the offset into the array of where to store the
first pixel
- scan

- the distance from one row of pixels to the next in
the array

**See Also:**
- Component.createImage(java.awt.image.ImageProducer)

,

ColorModel.getRGBdefault()

---

#### public MemoryImageSource​(int w,
int h,
int[] pix,
int off,
int scan,

Hashtable
<?,​?> props)

Constructs an ImageProducer object which uses an array of integers
in the default RGB ColorModel to produce data for an Image object.

**Parameters:**
- w

- the width of the rectangle of pixels
- h

- the height of the rectangle of pixels
- pix

- an array of pixels
- off

- the offset into the array of where to store the
first pixel
- scan

- the distance from one row of pixels to the next in
the array
- props

- a list of properties that the

ImageProducer

uses to process an image

**See Also:**
- Component.createImage(java.awt.image.ImageProducer)

,

ColorModel.getRGBdefault()

---

### Method Details

#### public void addConsumer​(
ImageConsumer
ic)

Adds an ImageConsumer to the list of consumers interested in
data for this image.

**Specified by:**
- addConsumer

in interface

ImageProducer

**Parameters:**
- ic

- the specified

ImageConsumer

**Throws:**
- NullPointerException

- if the specified

ImageConsumer

is null

**See Also:**
- ImageConsumer

---

#### public boolean isConsumer​(
ImageConsumer
ic)

Determines if an ImageConsumer is on the list of consumers currently
interested in data for this image.

**Specified by:**
- isConsumer

in interface

ImageProducer

**Parameters:**
- ic

- the specified

ImageConsumer

**Returns:**
- true

if the

ImageConsumer

is on the list;

false

otherwise.

**See Also:**
- ImageConsumer

---

#### public void removeConsumer​(
ImageConsumer
ic)

Removes an ImageConsumer from the list of consumers interested in
data for this image.

**Specified by:**
- removeConsumer

in interface

ImageProducer

**Parameters:**
- ic

- the specified

ImageConsumer

**See Also:**
- ImageConsumer

---

#### public void startProduction​(
ImageConsumer
ic)

Adds an ImageConsumer to the list of consumers interested in
data for this image and immediately starts delivery of the
image data through the ImageConsumer interface.

**Specified by:**
- startProduction

in interface

ImageProducer

**Parameters:**
- ic

- the specified

ImageConsumer

image data through the ImageConsumer interface.

**See Also:**
- ImageConsumer

---

#### public void requestTopDownLeftRightResend​(
ImageConsumer
ic)

Requests that a given ImageConsumer have the image data delivered
one more time in top-down, left-right order.

**Specified by:**
- requestTopDownLeftRightResend

in interface

ImageProducer

**Parameters:**
- ic

- the specified

ImageConsumer

**See Also:**
- ImageConsumer

---

#### public void setAnimated​(boolean animated)

Changes this memory image into a multi-frame animation or a
single-frame static image depending on the animated parameter.

This method should be called immediately after the
MemoryImageSource is constructed and before an image is
created with it to ensure that all ImageConsumers will
receive the correct multi-frame data. If an ImageConsumer
is added to this ImageProducer before this flag is set then
that ImageConsumer will see only a snapshot of the pixel
data that was available when it connected.

**Parameters:**
- animated

-

true

if the image is a
multi-frame animation

---

#### public void setFullBufferUpdates​(boolean fullbuffers)

Specifies whether this animated memory image should always be
updated by sending the complete buffer of pixels whenever
there is a change.
This flag is ignored if the animation flag is not turned on
through the setAnimated() method.

This method should be called immediately after the
MemoryImageSource is constructed and before an image is
created with it to ensure that all ImageConsumers will
receive the correct pixel delivery hints.

**Parameters:**
- fullbuffers

-

true

if the complete pixel
buffer should always
be sent

**See Also:**
- setAnimated(boolean)

---

#### public void newPixels()

Sends a whole new buffer of pixels to any ImageConsumers that
are currently interested in the data for this image and notify
them that an animation frame is complete.
This method only has effect if the animation flag has been
turned on through the setAnimated() method.

**See Also:**
- newPixels(int, int, int, int, boolean)

,

ImageConsumer

,

setAnimated(boolean)

---

#### public void newPixels​(int x,
int y,
int w,
int h)

Sends a rectangular region of the buffer of pixels to any
ImageConsumers that are currently interested in the data for
this image and notify them that an animation frame is complete.
This method only has effect if the animation flag has been
turned on through the setAnimated() method.
If the full buffer update flag was turned on with the
setFullBufferUpdates() method then the rectangle parameters
will be ignored and the entire buffer will always be sent.

**Parameters:**
- x

- the x coordinate of the upper left corner of the rectangle
of pixels to be sent
- y

- the y coordinate of the upper left corner of the rectangle
of pixels to be sent
- w

- the width of the rectangle of pixels to be sent
- h

- the height of the rectangle of pixels to be sent

**See Also:**
- newPixels(int, int, int, int, boolean)

,

ImageConsumer

,

setAnimated(boolean)

,

setFullBufferUpdates(boolean)

---

#### public void newPixels​(int x,
int y,
int w,
int h,
boolean framenotify)

Sends a rectangular region of the buffer of pixels to any
ImageConsumers that are currently interested in the data for
this image.
If the framenotify parameter is true then the consumers are
also notified that an animation frame is complete.
This method only has effect if the animation flag has been
turned on through the setAnimated() method.
If the full buffer update flag was turned on with the
setFullBufferUpdates() method then the rectangle parameters
will be ignored and the entire buffer will always be sent.

**Parameters:**
- x

- the x coordinate of the upper left corner of the rectangle
of pixels to be sent
- y

- the y coordinate of the upper left corner of the rectangle
of pixels to be sent
- w

- the width of the rectangle of pixels to be sent
- h

- the height of the rectangle of pixels to be sent
- framenotify

-

true

if the consumers should be sent a

SINGLEFRAMEDONE

notification

**See Also:**
- ImageConsumer

,

setAnimated(boolean)

,

setFullBufferUpdates(boolean)

---

#### public void newPixels​(byte[] newpix,

ColorModel
newmodel,
int offset,
int scansize)

Changes to a new byte array to hold the pixels for this image.
If the animation flag has been turned on through the setAnimated()
method, then the new pixels will be immediately delivered to any
ImageConsumers that are currently interested in the data for
this image.

**Parameters:**
- newpix

- the new pixel array
- newmodel

- the specified

ColorModel
- offset

- the offset into the array
- scansize

- the distance from one row of pixels to the next in
the array

**See Also:**
- newPixels(int, int, int, int, boolean)

,

setAnimated(boolean)

---

#### public void newPixels​(int[] newpix,

ColorModel
newmodel,
int offset,
int scansize)

Changes to a new int array to hold the pixels for this image.
If the animation flag has been turned on through the setAnimated()
method, then the new pixels will be immediately delivered to any
ImageConsumers that are currently interested in the data for
this image.

**Parameters:**
- newpix

- the new pixel array
- newmodel

- the specified

ColorModel
- offset

- the offset into the array
- scansize

- the distance from one row of pixels to the next in
the array

**See Also:**
- newPixels(int, int, int, int, boolean)

,

setAnimated(boolean)

---

### Additional Sections

#### Class MemoryImageSource

java.lang.Object

- java.awt.image.MemoryImageSource

java.awt.image.MemoryImageSource

**All Implemented Interfaces:** ImageProducer

```java
public class
MemoryImageSource

extends
Object

implements
ImageProducer
```

This class is an implementation of the ImageProducer interface which
uses an array to produce pixel values for an Image. Here is an example
which calculates a 100x100 image representing a fade from black to blue
along the X axis and a fade from black to red along the Y axis:

```java
int w = 100;
int h = 100;
int pix[] = new int[w * h];
int index = 0;
for (int y = 0; y < h; y++) {
int red = (y * 255) / (h - 1);
for (int x = 0; x < w; x++) {
int blue = (x * 255) / (w - 1);
pix[index++] = (255 << 24) | (red << 16) | blue;
}
}
Image img = createImage(new MemoryImageSource(w, h, pix, 0, w));
```

The MemoryImageSource is also capable of managing a memory image which
varies over time to allow animation or custom rendering. Here is an
example showing how to set up the animation source and signal changes
in the data (adapted from the MemoryAnimationSourceDemo by Garth Dickie):

```java
int pixels[];
MemoryImageSource source;

public void init() {
int width = 50;
int height = 50;
int size = width * height;
pixels = new int[size];

int value = getBackground().getRGB();
for (int i = 0; i < size; i++) {
pixels[i] = value;
}

source = new MemoryImageSource(width, height, pixels, 0, width);
source.setAnimated(true);
image = createImage(source);
}

public void run() {
Thread me = Thread.currentThread( );
me.setPriority(Thread.MIN_PRIORITY);

while (true) {
try {
Thread.sleep(10);
} catch( InterruptedException e ) {
return;
}

// Modify the values in the pixels array at (x, y, w, h)

// Send the new data to the interested ImageConsumers
source.newPixels(x, y, w, h);
}
}
```

**See Also:** ImageProducer

public class

MemoryImageSource

extends

Object

implements

ImageProducer

This class is an implementation of the ImageProducer interface which
uses an array to produce pixel values for an Image. Here is an example
which calculates a 100x100 image representing a fade from black to blue
along the X axis and a fade from black to red along the Y axis:

```java
int w = 100;
int h = 100;
int pix[] = new int[w * h];
int index = 0;
for (int y = 0; y < h; y++) {
int red = (y * 255) / (h - 1);
for (int x = 0; x < w; x++) {
int blue = (x * 255) / (w - 1);
pix[index++] = (255 << 24) | (red << 16) | blue;
}
}
Image img = createImage(new MemoryImageSource(w, h, pix, 0, w));
```

The MemoryImageSource is also capable of managing a memory image which
varies over time to allow animation or custom rendering. Here is an
example showing how to set up the animation source and signal changes
in the data (adapted from the MemoryAnimationSourceDemo by Garth Dickie):

```java
int pixels[];
MemoryImageSource source;

public void init() {
int width = 50;
int height = 50;
int size = width * height;
pixels = new int[size];

int value = getBackground().getRGB();
for (int i = 0; i < size; i++) {
pixels[i] = value;
}

source = new MemoryImageSource(width, height, pixels, 0, width);
source.setAnimated(true);
image = createImage(source);
}

public void run() {
Thread me = Thread.currentThread( );
me.setPriority(Thread.MIN_PRIORITY);

while (true) {
try {
Thread.sleep(10);
} catch( InterruptedException e ) {
return;
}

// Modify the values in the pixels array at (x, y, w, h)

// Send the new data to the interested ImageConsumers
source.newPixels(x, y, w, h);
}
}
```

int w = 100;
int h = 100;
int pix[] = new int[w * h];
int index = 0;
for (int y = 0; y < h; y++) {
int red = (y * 255) / (h - 1);
for (int x = 0; x < w; x++) {
int blue = (x * 255) / (w - 1);
pix[index++] = (255 << 24) | (red << 16) | blue;
}
}
Image img = createImage(new MemoryImageSource(w, h, pix, 0, w));

int pixels[];
MemoryImageSource source;

public void init() {
int width = 50;
int height = 50;
int size = width * height;
pixels = new int[size];

int value = getBackground().getRGB();
for (int i = 0; i < size; i++) {
pixels[i] = value;
}

source = new MemoryImageSource(width, height, pixels, 0, width);
source.setAnimated(true);
image = createImage(source);
}

public void run() {
Thread me = Thread.currentThread( );
me.setPriority(Thread.MIN_PRIORITY);

while (true) {
try {
Thread.sleep(10);
} catch( InterruptedException e ) {
return;
}

// Modify the values in the pixels array at (x, y, w, h)

// Send the new data to the interested ImageConsumers
source.newPixels(x, y, w, h);
}
}

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MemoryImageSource

​(int w,
int h,
int[] pix,
int off,
int scan)

Constructs an ImageProducer object which uses an array of integers
in the default RGB ColorModel to produce data for an Image object.

MemoryImageSource

​(int w,
int h,
int[] pix,
int off,
int scan,

Hashtable

<?,​?> props)

Constructs an ImageProducer object which uses an array of integers
in the default RGB ColorModel to produce data for an Image object.

MemoryImageSource

​(int w,
int h,

ColorModel

cm,
byte[] pix,
int off,
int scan)

Constructs an ImageProducer object which uses an array of bytes
to produce data for an Image object.

MemoryImageSource

​(int w,
int h,

ColorModel

cm,
byte[] pix,
int off,
int scan,

Hashtable

<?,​?> props)

Constructs an ImageProducer object which uses an array of bytes
to produce data for an Image object.

MemoryImageSource

​(int w,
int h,

ColorModel

cm,
int[] pix,
int off,
int scan)

Constructs an ImageProducer object which uses an array of integers
to produce data for an Image object.

MemoryImageSource

​(int w,
int h,

ColorModel

cm,
int[] pix,
int off,
int scan,

Hashtable

<?,​?> props)

Constructs an ImageProducer object which uses an array of integers
to produce data for an Image object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addConsumer

​(

ImageConsumer

ic)

Adds an ImageConsumer to the list of consumers interested in
data for this image.

boolean

isConsumer

​(

ImageConsumer

ic)

Determines if an ImageConsumer is on the list of consumers currently
interested in data for this image.

void

newPixels

()

Sends a whole new buffer of pixels to any ImageConsumers that
are currently interested in the data for this image and notify
them that an animation frame is complete.

void

newPixels

​(byte[] newpix,

ColorModel

newmodel,
int offset,
int scansize)

Changes to a new byte array to hold the pixels for this image.

void

newPixels

​(int[] newpix,

ColorModel

newmodel,
int offset,
int scansize)

Changes to a new int array to hold the pixels for this image.

void

newPixels

​(int x,
int y,
int w,
int h)

Sends a rectangular region of the buffer of pixels to any
ImageConsumers that are currently interested in the data for
this image and notify them that an animation frame is complete.

void

newPixels

​(int x,
int y,
int w,
int h,
boolean framenotify)

Sends a rectangular region of the buffer of pixels to any
ImageConsumers that are currently interested in the data for
this image.

void

removeConsumer

​(

ImageConsumer

ic)

Removes an ImageConsumer from the list of consumers interested in
data for this image.

void

requestTopDownLeftRightResend

​(

ImageConsumer

ic)

Requests that a given ImageConsumer have the image data delivered
one more time in top-down, left-right order.

void

setAnimated

​(boolean animated)

Changes this memory image into a multi-frame animation or a
single-frame static image depending on the animated parameter.

void

setFullBufferUpdates

​(boolean fullbuffers)

Specifies whether this animated memory image should always be
updated by sending the complete buffer of pixels whenever
there is a change.

void

startProduction

​(

ImageConsumer

ic)

Adds an ImageConsumer to the list of consumers interested in
data for this image and immediately starts delivery of the
image data through the ImageConsumer interface.

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

MemoryImageSource

​(int w,
int h,
int[] pix,
int off,
int scan)

Constructs an ImageProducer object which uses an array of integers
in the default RGB ColorModel to produce data for an Image object.

MemoryImageSource

​(int w,
int h,
int[] pix,
int off,
int scan,

Hashtable

<?,​?> props)

Constructs an ImageProducer object which uses an array of integers
in the default RGB ColorModel to produce data for an Image object.

MemoryImageSource

​(int w,
int h,

ColorModel

cm,
byte[] pix,
int off,
int scan)

Constructs an ImageProducer object which uses an array of bytes
to produce data for an Image object.

MemoryImageSource

​(int w,
int h,

ColorModel

cm,
byte[] pix,
int off,
int scan,

Hashtable

<?,​?> props)

Constructs an ImageProducer object which uses an array of bytes
to produce data for an Image object.

MemoryImageSource

​(int w,
int h,

ColorModel

cm,
int[] pix,
int off,
int scan)

Constructs an ImageProducer object which uses an array of integers
to produce data for an Image object.

MemoryImageSource

​(int w,
int h,

ColorModel

cm,
int[] pix,
int off,
int scan,

Hashtable

<?,​?> props)

Constructs an ImageProducer object which uses an array of integers
to produce data for an Image object.

---

#### Constructor Summary

Constructs an ImageProducer object which uses an array of integers
in the default RGB ColorModel to produce data for an Image object.

Constructs an ImageProducer object which uses an array of bytes
to produce data for an Image object.

Constructs an ImageProducer object which uses an array of integers
to produce data for an Image object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addConsumer

​(

ImageConsumer

ic)

Adds an ImageConsumer to the list of consumers interested in
data for this image.

boolean

isConsumer

​(

ImageConsumer

ic)

Determines if an ImageConsumer is on the list of consumers currently
interested in data for this image.

void

newPixels

()

Sends a whole new buffer of pixels to any ImageConsumers that
are currently interested in the data for this image and notify
them that an animation frame is complete.

void

newPixels

​(byte[] newpix,

ColorModel

newmodel,
int offset,
int scansize)

Changes to a new byte array to hold the pixels for this image.

void

newPixels

​(int[] newpix,

ColorModel

newmodel,
int offset,
int scansize)

Changes to a new int array to hold the pixels for this image.

void

newPixels

​(int x,
int y,
int w,
int h)

Sends a rectangular region of the buffer of pixels to any
ImageConsumers that are currently interested in the data for
this image and notify them that an animation frame is complete.

void

newPixels

​(int x,
int y,
int w,
int h,
boolean framenotify)

Sends a rectangular region of the buffer of pixels to any
ImageConsumers that are currently interested in the data for
this image.

void

removeConsumer

​(

ImageConsumer

ic)

Removes an ImageConsumer from the list of consumers interested in
data for this image.

void

requestTopDownLeftRightResend

​(

ImageConsumer

ic)

Requests that a given ImageConsumer have the image data delivered
one more time in top-down, left-right order.

void

setAnimated

​(boolean animated)

Changes this memory image into a multi-frame animation or a
single-frame static image depending on the animated parameter.

void

setFullBufferUpdates

​(boolean fullbuffers)

Specifies whether this animated memory image should always be
updated by sending the complete buffer of pixels whenever
there is a change.

void

startProduction

​(

ImageConsumer

ic)

Adds an ImageConsumer to the list of consumers interested in
data for this image and immediately starts delivery of the
image data through the ImageConsumer interface.

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

Adds an ImageConsumer to the list of consumers interested in
data for this image.

Determines if an ImageConsumer is on the list of consumers currently
interested in data for this image.

Sends a whole new buffer of pixels to any ImageConsumers that
are currently interested in the data for this image and notify
them that an animation frame is complete.

Changes to a new byte array to hold the pixels for this image.

Changes to a new int array to hold the pixels for this image.

Sends a rectangular region of the buffer of pixels to any
ImageConsumers that are currently interested in the data for
this image and notify them that an animation frame is complete.

Sends a rectangular region of the buffer of pixels to any
ImageConsumers that are currently interested in the data for
this image.

Removes an ImageConsumer from the list of consumers interested in
data for this image.

Requests that a given ImageConsumer have the image data delivered
one more time in top-down, left-right order.

Changes this memory image into a multi-frame animation or a
single-frame static image depending on the animated parameter.

Specifies whether this animated memory image should always be
updated by sending the complete buffer of pixels whenever
there is a change.

Adds an ImageConsumer to the list of consumers interested in
data for this image and immediately starts delivery of the
image data through the ImageConsumer interface.

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

- MemoryImageSource

```java
public MemoryImageSource​(int w,
int h,

ColorModel
cm,
byte[] pix,
int off,
int scan)
```

Constructs an ImageProducer object which uses an array of bytes
to produce data for an Image object.

**Parameters:** w

- the width of the rectangle of pixels
**Parameters:** h

- the height of the rectangle of pixels
**Parameters:** cm

- the specified

ColorModel
**Parameters:** pix

- an array of pixels
**Parameters:** off

- the offset into the array of where to store the
first pixel
**Parameters:** scan

- the distance from one row of pixels to the next in
the array
**See Also:** Component.createImage(java.awt.image.ImageProducer)

- MemoryImageSource

```java
public MemoryImageSource​(int w,
int h,

ColorModel
cm,
byte[] pix,
int off,
int scan,

Hashtable
<?,​?> props)
```

Constructs an ImageProducer object which uses an array of bytes
to produce data for an Image object.

**Parameters:** w

- the width of the rectangle of pixels
**Parameters:** h

- the height of the rectangle of pixels
**Parameters:** cm

- the specified

ColorModel
**Parameters:** pix

- an array of pixels
**Parameters:** off

- the offset into the array of where to store the
first pixel
**Parameters:** scan

- the distance from one row of pixels to the next in
the array
**Parameters:** props

- a list of properties that the

ImageProducer

uses to process an image
**See Also:** Component.createImage(java.awt.image.ImageProducer)

- MemoryImageSource

```java
public MemoryImageSource​(int w,
int h,

ColorModel
cm,
int[] pix,
int off,
int scan)
```

Constructs an ImageProducer object which uses an array of integers
to produce data for an Image object.

**Parameters:** w

- the width of the rectangle of pixels
**Parameters:** h

- the height of the rectangle of pixels
**Parameters:** cm

- the specified

ColorModel
**Parameters:** pix

- an array of pixels
**Parameters:** off

- the offset into the array of where to store the
first pixel
**Parameters:** scan

- the distance from one row of pixels to the next in
the array
**See Also:** Component.createImage(java.awt.image.ImageProducer)

- MemoryImageSource

```java
public MemoryImageSource​(int w,
int h,

ColorModel
cm,
int[] pix,
int off,
int scan,

Hashtable
<?,​?> props)
```

Constructs an ImageProducer object which uses an array of integers
to produce data for an Image object.

**Parameters:** w

- the width of the rectangle of pixels
**Parameters:** h

- the height of the rectangle of pixels
**Parameters:** cm

- the specified

ColorModel
**Parameters:** pix

- an array of pixels
**Parameters:** off

- the offset into the array of where to store the
first pixel
**Parameters:** scan

- the distance from one row of pixels to the next in
the array
**Parameters:** props

- a list of properties that the

ImageProducer

uses to process an image
**See Also:** Component.createImage(java.awt.image.ImageProducer)

- MemoryImageSource

```java
public MemoryImageSource​(int w,
int h,
int[] pix,
int off,
int scan)
```

Constructs an ImageProducer object which uses an array of integers
in the default RGB ColorModel to produce data for an Image object.

**Parameters:** w

- the width of the rectangle of pixels
**Parameters:** h

- the height of the rectangle of pixels
**Parameters:** pix

- an array of pixels
**Parameters:** off

- the offset into the array of where to store the
first pixel
**Parameters:** scan

- the distance from one row of pixels to the next in
the array
**See Also:** Component.createImage(java.awt.image.ImageProducer)

,

ColorModel.getRGBdefault()

- MemoryImageSource

```java
public MemoryImageSource​(int w,
int h,
int[] pix,
int off,
int scan,

Hashtable
<?,​?> props)
```

Constructs an ImageProducer object which uses an array of integers
in the default RGB ColorModel to produce data for an Image object.

**Parameters:** w

- the width of the rectangle of pixels
**Parameters:** h

- the height of the rectangle of pixels
**Parameters:** pix

- an array of pixels
**Parameters:** off

- the offset into the array of where to store the
first pixel
**Parameters:** scan

- the distance from one row of pixels to the next in
the array
**Parameters:** props

- a list of properties that the

ImageProducer

uses to process an image
**See Also:** Component.createImage(java.awt.image.ImageProducer)

,

ColorModel.getRGBdefault()

============ METHOD DETAIL ==========

- Method Detail

- addConsumer

```java
public void addConsumer​(
ImageConsumer
ic)
```

Adds an ImageConsumer to the list of consumers interested in
data for this image.

**Specified by:** addConsumer

in interface

ImageProducer
**Parameters:** ic

- the specified

ImageConsumer
**Throws:** NullPointerException

- if the specified

ImageConsumer

is null
**See Also:** ImageConsumer

- isConsumer

```java
public boolean isConsumer​(
ImageConsumer
ic)
```

Determines if an ImageConsumer is on the list of consumers currently
interested in data for this image.

**Specified by:** isConsumer

in interface

ImageProducer
**Parameters:** ic

- the specified

ImageConsumer
**Returns:** true

if the

ImageConsumer

is on the list;

false

otherwise.
**See Also:** ImageConsumer

- removeConsumer

```java
public void removeConsumer​(
ImageConsumer
ic)
```

Removes an ImageConsumer from the list of consumers interested in
data for this image.

**Specified by:** removeConsumer

in interface

ImageProducer
**Parameters:** ic

- the specified

ImageConsumer
**See Also:** ImageConsumer

- startProduction

```java
public void startProduction​(
ImageConsumer
ic)
```

Adds an ImageConsumer to the list of consumers interested in
data for this image and immediately starts delivery of the
image data through the ImageConsumer interface.

**Specified by:** startProduction

in interface

ImageProducer
**Parameters:** ic

- the specified

ImageConsumer

image data through the ImageConsumer interface.
**See Also:** ImageConsumer

- requestTopDownLeftRightResend

```java
public void requestTopDownLeftRightResend​(
ImageConsumer
ic)
```

Requests that a given ImageConsumer have the image data delivered
one more time in top-down, left-right order.

**Specified by:** requestTopDownLeftRightResend

in interface

ImageProducer
**Parameters:** ic

- the specified

ImageConsumer
**See Also:** ImageConsumer

- setAnimated

```java
public void setAnimated​(boolean animated)
```

Changes this memory image into a multi-frame animation or a
single-frame static image depending on the animated parameter.

This method should be called immediately after the
MemoryImageSource is constructed and before an image is
created with it to ensure that all ImageConsumers will
receive the correct multi-frame data. If an ImageConsumer
is added to this ImageProducer before this flag is set then
that ImageConsumer will see only a snapshot of the pixel
data that was available when it connected.

**Parameters:** animated

-

true

if the image is a
multi-frame animation

- setFullBufferUpdates

```java
public void setFullBufferUpdates​(boolean fullbuffers)
```

Specifies whether this animated memory image should always be
updated by sending the complete buffer of pixels whenever
there is a change.
This flag is ignored if the animation flag is not turned on
through the setAnimated() method.

This method should be called immediately after the
MemoryImageSource is constructed and before an image is
created with it to ensure that all ImageConsumers will
receive the correct pixel delivery hints.

**Parameters:** fullbuffers

-

true

if the complete pixel
buffer should always
be sent
**See Also:** setAnimated(boolean)

- newPixels

```java
public void newPixels()
```

Sends a whole new buffer of pixels to any ImageConsumers that
are currently interested in the data for this image and notify
them that an animation frame is complete.
This method only has effect if the animation flag has been
turned on through the setAnimated() method.

**See Also:** newPixels(int, int, int, int, boolean)

,

ImageConsumer

,

setAnimated(boolean)

- newPixels

```java
public void newPixels​(int x,
int y,
int w,
int h)
```

Sends a rectangular region of the buffer of pixels to any
ImageConsumers that are currently interested in the data for
this image and notify them that an animation frame is complete.
This method only has effect if the animation flag has been
turned on through the setAnimated() method.
If the full buffer update flag was turned on with the
setFullBufferUpdates() method then the rectangle parameters
will be ignored and the entire buffer will always be sent.

**Parameters:** x

- the x coordinate of the upper left corner of the rectangle
of pixels to be sent
**Parameters:** y

- the y coordinate of the upper left corner of the rectangle
of pixels to be sent
**Parameters:** w

- the width of the rectangle of pixels to be sent
**Parameters:** h

- the height of the rectangle of pixels to be sent
**See Also:** newPixels(int, int, int, int, boolean)

,

ImageConsumer

,

setAnimated(boolean)

,

setFullBufferUpdates(boolean)

- newPixels

```java
public void newPixels​(int x,
int y,
int w,
int h,
boolean framenotify)
```

Sends a rectangular region of the buffer of pixels to any
ImageConsumers that are currently interested in the data for
this image.
If the framenotify parameter is true then the consumers are
also notified that an animation frame is complete.
This method only has effect if the animation flag has been
turned on through the setAnimated() method.
If the full buffer update flag was turned on with the
setFullBufferUpdates() method then the rectangle parameters
will be ignored and the entire buffer will always be sent.

**Parameters:** x

- the x coordinate of the upper left corner of the rectangle
of pixels to be sent
**Parameters:** y

- the y coordinate of the upper left corner of the rectangle
of pixels to be sent
**Parameters:** w

- the width of the rectangle of pixels to be sent
**Parameters:** h

- the height of the rectangle of pixels to be sent
**Parameters:** framenotify

-

true

if the consumers should be sent a

SINGLEFRAMEDONE

notification
**See Also:** ImageConsumer

,

setAnimated(boolean)

,

setFullBufferUpdates(boolean)

- newPixels

```java
public void newPixels​(byte[] newpix,

ColorModel
newmodel,
int offset,
int scansize)
```

Changes to a new byte array to hold the pixels for this image.
If the animation flag has been turned on through the setAnimated()
method, then the new pixels will be immediately delivered to any
ImageConsumers that are currently interested in the data for
this image.

**Parameters:** newpix

- the new pixel array
**Parameters:** newmodel

- the specified

ColorModel
**Parameters:** offset

- the offset into the array
**Parameters:** scansize

- the distance from one row of pixels to the next in
the array
**See Also:** newPixels(int, int, int, int, boolean)

,

setAnimated(boolean)

- newPixels

```java
public void newPixels​(int[] newpix,

ColorModel
newmodel,
int offset,
int scansize)
```

Changes to a new int array to hold the pixels for this image.
If the animation flag has been turned on through the setAnimated()
method, then the new pixels will be immediately delivered to any
ImageConsumers that are currently interested in the data for
this image.

**Parameters:** newpix

- the new pixel array
**Parameters:** newmodel

- the specified

ColorModel
**Parameters:** offset

- the offset into the array
**Parameters:** scansize

- the distance from one row of pixels to the next in
the array
**See Also:** newPixels(int, int, int, int, boolean)

,

setAnimated(boolean)

Constructor Detail

- MemoryImageSource

```java
public MemoryImageSource​(int w,
int h,

ColorModel
cm,
byte[] pix,
int off,
int scan)
```

Constructs an ImageProducer object which uses an array of bytes
to produce data for an Image object.

**Parameters:** w

- the width of the rectangle of pixels
**Parameters:** h

- the height of the rectangle of pixels
**Parameters:** cm

- the specified

ColorModel
**Parameters:** pix

- an array of pixels
**Parameters:** off

- the offset into the array of where to store the
first pixel
**Parameters:** scan

- the distance from one row of pixels to the next in
the array
**See Also:** Component.createImage(java.awt.image.ImageProducer)

- MemoryImageSource

```java
public MemoryImageSource​(int w,
int h,

ColorModel
cm,
byte[] pix,
int off,
int scan,

Hashtable
<?,​?> props)
```

Constructs an ImageProducer object which uses an array of bytes
to produce data for an Image object.

**Parameters:** w

- the width of the rectangle of pixels
**Parameters:** h

- the height of the rectangle of pixels
**Parameters:** cm

- the specified

ColorModel
**Parameters:** pix

- an array of pixels
**Parameters:** off

- the offset into the array of where to store the
first pixel
**Parameters:** scan

- the distance from one row of pixels to the next in
the array
**Parameters:** props

- a list of properties that the

ImageProducer

uses to process an image
**See Also:** Component.createImage(java.awt.image.ImageProducer)

- MemoryImageSource

```java
public MemoryImageSource​(int w,
int h,

ColorModel
cm,
int[] pix,
int off,
int scan)
```

Constructs an ImageProducer object which uses an array of integers
to produce data for an Image object.

**Parameters:** w

- the width of the rectangle of pixels
**Parameters:** h

- the height of the rectangle of pixels
**Parameters:** cm

- the specified

ColorModel
**Parameters:** pix

- an array of pixels
**Parameters:** off

- the offset into the array of where to store the
first pixel
**Parameters:** scan

- the distance from one row of pixels to the next in
the array
**See Also:** Component.createImage(java.awt.image.ImageProducer)

- MemoryImageSource

```java
public MemoryImageSource​(int w,
int h,

ColorModel
cm,
int[] pix,
int off,
int scan,

Hashtable
<?,​?> props)
```

Constructs an ImageProducer object which uses an array of integers
to produce data for an Image object.

**Parameters:** w

- the width of the rectangle of pixels
**Parameters:** h

- the height of the rectangle of pixels
**Parameters:** cm

- the specified

ColorModel
**Parameters:** pix

- an array of pixels
**Parameters:** off

- the offset into the array of where to store the
first pixel
**Parameters:** scan

- the distance from one row of pixels to the next in
the array
**Parameters:** props

- a list of properties that the

ImageProducer

uses to process an image
**See Also:** Component.createImage(java.awt.image.ImageProducer)

- MemoryImageSource

```java
public MemoryImageSource​(int w,
int h,
int[] pix,
int off,
int scan)
```

Constructs an ImageProducer object which uses an array of integers
in the default RGB ColorModel to produce data for an Image object.

**Parameters:** w

- the width of the rectangle of pixels
**Parameters:** h

- the height of the rectangle of pixels
**Parameters:** pix

- an array of pixels
**Parameters:** off

- the offset into the array of where to store the
first pixel
**Parameters:** scan

- the distance from one row of pixels to the next in
the array
**See Also:** Component.createImage(java.awt.image.ImageProducer)

,

ColorModel.getRGBdefault()

- MemoryImageSource

```java
public MemoryImageSource​(int w,
int h,
int[] pix,
int off,
int scan,

Hashtable
<?,​?> props)
```

Constructs an ImageProducer object which uses an array of integers
in the default RGB ColorModel to produce data for an Image object.

**Parameters:** w

- the width of the rectangle of pixels
**Parameters:** h

- the height of the rectangle of pixels
**Parameters:** pix

- an array of pixels
**Parameters:** off

- the offset into the array of where to store the
first pixel
**Parameters:** scan

- the distance from one row of pixels to the next in
the array
**Parameters:** props

- a list of properties that the

ImageProducer

uses to process an image
**See Also:** Component.createImage(java.awt.image.ImageProducer)

,

ColorModel.getRGBdefault()

---

#### Constructor Detail

MemoryImageSource

```java
public MemoryImageSource​(int w,
int h,

ColorModel
cm,
byte[] pix,
int off,
int scan)
```

Constructs an ImageProducer object which uses an array of bytes
to produce data for an Image object.

**Parameters:** w

- the width of the rectangle of pixels
**Parameters:** h

- the height of the rectangle of pixels
**Parameters:** cm

- the specified

ColorModel
**Parameters:** pix

- an array of pixels
**Parameters:** off

- the offset into the array of where to store the
first pixel
**Parameters:** scan

- the distance from one row of pixels to the next in
the array
**See Also:** Component.createImage(java.awt.image.ImageProducer)

---

#### MemoryImageSource

public MemoryImageSource​(int w,
int h,

ColorModel

cm,
byte[] pix,
int off,
int scan)

Constructs an ImageProducer object which uses an array of bytes
to produce data for an Image object.

MemoryImageSource

```java
public MemoryImageSource​(int w,
int h,

ColorModel
cm,
byte[] pix,
int off,
int scan,

Hashtable
<?,​?> props)
```

Constructs an ImageProducer object which uses an array of bytes
to produce data for an Image object.

**Parameters:** w

- the width of the rectangle of pixels
**Parameters:** h

- the height of the rectangle of pixels
**Parameters:** cm

- the specified

ColorModel
**Parameters:** pix

- an array of pixels
**Parameters:** off

- the offset into the array of where to store the
first pixel
**Parameters:** scan

- the distance from one row of pixels to the next in
the array
**Parameters:** props

- a list of properties that the

ImageProducer

uses to process an image
**See Also:** Component.createImage(java.awt.image.ImageProducer)

---

#### MemoryImageSource

public MemoryImageSource​(int w,
int h,

ColorModel

cm,
byte[] pix,
int off,
int scan,

Hashtable

<?,​?> props)

Constructs an ImageProducer object which uses an array of bytes
to produce data for an Image object.

MemoryImageSource

```java
public MemoryImageSource​(int w,
int h,

ColorModel
cm,
int[] pix,
int off,
int scan)
```

Constructs an ImageProducer object which uses an array of integers
to produce data for an Image object.

**Parameters:** w

- the width of the rectangle of pixels
**Parameters:** h

- the height of the rectangle of pixels
**Parameters:** cm

- the specified

ColorModel
**Parameters:** pix

- an array of pixels
**Parameters:** off

- the offset into the array of where to store the
first pixel
**Parameters:** scan

- the distance from one row of pixels to the next in
the array
**See Also:** Component.createImage(java.awt.image.ImageProducer)

---

#### MemoryImageSource

public MemoryImageSource​(int w,
int h,

ColorModel

cm,
int[] pix,
int off,
int scan)

Constructs an ImageProducer object which uses an array of integers
to produce data for an Image object.

MemoryImageSource

```java
public MemoryImageSource​(int w,
int h,

ColorModel
cm,
int[] pix,
int off,
int scan,

Hashtable
<?,​?> props)
```

Constructs an ImageProducer object which uses an array of integers
to produce data for an Image object.

**Parameters:** w

- the width of the rectangle of pixels
**Parameters:** h

- the height of the rectangle of pixels
**Parameters:** cm

- the specified

ColorModel
**Parameters:** pix

- an array of pixels
**Parameters:** off

- the offset into the array of where to store the
first pixel
**Parameters:** scan

- the distance from one row of pixels to the next in
the array
**Parameters:** props

- a list of properties that the

ImageProducer

uses to process an image
**See Also:** Component.createImage(java.awt.image.ImageProducer)

---

#### MemoryImageSource

public MemoryImageSource​(int w,
int h,

ColorModel

cm,
int[] pix,
int off,
int scan,

Hashtable

<?,​?> props)

Constructs an ImageProducer object which uses an array of integers
to produce data for an Image object.

MemoryImageSource

```java
public MemoryImageSource​(int w,
int h,
int[] pix,
int off,
int scan)
```

Constructs an ImageProducer object which uses an array of integers
in the default RGB ColorModel to produce data for an Image object.

**Parameters:** w

- the width of the rectangle of pixels
**Parameters:** h

- the height of the rectangle of pixels
**Parameters:** pix

- an array of pixels
**Parameters:** off

- the offset into the array of where to store the
first pixel
**Parameters:** scan

- the distance from one row of pixels to the next in
the array
**See Also:** Component.createImage(java.awt.image.ImageProducer)

,

ColorModel.getRGBdefault()

---

#### MemoryImageSource

public MemoryImageSource​(int w,
int h,
int[] pix,
int off,
int scan)

Constructs an ImageProducer object which uses an array of integers
in the default RGB ColorModel to produce data for an Image object.

MemoryImageSource

```java
public MemoryImageSource​(int w,
int h,
int[] pix,
int off,
int scan,

Hashtable
<?,​?> props)
```

Constructs an ImageProducer object which uses an array of integers
in the default RGB ColorModel to produce data for an Image object.

**Parameters:** w

- the width of the rectangle of pixels
**Parameters:** h

- the height of the rectangle of pixels
**Parameters:** pix

- an array of pixels
**Parameters:** off

- the offset into the array of where to store the
first pixel
**Parameters:** scan

- the distance from one row of pixels to the next in
the array
**Parameters:** props

- a list of properties that the

ImageProducer

uses to process an image
**See Also:** Component.createImage(java.awt.image.ImageProducer)

,

ColorModel.getRGBdefault()

---

#### MemoryImageSource

public MemoryImageSource​(int w,
int h,
int[] pix,
int off,
int scan,

Hashtable

<?,​?> props)

Constructs an ImageProducer object which uses an array of integers
in the default RGB ColorModel to produce data for an Image object.

Method Detail

- addConsumer

```java
public void addConsumer​(
ImageConsumer
ic)
```

Adds an ImageConsumer to the list of consumers interested in
data for this image.

**Specified by:** addConsumer

in interface

ImageProducer
**Parameters:** ic

- the specified

ImageConsumer
**Throws:** NullPointerException

- if the specified

ImageConsumer

is null
**See Also:** ImageConsumer

- isConsumer

```java
public boolean isConsumer​(
ImageConsumer
ic)
```

Determines if an ImageConsumer is on the list of consumers currently
interested in data for this image.

**Specified by:** isConsumer

in interface

ImageProducer
**Parameters:** ic

- the specified

ImageConsumer
**Returns:** true

if the

ImageConsumer

is on the list;

false

otherwise.
**See Also:** ImageConsumer

- removeConsumer

```java
public void removeConsumer​(
ImageConsumer
ic)
```

Removes an ImageConsumer from the list of consumers interested in
data for this image.

**Specified by:** removeConsumer

in interface

ImageProducer
**Parameters:** ic

- the specified

ImageConsumer
**See Also:** ImageConsumer

- startProduction

```java
public void startProduction​(
ImageConsumer
ic)
```

Adds an ImageConsumer to the list of consumers interested in
data for this image and immediately starts delivery of the
image data through the ImageConsumer interface.

**Specified by:** startProduction

in interface

ImageProducer
**Parameters:** ic

- the specified

ImageConsumer

image data through the ImageConsumer interface.
**See Also:** ImageConsumer

- requestTopDownLeftRightResend

```java
public void requestTopDownLeftRightResend​(
ImageConsumer
ic)
```

Requests that a given ImageConsumer have the image data delivered
one more time in top-down, left-right order.

**Specified by:** requestTopDownLeftRightResend

in interface

ImageProducer
**Parameters:** ic

- the specified

ImageConsumer
**See Also:** ImageConsumer

- setAnimated

```java
public void setAnimated​(boolean animated)
```

Changes this memory image into a multi-frame animation or a
single-frame static image depending on the animated parameter.

This method should be called immediately after the
MemoryImageSource is constructed and before an image is
created with it to ensure that all ImageConsumers will
receive the correct multi-frame data. If an ImageConsumer
is added to this ImageProducer before this flag is set then
that ImageConsumer will see only a snapshot of the pixel
data that was available when it connected.

**Parameters:** animated

-

true

if the image is a
multi-frame animation

- setFullBufferUpdates

```java
public void setFullBufferUpdates​(boolean fullbuffers)
```

Specifies whether this animated memory image should always be
updated by sending the complete buffer of pixels whenever
there is a change.
This flag is ignored if the animation flag is not turned on
through the setAnimated() method.

This method should be called immediately after the
MemoryImageSource is constructed and before an image is
created with it to ensure that all ImageConsumers will
receive the correct pixel delivery hints.

**Parameters:** fullbuffers

-

true

if the complete pixel
buffer should always
be sent
**See Also:** setAnimated(boolean)

- newPixels

```java
public void newPixels()
```

Sends a whole new buffer of pixels to any ImageConsumers that
are currently interested in the data for this image and notify
them that an animation frame is complete.
This method only has effect if the animation flag has been
turned on through the setAnimated() method.

**See Also:** newPixels(int, int, int, int, boolean)

,

ImageConsumer

,

setAnimated(boolean)

- newPixels

```java
public void newPixels​(int x,
int y,
int w,
int h)
```

Sends a rectangular region of the buffer of pixels to any
ImageConsumers that are currently interested in the data for
this image and notify them that an animation frame is complete.
This method only has effect if the animation flag has been
turned on through the setAnimated() method.
If the full buffer update flag was turned on with the
setFullBufferUpdates() method then the rectangle parameters
will be ignored and the entire buffer will always be sent.

**Parameters:** x

- the x coordinate of the upper left corner of the rectangle
of pixels to be sent
**Parameters:** y

- the y coordinate of the upper left corner of the rectangle
of pixels to be sent
**Parameters:** w

- the width of the rectangle of pixels to be sent
**Parameters:** h

- the height of the rectangle of pixels to be sent
**See Also:** newPixels(int, int, int, int, boolean)

,

ImageConsumer

,

setAnimated(boolean)

,

setFullBufferUpdates(boolean)

- newPixels

```java
public void newPixels​(int x,
int y,
int w,
int h,
boolean framenotify)
```

Sends a rectangular region of the buffer of pixels to any
ImageConsumers that are currently interested in the data for
this image.
If the framenotify parameter is true then the consumers are
also notified that an animation frame is complete.
This method only has effect if the animation flag has been
turned on through the setAnimated() method.
If the full buffer update flag was turned on with the
setFullBufferUpdates() method then the rectangle parameters
will be ignored and the entire buffer will always be sent.

**Parameters:** x

- the x coordinate of the upper left corner of the rectangle
of pixels to be sent
**Parameters:** y

- the y coordinate of the upper left corner of the rectangle
of pixels to be sent
**Parameters:** w

- the width of the rectangle of pixels to be sent
**Parameters:** h

- the height of the rectangle of pixels to be sent
**Parameters:** framenotify

-

true

if the consumers should be sent a

SINGLEFRAMEDONE

notification
**See Also:** ImageConsumer

,

setAnimated(boolean)

,

setFullBufferUpdates(boolean)

- newPixels

```java
public void newPixels​(byte[] newpix,

ColorModel
newmodel,
int offset,
int scansize)
```

Changes to a new byte array to hold the pixels for this image.
If the animation flag has been turned on through the setAnimated()
method, then the new pixels will be immediately delivered to any
ImageConsumers that are currently interested in the data for
this image.

**Parameters:** newpix

- the new pixel array
**Parameters:** newmodel

- the specified

ColorModel
**Parameters:** offset

- the offset into the array
**Parameters:** scansize

- the distance from one row of pixels to the next in
the array
**See Also:** newPixels(int, int, int, int, boolean)

,

setAnimated(boolean)

- newPixels

```java
public void newPixels​(int[] newpix,

ColorModel
newmodel,
int offset,
int scansize)
```

Changes to a new int array to hold the pixels for this image.
If the animation flag has been turned on through the setAnimated()
method, then the new pixels will be immediately delivered to any
ImageConsumers that are currently interested in the data for
this image.

**Parameters:** newpix

- the new pixel array
**Parameters:** newmodel

- the specified

ColorModel
**Parameters:** offset

- the offset into the array
**Parameters:** scansize

- the distance from one row of pixels to the next in
the array
**See Also:** newPixels(int, int, int, int, boolean)

,

setAnimated(boolean)

---

#### Method Detail

addConsumer

```java
public void addConsumer​(
ImageConsumer
ic)
```

Adds an ImageConsumer to the list of consumers interested in
data for this image.

**Specified by:** addConsumer

in interface

ImageProducer
**Parameters:** ic

- the specified

ImageConsumer
**Throws:** NullPointerException

- if the specified

ImageConsumer

is null
**See Also:** ImageConsumer

---

#### addConsumer

public void addConsumer​(

ImageConsumer

ic)

Adds an ImageConsumer to the list of consumers interested in
data for this image.

isConsumer

```java
public boolean isConsumer​(
ImageConsumer
ic)
```

Determines if an ImageConsumer is on the list of consumers currently
interested in data for this image.

**Specified by:** isConsumer

in interface

ImageProducer
**Parameters:** ic

- the specified

ImageConsumer
**Returns:** true

if the

ImageConsumer

is on the list;

false

otherwise.
**See Also:** ImageConsumer

---

#### isConsumer

public boolean isConsumer​(

ImageConsumer

ic)

Determines if an ImageConsumer is on the list of consumers currently
interested in data for this image.

removeConsumer

```java
public void removeConsumer​(
ImageConsumer
ic)
```

Removes an ImageConsumer from the list of consumers interested in
data for this image.

**Specified by:** removeConsumer

in interface

ImageProducer
**Parameters:** ic

- the specified

ImageConsumer
**See Also:** ImageConsumer

---

#### removeConsumer

public void removeConsumer​(

ImageConsumer

ic)

Removes an ImageConsumer from the list of consumers interested in
data for this image.

startProduction

```java
public void startProduction​(
ImageConsumer
ic)
```

Adds an ImageConsumer to the list of consumers interested in
data for this image and immediately starts delivery of the
image data through the ImageConsumer interface.

**Specified by:** startProduction

in interface

ImageProducer
**Parameters:** ic

- the specified

ImageConsumer

image data through the ImageConsumer interface.
**See Also:** ImageConsumer

---

#### startProduction

public void startProduction​(

ImageConsumer

ic)

Adds an ImageConsumer to the list of consumers interested in
data for this image and immediately starts delivery of the
image data through the ImageConsumer interface.

requestTopDownLeftRightResend

```java
public void requestTopDownLeftRightResend​(
ImageConsumer
ic)
```

Requests that a given ImageConsumer have the image data delivered
one more time in top-down, left-right order.

**Specified by:** requestTopDownLeftRightResend

in interface

ImageProducer
**Parameters:** ic

- the specified

ImageConsumer
**See Also:** ImageConsumer

---

#### requestTopDownLeftRightResend

public void requestTopDownLeftRightResend​(

ImageConsumer

ic)

Requests that a given ImageConsumer have the image data delivered
one more time in top-down, left-right order.

setAnimated

```java
public void setAnimated​(boolean animated)
```

Changes this memory image into a multi-frame animation or a
single-frame static image depending on the animated parameter.

This method should be called immediately after the
MemoryImageSource is constructed and before an image is
created with it to ensure that all ImageConsumers will
receive the correct multi-frame data. If an ImageConsumer
is added to this ImageProducer before this flag is set then
that ImageConsumer will see only a snapshot of the pixel
data that was available when it connected.

**Parameters:** animated

-

true

if the image is a
multi-frame animation

---

#### setAnimated

public void setAnimated​(boolean animated)

Changes this memory image into a multi-frame animation or a
single-frame static image depending on the animated parameter.

This method should be called immediately after the
MemoryImageSource is constructed and before an image is
created with it to ensure that all ImageConsumers will
receive the correct multi-frame data. If an ImageConsumer
is added to this ImageProducer before this flag is set then
that ImageConsumer will see only a snapshot of the pixel
data that was available when it connected.

This method should be called immediately after the
MemoryImageSource is constructed and before an image is
created with it to ensure that all ImageConsumers will
receive the correct multi-frame data. If an ImageConsumer
is added to this ImageProducer before this flag is set then
that ImageConsumer will see only a snapshot of the pixel
data that was available when it connected.

setFullBufferUpdates

```java
public void setFullBufferUpdates​(boolean fullbuffers)
```

Specifies whether this animated memory image should always be
updated by sending the complete buffer of pixels whenever
there is a change.
This flag is ignored if the animation flag is not turned on
through the setAnimated() method.

This method should be called immediately after the
MemoryImageSource is constructed and before an image is
created with it to ensure that all ImageConsumers will
receive the correct pixel delivery hints.

**Parameters:** fullbuffers

-

true

if the complete pixel
buffer should always
be sent
**See Also:** setAnimated(boolean)

---

#### setFullBufferUpdates

public void setFullBufferUpdates​(boolean fullbuffers)

Specifies whether this animated memory image should always be
updated by sending the complete buffer of pixels whenever
there is a change.
This flag is ignored if the animation flag is not turned on
through the setAnimated() method.

This method should be called immediately after the
MemoryImageSource is constructed and before an image is
created with it to ensure that all ImageConsumers will
receive the correct pixel delivery hints.

This method should be called immediately after the
MemoryImageSource is constructed and before an image is
created with it to ensure that all ImageConsumers will
receive the correct pixel delivery hints.

newPixels

```java
public void newPixels()
```

Sends a whole new buffer of pixels to any ImageConsumers that
are currently interested in the data for this image and notify
them that an animation frame is complete.
This method only has effect if the animation flag has been
turned on through the setAnimated() method.

**See Also:** newPixels(int, int, int, int, boolean)

,

ImageConsumer

,

setAnimated(boolean)

---

#### newPixels

public void newPixels()

Sends a whole new buffer of pixels to any ImageConsumers that
are currently interested in the data for this image and notify
them that an animation frame is complete.
This method only has effect if the animation flag has been
turned on through the setAnimated() method.

newPixels

```java
public void newPixels​(int x,
int y,
int w,
int h)
```

Sends a rectangular region of the buffer of pixels to any
ImageConsumers that are currently interested in the data for
this image and notify them that an animation frame is complete.
This method only has effect if the animation flag has been
turned on through the setAnimated() method.
If the full buffer update flag was turned on with the
setFullBufferUpdates() method then the rectangle parameters
will be ignored and the entire buffer will always be sent.

**Parameters:** x

- the x coordinate of the upper left corner of the rectangle
of pixels to be sent
**Parameters:** y

- the y coordinate of the upper left corner of the rectangle
of pixels to be sent
**Parameters:** w

- the width of the rectangle of pixels to be sent
**Parameters:** h

- the height of the rectangle of pixels to be sent
**See Also:** newPixels(int, int, int, int, boolean)

,

ImageConsumer

,

setAnimated(boolean)

,

setFullBufferUpdates(boolean)

---

#### newPixels

public void newPixels​(int x,
int y,
int w,
int h)

Sends a rectangular region of the buffer of pixels to any
ImageConsumers that are currently interested in the data for
this image and notify them that an animation frame is complete.
This method only has effect if the animation flag has been
turned on through the setAnimated() method.
If the full buffer update flag was turned on with the
setFullBufferUpdates() method then the rectangle parameters
will be ignored and the entire buffer will always be sent.

newPixels

```java
public void newPixels​(int x,
int y,
int w,
int h,
boolean framenotify)
```

Sends a rectangular region of the buffer of pixels to any
ImageConsumers that are currently interested in the data for
this image.
If the framenotify parameter is true then the consumers are
also notified that an animation frame is complete.
This method only has effect if the animation flag has been
turned on through the setAnimated() method.
If the full buffer update flag was turned on with the
setFullBufferUpdates() method then the rectangle parameters
will be ignored and the entire buffer will always be sent.

**Parameters:** x

- the x coordinate of the upper left corner of the rectangle
of pixels to be sent
**Parameters:** y

- the y coordinate of the upper left corner of the rectangle
of pixels to be sent
**Parameters:** w

- the width of the rectangle of pixels to be sent
**Parameters:** h

- the height of the rectangle of pixels to be sent
**Parameters:** framenotify

-

true

if the consumers should be sent a

SINGLEFRAMEDONE

notification
**See Also:** ImageConsumer

,

setAnimated(boolean)

,

setFullBufferUpdates(boolean)

---

#### newPixels

public void newPixels​(int x,
int y,
int w,
int h,
boolean framenotify)

Sends a rectangular region of the buffer of pixels to any
ImageConsumers that are currently interested in the data for
this image.
If the framenotify parameter is true then the consumers are
also notified that an animation frame is complete.
This method only has effect if the animation flag has been
turned on through the setAnimated() method.
If the full buffer update flag was turned on with the
setFullBufferUpdates() method then the rectangle parameters
will be ignored and the entire buffer will always be sent.

newPixels

```java
public void newPixels​(byte[] newpix,

ColorModel
newmodel,
int offset,
int scansize)
```

Changes to a new byte array to hold the pixels for this image.
If the animation flag has been turned on through the setAnimated()
method, then the new pixels will be immediately delivered to any
ImageConsumers that are currently interested in the data for
this image.

**Parameters:** newpix

- the new pixel array
**Parameters:** newmodel

- the specified

ColorModel
**Parameters:** offset

- the offset into the array
**Parameters:** scansize

- the distance from one row of pixels to the next in
the array
**See Also:** newPixels(int, int, int, int, boolean)

,

setAnimated(boolean)

---

#### newPixels

public void newPixels​(byte[] newpix,

ColorModel

newmodel,
int offset,
int scansize)

Changes to a new byte array to hold the pixels for this image.
If the animation flag has been turned on through the setAnimated()
method, then the new pixels will be immediately delivered to any
ImageConsumers that are currently interested in the data for
this image.

newPixels

```java
public void newPixels​(int[] newpix,

ColorModel
newmodel,
int offset,
int scansize)
```

Changes to a new int array to hold the pixels for this image.
If the animation flag has been turned on through the setAnimated()
method, then the new pixels will be immediately delivered to any
ImageConsumers that are currently interested in the data for
this image.

**Parameters:** newpix

- the new pixel array
**Parameters:** newmodel

- the specified

ColorModel
**Parameters:** offset

- the offset into the array
**Parameters:** scansize

- the distance from one row of pixels to the next in
the array
**See Also:** newPixels(int, int, int, int, boolean)

,

setAnimated(boolean)

---

#### newPixels

public void newPixels​(int[] newpix,

ColorModel

newmodel,
int offset,
int scansize)

Changes to a new int array to hold the pixels for this image.
If the animation flag has been turned on through the setAnimated()
method, then the new pixels will be immediately delivered to any
ImageConsumers that are currently interested in the data for
this image.

---

