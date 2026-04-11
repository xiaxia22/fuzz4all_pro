# Class IIOImage

**Source:** `java.desktop\javax\imageio\IIOImage.html`

### Class Description

```java
public class
IIOImage

extends
Object
```

A simple container class to aggregate an image, a set of
thumbnail (preview) images, and an object representing metadata
associated with the image.

The image data may take the form of either a

RenderedImage

, or a

Raster

. Reader
methods that return an

IIOImage

will always return a

BufferedImage

using the

RenderedImage

reference. Writer methods that accept an

IIOImage

will always accept a

RenderedImage

, and may optionally
accept a

Raster

.

Exactly one of

getRenderedImage

and

getRaster

will return a non-

null

value.
Subclasses are responsible for ensuring this behavior.

**See Also:** ImageReader.readAll(int, ImageReadParam)

,

ImageReader.readAll(java.util.Iterator)

,

ImageWriter.write(javax.imageio.metadata.IIOMetadata,
IIOImage, ImageWriteParam)

,

ImageWriter.write(IIOImage)

,

ImageWriter.writeToSequence(IIOImage, ImageWriteParam)

,

ImageWriter.writeInsert(int, IIOImage, ImageWriteParam)

---

### Field Details

#### protected
RenderedImage
image

The

RenderedImage

being referenced.

---

#### protected
Raster
raster

The

Raster

being referenced.

---

#### protected
List
<? extends
BufferedImage
> thumbnails

A

List

of

BufferedImage

thumbnails,
or

null

. Non-

BufferedImage

objects
must not be stored in this

List

.

---

#### protected
IIOMetadata
metadata

An

IIOMetadata

object containing metadata
associated with the image.

---

### Constructor Details

#### public IIOImage​(
RenderedImage
image,

List
<? extends
BufferedImage
> thumbnails,

IIOMetadata
metadata)

Constructs an

IIOImage

containing a

RenderedImage

, and thumbnails and metadata
associated with it.

All parameters are stored by reference.

The

thumbnails

argument must either be

null

or contain only

BufferedImage

objects.

**Parameters:**
- image

- a

RenderedImage

.
- thumbnails

- a

List

of

BufferedImage

s,
or

null

.
- metadata

- an

IIOMetadata

object, or

null

.

**Throws:**
- IllegalArgumentException

- if

image

is

null

.

---

#### public IIOImage​(
Raster
raster,

List
<? extends
BufferedImage
> thumbnails,

IIOMetadata
metadata)

Constructs an

IIOImage

containing a

Raster

, and thumbnails and metadata
associated with it.

All parameters are stored by reference.

**Parameters:**
- raster

- a

Raster

.
- thumbnails

- a

List

of

BufferedImage

s,
or

null

.
- metadata

- an

IIOMetadata

object, or

null

.

**Throws:**
- IllegalArgumentException

- if

raster

is

null

.

---

### Method Details

#### public
RenderedImage
getRenderedImage()

Returns the currently set

RenderedImage

, or

null

if only a

Raster

is available.

**Returns:**
- a

RenderedImage

, or

null

.

**See Also:**
- setRenderedImage(java.awt.image.RenderedImage)

---

#### public void setRenderedImage​(
RenderedImage
image)

Sets the current

RenderedImage

. The value is
stored by reference. Any existing

Raster

is
discarded.

**Parameters:**
- image

- a

RenderedImage

.

**Throws:**
- IllegalArgumentException

- if

image

is

null

.

**See Also:**
- getRenderedImage()

---

#### public boolean hasRaster()

Returns

true

if this

IIOImage

stores
a

Raster

rather than a

RenderedImage

.

**Returns:**
- true

if a

Raster

is
available.

---

#### public
Raster
getRaster()

Returns the currently set

Raster

, or

null

if only a

RenderedImage

is
available.

**Returns:**
- a

Raster

, or

null

.

**See Also:**
- setRaster(java.awt.image.Raster)

---

#### public void setRaster​(
Raster
raster)

Sets the current

Raster

. The value is
stored by reference. Any existing

RenderedImage

is
discarded.

**Parameters:**
- raster

- a

Raster

.

**Throws:**
- IllegalArgumentException

- if

raster

is

null

.

**See Also:**
- getRaster()

