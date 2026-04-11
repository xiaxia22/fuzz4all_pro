# Class AbstractMultiResolutionImage

**Source:** `java.desktop\java\awt\image\AbstractMultiResolutionImage.html`

### Class Description

```java
public abstract class
AbstractMultiResolutionImage

extends
Image

implements
MultiResolutionImage
```

This class provides default implementations of several

Image

methods
for classes that want to implement the

MultiResolutionImage

interface.

For example,

```java
public class CustomMultiResolutionImage extends AbstractMultiResolutionImage {

final Image[] resolutionVariants;

public CustomMultiResolutionImage(Image... resolutionVariants) {
this.resolutionVariants = resolutionVariants;
}

public Image getResolutionVariant(
double destImageWidth, double destImageHeight) {
// return a resolution variant based on the given destination image size
}

public List<Image> getResolutionVariants() {
return Collections.unmodifiableList(Arrays.asList(resolutionVariants));
}

protected Image getBaseImage() {
return resolutionVariants[0];
}
}
```

**All Implemented Interfaces:** MultiResolutionImage

---

### Field Details

*No entries found.*

### Constructor Details

#### public AbstractMultiResolutionImage()

*No description found.*

---

### Method Details

#### public int getWidth​(
ImageObserver
observer)

This method simply delegates to the same method on the base image and
it is equivalent to:

getBaseImage().getWidth(observer)

.

**Specified by:**
- getWidth

in class

Image

**Parameters:**
- observer

- an object waiting for the image to be loaded.

**Returns:**
- the width of the base image, or -1 if the width is not yet known

**See Also:**
- getBaseImage()

**Since:**
- 9

---

#### public int getHeight​(
ImageObserver
observer)

This method simply delegates to the same method on the base image and
it is equivalent to:

getBaseImage().getHeight(observer)

.

**Specified by:**
- getHeight

in class

Image

**Parameters:**
- observer

- an object waiting for the image to be loaded.

**Returns:**
- the height of the base image, or -1 if the height is not yet known

**See Also:**
- getBaseImage()

**Since:**
- 9

---

#### public
ImageProducer
getSource()

This method simply delegates to the same method on the base image and
it is equivalent to:

getBaseImage().getSource()

.

**Specified by:**
- getSource

in class

Image

**Returns:**
- the image producer that produces the pixels for the base image

**See Also:**
- getBaseImage()

**Since:**
- 9

---

#### public
Graphics
getGraphics()

As per the contract of the base

Image#getGraphics()

method,
this implementation will always throw

UnsupportedOperationException

since only off-screen images can return a

Graphics

object.

**Specified by:**
- getGraphics

in class

Image

**Returns:**
- throws

UnsupportedOperationException

**Throws:**
- UnsupportedOperationException

- this method is not supported

**See Also:**
- Graphics

,

Component.createImage(int, int)

---

#### public
Object
getProperty​(
String
name,

ImageObserver
observer)

This method simply delegates to the same method on the base image and
it is equivalent to:

getBaseImage().getProperty(name, observer)

.

**Specified by:**
- getProperty

in class

Image

**Parameters:**
- name

- a property name.
- observer

- an object waiting for this image to be loaded.

**Returns:**
- the value of the named property in the base image

**See Also:**
- getBaseImage()

**Since:**
- 9

---

#### protected abstract
Image
getBaseImage()

Return the base image representing the best version of the image for
rendering at the default width and height.

**Returns:**
- the base image of the set of multi-resolution images

**Since:**
- 9

---

### Additional Sections

#### Class AbstractMultiResolutionImage

java.lang.Object

- java.awt.Image
- - java.awt.image.AbstractMultiResolutionImage

java.awt.Image

- java.awt.image.AbstractMultiResolutionImage

java.awt.image.AbstractMultiResolutionImage

**All Implemented Interfaces:** MultiResolutionImage

**Direct Known Subclasses:** BaseMultiResolutionImage

```java
public abstract class
AbstractMultiResolutionImage

extends
Image

implements
MultiResolutionImage
```

This class provides default implementations of several

Image

methods
for classes that want to implement the

MultiResolutionImage

interface.

For example,

```java
public class CustomMultiResolutionImage extends AbstractMultiResolutionImage {

final Image[] resolutionVariants;

public CustomMultiResolutionImage(Image... resolutionVariants) {
this.resolutionVariants = resolutionVariants;
}

public Image getResolutionVariant(
double destImageWidth, double destImageHeight) {
// return a resolution variant based on the given destination image size
}

public List<Image> getResolutionVariants() {
return Collections.unmodifiableList(Arrays.asList(resolutionVariants));
}

protected Image getBaseImage() {
return resolutionVariants[0];
}
}
```

**Since:** 9
**See Also:** Image

,

