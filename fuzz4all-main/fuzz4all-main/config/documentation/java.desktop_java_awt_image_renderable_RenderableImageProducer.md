# Class RenderableImageProducer

**Source:** `java.desktop\java\awt\image\renderable\RenderableImageProducer.html`

### Class Description

```java
public class
RenderableImageProducer

extends
Object

implements
ImageProducer
,
Runnable
```

An adapter class that implements ImageProducer to allow the
asynchronous production of a RenderableImage. The size of the
ImageConsumer is determined by the scale factor of the usr2dev
transform in the RenderContext. If the RenderContext is null, the
default rendering of the RenderableImage is used. This class
implements an asynchronous production that produces the image in
one thread at one resolution. This class may be subclassed to
implement versions that will render the image using several
threads. These threads could render either the same image at
progressively better quality, or different sections of the image at
a single resolution.

**All Implemented Interfaces:** ImageProducer

,

Runnable

---

### Field Details

*No entries found.*

### Constructor Details

#### public RenderableImageProducer​(
RenderableImage
rdblImage,

RenderContext
rc)

Constructs a new RenderableImageProducer from a RenderableImage
and a RenderContext.

**Parameters:**
- rdblImage

- the RenderableImage to be rendered.
- rc

- the RenderContext to use for producing the pixels.

---

### Method Details

#### public void setRenderContext​(
RenderContext
rc)

Sets a new RenderContext to use for the next startProduction() call.

**Parameters:**
- rc

- the new RenderContext.

---

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

- an ImageConsumer to be added to the interest list.

**See Also:**
- ImageProducer.startProduction(java.awt.image.ImageConsumer)

---

#### public boolean isConsumer​(
ImageConsumer
ic)

Determine if an ImageConsumer is on the list of consumers
currently interested in data for this image.

**Specified by:**
- isConsumer

in interface

ImageProducer

**Parameters:**
- ic

- the ImageConsumer to be checked.

**Returns:**
- true if the ImageConsumer is on the list; false otherwise.

---

#### public void removeConsumer​(
ImageConsumer
ic)

Remove an ImageConsumer from the list of consumers interested in
data for this image.

**Specified by:**
- removeConsumer

in interface

ImageProducer

**Parameters:**
- ic

- the ImageConsumer to be removed.

---

#### public void startProduction​(
ImageConsumer
ic)

Adds an ImageConsumer to the list of consumers interested in
data for this image, and immediately starts delivery of the
image data through the ImageConsumer interface.

**Specified by:**
- startProduction

in interface

ImageProducer

**Parameters:**
- ic

- the ImageConsumer to be added to the list of consumers.

**See Also:**
- ImageProducer.addConsumer(java.awt.image.ImageConsumer)

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

- the ImageConsumer requesting the resend.

**See Also:**
- ImageConsumer.setHints(int)

---

#### public void run()

The runnable method for this class. This will produce an image using
the current RenderableImage and RenderContext and send it to all the
ImageConsumer currently registered with this class.

**Specified by:**
- run

in interface

Runnable

**See Also:**
- Thread.run()

---

### Additional Sections

#### Class RenderableImageProducer

java.lang.Object

- java.awt.image.renderable.RenderableImageProducer

java.awt.image.renderable.RenderableImageProducer

**All Implemented Interfaces:** ImageProducer

,

Runnable

```java
public class
RenderableImageProducer

extends
Object

implements
ImageProducer
,
Runnable
```

An adapter class that implements ImageProducer to allow the
asynchronous production of a RenderableImage. The size of the
ImageConsumer is determined by the scale factor of the usr2dev
transform in the RenderContext. If the RenderContext is null, the
default rendering of the RenderableImage is used. This class
implements an asynchronous production that produces the image in
one thread at one resolution. This class may be subclassed to
implement versions that will render the image using several
threads. These threads could render either the same image at
progressively better quality, or different sections of the image at
a single resolution.

public class

RenderableImageProducer

extends

Object

implements

ImageProducer

,

Runnable

An adapter class that implements ImageProducer to allow the
asynchronous production of a RenderableImage. The size of the
ImageConsumer is determined by the scale factor of the usr2dev
transform in the RenderContext. If the RenderContext is null, the
default rendering of the RenderableImage is used. This class
implements an asynchronous production that produces the image in
one thread at one resolution. This class may be subclassed to
implement versions that will render the image using several
threads. These threads could render either the same image at
progressively better quality, or different sections of the image at
a single resolution.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

RenderableImageProducer

​(

RenderableImage

rdblImage,

RenderContext

rc)

Constructs a new RenderableImageProducer from a RenderableImage
and a RenderContext.

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

Determine if an ImageConsumer is on the list of consumers
currently interested in data for this image.

void

removeConsumer

​(

ImageConsumer

ic)