---

#### public int getNumThumbnails()

Returns the number of thumbnails stored in this

IIOImage

.

**Returns:**
- the number of thumbnails, as an

int

.

---

#### public
BufferedImage
getThumbnail​(int index)

Returns a thumbnail associated with the main image.

**Parameters:**
- index

- the index of the desired thumbnail image.

**Returns:**
- a thumbnail image, as a

BufferedImage

.

**Throws:**
- IndexOutOfBoundsException

- if the supplied index is
negative or larger than the largest valid index.
- ClassCastException

- if a
non-

BufferedImage

object is encountered in the
list of thumbnails at the given index.

**See Also:**
- getThumbnails()

,

setThumbnails(java.util.List<? extends java.awt.image.BufferedImage>)

---

#### public
List
<? extends
BufferedImage
> getThumbnails()

Returns the current

List

of thumbnail

BufferedImage

s, or

null

if none is
set. A live reference is returned.

**Returns:**
- the current

List

of

BufferedImage

thumbnails, or

null

.

**See Also:**
- getThumbnail(int)

,

setThumbnails(java.util.List<? extends java.awt.image.BufferedImage>)

---

#### public void setThumbnails​(
List
<? extends
BufferedImage
> thumbnails)

Sets the list of thumbnails to a new

List

of

BufferedImage

s, or to

null

. The
reference to the previous

List

is discarded.

The

thumbnails

argument must either be

null

or contain only

BufferedImage

objects.

**Parameters:**
- thumbnails

- a

List

of

BufferedImage

thumbnails, or

null

.

**See Also:**
- getThumbnail(int)

,

getThumbnails()

---

#### public
IIOMetadata
getMetadata()

Returns a reference to the current

IIOMetadata

object, or

null

is none is set.

**Returns:**
- an

IIOMetadata

object, or

null

.

**See Also:**
- setMetadata(javax.imageio.metadata.IIOMetadata)

---

#### public void setMetadata​(
IIOMetadata
metadata)

Sets the

IIOMetadata

to a new object, or

null

.

**Parameters:**
- metadata

- an

IIOMetadata

object, or

null

.

**See Also:**
- getMetadata()

---

### Additional Sections

#### Class IIOImage

java.lang.Object

- javax.imageio.IIOImage

javax.imageio.IIOImage

```java
public class
IIOImage

extends
Object
```

A simple container class to aggregate an image, a set of
thumbnail (preview) images, and an object representing metadata
associated with the image.

The image data may take the form of either a

RenderedImage

, or a

Raster

. Reader
methods that return an

IIOImage

will always return a

BufferedImage

using the

RenderedImage

reference. Writer methods that accept an

IIOImage

will always accept a

RenderedImage

, and may optionally
accept a

Raster

.

Exactly one of

getRenderedImage

and

getRaster

will return a non-

null

value.
Subclasses are responsible for ensuring this behavior.

**See Also:** ImageReader.readAll(int, ImageReadParam)

,

ImageReader.readAll(java.util.Iterator)

,

ImageWriter.write(javax.imageio.metadata.IIOMetadata,
IIOImage, ImageWriteParam)

,

ImageWriter.write(IIOImage)

,

ImageWriter.writeToSequence(IIOImage, ImageWriteParam)

,

ImageWriter.writeInsert(int, IIOImage, ImageWriteParam)

public class

IIOImage

extends

Object

A simple container class to aggregate an image, a set of
thumbnail (preview) images, and an object representing metadata
associated with the image.

The image data may take the form of either a

RenderedImage

, or a

Raster

. Reader
methods that return an

IIOImage

will always return a

BufferedImage

using the

RenderedImage

reference. Writer methods that accept an

IIOImage

will always accept a

RenderedImage

, and may optionally
accept a

Raster

.

Exactly one of

getRenderedImage

and

getRaster

will return a non-

null

value.
Subclasses are responsible for ensuring this behavior.

The image data may take the form of either a

RenderedImage

, or a

Raster

. Reader
methods that return an

IIOImage

will always return a

BufferedImage

using the

RenderedImage

reference. Writer methods that accept an

IIOImage

will always accept a

RenderedImage

, and may optionally
accept a

Raster

.

Exactly one of