MultiResolutionImage

public abstract class

AbstractMultiResolutionImage

extends

Image

implements

MultiResolutionImage

This class provides default implementations of several

Image

methods
for classes that want to implement the

MultiResolutionImage

interface.

For example,

```java
public class CustomMultiResolutionImage extends AbstractMultiResolutionImage {

final Image[] resolutionVariants;

public CustomMultiResolutionImage(Image... resolutionVariants) {
this.resolutionVariants = resolutionVariants;
}

public Image getResolutionVariant(
double destImageWidth, double destImageHeight) {
// return a resolution variant based on the given destination image size
}

public List<Image> getResolutionVariants() {
return Collections.unmodifiableList(Arrays.asList(resolutionVariants));
}

protected Image getBaseImage() {
return resolutionVariants[0];
}
}
```

public class CustomMultiResolutionImage extends AbstractMultiResolutionImage {

final Image[] resolutionVariants;

public CustomMultiResolutionImage(Image... resolutionVariants) {
this.resolutionVariants = resolutionVariants;
}

public Image getResolutionVariant(
double destImageWidth, double destImageHeight) {
// return a resolution variant based on the given destination image size
}

public List<Image> getResolutionVariants() {
return Collections.unmodifiableList(Arrays.asList(resolutionVariants));
}

protected Image getBaseImage() {
return resolutionVariants[0];
}
}

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.awt.

Image

accelerationPriority

,

SCALE_AREA_AVERAGING

,

SCALE_DEFAULT

,

SCALE_FAST

,

SCALE_REPLICATE

,

SCALE_SMOOTH

,

UndefinedProperty

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AbstractMultiResolutionImage

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

protected abstract

Image

getBaseImage

()

Return the base image representing the best version of the image for
rendering at the default width and height.

Graphics

getGraphics

()

As per the contract of the base

Image#getGraphics()

method,
this implementation will always throw

UnsupportedOperationException

since only off-screen images can return a

Graphics

object.

int

getHeight

​(

ImageObserver

observer)

This method simply delegates to the same method on the base image and
it is equivalent to:

getBaseImage().getHeight(observer)

.

Object

getProperty

​(

String

name,

ImageObserver

observer)

This method simply delegates to the same method on the base image and
it is equivalent to:

getBaseImage().getProperty(name, observer)

.

ImageProducer

getSource

()

This method simply delegates to the same method on the base image and
it is equivalent to:

getBaseImage().getSource()

.

int

getWidth

​(

ImageObserver

observer)

This method simply delegates to the same method on the base image and
it is equivalent to:

getBaseImage().getWidth(observer)

.

- Methods declared in class java.awt.

Image

flush

,

getAccelerationPriority

,

getCapabilities

,

getScaledInstance

,

setAccelerationPriority

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

- Methods declared in interface java.awt.image.

MultiResolutionImage

getResolutionVariant

,

getResolutionVariants

Field Summary

- Fields declared in class java.awt.

Image

accelerationPriority

,

SCALE_AREA_AVERAGING

,

SCALE_DEFAULT

,

SCALE_FAST

,

SCALE_REPLICATE

,

SCALE_SMOOTH

,

UndefinedProperty

---

#### Field Summary

Fields declared in class java.awt.

Image

accelerationPriority

,

SCALE_AREA_AVERAGING

,

SCALE_DEFAULT

,

SCALE_FAST

,

SCALE_REPLICATE

,

SCALE_SMOOTH

,

UndefinedProperty

---

#### Fields declared in class java.awt. Image

Constructor Summary

Constructors

Constructor

Description

AbstractMultiResolutionImage

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

protected abstract

Image

getBaseImage

()

Return the base image representing the best version of the image for
rendering at the default width and height.

Graphics

getGraphics

()

As per the contract of the base

Image#getGraphics()

method,
this implementation will always throw

UnsupportedOperationException

since only off-screen images can return a

Graphics

object.

int

getHeight

​(

ImageObserver

observer)

This method simply delegates to the same method on the base image and
it is equivalent to:

getBaseImage().getHeight(observer)

.

Object

getProperty

​(

String

name,

ImageObserver

observer)

This method simply delegates to the same method on the base image and
it is equivalent to:

getBaseImage().getProperty(name, observer)

.

ImageProducer

getSource

()

This method simply delegates to the same method on the base image and
it is equivalent to:

getBaseImage().getSource()

.

int

getWidth

​(

ImageObserver

observer)

This method simply delegates to the same method on the base image and
it is equivalent to:

getBaseImage().getWidth(observer)

.

- Methods declared in class java.awt.

Image

flush

,

getAccelerationPriority

,

getCapabilities

,

getScaledInstance

,

setAccelerationPriority

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

- Methods declared in interface java.awt.image.

MultiResolutionImage

