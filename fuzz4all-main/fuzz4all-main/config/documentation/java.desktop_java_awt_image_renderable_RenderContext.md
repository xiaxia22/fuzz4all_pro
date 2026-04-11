# Class RenderContext

**Source:** `java.desktop\java\awt\image\renderable\RenderContext.html`

### Class Description

```java
public class
RenderContext

extends
Object

implements
Cloneable
```

A RenderContext encapsulates the information needed to produce a
specific rendering from a RenderableImage. It contains the area to
be rendered specified in rendering-independent terms, the
resolution at which the rendering is to be performed, and hints
used to control the rendering process.

Users create RenderContexts and pass them to the
RenderableImage via the createRendering method. Most of the methods of
RenderContexts are not meant to be used directly by applications,
but by the RenderableImage and operator classes to which it is
passed.

The AffineTransform parameter passed into and out of this class
are cloned. The RenderingHints and Shape parameters are not
necessarily cloneable and are therefore only reference copied.
Altering RenderingHints or Shape instances that are in use by
instances of RenderContext may have undesired side effects.

**All Implemented Interfaces:** Cloneable

---

### Field Details

*No entries found.*

### Constructor Details

#### public RenderContext​(
AffineTransform
usr2dev,

Shape
aoi,

RenderingHints
hints)

Constructs a RenderContext with a given transform.
The area of interest is supplied as a Shape,
and the rendering hints are supplied as a RenderingHints object.

**Parameters:**
- usr2dev

- an AffineTransform.
- aoi

- a Shape representing the area of interest.
- hints

- a RenderingHints object containing rendering hints.

---

#### public RenderContext​(
AffineTransform
usr2dev)

Constructs a RenderContext with a given transform.
The area of interest is taken to be the entire renderable area.
No rendering hints are used.

**Parameters:**
- usr2dev

- an AffineTransform.

---

#### public RenderContext​(
AffineTransform
usr2dev,

RenderingHints
hints)

Constructs a RenderContext with a given transform and rendering hints.
The area of interest is taken to be the entire renderable area.

**Parameters:**
- usr2dev

- an AffineTransform.
- hints

- a RenderingHints object containing rendering hints.

---

#### public RenderContext​(
AffineTransform
usr2dev,

Shape
aoi)

Constructs a RenderContext with a given transform and area of interest.
The area of interest is supplied as a Shape.
No rendering hints are used.

**Parameters:**
- usr2dev

- an AffineTransform.
- aoi

- a Shape representing the area of interest.

---

### Method Details

#### public
RenderingHints
getRenderingHints()

Gets the rendering hints of this

RenderContext

.

**Returns:**
- a

RenderingHints

object that represents
the rendering hints of this

RenderContext

.

**See Also:**
- setRenderingHints(RenderingHints)

---

#### public void setRenderingHints​(
RenderingHints
hints)

Sets the rendering hints of this

RenderContext

.

**Parameters:**
- hints

- a

RenderingHints

object that represents
the rendering hints to assign to this

RenderContext

.

**See Also:**
- getRenderingHints()

---

#### public void setTransform​(
AffineTransform
newTransform)

Sets the current user-to-device AffineTransform contained
in the RenderContext to a given transform.

**Parameters:**
- newTransform

- the new AffineTransform.

**See Also:**
- getTransform()

---

#### public void preConcatenateTransform​(
AffineTransform
modTransform)

Modifies the current user-to-device transform by prepending another
transform. In matrix notation the operation is:

```java
[this] = [modTransform] x [this]
```

**Parameters:**
- modTransform

- the AffineTransform to prepend to the
current usr2dev transform.

**Since:**
- 1.3

---

#### @Deprecated

public void preConcetenateTransform​(
AffineTransform
modTransform)

Modifies the current user-to-device transform by prepending another
transform. In matrix notation the operation is:

```java
[this] = [modTransform] x [this]
```