getRenderedImage

and

getRaster

will return a non-

null

value.
Subclasses are responsible for ensuring this behavior.

Exactly one of

getRenderedImage

and

getRaster

will return a non-

null

value.
Subclasses are responsible for ensuring this behavior.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

RenderedImage

image

The

RenderedImage

being referenced.

protected

IIOMetadata

metadata

An

IIOMetadata

object containing metadata
associated with the image.

protected

Raster

raster

The

Raster

being referenced.

protected

List

<? extends

BufferedImage

>

thumbnails

A

List

of

BufferedImage

thumbnails,
or

null

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

IIOImage

​(

Raster

raster,

List

<? extends

BufferedImage

> thumbnails,

IIOMetadata

metadata)

Constructs an

IIOImage

containing a

Raster

, and thumbnails and metadata
associated with it.

IIOImage

​(

RenderedImage

image,

List

<? extends

BufferedImage

> thumbnails,

IIOMetadata

metadata)

Constructs an

IIOImage

containing a

RenderedImage

, and thumbnails and metadata
associated with it.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

IIOMetadata

getMetadata

()

Returns a reference to the current

IIOMetadata

object, or

null

is none is set.

int

getNumThumbnails

()

Returns the number of thumbnails stored in this

IIOImage

.

Raster

getRaster

()

Returns the currently set

Raster

, or

null

if only a

RenderedImage

is
available.

RenderedImage

getRenderedImage

()

Returns the currently set

RenderedImage

, or

null

if only a

Raster

is available.

BufferedImage

getThumbnail

​(int index)

Returns a thumbnail associated with the main image.

List

<? extends

BufferedImage

>

getThumbnails

()

Returns the current

List

of thumbnail

BufferedImage

s, or

null

if none is
set.

boolean

hasRaster

()

Returns

true

if this

IIOImage

stores
a

Raster

rather than a

RenderedImage

.

void

setMetadata

​(

IIOMetadata

metadata)

Sets the

IIOMetadata

to a new object, or

null

.

void

setRaster

​(

Raster

raster)

Sets the current

Raster

.

void

setRenderedImage

​(

RenderedImage

image)

Sets the current

RenderedImage

.

void

setThumbnails

​(

List

<? extends

BufferedImage

> thumbnails)

Sets the list of thumbnails to a new

List

of

BufferedImage

s, or to

null

.

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

protected

RenderedImage

image

The

RenderedImage

being referenced.

protected

IIOMetadata

metadata

An

IIOMetadata

object containing metadata
associated with the image.

protected

Raster

raster

The

Raster

being referenced.

protected

List

<? extends

BufferedImage

>

thumbnails

A

List

of

BufferedImage

thumbnails,
or

null

.

---

#### Field Summary

The

RenderedImage

being referenced.

An

IIOMetadata

object containing metadata
associated with the image.

The

Raster

being referenced.

A

List

of

BufferedImage

thumbnails,
or

null

.

Constructor Summary

Constructors

Constructor

Description

IIOImage

​(

Raster

raster,

List

<? extends

BufferedImage

> thumbnails,

IIOMetadata

metadata)

Constructs an

IIOImage

containing a

Raster

, and thumbnails and metadata
associated with it.

IIOImage

​(

RenderedImage

image,

List

<? extends

BufferedImage

> thumbnails,

IIOMetadata

metadata)

Constructs an

IIOImage

containing a

RenderedImage

, and thumbnails and metadata
associated with it.

---

#### Constructor Summary

Constructs an

IIOImage

containing a

Raster

, and thumbnails and metadata
associated with it.

Constructs an

IIOImage

containing a

RenderedImage

, and thumbnails and metadata
associated with it.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

IIOMetadata

getMetadata

()

Returns a reference to the current

IIOMetadata

object, or

null

is none is set.

int

getNumThumbnails

()

Returns the number of thumbnails stored in this

IIOImage

.

Raster

getRaster

()

Returns the currently set

Raster

, or

null

if only a

RenderedImage

is
available.

RenderedImage

getRenderedImage

()

Returns the currently set

RenderedImage

, or

null

if only a

Raster

is available.

BufferedImage

getThumbnail

​(int index)

Returns a thumbnail associated with the main image.

List

<? extends

