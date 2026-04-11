# Class FilteredImageSource

**Source:** `java.desktop\java\awt\image\FilteredImageSource.html`

### Class Description

```java
public class
FilteredImageSource

extends
Object

implements
ImageProducer
```

This class is an implementation of the ImageProducer interface which
takes an existing image and a filter object and uses them to produce
image data for a new filtered version of the original image. Furthermore,

FilteredImageSource

is safe for use by multiple threads.
Here is an example which filters an image by swapping the red and
blue components:

```java
Image src = getImage("doc:///demo/images/duke/T1.gif");
ImageFilter colorfilter = new RedBlueSwapFilter();
Image img = createImage(new FilteredImageSource(src.getSource(),
colorfilter));
```

**All Implemented Interfaces:** ImageProducer

---

### Field Details

*No entries found.*

### Constructor Details

#### public FilteredImageSource​(
ImageProducer
orig,

ImageFilter
imgf)

Constructs an ImageProducer object from an existing ImageProducer
and a filter object.

**Parameters:**
- orig

- the specified

ImageProducer
- imgf

- the specified

ImageFilter

**See Also:**
- ImageFilter

,

Component.createImage(java.awt.image.ImageProducer)

---

### Method Details

#### public void addConsumer​(
ImageConsumer
ic)

Adds the specified

ImageConsumer

to the list of consumers interested in data for the filtered image.
An instance of the original

ImageFilter

is created
(using the filter's

getFilterInstance

method)
to manipulate the image data
for the specified

ImageConsumer

.
The newly created filter instance
is then passed to the

addConsumer

method
of the original

ImageProducer

.

This method is public as a side effect
of this class implementing
the

ImageProducer

interface.
It should not be called from user code,
and its behavior if called from user code is unspecified.

**Specified by:**
- addConsumer

in interface

ImageProducer

**Parameters:**
- ic

- the consumer for the filtered image

**See Also:**
- ImageConsumer

---

#### public boolean isConsumer​(
ImageConsumer
ic)

Determines whether an ImageConsumer is on the list of consumers
currently interested in data for this image.

This method is public as a side effect
of this class implementing
the

ImageProducer

interface.
It should not be called from user code,
and its behavior if called from user code is unspecified.

**Specified by:**
- isConsumer

in interface

ImageProducer

**Parameters:**
- ic

- the specified

ImageConsumer

**Returns:**
- true if the ImageConsumer is on the list; false otherwise

**See Also:**
- ImageConsumer

---

#### public void removeConsumer​(
ImageConsumer
ic)

Removes an ImageConsumer from the list of consumers interested in
data for this image.

This method is public as a side effect
of this class implementing
the

ImageProducer

interface.
It should not be called from user code,
and its behavior if called from user code is unspecified.

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

Starts production of the filtered image.
If the specified

ImageConsumer

isn't already a consumer of the filtered image,
an instance of the original

ImageFilter

is created
(using the filter's

getFilterInstance

method)
to manipulate the image data
for the

ImageConsumer

.
The filter instance for the

ImageConsumer

is then passed to the

startProduction

method
of the original

ImageProducer

.

This method is public as a side effect
of this class implementing
the

ImageProducer

interface.
It should not be called from user code,
and its behavior if called from user code is unspecified.

**Specified by:**
- startProduction

in interface

ImageProducer

**Parameters:**
- ic

- the consumer for the filtered image

**See Also:**
- ImageConsumer

---

#### public void requestTopDownLeftRightResend​(
ImageConsumer
ic)

Requests that a given ImageConsumer have the image data delivered
one more time in top-down, left-right order. The request is
handed to the ImageFilter for further processing, since the
ability to preserve the pixel ordering depends on the filter.

This method is public as a side effect
of this class implementing
the

ImageProducer

interface.
It should not be called from user code,
and its behavior if called from user code is unspecified.

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

### Additional Sections

#### Class FilteredImageSource