Remove an ImageConsumer from the list of consumers interested in
data for this image.

void

requestTopDownLeftRightResend

​(

ImageConsumer

ic)

Requests that a given ImageConsumer have the image data delivered
one more time in top-down, left-right order.

void

run

()

The runnable method for this class.

void

setRenderContext

​(

RenderContext

rc)

Sets a new RenderContext to use for the next startProduction() call.

void

startProduction

​(

ImageConsumer

ic)

Adds an ImageConsumer to the list of consumers interested in
data for this image, and immediately starts delivery of the
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

RenderableImageProducer

​(

RenderableImage

rdblImage,

RenderContext

rc)

Constructs a new RenderableImageProducer from a RenderableImage
and a RenderContext.

---

#### Constructor Summary

Constructs a new RenderableImageProducer from a RenderableImage
and a RenderContext.

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

Determine if an ImageConsumer is on the list of consumers
currently interested in data for this image.

void

removeConsumer

​(

ImageConsumer

ic)

Remove an ImageConsumer from the list of consumers interested in
data for this image.

void

requestTopDownLeftRightResend

​(

ImageConsumer

ic)

Requests that a given ImageConsumer have the image data delivered
one more time in top-down, left-right order.

void

run

()

The runnable method for this class.

void

setRenderContext

​(

RenderContext

rc)

Sets a new RenderContext to use for the next startProduction() call.

void

startProduction

​(

ImageConsumer

ic)

Adds an ImageConsumer to the list of consumers interested in
data for this image, and immediately starts delivery of the
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

Determine if an ImageConsumer is on the list of consumers
currently interested in data for this image.

Remove an ImageConsumer from the list of consumers interested in
data for this image.

Requests that a given ImageConsumer have the image data delivered
one more time in top-down, left-right order.

The runnable method for this class.

Sets a new RenderContext to use for the next startProduction() call.

Adds an ImageConsumer to the list of consumers interested in
data for this image, and immediately starts delivery of the
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

- RenderableImageProducer

```java
public RenderableImageProducer​(
RenderableImage
rdblImage,

RenderContext
rc)
```

Constructs a new RenderableImageProducer from a RenderableImage
and a RenderContext.

**Parameters:** rdblImage

- the RenderableImage to be rendered.
**Parameters:** rc

- the RenderContext to use for producing the pixels.

============ METHOD DETAIL ==========

- Method Detail

- setRenderContext

```java
public void setRenderContext​(
RenderContext
rc)
```

Sets a new RenderContext to use for the next startProduction() call.

**Parameters:** rc

- the new RenderContext.

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

- an ImageConsumer to be added to the interest list.
**See Also:** ImageProducer.startProduction(java.awt.image.ImageConsumer)

- isConsumer

```java
public boolean isConsumer​(
ImageConsumer
ic)
```

Determine if an ImageConsumer is on the list of consumers
currently interested in data for this image.

**Specified by:** isConsumer

in interface

ImageProducer
**Parameters:** ic

- the ImageConsumer to be checked.
**Returns:** true if the ImageConsumer is on the list; false otherwise.

- removeConsumer

```java
public void removeConsumer​(
ImageConsumer
ic)
```

Remove an ImageConsumer from the list of consumers interested in
data for this image.

**Specified by:** removeConsumer

in interface

ImageProducer
**Parameters:** ic

- the ImageConsumer to be removed.

- startProduction

```java
public void startProduction​(
ImageConsumer
ic)
```

Adds an ImageConsumer to the list of consumers interested in
data for this image, and immediately starts delivery of the
image data through the ImageConsumer interface.

**Specified by:** startProduction

in interface

ImageProducer
**Parameters:** ic

- the ImageConsumer to be added to the list of consumers.
**See Also:** ImageProducer.addConsumer(java.awt.image.ImageConsumer)

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

- the ImageConsumer requesting the resend.
**See Also:** ImageConsumer.setHints(int)

- run

```java
public void run()
```

The runnable method for this class. This will produce an image using
the current RenderableImage and RenderContext and send it to all the
ImageConsumer currently registered with this class.

**Specified by:** run

in interface

Runnable
**See Also:** Thread.run()

Constructor Detail

- RenderableImageProducer

```java
public RenderableImageProducer​(
RenderableImage
rdblImage,

RenderContext
rc)
```

Constructs a new RenderableImageProducer from a RenderableImage
and a RenderContext.

**Parameters:** rdblImage

- the RenderableImage to be rendered.
**Parameters:** rc

- the RenderContext to use for producing the pixels.

---

#### Constructor Detail

RenderableImageProducer

```java
public RenderableImageProducer​(
RenderableImage
rdblImage,

RenderContext
rc)
```

Constructs a new RenderableImageProducer from a RenderableImage
and a RenderContext.

**Parameters:** rdblImage