This method does the same thing as the preConcatenateTransform
method. It is here for backward compatibility with previous releases
which misspelled the method name.

**Parameters:**
- modTransform

- the AffineTransform to prepend to the
current usr2dev transform.

---

#### public void concatenateTransform​(
AffineTransform
modTransform)

Modifies the current user-to-device transform by appending another
transform. In matrix notation the operation is:

```java
[this] = [this] x [modTransform]
```

**Parameters:**
- modTransform

- the AffineTransform to append to the
current usr2dev transform.

**Since:**
- 1.3

---

#### @Deprecated

public void concetenateTransform​(
AffineTransform
modTransform)

Modifies the current user-to-device transform by appending another
transform. In matrix notation the operation is:

```java
[this] = [this] x [modTransform]
```

This method does the same thing as the concatenateTransform
method. It is here for backward compatibility with previous releases
which misspelled the method name.

**Parameters:**
- modTransform

- the AffineTransform to append to the
current usr2dev transform.

---

#### public
AffineTransform
getTransform()

Gets the current user-to-device AffineTransform.

**Returns:**
- a reference to the current AffineTransform.

**See Also:**
- setTransform(AffineTransform)

---

#### public void setAreaOfInterest​(
Shape
newAoi)

Sets the current area of interest. The old area is discarded.

**Parameters:**
- newAoi

- The new area of interest.

**See Also:**
- getAreaOfInterest()

---

#### public
Shape
getAreaOfInterest()

Gets the ares of interest currently contained in the
RenderContext.

**Returns:**
- a reference to the area of interest of the RenderContext,
or null if none is specified.

**See Also:**
- setAreaOfInterest(Shape)

---

#### public
Object
clone()

Makes a copy of a RenderContext. The area of interest is copied
by reference. The usr2dev AffineTransform and hints are cloned,
while the area of interest is copied by reference.

**Overrides:**
- clone

in class

Object

**Returns:**
- the new cloned RenderContext.

**See Also:**
- Cloneable

---

### Additional Sections

#### Class RenderContext

java.lang.Object

- java.awt.image.renderable.RenderContext

java.awt.image.renderable.RenderContext

**All Implemented Interfaces:** Cloneable

```java
public class
RenderContext

extends
Object

implements
Cloneable
```

A RenderContext encapsulates the information needed to produce a
specific rendering from a RenderableImage. It contains the area to
be rendered specified in rendering-independent terms, the
resolution at which the rendering is to be performed, and hints
used to control the rendering process.

Users create RenderContexts and pass them to the
RenderableImage via the createRendering method. Most of the methods of
RenderContexts are not meant to be used directly by applications,
but by the RenderableImage and operator classes to which it is
passed.

The AffineTransform parameter passed into and out of this class
are cloned. The RenderingHints and Shape parameters are not
necessarily cloneable and are therefore only reference copied.
Altering RenderingHints or Shape instances that are in use by
instances of RenderContext may have undesired side effects.

public class

RenderContext

extends

Object

implements

Cloneable

A RenderContext encapsulates the information needed to produce a
specific rendering from a RenderableImage. It contains the area to
be rendered specified in rendering-independent terms, the
resolution at which the rendering is to be performed, and hints
used to control the rendering process.

Users create RenderContexts and pass them to the
RenderableImage via the createRendering method. Most of the methods of
RenderContexts are not meant to be used directly by applications,
but by the RenderableImage and operator classes to which it is
passed.

The AffineTransform parameter passed into and out of this class
are cloned. The RenderingHints and Shape parameters are not
necessarily cloneable and are therefore only reference copied.
Altering RenderingHints or Shape instances that are in use by
instances of RenderContext may have undesired side effects.

Users create RenderContexts and pass them to the
RenderableImage via the createRendering method. Most of the methods of
RenderContexts are not meant to be used directly by applications,
but by the RenderableImage and operator classes to which it is
passed.