BufferedImage

>

getThumbnails

()

Returns the current

List

of thumbnail

BufferedImage

s, or

null

if none is
set.

boolean

hasRaster

()

Returns

true

if this

IIOImage

stores
a

Raster

rather than a

RenderedImage

.

void

setMetadata

​(

IIOMetadata

metadata)

Sets the

IIOMetadata

to a new object, or

null

.

void

setRaster

​(

Raster

raster)

Sets the current

Raster

.

void

setRenderedImage

​(

RenderedImage

image)

Sets the current

RenderedImage

.

void

setThumbnails

​(

List

<? extends

BufferedImage

> thumbnails)

Sets the list of thumbnails to a new

List

of

BufferedImage

s, or to

null

.

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

Returns a reference to the current

IIOMetadata

object, or

null

is none is set.

Returns the number of thumbnails stored in this

IIOImage

.

Returns the currently set

Raster

, or

null

if only a

RenderedImage

is
available.

Returns the currently set

RenderedImage

, or

null

if only a

Raster

is available.

Returns a thumbnail associated with the main image.

Returns the current

List

of thumbnail

BufferedImage

s, or

null

if none is
set.

Returns

true

if this

IIOImage

stores
a

Raster

rather than a

RenderedImage

.

Sets the

IIOMetadata

to a new object, or

null

.

Sets the current

Raster

.

Sets the current

RenderedImage

.

Sets the list of thumbnails to a new

List

of

BufferedImage

s, or to

null

.

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

- image

```java
protected
RenderedImage
image
```

The

RenderedImage

being referenced.

- raster

```java
protected
Raster
raster
```

The

Raster

being referenced.

- thumbnails

```java
protected
List
<? extends
BufferedImage
> thumbnails
```

A

List

of

BufferedImage

thumbnails,
or

null

. Non-

BufferedImage

objects
must not be stored in this

List

.

- metadata

```java
protected
IIOMetadata
metadata
```

An

IIOMetadata

object containing metadata
associated with the image.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- IIOImage

```java
public IIOImage​(
RenderedImage
image,

List
<? extends
BufferedImage
> thumbnails,

IIOMetadata
metadata)
```

Constructs an

IIOImage

containing a

RenderedImage

, and thumbnails and metadata
associated with it.

All parameters are stored by reference.

The

thumbnails

argument must either be

null

or contain only

BufferedImage

objects.

**Parameters:** image

- a

RenderedImage

.
**Parameters:** thumbnails

- a

List

of

BufferedImage

s,
or

null

.
**Parameters:** metadata

- an

IIOMetadata

object, or

null

.
**Throws:** IllegalArgumentException

- if

image

is

null

.

- IIOImage

```java
public IIOImage​(
Raster
raster,

List
<? extends
BufferedImage
> thumbnails,

IIOMetadata
metadata)
```

Constructs an

IIOImage

containing a

Raster

, and thumbnails and metadata
associated with it.

All parameters are stored by reference.

**Parameters:** raster

- a

Raster

.
**Parameters:** thumbnails

- a

List

of

BufferedImage

s,
or

null

.
**Parameters:** metadata

- an

IIOMetadata

object, or

null

.
**Throws:** IllegalArgumentException

- if

raster

is

null

.

============ METHOD DETAIL ==========

- Method Detail

- getRenderedImage

```java
public
RenderedImage
getRenderedImage()
```

Returns the currently set

RenderedImage

, or

null

if only a

Raster

is available.

**Returns:** a

RenderedImage

, or

null

.
**See Also:** setRenderedImage(java.awt.image.RenderedImage)

- setRenderedImage

```java
public void setRenderedImage​(
RenderedImage
image)
```

Sets the current

RenderedImage

. The value is
stored by reference. Any existing

Raster

is
discarded.

**Parameters:** image

- a

RenderedImage

.
**Throws:** IllegalArgumentException

- if

image

is

null

.
**See Also:** getRenderedImage()

- hasRaster

```java
public boolean hasRaster()
```

Returns

true

if this

IIOImage

stores
a

Raster

rather than a

RenderedImage

.

**Returns:** true

if a

Raster

is
available.

- getRaster

```java
public
Raster
getRaster()
```

Returns the currently set

Raster

, or

