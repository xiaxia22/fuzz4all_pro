# Class Image

**Source:** `java.desktop\java\awt\Image.html`

### Class Description

```java
public abstract class
Image

extends
Object
```

The abstract class

Image

is the superclass of all
classes that represent graphical images. The image must be
obtained in a platform-specific manner.

**Direct Known Subclasses:** AbstractMultiResolutionImage

,

BufferedImage

,

VolatileImage

---

### Field Details

#### protected float accelerationPriority

Priority for accelerating this image. Subclasses are free to
set different default priorities and applications are free to
set the priority for specific images via the

setAccelerationPriority(float)

method.

**Since:**
- 1.5

---

#### public static final
Object
UndefinedProperty

The

UndefinedProperty

object should be returned whenever a
property which was not defined for a particular image is fetched.

---

#### public static final int SCALE_DEFAULT

Use the default image-scaling algorithm.

**See Also:**
- Constant Field Values

**Since:**
- 1.1

---

#### public static final int SCALE_FAST

Choose an image-scaling algorithm that gives higher priority
to scaling speed than smoothness of the scaled image.

**See Also:**
- Constant Field Values

**Since:**
- 1.1

---

#### public static final int SCALE_SMOOTH

Choose an image-scaling algorithm that gives higher priority
to image smoothness than scaling speed.

**See Also:**
- Constant Field Values

**Since:**
- 1.1

---

#### public static final int SCALE_REPLICATE

Use the image scaling algorithm embodied in the

ReplicateScaleFilter

class.
The

Image

object is free to substitute a different filter
that performs the same algorithm yet integrates more efficiently
into the imaging infrastructure supplied by the toolkit.

**See Also:**
- ReplicateScaleFilter

,

Constant Field Values

**Since:**
- 1.1

---

#### public static final int SCALE_AREA_AVERAGING

Use the Area Averaging image scaling algorithm. The
image object is free to substitute a different filter that
performs the same algorithm yet integrates more efficiently
into the image infrastructure supplied by the toolkit.

**See Also:**
- AreaAveragingScaleFilter

,

Constant Field Values

**Since:**
- 1.1

---

### Constructor Details

#### public Image()

*No description found.*

---

### Method Details

#### public abstract int getWidth​(
ImageObserver
observer)

Determines the width of the image. If the width is not yet known,
this method returns

-1

and the specified

ImageObserver

object is notified later.

**Parameters:**
- observer

- an object waiting for the image to be loaded.

**Returns:**
- the width of this image, or

-1

if the width is not yet known.

**See Also:**
- getHeight(java.awt.image.ImageObserver)

,

ImageObserver

---

#### public abstract int getHeight​(
ImageObserver
observer)

Determines the height of the image. If the height is not yet known,
this method returns

-1

and the specified

ImageObserver

object is notified later.

**Parameters:**
- observer

- an object waiting for the image to be loaded.

**Returns:**
- the height of this image, or

-1

if the height is not yet known.

**See Also:**
- getWidth(java.awt.image.ImageObserver)

,

ImageObserver

---

#### public abstract
ImageProducer
getSource()

Gets the object that produces the pixels for the image.
This method is called by the image filtering classes and by
methods that perform image conversion and scaling.

**Returns:**
- the image producer that produces the pixels
for this image.

**See Also:**
- ImageProducer

---

#### public abstract
Graphics
getGraphics()

Creates a graphics context for drawing to an off-screen image.
This method can only be called for off-screen images.

**Returns:**
- a graphics context to draw to the off-screen image.

**Throws:**
- UnsupportedOperationException

- if called for a
non-off-screen image.

**See Also:**
- Graphics

,

Component.createImage(int, int)

---

#### public abstract
Object
getProperty​(
String
name,

ImageObserver
observer)

Gets a property of this image by name.

Individual property names are defined by the various image
formats. If a property is not defined for a particular image, this
method returns the

UndefinedProperty

object.

If the properties for this image are not yet known, this method
returns

null

, and the

ImageObserver

object is notified later.

The property name

"comment"

should be used to store
an optional comment which can be presented to the application as a
description of the image, its source, or its author.

**Parameters:**
- name

- a property name.
- observer

- an object waiting for this image to be loaded.

**Returns:**
- the value of the named property.

**Throws:**
- NullPointerException

- if the property name is null.

**See Also:**
- ImageObserver

,

UndefinedProperty

---

#### public
Image
getScaledInstance​(int width,
int height,
int hints)

Creates a scaled version of this image.
A new

Image

object is returned which will render
the image at the specified

width

and

height

by default. The new

Image

object
may be loaded asynchronously even if the original source image
has already been loaded completely.

If either

width

or

height

is a negative number then a value is
substituted to maintain the aspect ratio of the original image
dimensions. If both

width

and

height

are negative, then the original image dimensions are used.

**Parameters:**
- width

- the width to which to scale the image.
- height

- the height to which to scale the image.
- hints

- flags to indicate the type of algorithm to use
for image resampling.

**Returns:**
- a scaled version of the image.

**Throws:**
- IllegalArgumentException

- if

width

or

height

is zero.

**See Also:**
- SCALE_DEFAULT

,

SCALE_FAST

,

SCALE_SMOOTH

,

SCALE_REPLICATE

,

SCALE_AREA_AVERAGING

**Since:**
- 1.1

---

#### public void flush()

Flushes all reconstructable resources being used by this Image object.
This includes any pixel data that is being cached for rendering to
the screen as well as any system resources that are being used
to store data or pixels for the image if they can be recreated.
The image is reset to a state similar to when it was first created
so that if it is again rendered, the image data will have to be
recreated or fetched again from its source.

Examples of how this method affects specific types of Image object:

- BufferedImage objects leave the primary Raster which stores their
pixels untouched, but flush any information cached about those
pixels such as copies uploaded to the display hardware for
accelerated blits.

Image objects created by the Component methods which take a
width and height leave their primary buffer of pixels untouched,
but have all cached information released much like is done for
BufferedImage objects.

VolatileImage objects release all of their pixel resources
including their primary copy which is typically stored on
the display hardware where resources are scarce.
These objects can later be restored using their

validate

method.

Image objects created by the Toolkit and Component classes which are
loaded from files, URLs or produced by an

ImageProducer

are unloaded and all local resources are released.
These objects can later be reloaded from their original source
as needed when they are rendered, just as when they were first
created.

---

#### public
ImageCapabilities
getCapabilities​(
GraphicsConfiguration
gc)

Returns an ImageCapabilities object which can be
inquired as to the capabilities of this
Image on the specified GraphicsConfiguration.
This allows programmers to find
out more runtime information on the specific Image
object that they have created. For example, the user
might create a BufferedImage but the system may have
no video memory left for creating an image of that
size on the given GraphicsConfiguration, so although the object
may be acceleratable in general, it
does not have that capability on this GraphicsConfiguration.

**Parameters:**
- gc

- a

GraphicsConfiguration

object. A value of null
for this parameter will result in getting the image capabilities
for the default

GraphicsConfiguration

.

**Returns:**
- an

ImageCapabilities

object that contains
the capabilities of this

Image

on the specified
GraphicsConfiguration.

**See Also:**
- VolatileImage.getCapabilities()

**Since:**
- 1.5

---

#### public void setAccelerationPriority​(float priority)

Sets a hint for this image about how important acceleration is.
This priority hint is used to compare to the priorities of other
Image objects when determining how to use scarce acceleration
resources such as video memory. When and if it is possible to
accelerate this Image, if there are not enough resources available
to provide that acceleration but enough can be freed up by
de-accelerating some other image of lower priority, then that other
Image may be de-accelerated in deference to this one. Images
that have the same priority take up resources on a first-come,
first-served basis.

**Parameters:**
- priority

- a value between 0 and 1, inclusive, where higher
values indicate more importance for acceleration. A value of 0
means that this Image should never be accelerated. Other values
are used simply to determine acceleration priority relative to other
Images.

**Throws:**
- IllegalArgumentException

- if

priority

is less
than zero or greater than 1.

**Since:**
- 1.5

---

#### public float getAccelerationPriority()

Returns the current value of the acceleration priority hint.

**Returns:**
- value between 0 and 1, inclusive, which represents the current
priority value

**See Also:**
- setAccelerationPriority

**Since:**
- 1.5

---

### Additional Sections

#### Class Image

java.lang.Object

- java.awt.Image

java.awt.Image

**Direct Known Subclasses:** AbstractMultiResolutionImage

,

BufferedImage

,

VolatileImage

```java
public abstract class
Image

extends
Object
```

The abstract class

Image

is the superclass of all
classes that represent graphical images. The image must be
obtained in a platform-specific manner.

**Since:** 1.0

public abstract class

Image

extends

Object

The abstract class

Image

is the superclass of all
classes that represent graphical images. The image must be
obtained in a platform-specific manner.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected float

accelerationPriority

Priority for accelerating this image.

static int

SCALE_AREA_AVERAGING

Use the Area Averaging image scaling algorithm.

static int

SCALE_DEFAULT

Use the default image-scaling algorithm.

static int

SCALE_FAST

Choose an image-scaling algorithm that gives higher priority
to scaling speed than smoothness of the scaled image.

static int

SCALE_REPLICATE

Use the image scaling algorithm embodied in the

ReplicateScaleFilter

class.

static int

SCALE_SMOOTH

Choose an image-scaling algorithm that gives higher priority
to image smoothness than scaling speed.

static

Object

UndefinedProperty

The

UndefinedProperty

object should be returned whenever a
property which was not defined for a particular image is fetched.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Image

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

void

flush

()

Flushes all reconstructable resources being used by this Image object.

float

getAccelerationPriority

()

Returns the current value of the acceleration priority hint.

ImageCapabilities

getCapabilities

​(

GraphicsConfiguration

gc)

Returns an ImageCapabilities object which can be
inquired as to the capabilities of this
Image on the specified GraphicsConfiguration.

abstract

Graphics

getGraphics

()

Creates a graphics context for drawing to an off-screen image.

abstract int

getHeight

​(

ImageObserver

observer)

Determines the height of the image.

abstract

Object

getProperty

​(

String

name,

ImageObserver

observer)

Gets a property of this image by name.

Image

getScaledInstance

​(int width,
int height,
int hints)

Creates a scaled version of this image.

abstract

ImageProducer

getSource

()

Gets the object that produces the pixels for the image.

abstract int

getWidth

​(

ImageObserver

observer)

Determines the width of the image.

void

setAccelerationPriority

​(float priority)

Sets a hint for this image about how important acceleration is.

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

protected float

accelerationPriority

Priority for accelerating this image.

static int

SCALE_AREA_AVERAGING

Use the Area Averaging image scaling algorithm.

static int

SCALE_DEFAULT

Use the default image-scaling algorithm.

static int

SCALE_FAST

Choose an image-scaling algorithm that gives higher priority
to scaling speed than smoothness of the scaled image.

static int

SCALE_REPLICATE

Use the image scaling algorithm embodied in the

ReplicateScaleFilter

class.

static int

SCALE_SMOOTH

Choose an image-scaling algorithm that gives higher priority
to image smoothness than scaling speed.

static

Object

UndefinedProperty

The

UndefinedProperty

object should be returned whenever a
property which was not defined for a particular image is fetched.