The AffineTransform parameter passed into and out of this class
are cloned. The RenderingHints and Shape parameters are not
necessarily cloneable and are therefore only reference copied.
Altering RenderingHints or Shape instances that are in use by
instances of RenderContext may have undesired side effects.

The AffineTransform parameter passed into and out of this class
are cloned. The RenderingHints and Shape parameters are not
necessarily cloneable and are therefore only reference copied.
Altering RenderingHints or Shape instances that are in use by
instances of RenderContext may have undesired side effects.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

RenderContext

​(

AffineTransform

usr2dev)

Constructs a RenderContext with a given transform.

RenderContext

​(

AffineTransform

usr2dev,

RenderingHints

hints)

Constructs a RenderContext with a given transform and rendering hints.

RenderContext

​(

AffineTransform

usr2dev,

Shape

aoi)

Constructs a RenderContext with a given transform and area of interest.

RenderContext

​(

AffineTransform

usr2dev,

Shape

aoi,

RenderingHints

hints)

Constructs a RenderContext with a given transform.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

Object

clone

()

Makes a copy of a RenderContext.

void

concatenateTransform

​(

AffineTransform

modTransform)

Modifies the current user-to-device transform by appending another
transform.

void

concetenateTransform

​(

AffineTransform

modTransform)

Deprecated.

replaced by

concatenateTransform(AffineTransform)

.

Shape

getAreaOfInterest

()

Gets the ares of interest currently contained in the
RenderContext.

RenderingHints

getRenderingHints

()

Gets the rendering hints of this

RenderContext

.

AffineTransform

getTransform

()

Gets the current user-to-device AffineTransform.

void

preConcatenateTransform

​(

AffineTransform

modTransform)

Modifies the current user-to-device transform by prepending another
transform.

void

preConcetenateTransform

​(

AffineTransform

modTransform)

Deprecated.

replaced by

preConcatenateTransform(AffineTransform)

.

void

setAreaOfInterest

​(

Shape

newAoi)

Sets the current area of interest.

void

setRenderingHints

​(

RenderingHints

hints)

Sets the rendering hints of this

RenderContext

.

void

setTransform

​(

AffineTransform

newTransform)

Sets the current user-to-device AffineTransform contained
in the RenderContext to a given transform.

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

Constructor Summary

Constructors

Constructor

Description

RenderContext

​(

AffineTransform

usr2dev)

Constructs a RenderContext with a given transform.

RenderContext

​(

AffineTransform

usr2dev,

RenderingHints

hints)

Constructs a RenderContext with a given transform and rendering hints.

RenderContext

​(

AffineTransform

usr2dev,

Shape

aoi)

Constructs a RenderContext with a given transform and area of interest.

RenderContext

​(

AffineTransform

usr2dev,

Shape

aoi,

RenderingHints

hints)

Constructs a RenderContext with a given transform.

---

#### Constructor Summary

Constructs a RenderContext with a given transform.

Constructs a RenderContext with a given transform and rendering hints.

Constructs a RenderContext with a given transform and area of interest.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

Object

clone

()

Makes a copy of a RenderContext.

void

concatenateTransform

​(

AffineTransform

modTransform)

Modifies the current user-to-device transform by appending another
transform.

void

concetenateTransform

​(

AffineTransform

modTransform)

Deprecated.

replaced by

concatenateTransform(AffineTransform)

.

Shape

getAreaOfInterest

()

Gets the ares of interest currently contained in the
RenderContext.

RenderingHints

getRenderingHints

()

Gets the rendering hints of this

RenderContext

.

AffineTransform

getTransform

()

Gets the current user-to-device AffineTransform.

void

preConcatenateTransform

​(

AffineTransform

modTransform)

Modifies the current user-to-device transform by prepending another
transform.

void

preConcetenateTransform

​(

AffineTransform

modTransform)

Deprecated.

replaced by

preConcatenateTransform(AffineTransform)

.

void

setAreaOfInterest

​(

Shape

newAoi)