null

if only a

RenderedImage

is
available.

**Returns:** a

Raster

, or

null

.
**See Also:** setRaster(java.awt.image.Raster)

- setRaster

```java
public void setRaster​(
Raster
raster)
```

Sets the current

Raster

. The value is
stored by reference. Any existing

RenderedImage

is
discarded.

**Parameters:** raster

- a

Raster

.
**Throws:** IllegalArgumentException

- if

raster

is

null

.
**See Also:** getRaster()

- getNumThumbnails

```java
public int getNumThumbnails()
```

Returns the number of thumbnails stored in this

IIOImage

.

**Returns:** the number of thumbnails, as an

int

.

- getThumbnail

```java
public
BufferedImage
getThumbnail​(int index)
```

Returns a thumbnail associated with the main image.

**Parameters:** index

- the index of the desired thumbnail image.
**Returns:** a thumbnail image, as a

BufferedImage

.
**Throws:** IndexOutOfBoundsException

- if the supplied index is
negative or larger than the largest valid index.
**Throws:** ClassCastException

- if a
non-

BufferedImage

object is encountered in the
list of thumbnails at the given index.
**See Also:** getThumbnails()

,

setThumbnails(java.util.List<? extends java.awt.image.BufferedImage>)

- getThumbnails

```java
public
List
<? extends
BufferedImage
> getThumbnails()
```

Returns the current

List

of thumbnail

BufferedImage

s, or

null

if none is
set. A live reference is returned.

**Returns:** the current

List

of

BufferedImage

thumbnails, or

null

.
**See Also:** getThumbnail(int)

,

setThumbnails(java.util.List<? extends java.awt.image.BufferedImage>)

- setThumbnails

```java
public void setThumbnails​(
List
<? extends
BufferedImage
> thumbnails)
```

Sets the list of thumbnails to a new

List

of

BufferedImage

s, or to

null

. The
reference to the previous

List

is discarded.

The

thumbnails

argument must either be

null

or contain only

BufferedImage

objects.

**Parameters:** thumbnails

- a

List

of

BufferedImage

thumbnails, or

null

.
**See Also:** getThumbnail(int)

,

getThumbnails()

- getMetadata

```java
public
IIOMetadata
getMetadata()
```

Returns a reference to the current

IIOMetadata

object, or

null

is none is set.

**Returns:** an

IIOMetadata

object, or

null

.
**See Also:** setMetadata(javax.imageio.metadata.IIOMetadata)

- setMetadata

```java
public void setMetadata​(
IIOMetadata
metadata)
```

Sets the

IIOMetadata

to a new object, or

null

.

**Parameters:** metadata

- an

IIOMetadata

object, or

null

.
**See Also:** getMetadata()

Field Detail

- image

```java
protected
RenderedImage
image
```

The

RenderedImage

being referenced.

- raster

```java
protected
Raster
raster
```

The

Raster

being referenced.

- thumbnails

```java
protected
List
<? extends
BufferedImage
> thumbnails
```

A

List

of

BufferedImage

thumbnails,
or

null

. Non-

BufferedImage

objects
must not be stored in this

List

.

- metadata

```java
protected
IIOMetadata
metadata
```

An

IIOMetadata

object containing metadata
associated with the image.

---

#### Field Detail

image

```java
protected
RenderedImage
image
```

The

RenderedImage

being referenced.

---

#### image

protected

RenderedImage

image

The

RenderedImage

being referenced.

raster

```java
protected
Raster
raster
```

The

Raster

being referenced.

---

#### raster

protected

Raster

raster

The

Raster

being referenced.

thumbnails

```java
protected
List
<? extends
BufferedImage
> thumbnails
```

A

List

of

BufferedImage

thumbnails,
or

null

. Non-

BufferedImage

objects
must not be stored in this

List

.

---

#### thumbnails

protected

List

<? extends

BufferedImage

> thumbnails

A

List

of

BufferedImage

thumbnails,
or

null

. Non-

BufferedImage

objects
must not be stored in this

List

.

metadata

```java
protected
IIOMetadata
metadata
```

An

IIOMetadata

object containing metadata
associated with the image.

---

#### metadata

protected

IIOMetadata

metadata

An

IIOMetadata