java.lang.Object

- java.awt.image.FilteredImageSource

java.awt.image.FilteredImageSource

**All Implemented Interfaces:** ImageProducer

```java
public class
FilteredImageSource

extends
Object

implements
ImageProducer
```

This class is an implementation of the ImageProducer interface which
takes an existing image and a filter object and uses them to produce
image data for a new filtered version of the original image. Furthermore,

FilteredImageSource

is safe for use by multiple threads.
Here is an example which filters an image by swapping the red and
blue components:

```java
Image src = getImage("doc:///demo/images/duke/T1.gif");
ImageFilter colorfilter = new RedBlueSwapFilter();
Image img = createImage(new FilteredImageSource(src.getSource(),
colorfilter));
```

**See Also:** ImageProducer

public class

FilteredImageSource

extends

Object

implements

ImageProducer

This class is an implementation of the ImageProducer interface which
takes an existing image and a filter object and uses them to produce
image data for a new filtered version of the original image. Furthermore,

FilteredImageSource

is safe for use by multiple threads.
Here is an example which filters an image by swapping the red and
blue components:

```java
Image src = getImage("doc:///demo/images/duke/T1.gif");
ImageFilter colorfilter = new RedBlueSwapFilter();
Image img = createImage(new FilteredImageSource(src.getSource(),
colorfilter));
```

Image src = getImage("doc:///demo/images/duke/T1.gif");
ImageFilter colorfilter = new RedBlueSwapFilter();
Image img = createImage(new FilteredImageSource(src.getSource(),
colorfilter));

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

FilteredImageSource

​(

ImageProducer

orig,

ImageFilter

imgf)

Constructs an ImageProducer object from an existing ImageProducer
and a filter object.

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

Adds the specified

ImageConsumer

to the list of consumers interested in data for the filtered image.

boolean

isConsumer

​(

ImageConsumer

ic)

Determines whether an ImageConsumer is on the list of consumers
currently interested in data for this image.

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

startProduction

​(

ImageConsumer

ic)

Starts production of the filtered image.

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

FilteredImageSource

​(

ImageProducer

orig,

ImageFilter

imgf)

Constructs an ImageProducer object from an existing ImageProducer
and a filter object.

---

#### Constructor Summary

Constructs an ImageProducer object from an existing ImageProducer
and a filter object.

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

Adds the specified

ImageConsumer

to the list of consumers interested in data for the filtered image.

boolean

isConsumer

​(

ImageConsumer

ic)

Determines whether an ImageConsumer is on the list of consumers
currently interested in data for this image.

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

startProduction

​(

ImageConsumer

ic)

Starts production of the filtered image.

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

Adds the specified

ImageConsumer

to the list of consumers interested in data for the filtered image.

Determines whether an ImageConsumer is on the list of consumers
currently interested in data for this image.

Removes an ImageConsumer from the list of consumers interested in
data for this image.

Requests that a given ImageConsumer have the image data delivered
one more time in top-down, left-right order.

Starts production of the filtered image.

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

- FilteredImageSource

```java
public FilteredImageSource​(
ImageProducer
orig,

ImageFilter
imgf)
```

Constructs an ImageProducer object from an existing ImageProducer
and a filter object.

**Parameters:** orig

- the specified

ImageProducer
**Parameters:** imgf

- the specified

ImageFilter
**See Also:** ImageFilter

,

Component.createImage(java.awt.image.ImageProducer)

============ METHOD DETAIL ==========

- Method Detail

- addConsumer

```java
public void addConsumer​(
ImageConsumer
ic)
```

Adds the specified

ImageConsumer

to the list of consumers interested in data for the filtered image.
An instance of the original

ImageFilter

is created
(using the filter's

getFilterInstance

method)
to manipulate the image data
for the specified

ImageConsumer

.
The newly created filter instance
is then passed to the

addConsumer

method
of the original

ImageProducer

.