---

#### Field Summary

Priority for accelerating this image.

Use the Area Averaging image scaling algorithm.

Use the default image-scaling algorithm.

Choose an image-scaling algorithm that gives higher priority
to scaling speed than smoothness of the scaled image.

Use the image scaling algorithm embodied in the

ReplicateScaleFilter

class.

Choose an image-scaling algorithm that gives higher priority
to image smoothness than scaling speed.

The

UndefinedProperty

object should be returned whenever a
property which was not defined for a particular image is fetched.

Constructor Summary

Constructors

Constructor

Description

Image

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

void

flush

()

Flushes all reconstructable resources being used by this Image object.

float

getAccelerationPriority

()

Returns the current value of the acceleration priority hint.

ImageCapabilities

getCapabilities

​(

GraphicsConfiguration

gc)

Returns an ImageCapabilities object which can be
inquired as to the capabilities of this
Image on the specified GraphicsConfiguration.

abstract

Graphics

getGraphics

()

Creates a graphics context for drawing to an off-screen image.

abstract int

getHeight

​(

ImageObserver

observer)

Determines the height of the image.

abstract

Object

getProperty

​(

String

name,

ImageObserver

observer)

Gets a property of this image by name.

Image

getScaledInstance

​(int width,
int height,
int hints)

Creates a scaled version of this image.

abstract

ImageProducer

getSource

()

Gets the object that produces the pixels for the image.

abstract int

getWidth

​(

ImageObserver

observer)

Determines the width of the image.

void

setAccelerationPriority

​(float priority)

Sets a hint for this image about how important acceleration is.

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

Flushes all reconstructable resources being used by this Image object.

Returns the current value of the acceleration priority hint.

Returns an ImageCapabilities object which can be
inquired as to the capabilities of this
Image on the specified GraphicsConfiguration.

Creates a graphics context for drawing to an off-screen image.

Determines the height of the image.

Gets a property of this image by name.

Creates a scaled version of this image.

Gets the object that produces the pixels for the image.

Determines the width of the image.

Sets a hint for this image about how important acceleration is.

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

- accelerationPriority

```java
protected float accelerationPriority
```

Priority for accelerating this image. Subclasses are free to
set different default priorities and applications are free to
set the priority for specific images via the

setAccelerationPriority(float)

method.

**Since:** 1.5

- UndefinedProperty

```java
public static final
Object
UndefinedProperty
```

The

UndefinedProperty

object should be returned whenever a
property which was not defined for a particular image is fetched.

- SCALE_DEFAULT

```java
public static final int SCALE_DEFAULT
```

Use the default image-scaling algorithm.

**Since:** 1.1
**See Also:** Constant Field Values

- SCALE_FAST

```java
public static final int SCALE_FAST
```

Choose an image-scaling algorithm that gives higher priority
to scaling speed than smoothness of the scaled image.

**Since:** 1.1
**See Also:** Constant Field Values

- SCALE_SMOOTH

```java
public static final int SCALE_SMOOTH
```

Choose an image-scaling algorithm that gives higher priority
to image smoothness than scaling speed.

**Since:** 1.1
**See Also:** Constant Field Values

- SCALE_REPLICATE

```java
public static final int SCALE_REPLICATE
```

Use the image scaling algorithm embodied in the

ReplicateScaleFilter

class.
The

Image

object is free to substitute a different filter
that performs the same algorithm yet integrates more efficiently
into the imaging infrastructure supplied by the toolkit.

**Since:** 1.1
**See Also:** ReplicateScaleFilter

,

Constant Field Values

- SCALE_AREA_AVERAGING

```java
public static final int SCALE_AREA_AVERAGING
```

Use the Area Averaging image scaling algorithm. The
image object is free to substitute a different filter that
performs the same algorithm yet integrates more efficiently
into the image infrastructure supplied by the toolkit.

**Since:** 1.1
**See Also:** AreaAveragingScaleFilter

,

Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Image

```java
public Image()
```

============ METHOD DETAIL ==========

- Method Detail

- getWidth

```java
public abstract int getWidth​(
ImageObserver
observer)
```

Determines the width of the image. If the width is not yet known,
this method returns

-1

and the specified

ImageObserver

object is notified later.

**Parameters:** observer

- an object waiting for the image to be loaded.
**Returns:** the width of this image, or

-1

if the width is not yet known.
**See Also:** getHeight(java.awt.image.ImageObserver)

,

ImageObserver

- getHeight

```java
public abstract int getHeight​(
ImageObserver
observer)
```

Determines the height of the image. If the height is not yet known,
this method returns

-1

and the specified

ImageObserver

object is notified later.

**Parameters:** observer

- an object waiting for the image to be loaded.
**Returns:** the height of this image, or

-1

if the height is not yet known.
**See Also:** getWidth(java.awt.image.ImageObserver)

,

ImageObserver

- getSource

```java
public abstract
ImageProducer
getSource()
```

Gets the object that produces the pixels for the image.
This method is called by the image filtering classes and by
methods that perform image conversion and scaling.

**Returns:** the image producer that produces the pixels
for this image.
**See Also:** ImageProducer

- getGraphics

```java
public abstract
Graphics
getGraphics()
```

Creates a graphics context for drawing to an off-screen image.
This method can only be called for off-screen images.

**Returns:** a graphics context to draw to the off-screen image.
**Throws:** UnsupportedOperationException

- if called for a
non-off-screen image.
**See Also:** Graphics

,

Component.createImage(int, int)

- getProperty

```java
public abstract
Object
getProperty​(
String
name,

ImageObserver
observer)
```

Gets a property of this image by name.

Individual property names are defined by the various image
formats. If a property is not defined for a particular image, this
method returns the

UndefinedProperty