object containing metadata
associated with the image.

Constructor Detail

- IIOImage

```java
public IIOImage​(
RenderedImage
image,

List
<? extends
BufferedImage
> thumbnails,

IIOMetadata
metadata)
```

Constructs an

IIOImage

containing a

RenderedImage

, and thumbnails and metadata
associated with it.

All parameters are stored by reference.

The

thumbnails

argument must either be

null

or contain only

BufferedImage

objects.

**Parameters:** image

- a

RenderedImage

.
**Parameters:** thumbnails

- a

List

of

BufferedImage

s,
or

null

.
**Parameters:** metadata

- an

IIOMetadata

object, or

null

.
**Throws:** IllegalArgumentException

- if

image

is

null

.

- IIOImage

```java
public IIOImage​(
Raster
raster,

List
<? extends
BufferedImage
> thumbnails,

IIOMetadata
metadata)
```

Constructs an

IIOImage

containing a

Raster

, and thumbnails and metadata
associated with it.

All parameters are stored by reference.

**Parameters:** raster

- a

Raster

.
**Parameters:** thumbnails

- a

List

of

BufferedImage

s,
or

null

.
**Parameters:** metadata

- an

IIOMetadata

object, or

null

.
**Throws:** IllegalArgumentException

- if

raster

is

null

.

---

#### Constructor Detail

IIOImage

```java
public IIOImage​(
RenderedImage
image,

List
<? extends
BufferedImage
> thumbnails,

IIOMetadata
metadata)
```

Constructs an

IIOImage

containing a

RenderedImage

, and thumbnails and metadata
associated with it.

All parameters are stored by reference.

The

thumbnails

argument must either be

null

or contain only

BufferedImage

objects.

**Parameters:** image

- a

RenderedImage

.
**Parameters:** thumbnails

- a

List

of

BufferedImage

s,
or

null

.
**Parameters:** metadata

- an

IIOMetadata

object, or

null

.
**Throws:** IllegalArgumentException

- if

image

is

null

.

---

#### IIOImage

public IIOImage​(

RenderedImage

image,

List

<? extends

BufferedImage

> thumbnails,

IIOMetadata

metadata)

Constructs an

IIOImage

containing a

RenderedImage

, and thumbnails and metadata
associated with it.

All parameters are stored by reference.

The

thumbnails

argument must either be

null

or contain only

BufferedImage

objects.

All parameters are stored by reference.

The

thumbnails

argument must either be

null

or contain only

BufferedImage

objects.

The

thumbnails

argument must either be

null

or contain only

BufferedImage

objects.

IIOImage

```java
public IIOImage​(
Raster
raster,

List
<? extends
BufferedImage
> thumbnails,

IIOMetadata
metadata)
```

Constructs an

IIOImage

containing a

Raster

, and thumbnails and metadata
associated with it.

All parameters are stored by reference.

**Parameters:** raster

- a

Raster

.
**Parameters:** thumbnails

- a

List

of

BufferedImage

s,
or

null

.
**Parameters:** metadata

- an

IIOMetadata

object, or

null

.
**Throws:** IllegalArgumentException

- if

raster

is

null

.

---

#### IIOImage

public IIOImage​(

Raster

raster,

List

<? extends

BufferedImage

> thumbnails,

IIOMetadata

metadata)

Constructs an

IIOImage

containing a

Raster

, and thumbnails and metadata
associated with it.

All parameters are stored by reference.

All parameters are stored by reference.

Method Detail

- getRenderedImage

```java
public
RenderedImage
getRenderedImage()
```

Returns the currently set

RenderedImage

, or

null

if only a

Raster

is available.

**Returns:** a

RenderedImage

, or

null

.
**See Also:** setRenderedImage(java.awt.image.RenderedImage)

- setRenderedImage

```java
public void setRenderedImage​(
RenderedImage
image)
```

Sets the current

RenderedImage

. The value is
stored by reference. Any existing

Raster

is
discarded.

**Parameters:** image

- a

RenderedImage

.
**Throws:** IllegalArgumentException

- if

image

is

null

.
**See Also:** getRenderedImage()

- hasRaster

```java
public boolean hasRaster()
```

Returns

true

if this

IIOImage

stores
a

Raster

rather than a