- the RenderableImage to be rendered.
**Parameters:** rc

- the RenderContext to use for producing the pixels.

---

#### RenderableImageProducer

public RenderableImageProducer​(

RenderableImage

rdblImage,

RenderContext

rc)

Constructs a new RenderableImageProducer from a RenderableImage
and a RenderContext.

Method Detail

- setRenderContext

```java
public void setRenderContext​(
RenderContext
rc)
```

Sets a new RenderContext to use for the next startProduction() call.

**Parameters:** rc

- the new RenderContext.

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

- an ImageConsumer to be added to the interest list.
**See Also:** ImageProducer.startProduction(java.awt.image.ImageConsumer)

- isConsumer

```java
public boolean isConsumer​(
ImageConsumer
ic)
```

Determine if an ImageConsumer is on the list of consumers
currently interested in data for this image.

**Specified by:** isConsumer

in interface

ImageProducer
**Parameters:** ic

- the ImageConsumer to be checked.
**Returns:** true if the ImageConsumer is on the list; false otherwise.

- removeConsumer

```java
public void removeConsumer​(
ImageConsumer
ic)
```

Remove an ImageConsumer from the list of consumers interested in
data for this image.

**Specified by:** removeConsumer

in interface

ImageProducer
**Parameters:** ic

- the ImageConsumer to be removed.

- startProduction

```java
public void startProduction​(
ImageConsumer
ic)
```

Adds an ImageConsumer to the list of consumers interested in
data for this image, and immediately starts delivery of the
image data through the ImageConsumer interface.

**Specified by:** startProduction

in interface

ImageProducer
**Parameters:** ic

- the ImageConsumer to be added to the list of consumers.
**See Also:** ImageProducer.addConsumer(java.awt.image.ImageConsumer)

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

- the ImageConsumer requesting the resend.
**See Also:** ImageConsumer.setHints(int)

- run

```java
public void run()
```

The runnable method for this class. This will produce an image using
the current RenderableImage and RenderContext and send it to all the
ImageConsumer currently registered with this class.

**Specified by:** run

in interface

Runnable
**See Also:** Thread.run()

---

#### Method Detail

setRenderContext

```java
public void setRenderContext​(
RenderContext
rc)
```

Sets a new RenderContext to use for the next startProduction() call.

**Parameters:** rc

- the new RenderContext.

---

#### setRenderContext

public void setRenderContext​(

RenderContext

rc)

Sets a new RenderContext to use for the next startProduction() call.

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

- an ImageConsumer to be added to the interest list.
**See Also:** ImageProducer.startProduction(java.awt.image.ImageConsumer)

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

Determine if an ImageConsumer is on the list of consumers
currently interested in data for this image.

**Specified by:** isConsumer

in interface

ImageProducer
**Parameters:** ic

- the ImageConsumer to be checked.
**Returns:** true if the ImageConsumer is on the list; false otherwise.

---

#### isConsumer

public boolean isConsumer​(

ImageConsumer

ic)

Determine if an ImageConsumer is on the list of consumers
currently interested in data for this image.

removeConsumer

```java
public void removeConsumer​(
ImageConsumer
ic)
```

Remove an ImageConsumer from the list of consumers interested in
data for this image.

**Specified by:** removeConsumer

in interface

ImageProducer
**Parameters:** ic

- the ImageConsumer to be removed.

---

#### removeConsumer

public void removeConsumer​(

ImageConsumer

ic)

Remove an ImageConsumer from the list of consumers interested in
data for this image.

startProduction

```java
public void startProduction​(
ImageConsumer
ic)
```

Adds an ImageConsumer to the list of consumers interested in
data for this image, and immediately starts delivery of the
image data through the ImageConsumer interface.

**Specified by:** startProduction

in interface

ImageProducer
**Parameters:** ic

- the ImageConsumer to be added to the list of consumers.
**See Also:** ImageProducer.addConsumer(java.awt.image.ImageConsumer)

---

#### startProduction

public void startProduction​(

ImageConsumer

ic)

Adds an ImageConsumer to the list of consumers interested in
data for this image, and immediately starts delivery of the
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

- the ImageConsumer requesting the resend.
**See Also:** ImageConsumer.setHints(int)

---

#### requestTopDownLeftRightResend

public void requestTopDownLeftRightResend​(

ImageConsumer

ic)

Requests that a given ImageConsumer have the image data delivered
one more time in top-down, left-right order.

run

```java
public void run()
```

The runnable method for this class. This will produce an image using
the current RenderableImage and RenderContext and send it to all the
ImageConsumer currently registered with this class.

**Specified by:** run

in interface

Runnable
**See Also:** Thread.run()

---

#### run

public void run()

The runnable method for this class. This will produce an image using
the current RenderableImage and RenderContext and send it to all the
ImageConsumer currently registered with this class.

---