This method is public as a side effect
of this class implementing
the

ImageProducer

interface.
It should not be called from user code,
and its behavior if called from user code is unspecified.

**Specified by:** addConsumer

in interface

ImageProducer
**Parameters:** ic

- the consumer for the filtered image
**See Also:** ImageConsumer

- isConsumer

```java
public boolean isConsumer​(
ImageConsumer
ic)
```

Determines whether an ImageConsumer is on the list of consumers
currently interested in data for this image.

This method is public as a side effect
of this class implementing
the

ImageProducer

interface.
It should not be called from user code,
and its behavior if called from user code is unspecified.

**Specified by:** isConsumer

in interface

ImageProducer
**Parameters:** ic

- the specified

ImageConsumer
**Returns:** true if the ImageConsumer is on the list; false otherwise
**See Also:** ImageConsumer

- removeConsumer

```java
public void removeConsumer​(
ImageConsumer
ic)
```

Removes an ImageConsumer from the list of consumers interested in
data for this image.

This method is public as a side effect
of this class implementing
the

ImageProducer

interface.
It should not be called from user code,
and its behavior if called from user code is unspecified.

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

Starts production of the filtered image.
If the specified

ImageConsumer

isn't already a consumer of the filtered image,
an instance of the original

ImageFilter

is created
(using the filter's

getFilterInstance

method)
to manipulate the image data
for the

ImageConsumer

.
The filter instance for the

ImageConsumer

is then passed to the

startProduction

method
of the original

ImageProducer

.

This method is public as a side effect
of this class implementing
the

ImageProducer

interface.
It should not be called from user code,
and its behavior if called from user code is unspecified.

**Specified by:** startProduction

in interface

ImageProducer
**Parameters:** ic

- the consumer for the filtered image
**See Also:** ImageConsumer

- requestTopDownLeftRightResend

```java
public void requestTopDownLeftRightResend​(
ImageConsumer
ic)
```

Requests that a given ImageConsumer have the image data delivered
one more time in top-down, left-right order. The request is
handed to the ImageFilter for further processing, since the
ability to preserve the pixel ordering depends on the filter.

This method is public as a side effect
of this class implementing
the

ImageProducer

interface.
It should not be called from user code,
and its behavior if called from user code is unspecified.

**Specified by:** requestTopDownLeftRightResend

in interface

ImageProducer
**Parameters:** ic

- the specified

ImageConsumer
**See Also:** ImageConsumer

Constructor Detail

- FilteredImageSource

```java
public FilteredImageSource​(
ImageProducer
orig,

ImageFilter
imgf)
```

Constructs an ImageProducer object from an existing ImageProducer
and a filter object.

**Parameters:** orig

- the specified

ImageProducer
**Parameters:** imgf

- the specified

ImageFilter
**See Also:** ImageFilter

,

Component.createImage(java.awt.image.ImageProducer)

---

#### Constructor Detail

FilteredImageSource

```java
public FilteredImageSource​(
ImageProducer
orig,

ImageFilter
imgf)
```

Constructs an ImageProducer object from an existing ImageProducer
and a filter object.

**Parameters:** orig

- the specified

ImageProducer
**Parameters:** imgf

- the specified

ImageFilter
**See Also:** ImageFilter

,

Component.createImage(java.awt.image.ImageProducer)

---

#### FilteredImageSource

public FilteredImageSource​(

ImageProducer

orig,

ImageFilter

imgf)

Constructs an ImageProducer object from an existing ImageProducer
and a filter object.

Method Detail

- addConsumer

```java
public void addConsumer​(
ImageConsumer
ic)
```

Adds the specified

ImageConsumer

to the list of consumers interested in data for the filtered image.
An instance of the original

ImageFilter

is created
(using the filter's

getFilterInstance

method)
to manipulate the image data
for the specified

ImageConsumer

.
The newly created filter instance
is then passed to the

addConsumer

method
of the original

ImageProducer

.