Sets the current area of interest.

void

setRenderingHints

​(

RenderingHints

hints)

Sets the rendering hints of this

RenderContext

.

void

setTransform

​(

AffineTransform

newTransform)

Sets the current user-to-device AffineTransform contained
in the RenderContext to a given transform.

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

Makes a copy of a RenderContext.

Modifies the current user-to-device transform by appending another
transform.

Deprecated.

replaced by

concatenateTransform(AffineTransform)

.

Gets the ares of interest currently contained in the
RenderContext.

Gets the rendering hints of this

RenderContext

.

Gets the current user-to-device AffineTransform.

Modifies the current user-to-device transform by prepending another
transform.

Deprecated.

replaced by

preConcatenateTransform(AffineTransform)

.

Sets the current area of interest.

Sets the rendering hints of this

RenderContext

.

Sets the current user-to-device AffineTransform contained
in the RenderContext to a given transform.

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

- RenderContext

```java
public RenderContext​(
AffineTransform
usr2dev,

Shape
aoi,

RenderingHints
hints)
```

Constructs a RenderContext with a given transform.
The area of interest is supplied as a Shape,
and the rendering hints are supplied as a RenderingHints object.

**Parameters:** usr2dev

- an AffineTransform.
**Parameters:** aoi

- a Shape representing the area of interest.
**Parameters:** hints

- a RenderingHints object containing rendering hints.

- RenderContext

```java
public RenderContext​(
AffineTransform
usr2dev)
```

Constructs a RenderContext with a given transform.
The area of interest is taken to be the entire renderable area.
No rendering hints are used.

**Parameters:** usr2dev

- an AffineTransform.

- RenderContext

```java
public RenderContext​(
AffineTransform
usr2dev,

RenderingHints
hints)
```

Constructs a RenderContext with a given transform and rendering hints.
The area of interest is taken to be the entire renderable area.

**Parameters:** usr2dev

- an AffineTransform.
**Parameters:** hints

- a RenderingHints object containing rendering hints.

- RenderContext

```java
public RenderContext​(
AffineTransform
usr2dev,

Shape
aoi)
```

Constructs a RenderContext with a given transform and area of interest.
The area of interest is supplied as a Shape.
No rendering hints are used.

**Parameters:** usr2dev

- an AffineTransform.
**Parameters:** aoi

- a Shape representing the area of interest.

============ METHOD DETAIL ==========

- Method Detail

- getRenderingHints

```java
public
RenderingHints
getRenderingHints()
```

Gets the rendering hints of this

RenderContext

.

**Returns:** a

RenderingHints

object that represents
the rendering hints of this

RenderContext

.
**See Also:** setRenderingHints(RenderingHints)

- setRenderingHints

```java
public void setRenderingHints​(
RenderingHints
hints)
```

Sets the rendering hints of this

RenderContext

.

**Parameters:** hints

- a

RenderingHints

object that represents
the rendering hints to assign to this

RenderContext

.
**See Also:** getRenderingHints()

- setTransform

```java
public void setTransform​(
AffineTransform
newTransform)
```

Sets the current user-to-device AffineTransform contained
in the RenderContext to a given transform.

**Parameters:** newTransform

- the new AffineTransform.
**See Also:** getTransform()

- preConcatenateTransform

```java
public void preConcatenateTransform​(
AffineTransform
modTransform)
```

Modifies the current user-to-device transform by prepending another
transform. In matrix notation the operation is:

```java
[this] = [modTransform] x [this]
```

**Parameters:** modTransform

- the AffineTransform to prepend to the
current usr2dev transform.
**Since:** 1.3

- preConcetenateTransform

```java
@Deprecated

public void preConcetenateTransform​(
AffineTransform
modTransform)
```

Deprecated.

replaced by

preConcatenateTransform(AffineTransform)

.

Modifies the current user-to-device transform by prepending another
transform. In matrix notation the operation is:

```java
[this] = [modTransform] x [this]
```

This method does the same thing as the preConcatenateTransform
method. It is here for backward compatibility with previous releases
which misspelled the method name.

**Parameters:** modTransform

- the AffineTransform to prepend to the
current usr2dev transform.

- concatenateTransform

```java
public void concatenateTransform​(
AffineTransform
modTransform)
```

Modifies the current user-to-device transform by appending another
transform. In matrix notation the operation is:

```java
[this] = [this] x [modTransform]
```

**Parameters:** modTransform

- the AffineTransform to append to the
current usr2dev transform.
**Since:** 1.3

- concetenateTransform

```java
@Deprecated

public void concetenateTransform​(
AffineTransform
modTransform)
```

Deprecated.

replaced by

concatenateTransform(AffineTransform)

.

Modifies the current user-to-device transform by appending another
transform. In matrix notation the operation is:

```java
[this] = [this] x [modTransform]
```

This method does the same thing as the concatenateTransform
method. It is here for backward compatibility with previous releases
which misspelled the method name.

**Parameters:** modTransform

- the AffineTransform to append to the
current usr2dev transform.

- getTransform

```java
public
AffineTransform
getTransform()
```

Gets the current user-to-device AffineTransform.

**Returns:** a reference to the current AffineTransform.
**See Also:** setTransform(AffineTransform)

- setAreaOfInterest

```java
public void setAreaOfInterest​(
Shape
newAoi)
```

Sets the current area of interest. The old area is discarded.

**Parameters:** newAoi

- The new area of interest.
**See Also:** getAreaOfInterest()

- getAreaOfInterest

```java
public
Shape
getAreaOfInterest()
```

Gets the ares of interest currently contained in the
RenderContext.

**Returns:** a reference to the area of interest of the RenderContext,
or null if none is specified.
**See Also:** setAreaOfInterest(Shape)

- clone

```java
public
Object
clone()
```

Makes a copy of a RenderContext. The area of interest is copied
by reference. The usr2dev AffineTransform and hints are cloned,
while the area of interest is copied by reference.

**Overrides:** clone

in class

Object
**Returns:** the new cloned RenderContext.
**See Also:** Cloneable

Constructor Detail

- RenderContext

```java
public RenderContext​(
AffineTransform
usr2dev,

Shape
aoi,

RenderingHints
hints)
```

Constructs a RenderContext with a given transform.
The area of interest is supplied as a Shape,
and the rendering hints are supplied as a RenderingHints object.

**Parameters:** usr2dev

- an AffineTransform.
**Parameters:** aoi

- a Shape representing the area of interest.
**Parameters:** hints

- a RenderingHints object containing rendering hints.

- RenderContext

```java
public RenderContext​(
AffineTransform
usr2dev)
```

Constructs a RenderContext with a given transform.
The area of interest is taken to be the entire renderable area.
No rendering hints are used.

**Parameters:** usr2dev

- an AffineTransform.

- RenderContext

```java
public RenderContext​(
AffineTransform
usr2dev,

RenderingHints
hints)
```

Constructs a RenderContext with a given transform and rendering hints.
The area of interest is taken to be the entire renderable area.

**Parameters:** usr2dev

- an AffineTransform.
**Parameters:** hints

- a RenderingHints object containing rendering hints.

- RenderContext

```java
public RenderContext​(
AffineTransform
usr2dev,

Shape
aoi)
```

Constructs a RenderContext with a given transform and area of interest.
The area of interest is supplied as a Shape.
No rendering hints are used.

**Parameters:** usr2dev

- an AffineTransform.
**Parameters:** aoi

- a Shape representing the area of interest.

---

#### Constructor Detail

RenderContext

```java
public RenderContext​(
AffineTransform
usr2dev,

Shape
aoi,

RenderingHints
hints)
```

Constructs a RenderContext with a given transform.
The area of interest is supplied as a Shape,
and the rendering hints are supplied as a RenderingHints object.