getResolutionVariant

,

getResolutionVariants

---

#### Method Summary

Return the base image representing the best version of the image for
rendering at the default width and height.

As per the contract of the base

Image#getGraphics()

method,
this implementation will always throw

UnsupportedOperationException

since only off-screen images can return a

Graphics

object.

This method simply delegates to the same method on the base image and
it is equivalent to:

getBaseImage().getHeight(observer)

.

This method simply delegates to the same method on the base image and
it is equivalent to:

getBaseImage().getProperty(name, observer)

.

This method simply delegates to the same method on the base image and
it is equivalent to:

getBaseImage().getSource()

.

This method simply delegates to the same method on the base image and
it is equivalent to:

getBaseImage().getWidth(observer)

.

Methods declared in class java.awt.

Image

flush

,

getAccelerationPriority

,

getCapabilities

,

getScaledInstance

,

setAccelerationPriority

---

#### Methods declared in class java.awt. Image

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

Methods declared in interface java.awt.image.

MultiResolutionImage

getResolutionVariant

,

getResolutionVariants

---

#### Methods declared in interface java.awt.image. MultiResolutionImage

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AbstractMultiResolutionImage

```java
public AbstractMultiResolutionImage()
```

============ METHOD DETAIL ==========

- Method Detail

- getWidth

```java
public int getWidth​(
ImageObserver
observer)
```

This method simply delegates to the same method on the base image and
it is equivalent to:

getBaseImage().getWidth(observer)

.

**Specified by:** getWidth

in class

Image
**Parameters:** observer

- an object waiting for the image to be loaded.
**Returns:** the width of the base image, or -1 if the width is not yet known
**Since:** 9
**See Also:** getBaseImage()

- getHeight

```java
public int getHeight​(
ImageObserver
observer)
```

This method simply delegates to the same method on the base image and
it is equivalent to:

getBaseImage().getHeight(observer)

.

**Specified by:** getHeight

in class

Image
**Parameters:** observer

- an object waiting for the image to be loaded.
**Returns:** the height of the base image, or -1 if the height is not yet known
**Since:** 9
**See Also:** getBaseImage()

- getSource

```java
public
ImageProducer
getSource()
```

This method simply delegates to the same method on the base image and
it is equivalent to:

getBaseImage().getSource()

.

**Specified by:** getSource

in class

Image
**Returns:** the image producer that produces the pixels for the base image
**Since:** 9
**See Also:** getBaseImage()

- getGraphics

```java
public
Graphics
getGraphics()
```

As per the contract of the base

Image#getGraphics()

method,
this implementation will always throw

UnsupportedOperationException

since only off-screen images can return a

Graphics

object.

**Specified by:** getGraphics

in class

Image
**Returns:** throws

UnsupportedOperationException
**Throws:** UnsupportedOperationException

- this method is not supported
**See Also:** Graphics

,

Component.createImage(int, int)

- getProperty

```java
public
Object
getProperty​(
String
name,

ImageObserver
observer)
```

This method simply delegates to the same method on the base image and
it is equivalent to:

getBaseImage().getProperty(name, observer)

.

**Specified by:** getProperty

in class

Image
**Parameters:** name

- a property name.
**Parameters:** observer

- an object waiting for this image to be loaded.
**Returns:** the value of the named property in the base image
**Since:** 9
**See Also:** getBaseImage()

- getBaseImage

```java
protected abstract
Image
getBaseImage()
```

Return the base image representing the best version of the image for
rendering at the default width and height.

**Returns:** the base image of the set of multi-resolution images
**Since:** 9

Constructor Detail

- AbstractMultiResolutionImage

```java
public AbstractMultiResolutionImage()
```

---

#### Constructor Detail

AbstractMultiResolutionImage

```java
public AbstractMultiResolutionImage()
```

---

#### AbstractMultiResolutionImage

public AbstractMultiResolutionImage()

Method Detail

- getWidth

```java
public int getWidth​(
ImageObserver
observer)
```

This method simply delegates to the same method on the base image and
it is equivalent to:

getBaseImage().getWidth(observer)

.

**Specified by:** getWidth

in class

Image
**Parameters:** observer

- an object waiting for the image to be loaded.
**Returns:** the width of the base image, or -1 if the width is not yet known
**Since:** 9
**See Also:** getBaseImage()

- getHeight

```java
public int getHeight​(
ImageObserver
observer)
```

This method simply delegates to the same method on the base image and
it is equivalent to:

getBaseImage().getHeight(observer)

.

**Specified by:** getHeight

in class

Image
**Parameters:** observer

- an object waiting for the image to be loaded.
**Returns:** the height of the base image, or -1 if the height is not yet known
**Since:** 9
**See Also:** getBaseImage()

- getSource

```java
public
ImageProducer
getSource()
```