This method is public as a side effect
of this class implementing
the

ImageProducer

interface.
It should not be called from user code,
and its behavior if called from user code is unspecified.

**Specified by:** addConsumer

in interface

ImageProducer
**Parameters:** ic

- the consumer for the filtered image
**See Also:** ImageConsumer

- isConsumer

```java
public boolean isConsumer​(
ImageConsumer
ic)
```

Determines whether an ImageConsumer is on the list of consumers
currently interested in data for this image.

This method is public as a side effect
of this class implementing
the

ImageProducer

interface.
It should not be called from user code,
and its behavior if called from user code is unspecified.

**Specified by:** isConsumer

in interface

ImageProducer
**Parameters:** ic

- the specified

ImageConsumer
**Returns:** true if the ImageConsumer is on the list; false otherwise
**See Also:** ImageConsumer

- removeConsumer

```java
public void removeConsumer​(
ImageConsumer
ic)
```

Removes an ImageConsumer from the list of consumers interested in
data for this image.

This method is public as a side effect
of this class implementing
the

ImageProducer

interface.
It should not be called from user code,
and its behavior if called from user code is unspecified.

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

Starts production of the filtered image.
If the specified

ImageConsumer

isn't already a consumer of the filtered image,
an instance of the original

ImageFilter

is created
(using the filter's

getFilterInstance

method)
to manipulate the image data
for the

ImageConsumer

.
The filter instance for the

ImageConsumer

is then passed to the

startProduction

method
of the original

ImageProducer

.

This method is public as a side effect
of this class implementing
the

ImageProducer

interface.
It should not be called from user code,
and its behavior if called from user code is unspecified.

**Specified by:** startProduction

in interface

ImageProducer
**Parameters:** ic

- the consumer for the filtered image
**See Also:** ImageConsumer

- requestTopDownLeftRightResend

```java
public void requestTopDownLeftRightResend​(
ImageConsumer
ic)
```

Requests that a given ImageConsumer have the image data delivered
one more time in top-down, left-right order. The request is
handed to the ImageFilter for further processing, since the
ability to preserve the pixel ordering depends on the filter.

This method is public as a side effect
of this class implementing
the

ImageProducer

interface.
It should not be called from user code,
and its behavior if called from user code is unspecified.

**Specified by:** requestTopDownLeftRightResend

in interface

ImageProducer
**Parameters:** ic

- the specified

ImageConsumer
**See Also:** ImageConsumer

---

#### Method Detail

addConsumer

```java
public void addConsumer​(
ImageConsumer
ic)
```

Adds the specified

ImageConsumer

to the list of consumers interested in data for the filtered image.
An instance of the original

ImageFilter

is created
(using the filter's

getFilterInstance

method)
to manipulate the image data
for the specified

ImageConsumer

.
The newly created filter instance
is then passed to the

addConsumer

method
of the original

ImageProducer

.

This method is public as a side effect
of this class implementing
the

ImageProducer

interface.
It should not be called from user code,
and its behavior if called from user code is unspecified.

**Specified by:** addConsumer

in interface

ImageProducer
**Parameters:** ic

- the consumer for the filtered image
**See Also:** ImageConsumer

---

#### addConsumer

public void addConsumer​(

ImageConsumer

ic)

Adds the specified

ImageConsumer

to the list of consumers interested in data for the filtered image.
An instance of the original

ImageFilter

is created
(using the filter's

getFilterInstance

method)
to manipulate the image data
for the specified

ImageConsumer

.
The newly created filter instance
is then passed to the

addConsumer

method
of the original

ImageProducer

.

This method is public as a side effect
of this class implementing
the

ImageProducer

interface.
It should not be called from user code,
and its behavior if called from user code is unspecified.

This method is public as a side effect
of this class implementing
the

ImageProducer

interface.
It should not be called from user code,
and its behavior if called from user code is unspecified.

isConsumer