object.

If the properties for this image are not yet known, this method
returns

null

, and the

ImageObserver

object is notified later.

The property name

"comment"

should be used to store
an optional comment which can be presented to the application as a
description of the image, its source, or its author.

**Parameters:** name

- a property name.
**Parameters:** observer

- an object waiting for this image to be loaded.
**Returns:** the value of the named property.
**Throws:** NullPointerException

- if the property name is null.
**See Also:** ImageObserver

,

UndefinedProperty

- getScaledInstance

```java
public
Image
getScaledInstance​(int width,
int height,
int hints)
```

Creates a scaled version of this image.
A new

Image

object is returned which will render
the image at the specified

width

and

height

by default. The new

Image

object
may be loaded asynchronously even if the original source image
has already been loaded completely.

If either

width

or

height

is a negative number then a value is
substituted to maintain the aspect ratio of the original image
dimensions. If both

width

and

height

are negative, then the original image dimensions are used.

**Parameters:** width

- the width to which to scale the image.
**Parameters:** height

- the height to which to scale the image.
**Parameters:** hints

- flags to indicate the type of algorithm to use
for image resampling.
**Returns:** a scaled version of the image.
**Throws:** IllegalArgumentException

- if

width

or

height

is zero.
**Since:** 1.1
**See Also:** SCALE_DEFAULT

,

SCALE_FAST

,

SCALE_SMOOTH

,

SCALE_REPLICATE

,

SCALE_AREA_AVERAGING

- flush

```java
public void flush()
```

Flushes all reconstructable resources being used by this Image object.
This includes any pixel data that is being cached for rendering to
the screen as well as any system resources that are being used
to store data or pixels for the image if they can be recreated.
The image is reset to a state similar to when it was first created
so that if it is again rendered, the image data will have to be
recreated or fetched again from its source.

Examples of how this method affects specific types of Image object:

- BufferedImage objects leave the primary Raster which stores their
pixels untouched, but flush any information cached about those
pixels such as copies uploaded to the display hardware for
accelerated blits.

Image objects created by the Component methods which take a
width and height leave their primary buffer of pixels untouched,
but have all cached information released much like is done for
BufferedImage objects.

VolatileImage objects release all of their pixel resources
including their primary copy which is typically stored on
the display hardware where resources are scarce.
These objects can later be restored using their

validate

method.

Image objects created by the Toolkit and Component classes which are
loaded from files, URLs or produced by an

ImageProducer

are unloaded and all local resources are released.
These objects can later be reloaded from their original source
as needed when they are rendered, just as when they were first
created.

- getCapabilities

```java
public
ImageCapabilities
getCapabilities​(
GraphicsConfiguration
gc)
```

Returns an ImageCapabilities object which can be
inquired as to the capabilities of this
Image on the specified GraphicsConfiguration.
This allows programmers to find
out more runtime information on the specific Image
object that they have created. For example, the user
might create a BufferedImage but the system may have
no video memory left for creating an image of that
size on the given GraphicsConfiguration, so although the object
may be acceleratable in general, it
does not have that capability on this GraphicsConfiguration.

**Parameters:** gc

- a

GraphicsConfiguration

object. A value of null
for this parameter will result in getting the image capabilities
for the default

GraphicsConfiguration

.
**Returns:** an

ImageCapabilities

object that contains
the capabilities of this

Image

on the specified
GraphicsConfiguration.
**Since:** 1.5
**See Also:** VolatileImage.getCapabilities()

- setAccelerationPriority

```java
public void setAccelerationPriority​(float priority)
```

Sets a hint for this image about how important acceleration is.
This priority hint is used to compare to the priorities of other
Image objects when determining how to use scarce acceleration
resources such as video memory. When and if it is possible to
accelerate this Image, if there are not enough resources available
to provide that acceleration but enough can be freed up by
de-accelerating some other image of lower priority, then that other
Image may be de-accelerated in deference to this one. Images
that have the same priority take up resources on a first-come,
first-served basis.

**Parameters:** priority

- a value between 0 and 1, inclusive, where higher
values indicate more importance for acceleration. A value of 0
means that this Image should never be accelerated. Other values
are used simply to determine acceleration priority relative to other
Images.
**Throws:** IllegalArgumentException

- if

priority

is less
than zero or greater than 1.
**Since:** 1.5

- getAccelerationPriority

```java
public float getAccelerationPriority()
```

Returns the current value of the acceleration priority hint.

**Returns:** value between 0 and 1, inclusive, which represents the current
priority value
**Since:** 1.5
**See Also:** setAccelerationPriority

Field Detail

- accelerationPriority

```java
protected float accelerationPriority
```

Priority for accelerating this image. Subclasses are free to
set different default priorities and applications are free to
set the priority for specific images via the

setAccelerationPriority(float)

method.

**Since:** 1.5

- UndefinedProperty

```java
public static final
Object
UndefinedProperty
```

The

UndefinedProperty

object should be returned whenever a
property which was not defined for a particular image is fetched.

- SCALE_DEFAULT

```java
public static final int SCALE_DEFAULT
```

Use the default image-scaling algorithm.

**Since:** 1.1
**See Also:** Constant Field Values

- SCALE_FAST

```java
public static final int SCALE_FAST
```

Choose an image-scaling algorithm that gives higher priority
to scaling speed than smoothness of the scaled image.

**Since:** 1.1
**See Also:** Constant Field Values

- SCALE_SMOOTH

```java
public static final int SCALE_SMOOTH
```

Choose an image-scaling algorithm that gives higher priority
to image smoothness than scaling speed.

**Since:** 1.1
**See Also:** Constant Field Values

- SCALE_REPLICATE

```java
public static final int SCALE_REPLICATE
```