RenderedImage

.

**Returns:** true

if a

Raster

is
available.

- getRaster

```java
public
Raster
getRaster()
```

Returns the currently set

Raster

, or

null

if only a

RenderedImage

is
available.

**Returns:** a

Raster

, or

null

.
**See Also:** setRaster(java.awt.image.Raster)

- setRaster

```java
public void setRaster​(
Raster
raster)
```

Sets the current

Raster

. The value is
stored by reference. Any existing

RenderedImage

is
discarded.

**Parameters:** raster

- a

Raster

.
**Throws:** IllegalArgumentException

- if

raster

is

null

.
**See Also:** getRaster()

- getNumThumbnails

```java
public int getNumThumbnails()
```

Returns the number of thumbnails stored in this

IIOImage

.

**Returns:** the number of thumbnails, as an

int

.

- getThumbnail

```java
public
BufferedImage
getThumbnail​(int index)
```

Returns a thumbnail associated with the main image.

**Parameters:** index

- the index of the desired thumbnail image.
**Returns:** a thumbnail image, as a

BufferedImage

.
**Throws:** IndexOutOfBoundsException

- if the supplied index is
negative or larger than the largest valid index.
**Throws:** ClassCastException

- if a
non-

BufferedImage

object is encountered in the
list of thumbnails at the given index.
**See Also:** getThumbnails()

,

setThumbnails(java.util.List<? extends java.awt.image.BufferedImage>)

- getThumbnails

```java
public
List
<? extends
BufferedImage
> getThumbnails()
```

Returns the current

List

of thumbnail

BufferedImage

s, or

null

if none is
set. A live reference is returned.

**Returns:** the current

List

of

BufferedImage

thumbnails, or

null

.
**See Also:** getThumbnail(int)

,

setThumbnails(java.util.List<? extends java.awt.image.BufferedImage>)

- setThumbnails

```java
public void setThumbnails​(
List
<? extends
BufferedImage
> thumbnails)
```

Sets the list of thumbnails to a new

List

of

BufferedImage

s, or to

null

. The
reference to the previous

List

is discarded.

The

thumbnails

argument must either be

null

or contain only

BufferedImage

objects.

**Parameters:** thumbnails

- a

List

of

BufferedImage

thumbnails, or

null

.
**See Also:** getThumbnail(int)

,

getThumbnails()

- getMetadata

```java
public
IIOMetadata
getMetadata()
```

Returns a reference to the current

IIOMetadata

object, or

null

is none is set.

**Returns:** an

IIOMetadata

object, or

null

.
**See Also:** setMetadata(javax.imageio.metadata.IIOMetadata)

- setMetadata

```java
public void setMetadata​(
IIOMetadata
metadata)
```

Sets the

IIOMetadata

to a new object, or

null

.

**Parameters:** metadata

- an

IIOMetadata

object, or

null

.
**See Also:** getMetadata()

---

#### Method Detail

getRenderedImage

```java
public
RenderedImage
getRenderedImage()
```

Returns the currently set

RenderedImage

, or

null

if only a

Raster

is available.

**Returns:** a

RenderedImage

, or

null

.
**See Also:** setRenderedImage(java.awt.image.RenderedImage)

---

#### getRenderedImage

public

RenderedImage

getRenderedImage()

Returns the currently set

RenderedImage

, or

null

if only a

Raster

is available.

setRenderedImage

```java
public void setRenderedImage​(
RenderedImage
image)
```

Sets the current

RenderedImage

. The value is
stored by reference. Any existing

Raster

is
discarded.

**Parameters:** image

- a

RenderedImage

.
**Throws:** IllegalArgumentException

- if

image

is

null

.
**See Also:** getRenderedImage()

---

#### setRenderedImage

public void setRenderedImage​(

RenderedImage

image)

Sets the current

RenderedImage

. The value is
stored by reference. Any existing

Raster

is
discarded.

hasRaster

```java
public boolean hasRaster()
```

Returns

true

if this

IIOImage

stores
a

Raster

rather than a

RenderedImage

.

**Returns:** true

if a

Raster

is
available.

---

#### hasRaster

public boolean hasRaster()

Returns

true

if this

IIOImage

stores
a

Raster

rather than a

RenderedImage

.