This method simply delegates to the same method on the base image and
it is equivalent to:

getBaseImage().getSource()

.

**Specified by:** getSource

in class

Image
**Returns:** the image producer that produces the pixels for the base image
**Since:** 9
**See Also:** getBaseImage()

- getGraphics

```java
public
Graphics
getGraphics()
```

As per the contract of the base

Image#getGraphics()

method,
this implementation will always throw

UnsupportedOperationException

since only off-screen images can return a

Graphics

object.

**Specified by:** getGraphics

in class

Image
**Returns:** throws

UnsupportedOperationException
**Throws:** UnsupportedOperationException

- this method is not supported
**See Also:** Graphics

,

Component.createImage(int, int)

- getProperty

```java
public
Object
getProperty​(
String
name,

ImageObserver
observer)
```

This method simply delegates to the same method on the base image and
it is equivalent to:

getBaseImage().getProperty(name, observer)

.

**Specified by:** getProperty

in class

Image
**Parameters:** name

- a property name.
**Parameters:** observer

- an object waiting for this image to be loaded.
**Returns:** the value of the named property in the base image
**Since:** 9
**See Also:** getBaseImage()

- getBaseImage

```java
protected abstract
Image
getBaseImage()
```

Return the base image representing the best version of the image for
rendering at the default width and height.

**Returns:** the base image of the set of multi-resolution images
**Since:** 9

---

#### Method Detail

getWidth

```java
public int getWidth​(
ImageObserver
observer)
```

This method simply delegates to the same method on the base image and
it is equivalent to:

getBaseImage().getWidth(observer)

.

**Specified by:** getWidth

in class

Image
**Parameters:** observer

- an object waiting for the image to be loaded.
**Returns:** the width of the base image, or -1 if the width is not yet known
**Since:** 9
**See Also:** getBaseImage()

---

#### getWidth

public int getWidth​(

ImageObserver

observer)

This method simply delegates to the same method on the base image and
it is equivalent to:

getBaseImage().getWidth(observer)

.

getHeight

```java
public int getHeight​(
ImageObserver
observer)
```

This method simply delegates to the same method on the base image and
it is equivalent to:

getBaseImage().getHeight(observer)

.

**Specified by:** getHeight

in class

Image
**Parameters:** observer

- an object waiting for the image to be loaded.
**Returns:** the height of the base image, or -1 if the height is not yet known
**Since:** 9
**See Also:** getBaseImage()

---

#### getHeight

public int getHeight​(

ImageObserver

observer)

This method simply delegates to the same method on the base image and
it is equivalent to:

getBaseImage().getHeight(observer)

.

getSource

```java
public
ImageProducer
getSource()
```

This method simply delegates to the same method on the base image and
it is equivalent to:

getBaseImage().getSource()

.

**Specified by:** getSource

in class

Image
**Returns:** the image producer that produces the pixels for the base image
**Since:** 9
**See Also:** getBaseImage()

---

#### getSource

public

ImageProducer

getSource()

This method simply delegates to the same method on the base image and
it is equivalent to:

getBaseImage().getSource()

.

getGraphics

```java
public
Graphics
getGraphics()
```

As per the contract of the base

Image#getGraphics()

method,
this implementation will always throw

UnsupportedOperationException

since only off-screen images can return a

Graphics

object.

**Specified by:** getGraphics

in class

Image
**Returns:** throws

UnsupportedOperationException
**Throws:** UnsupportedOperationException

- this method is not supported
**See Also:** Graphics

,

Component.createImage(int, int)

---

#### getGraphics

public

Graphics

getGraphics()

As per the contract of the base

Image#getGraphics()

method,
this implementation will always throw

UnsupportedOperationException

since only off-screen images can return a

Graphics

object.

getProperty

```java
public
Object
getProperty​(
String
name,

ImageObserver
observer)
```

This method simply delegates to the same method on the base image and
it is equivalent to:

getBaseImage().getProperty(name, observer)

.

**Specified by:** getProperty

in class

Image
**Parameters:** name

- a property name.
**Parameters:** observer

- an object waiting for this image to be loaded.
**Returns:** the value of the named property in the base image
**Since:** 9
**See Also:** getBaseImage()

---

#### getProperty

public

Object

getProperty​(

String

name,

ImageObserver

observer)

This method simply delegates to the same method on the base image and
it is equivalent to:

getBaseImage().getProperty(name, observer)

.

getBaseImage

```java
protected abstract
Image
getBaseImage()
```

Return the base image representing the best version of the image for
rendering at the default width and height.

**Returns:** the base image of the set of multi-resolution images
**Since:** 9

---

#### getBaseImage

protected abstract

Image

getBaseImage()

Return the base image representing the best version of the image for
rendering at the default width and height.

---