Use the image scaling algorithm embodied in the

ReplicateScaleFilter

class.
The

Image

object is free to substitute a different filter
that performs the same algorithm yet integrates more efficiently
into the imaging infrastructure supplied by the toolkit.

**Since:** 1.1
**See Also:** ReplicateScaleFilter

,

Constant Field Values

- SCALE_AREA_AVERAGING

```java
public static final int SCALE_AREA_AVERAGING
```

Use the Area Averaging image scaling algorithm. The
image object is free to substitute a different filter that
performs the same algorithm yet integrates more efficiently
into the image infrastructure supplied by the toolkit.

**Since:** 1.1
**See Also:** AreaAveragingScaleFilter

,

Constant Field Values

---

#### Field Detail

accelerationPriority

```java
protected float accelerationPriority
```

Priority for accelerating this image. Subclasses are free to
set different default priorities and applications are free to
set the priority for specific images via the

setAccelerationPriority(float)

method.

**Since:** 1.5

---

#### accelerationPriority

protected float accelerationPriority

Priority for accelerating this image. Subclasses are free to
set different default priorities and applications are free to
set the priority for specific images via the

setAccelerationPriority(float)

method.

UndefinedProperty

```java
public static final
Object
UndefinedProperty
```

The

UndefinedProperty

object should be returned whenever a
property which was not defined for a particular image is fetched.

---

#### UndefinedProperty

public static final

Object

UndefinedProperty

The

UndefinedProperty

object should be returned whenever a
property which was not defined for a particular image is fetched.

SCALE_DEFAULT

```java
public static final int SCALE_DEFAULT
```

Use the default image-scaling algorithm.

**Since:** 1.1
**See Also:** Constant Field Values

---

#### SCALE_DEFAULT

public static final int SCALE_DEFAULT

Use the default image-scaling algorithm.

SCALE_FAST

```java
public static final int SCALE_FAST
```

Choose an image-scaling algorithm that gives higher priority
to scaling speed than smoothness of the scaled image.

**Since:** 1.1
**See Also:** Constant Field Values

---

#### SCALE_FAST

public static final int SCALE_FAST

Choose an image-scaling algorithm that gives higher priority
to scaling speed than smoothness of the scaled image.

SCALE_SMOOTH

```java
public static final int SCALE_SMOOTH
```

Choose an image-scaling algorithm that gives higher priority
to image smoothness than scaling speed.

**Since:** 1.1
**See Also:** Constant Field Values

---

#### SCALE_SMOOTH

public static final int SCALE_SMOOTH

Choose an image-scaling algorithm that gives higher priority
to image smoothness than scaling speed.

SCALE_REPLICATE

```java
public static final int SCALE_REPLICATE
```

Use the image scaling algorithm embodied in the

ReplicateScaleFilter

class.
The

Image

object is free to substitute a different filter
that performs the same algorithm yet integrates more efficiently
into the imaging infrastructure supplied by the toolkit.

**Since:** 1.1
**See Also:** ReplicateScaleFilter

,

Constant Field Values

---

#### SCALE_REPLICATE

public static final int SCALE_REPLICATE

Use the image scaling algorithm embodied in the

ReplicateScaleFilter

class.
The

Image

object is free to substitute a different filter
that performs the same algorithm yet integrates more efficiently
into the imaging infrastructure supplied by the toolkit.

SCALE_AREA_AVERAGING

```java
public static final int SCALE_AREA_AVERAGING
```

Use the Area Averaging image scaling algorithm. The
image object is free to substitute a different filter that
performs the same algorithm yet integrates more efficiently
into the image infrastructure supplied by the toolkit.

**Since:** 1.1
**See Also:** AreaAveragingScaleFilter

,

Constant Field Values

---

#### SCALE_AREA_AVERAGING

public static final int SCALE_AREA_AVERAGING

Use the Area Averaging image scaling algorithm. The
image object is free to substitute a different filter that
performs the same algorithm yet integrates more efficiently
into the image infrastructure supplied by the toolkit.

Constructor Detail

- Image

```java
public Image()
```

---

#### Constructor Detail

Image

```java
public Image()
```

---

#### Image

public Image()

Method Detail

- getWidth

```java
public abstract int getWidth​(
ImageObserver
observer)
```

Determines the width of the image. If the width is not yet known,
this method returns

-1

and the specified

ImageObserver

object is notified later.

**Parameters:** observer

- an object waiting for the image to be loaded.
**Returns:** the width of this image, or

-1

if the width is not yet known.
**See Also:** getHeight(java.awt.image.ImageObserver)

,

ImageObserver

- getHeight

```java
public abstract int getHeight​(
ImageObserver
observer)
```

Determines the height of the image. If the height is not yet known,
this method returns

-1

and the specified

ImageObserver

object is notified later.

**Parameters:** observer

- an object waiting for the image to be loaded.
**Returns:** the height of this image, or

-1

if the height is not yet known.
**See Also:** getWidth(java.awt.image.ImageObserver)

,

ImageObserver

- getSource

```java
public abstract
ImageProducer
getSource()
```

Gets the object that produces the pixels for the image.
This method is called by the image filtering classes and by
methods that perform image conversion and scaling.

**Returns:** the image producer that produces the pixels
for this image.
**See Also:** ImageProducer

- getGraphics

```java
public abstract
Graphics
getGraphics()
```

Creates a graphics context for drawing to an off-screen image.
This method can only be called for off-screen images.

**Returns:** a graphics context to draw to the off-screen image.
**Throws:** UnsupportedOperationException

- if called for a
non-off-screen image.
**See Also:** Graphics

,

Component.createImage(int, int)

- getProperty

```java
public abstract
Object
getProperty​(
String
name,

ImageObserver
observer)
```