getRaster

```java
public
Raster
getRaster()
```

Returns the currently set

Raster

, or

null

if only a

RenderedImage

is
available.

**Returns:** a

Raster

, or

null

.
**See Also:** setRaster(java.awt.image.Raster)

---

#### getRaster

public

Raster

getRaster()

Returns the currently set

Raster

, or

null

if only a

RenderedImage

is
available.

setRaster

```java
public void setRaster​(
Raster
raster)
```

Sets the current

Raster

. The value is
stored by reference. Any existing

RenderedImage

is
discarded.

**Parameters:** raster

- a

Raster

.
**Throws:** IllegalArgumentException

- if

raster

is

null

.
**See Also:** getRaster()

---

#### setRaster

public void setRaster​(

Raster

raster)

Sets the current

Raster

. The value is
stored by reference. Any existing

RenderedImage

is
discarded.

getNumThumbnails

```java
public int getNumThumbnails()
```

Returns the number of thumbnails stored in this

IIOImage

.

**Returns:** the number of thumbnails, as an

int

.

---

#### getNumThumbnails

public int getNumThumbnails()

Returns the number of thumbnails stored in this

IIOImage

.

getThumbnail

```java
public
BufferedImage
getThumbnail​(int index)
```

Returns a thumbnail associated with the main image.

**Parameters:** index

- the index of the desired thumbnail image.
**Returns:** a thumbnail image, as a

BufferedImage

.
**Throws:** IndexOutOfBoundsException

- if the supplied index is
negative or larger than the largest valid index.
**Throws:** ClassCastException

- if a
non-

BufferedImage

object is encountered in the
list of thumbnails at the given index.
**See Also:** getThumbnails()

,

setThumbnails(java.util.List<? extends java.awt.image.BufferedImage>)

---

#### getThumbnail

public

BufferedImage

getThumbnail​(int index)

Returns a thumbnail associated with the main image.

getThumbnails

```java
public
List
<? extends
BufferedImage
> getThumbnails()
```

Returns the current

List

of thumbnail

BufferedImage

s, or

null

if none is
set. A live reference is returned.

**Returns:** the current

List

of

BufferedImage

thumbnails, or

null

.
**See Also:** getThumbnail(int)

,

setThumbnails(java.util.List<? extends java.awt.image.BufferedImage>)

---

#### getThumbnails

public

List

<? extends

BufferedImage

> getThumbnails()

Returns the current

List

of thumbnail

BufferedImage

s, or

null

if none is
set. A live reference is returned.

setThumbnails

```java
public void setThumbnails​(
List
<? extends
BufferedImage
> thumbnails)
```

Sets the list of thumbnails to a new

List

of

BufferedImage

s, or to

null

. The
reference to the previous

List

is discarded.

The

thumbnails

argument must either be

null

or contain only

BufferedImage

objects.

**Parameters:** thumbnails

- a

List

of

BufferedImage

thumbnails, or

null

.
**See Also:** getThumbnail(int)

,

getThumbnails()

---

#### setThumbnails

public void setThumbnails​(

List

<? extends

BufferedImage

> thumbnails)

Sets the list of thumbnails to a new

List

of

BufferedImage

s, or to

null

. The
reference to the previous

List

is discarded.

The

thumbnails

argument must either be

null

or contain only

BufferedImage

objects.

The

thumbnails

argument must either be

null

or contain only

BufferedImage

objects.

getMetadata

```java
public
IIOMetadata
getMetadata()
```

Returns a reference to the current

IIOMetadata

object, or

null

is none is set.

**Returns:** an

IIOMetadata

object, or

null

.
**See Also:** setMetadata(javax.imageio.metadata.IIOMetadata)

---

#### getMetadata

public

IIOMetadata

getMetadata()

Returns a reference to the current

IIOMetadata

object, or

null

is none is set.

setMetadata

```java
public void setMetadata​(
IIOMetadata
metadata)
```

Sets the

IIOMetadata

to a new object, or

null

.

**Parameters:** metadata

- an

IIOMetadata

object, or

null

.
**See Also:** getMetadata()

---

#### setMetadata

public void setMetadata​(

IIOMetadata

metadata)

Sets the

IIOMetadata

to a new object, or

null

.

---