**Parameters:** usr2dev

- an AffineTransform.
**Parameters:** aoi

- a Shape representing the area of interest.
**Parameters:** hints

- a RenderingHints object containing rendering hints.

---

#### RenderContext

public RenderContext​(

AffineTransform

usr2dev,

Shape

aoi,

RenderingHints

hints)

Constructs a RenderContext with a given transform.
The area of interest is supplied as a Shape,
and the rendering hints are supplied as a RenderingHints object.

RenderContext

```java
public RenderContext​(
AffineTransform
usr2dev)
```

Constructs a RenderContext with a given transform.
The area of interest is taken to be the entire renderable area.
No rendering hints are used.

**Parameters:** usr2dev

- an AffineTransform.

---

#### RenderContext

public RenderContext​(

AffineTransform

usr2dev)

Constructs a RenderContext with a given transform.
The area of interest is taken to be the entire renderable area.
No rendering hints are used.

RenderContext

```java
public RenderContext​(
AffineTransform
usr2dev,

RenderingHints
hints)
```

Constructs a RenderContext with a given transform and rendering hints.
The area of interest is taken to be the entire renderable area.

**Parameters:** usr2dev

- an AffineTransform.
**Parameters:** hints

- a RenderingHints object containing rendering hints.

---

#### RenderContext

public RenderContext​(

AffineTransform

usr2dev,

RenderingHints

hints)

Constructs a RenderContext with a given transform and rendering hints.
The area of interest is taken to be the entire renderable area.

RenderContext

```java
public RenderContext​(
AffineTransform
usr2dev,

Shape
aoi)
```

Constructs a RenderContext with a given transform and area of interest.
The area of interest is supplied as a Shape.
No rendering hints are used.

**Parameters:** usr2dev

- an AffineTransform.
**Parameters:** aoi

- a Shape representing the area of interest.

---

#### RenderContext

public RenderContext​(

AffineTransform

usr2dev,

Shape

aoi)

Constructs a RenderContext with a given transform and area of interest.
The area of interest is supplied as a Shape.
No rendering hints are used.

Method Detail

- getRenderingHints

```java
public
RenderingHints
getRenderingHints()
```

Gets the rendering hints of this

RenderContext

.

**Returns:** a

RenderingHints

object that represents
the rendering hints of this

RenderContext

.
**See Also:** setRenderingHints(RenderingHints)

- setRenderingHints

```java
public void setRenderingHints​(
RenderingHints
hints)
```

Sets the rendering hints of this

RenderContext

.

**Parameters:** hints

- a

RenderingHints

object that represents
the rendering hints to assign to this

RenderContext

.
**See Also:** getRenderingHints()

- setTransform

```java
public void setTransform​(
AffineTransform
newTransform)
```

Sets the current user-to-device AffineTransform contained
in the RenderContext to a given transform.

**Parameters:** newTransform

- the new AffineTransform.
**See Also:** getTransform()

- preConcatenateTransform

```java
public void preConcatenateTransform​(
AffineTransform
modTransform)
```

Modifies the current user-to-device transform by prepending another
transform. In matrix notation the operation is:

```java
[this] = [modTransform] x [this]
```

**Parameters:** modTransform

- the AffineTransform to prepend to the
current usr2dev transform.
**Since:** 1.3

- preConcetenateTransform

```java
@Deprecated

public void preConcetenateTransform​(
AffineTransform
modTransform)
```

Deprecated.

replaced by

preConcatenateTransform(AffineTransform)

.

Modifies the current user-to-device transform by prepending another
transform. In matrix notation the operation is:

```java
[this] = [modTransform] x [this]
```

This method does the same thing as the preConcatenateTransform
method. It is here for backward compatibility with previous releases
which misspelled the method name.

**Parameters:** modTransform

- the AffineTransform to prepend to the
current usr2dev transform.

- concatenateTransform

```java
public void concatenateTransform​(
AffineTransform
modTransform)
```