Gets a property of this image by name.

Individual property names are defined by the various image
formats. If a property is not defined for a particular image, this
method returns the

UndefinedProperty

object.

If the properties for this image are not yet known, this method
returns

null

, and the

ImageObserver

object is notified later.

The property name

"comment"

should be used to store
an optional comment which can be presented to the application as a
description of the image, its source, or its author.

**Parameters:** name

- a property name.
**Parameters:** observer

- an object waiting for this image to be loaded.
**Returns:** the value of the named property.
**Throws:** NullPointerException

- if the property name is null.
**See Also:** ImageObserver

,

UndefinedProperty

- getScaledInstance

```java
public
Image
getScaledInstance​(int width,
int height,
int hints)
```

Creates a scaled version of this image.
A new

Image

object is returned which will render
the image at the specified

width

and

height

by default. The new

Image

object
may be loaded asynchronously even if the original source image
has already been loaded completely.

If either

width

or

height

is a negative number then a value is
substituted to maintain the aspect ratio of the original image
dimensions. If both

width

and

height

are negative, then the original image dimensions are used.

**Parameters:** width

- the width to which to scale the image.
**Parameters:** height

- the height to which to scale the image.
**Parameters:** hints

- flags to indicate the type of algorithm to use
for image resampling.
**Returns:** a scaled version of the image.
**Throws:** IllegalArgumentException

- if

width

or

height

is zero.
**Since:** 1.1
**See Also:** SCALE_DEFAULT

,

SCALE_FAST

,

SCALE_SMOOTH

,

SCALE_REPLICATE

,

SCALE_AREA_AVERAGING

- flush

```java
public void flush()
```

Flushes all reconstructable resources being used by this Image object.
This includes any pixel data that is being cached for rendering to
the screen as well as any system resources that are being used
to store data or pixels for the image if they can be recreated.
The image is reset to a state similar to when it was first created
so that if it is again rendered, the image data will have to be
recreated or fetched again from its source.

Examples of how this method affects specific types of Image object:

- BufferedImage objects leave the primary Raster which stores their
pixels untouched, but flush any information cached about those
pixels such as copies uploaded to the display hardware for
accelerated blits.

Image objects created by the Component methods which take a
width and height leave their primary buffer of pixels untouched,
but have all cached information released much like is done for
BufferedImage objects.

VolatileImage objects release all of their pixel resources
including their primary copy which is typically stored on
the display hardware where resources are scarce.
These objects can later be restored using their

validate

method.

Image objects created by the Toolkit and Component classes which are
loaded from files, URLs or produced by an

ImageProducer

are unloaded and all local resources are released.
These objects can later be reloaded from their original source
as needed when they are rendered, just as when they were first
created.

- getCapabilities

```java
public
ImageCapabilities
getCapabilities​(
GraphicsConfiguration
gc)
```

Returns an ImageCapabilities object which can be
inquired as to the capabilities of this
Image on the specified GraphicsConfiguration.
This allows programmers to find
out more runtime information on the specific Image
object that they have created. For example, the user
might create a BufferedImage but the system may have
no video memory left for creating an image of that
size on the given GraphicsConfiguration, so although the object
may be acceleratable in general, it
does not have that capability on this GraphicsConfiguration.

**Parameters:** gc

- a

GraphicsConfiguration

object. A value of null
for this parameter will result in getting the image capabilities
for the default

GraphicsConfiguration

.
**Returns:** an

ImageCapabilities

object that contains
the capabilities of this

Image

on the specified
GraphicsConfiguration.
**Since:** 1.5
**See Also:** VolatileImage.getCapabilities()

- setAccelerationPriority

```java
public void setAccelerationPriority​(float priority)
```

Sets a hint for this image about how important acceleration is.
This priority hint is used to compare to the priorities of other
Image objects when determining how to use scarce acceleration
resources such as video memory. When and if it is possible to
accelerate this Image, if there are not enough resources available
to provide that acceleration but enough can be freed up by
de-accelerating some other image of lower priority, then that other
Image may be de-accelerated in deference to this one. Images
that have the same priority take up resources on a first-come,
first-served basis.

**Parameters:** priority

- a value between 0 and 1, inclusive, where higher
values indicate more importance for acceleration. A value of 0
means that this Image should never be accelerated. Other values
are used simply to determine acceleration priority relative to other
Images.
**Throws:** IllegalArgumentException

- if

priority

is less
than zero or greater than 1.
**Since:** 1.5

- getAccelerationPriority

```java
public float getAccelerationPriority()
```

Returns the current value of the acceleration priority hint.

**Returns:** value between 0 and 1, inclusive, which represents the current
priority value
**Since:** 1.5
**See Also:** setAccelerationPriority

---

#### Method Detail

getWidth

```java
public abstract int getWidth​(
ImageObserver
observer)
```

Determines the width of the image. If the width is not yet known,
this method returns

-1

and the specified

ImageObserver

object is notified later.

**Parameters:** observer

- an object waiting for the image to be loaded.
**Returns:** the width of this image, or

-1

if the width is not yet known.
**See Also:** getHeight(java.awt.image.ImageObserver)

,

ImageObserver

---

#### getWidth

public abstract int getWidth​(

ImageObserver

observer)

Determines the width of the image. If the width is not yet known,
this method returns

-1

and the specified

ImageObserver

object is notified later.

getHeight

```java
public abstract int getHeight​(
ImageObserver
observer)
```

Determines the height of the image. If the height is not yet known,
this method returns

-1

and the specified

ImageObserver

object is notified later.

**Parameters:** observer

- an object waiting for the image to be loaded.
**Returns:** the height of this image, or

-1

if the height is not yet known.
**See Also:** getWidth(java.awt.image.ImageObserver)