```java
public boolean isConsumer​(
ImageConsumer
ic)
```

Determines whether an ImageConsumer is on the list of consumers
currently interested in data for this image.

This method is public as a side effect
of this class implementing
the

ImageProducer

interface.
It should not be called from user code,
and its behavior if called from user code is unspecified.

**Specified by:** isConsumer

in interface

ImageProducer
**Parameters:** ic

- the specified

ImageConsumer
**Returns:** true if the ImageConsumer is on the list; false otherwise
**See Also:** ImageConsumer

---

#### isConsumer

public boolean isConsumer​(

ImageConsumer

ic)

Determines whether an ImageConsumer is on the list of consumers
currently interested in data for this image.

This method is public as a side effect
of this class implementing
the

ImageProducer

interface.
It should not be called from user code,
and its behavior if called from user code is unspecified.

This method is public as a side effect
of this class implementing
the

ImageProducer

interface.
It should not be called from user code,
and its behavior if called from user code is unspecified.

removeConsumer

```java
public void removeConsumer​(
ImageConsumer
ic)
```

Removes an ImageConsumer from the list of consumers interested in
data for this image.

This method is public as a side effect
of this class implementing
the

ImageProducer

interface.
It should not be called from user code,
and its behavior if called from user code is unspecified.

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

This method is public as a side effect
of this class implementing
the

ImageProducer

interface.
It should not be called from user code,
and its behavior if called from user code is unspecified.

This method is public as a side effect
of this class implementing
the

ImageProducer

interface.
It should not be called from user code,
and its behavior if called from user code is unspecified.

startProduction

```java
public void startProduction​(
ImageConsumer
ic)
```

Starts production of the filtered image.
If the specified

ImageConsumer

isn't already a consumer of the filtered image,
an instance of the original

ImageFilter

is created
(using the filter's

getFilterInstance

method)
to manipulate the image data
for the

ImageConsumer

.
The filter instance for the

ImageConsumer

is then passed to the

startProduction

method
of the original

ImageProducer

.

This method is public as a side effect
of this class implementing
the

ImageProducer

interface.
It should not be called from user code,
and its behavior if called from user code is unspecified.

**Specified by:** startProduction

in interface

ImageProducer
**Parameters:** ic

- the consumer for the filtered image
**See Also:** ImageConsumer

---

#### startProduction

public void startProduction​(

ImageConsumer

ic)

Starts production of the filtered image.
If the specified

ImageConsumer

isn't already a consumer of the filtered image,
an instance of the original

ImageFilter

is created
(using the filter's

getFilterInstance

method)
to manipulate the image data
for the

ImageConsumer

.
The filter instance for the

ImageConsumer

is then passed to the

startProduction

method
of the original

ImageProducer

.

This method is public as a side effect
of this class implementing
the

ImageProducer

interface.
It should not be called from user code,
and its behavior if called from user code is unspecified.

This method is public as a side effect
of this class implementing
the

ImageProducer

interface.
It should not be called from user code,
and its behavior if called from user code is unspecified.

requestTopDownLeftRightResend

```java
public void requestTopDownLeftRightResend​(
ImageConsumer
ic)
```

Requests that a given ImageConsumer have the image data delivered
one more time in top-down, left-right order. The request is
handed to the ImageFilter for further processing, since the
ability to preserve the pixel ordering depends on the filter.

This method is public as a side effect
of this class implementing
the

ImageProducer

interface.
It should not be called from user code,
and its behavior if called from user code is unspecified.

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
one more time in top-down, left-right order. The request is
handed to the ImageFilter for further processing, since the
ability to preserve the pixel ordering depends on the filter.

This method is public as a side effect
of this class implementing
the

ImageProducer

interface.
It should not be called from user code,
and its behavior if called from user code is unspecified.

This method is public as a side effect
of this class implementing
the

ImageProducer

interface.
It should not be called from user code,
and its behavior if called from user code is unspecified.

---