Modifies the current user-to-device transform by appending another
transform. In matrix notation the operation is:

```java
[this] = [this] x [modTransform]
```

**Parameters:** modTransform

- the AffineTransform to append to the
current usr2dev transform.
**Since:** 1.3

- concetenateTransform

```java
@Deprecated

public void concetenateTransform​(
AffineTransform
modTransform)
```

Deprecated.

replaced by

concatenateTransform(AffineTransform)

.

Modifies the current user-to-device transform by appending another
transform. In matrix notation the operation is:

```java
[this] = [this] x [modTransform]
```

This method does the same thing as the concatenateTransform
method. It is here for backward compatibility with previous releases
which misspelled the method name.

**Parameters:** modTransform

- the AffineTransform to append to the
current usr2dev transform.

- getTransform

```java
public
AffineTransform
getTransform()
```

Gets the current user-to-device AffineTransform.

**Returns:** a reference to the current AffineTransform.
**See Also:** setTransform(AffineTransform)

- setAreaOfInterest

```java
public void setAreaOfInterest​(
Shape
newAoi)
```

Sets the current area of interest. The old area is discarded.

**Parameters:** newAoi

- The new area of interest.
**See Also:** getAreaOfInterest()

- getAreaOfInterest

```java
public
Shape
getAreaOfInterest()
```

Gets the ares of interest currently contained in the
RenderContext.

**Returns:** a reference to the area of interest of the RenderContext,
or null if none is specified.
**See Also:** setAreaOfInterest(Shape)

- clone

```java
public
Object
clone()
```

Makes a copy of a RenderContext. The area of interest is copied
by reference. The usr2dev AffineTransform and hints are cloned,
while the area of interest is copied by reference.

**Overrides:** clone

in class

Object
**Returns:** the new cloned RenderContext.
**See Also:** Cloneable

---

#### Method Detail

getRenderingHints

```java
public
RenderingHints
getRenderingHints()
```

Gets the rendering hints of this

RenderContext

.

**Returns:** a

RenderingHints

object that represents
the rendering hints of this

RenderContext

.
**See Also:** setRenderingHints(RenderingHints)

---

#### getRenderingHints

public

RenderingHints

getRenderingHints()

Gets the rendering hints of this

RenderContext

.

setRenderingHints

```java
public void setRenderingHints​(
RenderingHints
hints)
```

Sets the rendering hints of this

RenderContext

.

**Parameters:** hints

- a

RenderingHints

object that represents
the rendering hints to assign to this

RenderContext

.
**See Also:** getRenderingHints()

---

#### setRenderingHints

public void setRenderingHints​(

RenderingHints

hints)

Sets the rendering hints of this

RenderContext

.

setTransform

```java
public void setTransform​(
AffineTransform
newTransform)
```

Sets the current user-to-device AffineTransform contained
in the RenderContext to a given transform.

**Parameters:** newTransform

- the new AffineTransform.
**See Also:** getTransform()

---

#### setTransform

public void setTransform​(

AffineTransform

newTransform)

Sets the current user-to-device AffineTransform contained
in the RenderContext to a given transform.

preConcatenateTransform

```java
public void preConcatenateTransform​(
AffineTransform
modTransform)
```

Modifies the current user-to-device transform by prepending another
transform. In matrix notation the operation is:

```java
[this] = [modTransform] x [this]
```

**Parameters:** modTransform

- the AffineTransform to prepend to the
current usr2dev transform.
**Since:** 1.3

---

#### preConcatenateTransform

public void preConcatenateTransform​(

AffineTransform

modTransform)

Modifies the current user-to-device transform by prepending another
transform. In matrix notation the operation is:

```java
[this] = [modTransform] x [this]
```

[this] = [modTransform] x [this]

preConcetenateTransform

```java
@Deprecated

public void preConcetenateTransform​(
AffineTransform
modTransform)
```

Deprecated.