,

ImageObserver

---

#### getHeight

public abstract int getHeight​(

ImageObserver

observer)

Determines the height of the image. If the height is not yet known,
this method returns

-1

and the specified

ImageObserver

object is notified later.

getSource

```java
public abstract
ImageProducer
getSource()
```

Gets the object that produces the pixels for the image.
This method is called by the image filtering classes and by
methods that perform image conversion and scaling.

**Returns:** the image producer that produces the pixels
for this image.
**See Also:** ImageProducer

---

#### getSource

public abstract

ImageProducer

getSource()

Gets the object that produces the pixels for the image.
This method is called by the image filtering classes and by
methods that perform image conversion and scaling.

getGraphics

```java
public abstract
Graphics
getGraphics()
```

Creates a graphics context for drawing to an off-screen image.
This method can only be called for off-screen images.

**Returns:** a graphics context to draw to the off-screen image.
**Throws:** UnsupportedOperationException

- if called for a
non-off-screen image.
**See Also:** Graphics

,

Component.createImage(int, int)

---

#### getGraphics

public abstract

Graphics

getGraphics()

Creates a graphics context for drawing to an off-screen image.
This method can only be called for off-screen images.

getProperty

```java
public abstract
Object
getProperty​(
String
name,

ImageObserver
observer)
```

Gets a property of this image by name.

Individual property names are defined by the various image
formats. If a property is not defined for a particular image, this
method returns the

UndefinedProperty

object.

If the properties for this image are not yet known, this method
returns

null

, and the

ImageObserver

object is notified later.

The property name

"comment"

should be used to store
an optional comment which can be presented to the application as a
description of the image, its source, or its author.

**Parameters:** name

- a property name.
**Parameters:** observer

- an object waiting for this image to be loaded.
**Returns:** the value of the named property.
**Throws:** NullPointerException

- if the property name is null.
**See Also:** ImageObserver

,

UndefinedProperty

---

#### getProperty

public abstract

Object

getProperty​(

String

name,

ImageObserver

observer)

Gets a property of this image by name.

Individual property names are defined by the various image
formats. If a property is not defined for a particular image, this
method returns the

UndefinedProperty

object.

If the properties for this image are not yet known, this method
returns

null

, and the

ImageObserver

object is notified later.

The property name

"comment"

should be used to store
an optional comment which can be presented to the application as a
description of the image, its source, or its author.

Individual property names are defined by the various image
formats. If a property is not defined for a particular image, this
method returns the

UndefinedProperty

object.

If the properties for this image are not yet known, this method
returns

null

, and the

ImageObserver

object is notified later.

The property name

"comment"

should be used to store
an optional comment which can be presented to the application as a
description of the image, its source, or its author.

If the properties for this image are not yet known, this method
returns

null

, and the

ImageObserver

object is notified later.

The property name

"comment"

should be used to store
an optional comment which can be presented to the application as a
description of the image, its source, or its author.

The property name

"comment"

should be used to store
an optional comment which can be presented to the application as a
description of the image, its source, or its author.

getScaledInstance

```java
public
Image
getScaledInstance​(int width,
int height,
int hints)
```

Creates a scaled version of this image.
A new

Image

object is returned which will render
the image at the specified

width

and

height

by default. The new

Image

object
may be loaded asynchronously even if the original source image
has already been loaded completely.

If either

width

or

height

is a negative number then a value is
substituted to maintain the aspect ratio of the original image
dimensions. If both

width

and

height

are negative, then the original image dimensions are used.

**Parameters:** width

- the width to which to scale the image.
**Parameters:** height

- the height to which to scale the image.
**Parameters:** hints

- flags to indicate the type of algorithm to use
for image resampling.
**Returns:** a scaled version of the image.
**Throws:** IllegalArgumentException

- if

width

or

height

is zero.
**Since:** 1.1
**See Also:** SCALE_DEFAULT

,

SCALE_FAST

,

SCALE_SMOOTH

,

SCALE_REPLICATE

,

SCALE_AREA_AVERAGING

---

#### getScaledInstance

public

Image

getScaledInstance​(int width,
int height,
int hints)

Creates a scaled version of this image.
A new

Image

object is returned which will render
the image at the specified

width

and

height

by default. The new

Image

object
may be loaded asynchronously even if the original source image
has already been loaded completely.

If either

width

or

height

is a negative number then a value is
substituted to maintain the aspect ratio of the original image
dimensions. If both

width

and

height

are negative, then the original image dimensions are used.

If either

width

or

height

is a negative number then a value is
substituted to maintain the aspect ratio of the original image
dimensions. If both

width

and

height

are negative, then the original image dimensions are used.

flush

```java
public void flush()
```

Flushes all reconstructable resources being used by this Image object.
This includes any pixel data that is being cached for rendering to
the screen as well as any system resources that are being used
to store data or pixels for the image if they can be recreated.
The image is reset to a state similar to when it was first created
so that if it is again rendered, the image data will have to be
recreated or fetched again from its source.

Examples of how this method affects specific types of Image object:

- BufferedImage objects leave the primary Raster which stores their
pixels untouched, but flush any information cached about those
pixels such as copies uploaded to the display hardware for
accelerated blits.

Image objects created by the Component methods which take a
width and height leave their primary buffer of pixels untouched,
but have all cached information released much like is done for
BufferedImage objects.

VolatileImage objects release all of their pixel resources
including their primary copy which is typically stored on
the display hardware where resources are scarce.
These objects can later be restored using their

validate

method.

Image objects created by the Toolkit and Component classes which are
loaded from files, URLs or produced by an

ImageProducer

are unloaded and all local resources are released.
These objects can later be reloaded from their original source
as needed when they are rendered, just as when they were first
created.

---

#### flush

public void flush()

Flushes all reconstructable resources being used by this Image object.
This includes any pixel data that is being cached for rendering to
the screen as well as any system resources that are being used
to store data or pixels for the image if they can be recreated.
The image is reset to a state similar to when it was first created
so that if it is again rendered, the image data will have to be
recreated or fetched again from its source.

Examples of how this method affects specific types of Image object:

- BufferedImage objects leave the primary Raster which stores their
pixels untouched, but flush any information cached about those
pixels such as copies uploaded to the display hardware for
accelerated blits.

Image objects created by the Component methods which take a
width and height leave their primary buffer of pixels untouched,
but have all cached information released much like is done for
BufferedImage objects.

VolatileImage objects release all of their pixel resources
including their primary copy which is typically stored on
the display hardware where resources are scarce.
These objects can later be restored using their

validate

method.

Image objects created by the Toolkit and Component classes which are
loaded from files, URLs or produced by an

ImageProducer

are unloaded and all local resources are released.
These objects can later be reloaded from their original source
as needed when they are rendered, just as when they were first
created.

Examples of how this method affects specific types of Image object:

- BufferedImage objects leave the primary Raster which stores their
pixels untouched, but flush any information cached about those
pixels such as copies uploaded to the display hardware for
accelerated blits.

Image objects created by the Component methods which take a
width and height leave their primary buffer of pixels untouched,
but have all cached information released much like is done for
BufferedImage objects.

VolatileImage objects release all of their pixel resources
including their primary copy which is typically stored on
the display hardware where resources are scarce.
These objects can later be restored using their

validate

method.

Image objects created by the Toolkit and Component classes which are
loaded from files, URLs or produced by an

ImageProducer

are unloaded and all local resources are released.
These objects can later be reloaded from their original source
as needed when they are rendered, just as when they were first
created.

BufferedImage objects leave the primary Raster which stores their
pixels untouched, but flush any information cached about those
pixels such as copies uploaded to the display hardware for
accelerated blits.

Image objects created by the Component methods which take a
width and height leave their primary buffer of pixels untouched,
but have all cached information released much like is done for
BufferedImage objects.

VolatileImage objects release all of their pixel resources
including their primary copy which is typically stored on
the display hardware where resources are scarce.
These objects can later be restored using their

validate

method.

Image objects created by the Toolkit and Component classes which are
loaded from files, URLs or produced by an

ImageProducer

are unloaded and all local resources are released.
These objects can later be reloaded from their original source
as needed when they are rendered, just as when they were first
created.

getCapabilities

```java
public
ImageCapabilities
getCapabilities​(
GraphicsConfiguration
gc)
```

Returns an ImageCapabilities object which can be
inquired as to the capabilities of this
Image on the specified GraphicsConfiguration.
This allows programmers to find
out more runtime information on the specific Image
object that they have created. For example, the user
might create a BufferedImage but the system may have
no video memory left for creating an image of that
size on the given GraphicsConfiguration, so although the object
may be acceleratable in general, it
does not have that capability on this GraphicsConfiguration.

**Parameters:** gc

- a

GraphicsConfiguration

object. A value of null
for this parameter will result in getting the image capabilities
for the default

GraphicsConfiguration

.
**Returns:** an

ImageCapabilities

object that contains
the capabilities of this

Image

on the specified
GraphicsConfiguration.
**Since:** 1.5
**See Also:** VolatileImage.getCapabilities()

---

#### getCapabilities

public

ImageCapabilities

getCapabilities​(

GraphicsConfiguration

gc)

Returns an ImageCapabilities object which can be
inquired as to the capabilities of this
Image on the specified GraphicsConfiguration.
This allows programmers to find
out more runtime information on the specific Image
object that they have created. For example, the user
might create a BufferedImage but the system may have
no video memory left for creating an image of that
size on the given GraphicsConfiguration, so although the object
may be acceleratable in general, it
does not have that capability on this GraphicsConfiguration.

setAccelerationPriority

```java
public void setAccelerationPriority​(float priority)
```

Sets a hint for this image about how important acceleration is.
This priority hint is used to compare to the priorities of other
Image objects when determining how to use scarce acceleration
resources such as video memory. When and if it is possible to
accelerate this Image, if there are not enough resources available
to provide that acceleration but enough can be freed up by
de-accelerating some other image of lower priority, then that other
Image may be de-accelerated in deference to this one. Images
that have the same priority take up resources on a first-come,
first-served basis.

**Parameters:** priority

- a value between 0 and 1, inclusive, where higher
values indicate more importance for acceleration. A value of 0
means that this Image should never be accelerated. Other values
are used simply to determine acceleration priority relative to other
Images.
**Throws:** IllegalArgumentException

- if

priority

is less
than zero or greater than 1.
**Since:** 1.5

---

#### setAccelerationPriority

public void setAccelerationPriority​(float priority)

Sets a hint for this image about how important acceleration is.
This priority hint is used to compare to the priorities of other
Image objects when determining how to use scarce acceleration
resources such as video memory. When and if it is possible to
accelerate this Image, if there are not enough resources available
to provide that acceleration but enough can be freed up by
de-accelerating some other image of lower priority, then that other
Image may be de-accelerated in deference to this one. Images
that have the same priority take up resources on a first-come,
first-served basis.

getAccelerationPriority

```java
public float getAccelerationPriority()
```

Returns the current value of the acceleration priority hint.

**Returns:** value between 0 and 1, inclusive, which represents the current
priority value
**Since:** 1.5
**See Also:** setAccelerationPriority

---

#### getAccelerationPriority

public float getAccelerationPriority()

Returns the current value of the acceleration priority hint.

---