replaced by

preConcatenateTransform(AffineTransform)

.

Modifies the current user-to-device transform by prepending another
transform. In matrix notation the operation is:

```java
[this] = [modTransform] x [this]
```

This method does the same thing as the preConcatenateTransform
method. It is here for backward compatibility with previous releases
which misspelled the method name.

**Parameters:** modTransform

- the AffineTransform to prepend to the
current usr2dev transform.

---

#### preConcetenateTransform

@Deprecated

public void preConcetenateTransform​(

AffineTransform

modTransform)

Modifies the current user-to-device transform by prepending another
transform. In matrix notation the operation is:

```java
[this] = [modTransform] x [this]
```

This method does the same thing as the preConcatenateTransform
method. It is here for backward compatibility with previous releases
which misspelled the method name.

[this] = [modTransform] x [this]

concatenateTransform

```java
public void concatenateTransform​(
AffineTransform
modTransform)
```

Modifies the current user-to-device transform by appending another
transform. In matrix notation the operation is:

```java
[this] = [this] x [modTransform]
```

**Parameters:** modTransform

- the AffineTransform to append to the
current usr2dev transform.
**Since:** 1.3

---

#### concatenateTransform

public void concatenateTransform​(

AffineTransform

modTransform)

Modifies the current user-to-device transform by appending another
transform. In matrix notation the operation is:

```java
[this] = [this] x [modTransform]
```

[this] = [this] x [modTransform]

concetenateTransform

```java
@Deprecated

public void concetenateTransform​(
AffineTransform
modTransform)
```

Deprecated.

replaced by

concatenateTransform(AffineTransform)

.

Modifies the current user-to-device transform by appending another
transform. In matrix notation the operation is:

```java
[this] = [this] x [modTransform]
```

This method does the same thing as the concatenateTransform
method. It is here for backward compatibility with previous releases
which misspelled the method name.

**Parameters:** modTransform

- the AffineTransform to append to the
current usr2dev transform.

---

#### concetenateTransform

@Deprecated

public void concetenateTransform​(

AffineTransform

modTransform)

Modifies the current user-to-device transform by appending another
transform. In matrix notation the operation is:

```java
[this] = [this] x [modTransform]
```

This method does the same thing as the concatenateTransform
method. It is here for backward compatibility with previous releases
which misspelled the method name.

[this] = [this] x [modTransform]

getTransform

```java
public
AffineTransform
getTransform()
```

Gets the current user-to-device AffineTransform.

**Returns:** a reference to the current AffineTransform.
**See Also:** setTransform(AffineTransform)

---

#### getTransform

public

AffineTransform

getTransform()

Gets the current user-to-device AffineTransform.

setAreaOfInterest

```java
public void setAreaOfInterest​(
Shape
newAoi)
```

Sets the current area of interest. The old area is discarded.

**Parameters:** newAoi

- The new area of interest.
**See Also:** getAreaOfInterest()

---

#### setAreaOfInterest

public void setAreaOfInterest​(

Shape

newAoi)

Sets the current area of interest. The old area is discarded.

getAreaOfInterest

```java
public
Shape
getAreaOfInterest()
```

Gets the ares of interest currently contained in the
RenderContext.

**Returns:** a reference to the area of interest of the RenderContext,
or null if none is specified.
**See Also:** setAreaOfInterest(Shape)

---

#### getAreaOfInterest

public

Shape

getAreaOfInterest()

Gets the ares of interest currently contained in the
RenderContext.

clone

```java
public
Object
clone()
```

Makes a copy of a RenderContext. The area of interest is copied
by reference. The usr2dev AffineTransform and hints are cloned,
while the area of interest is copied by reference.

**Overrides:** clone

in class

Object
**Returns:** the new cloned RenderContext.
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Makes a copy of a RenderContext. The area of interest is copied
by reference. The usr2dev AffineTransform and hints are cloned,
while the area of interest is copied by reference.

---

