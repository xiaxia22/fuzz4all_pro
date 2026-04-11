# Class ParameterBlock

**Source:** `java.desktop\java\awt\image\renderable\ParameterBlock.html`

### Class Description

```java
public class
ParameterBlock

extends
Object

implements
Cloneable
,
Serializable
```

A

ParameterBlock

encapsulates all the information about sources and
parameters (Objects) required by a RenderableImageOp, or other
classes that process images.

Although it is possible to place arbitrary objects in the
source Vector, users of this class may impose semantic constraints
such as requiring all sources to be RenderedImages or
RenderableImage.

ParameterBlock

itself is merely a container and
performs no checking on source or parameter types.

All parameters in a

ParameterBlock

are objects; convenience
add and set methods are available that take arguments of base type and
construct the appropriate subclass of Number (such as
Integer or Float). Corresponding get methods perform a
downward cast and have return values of base type; an exception
will be thrown if the stored values do not have the correct type.
There is no way to distinguish between the results of
"short s; add(s)" and "add(new Short(s))".

Note that the get and set methods operate on references.
Therefore, one must be careful not to share references between

ParameterBlock

s when this is inappropriate. For example, to create
a new

ParameterBlock

that is equal to an old one except for an
added source, one might be tempted to write:

```java
ParameterBlock addSource(ParameterBlock pb, RenderableImage im) {
ParameterBlock pb1 = new ParameterBlock(pb.getSources());
pb1.addSource(im);
return pb1;
}
```

This code will have the side effect of altering the original

ParameterBlock

, since the getSources operation returned a reference
to its source Vector. Both pb and pb1 share their source Vector,
and a change in either is visible to both.

A correct way to write the addSource function is to clone
the source Vector:

```java
ParameterBlock addSource (ParameterBlock pb, RenderableImage im) {
ParameterBlock pb1 = new ParameterBlock(pb.getSources().clone());
pb1.addSource(im);
return pb1;
}
```

The clone method of

ParameterBlock

has been defined to
perform a clone of both the source and parameter Vectors for
this reason. A standard, shallow clone is available as
shallowClone.

The addSource, setSource, add, and set methods are
defined to return 'this' after adding their argument. This allows
use of syntax like:

```java
ParameterBlock pb = new ParameterBlock();
op = new RenderableImageOp("operation", pb.add(arg1).add(arg2));
```

**All Implemented Interfaces:** Serializable

,

Cloneable

---

### Field Details

#### protected
Vector
<
Object
> sources

A Vector of sources, stored as arbitrary Objects.

---

#### protected
Vector
<
Object
> parameters

A Vector of non-source parameters, stored as arbitrary Objects.

---

### Constructor Details

#### public ParameterBlock()

A dummy constructor.

---

#### public ParameterBlock​(
Vector
<
Object
> sources)

Constructs a

ParameterBlock

with a given Vector
of sources.

**Parameters:**
- sources

- a

Vector

of source images

---

#### public ParameterBlock​(
Vector
<
Object
> sources,

Vector
<
Object
> parameters)

Constructs a

ParameterBlock

with a given Vector of sources and
Vector of parameters.

**Parameters:**
- sources

- a

Vector

of source images
- parameters

- a

Vector

of parameters to be used in the
rendering operation

---

### Method Details

#### public
Object
shallowClone()

Creates a shallow copy of a

ParameterBlock

. The source and
parameter Vectors are copied by reference -- additions or
changes will be visible to both versions.

**Returns:**
- an Object clone of the

ParameterBlock

.

---

#### public
Object
clone()

Creates a copy of a

ParameterBlock

. The source and parameter
Vectors are cloned, but the actual sources and parameters are
copied by reference. This allows modifications to the order
and number of sources and parameters in the clone to be invisible
to the original

ParameterBlock

. Changes to the shared sources or
parameters themselves will still be visible.

**Overrides:**
- clone

in class

Object

**Returns:**
- an Object clone of the

ParameterBlock

.

**See Also:**
- Cloneable

---

#### public
ParameterBlock
addSource​(
Object
source)

Adds an image to end of the list of sources. The image is
stored as an object in order to allow new node types in the
future.

**Parameters:**
- source

- an image object to be stored in the source list.

**Returns:**
- a new

ParameterBlock

containing the specified

source

.

---

#### public
Object
getSource​(int index)

Returns a source as a general Object. The caller must cast it into
an appropriate type.

**Parameters:**
- index

- the index of the source to be returned.

**Returns:**
- an

Object

that represents the source located
at the specified index in the

sources

Vector

.

**See Also:**
- setSource(Object, int)

---

#### public
ParameterBlock
setSource​(
Object
source,
int index)

Replaces an entry in the list of source with a new source.
If the index lies beyond the current source list,
the list is extended with nulls as needed.

**Parameters:**
- source

- the specified source image
- index

- the index into the

sources

Vector

at which to
insert the specified

source

**Returns:**
- a new

ParameterBlock

that contains the
specified

source

at the specified

index

.

**See Also:**
- getSource(int)

---

#### public
RenderedImage
getRenderedSource​(int index)

Returns a source as a

RenderedImage

. This method is
a convenience method.
An exception will be thrown if the source is not a RenderedImage.

**Parameters:**
- index

- the index of the source to be returned

**Returns:**
- a

RenderedImage

that represents the source
image that is at the specified index in the

sources Vector

.

---

#### public
RenderableImage
getRenderableSource​(int index)

Returns a source as a RenderableImage. This method is a
convenience method.
An exception will be thrown if the sources is not a RenderableImage.

**Parameters:**
- index

- the index of the source to be returned

**Returns:**
- a

RenderableImage

that represents the source
image that is at the specified index in the

sources Vector

.

---

#### public int getNumSources()

Returns the number of source images.

**Returns:**
- the number of source images in the

sources

Vector

.

---

#### public
Vector
<
Object
> getSources()

Returns the entire Vector of sources.

**Returns:**
- the

sources Vector

.

**See Also:**
- setSources(Vector)

---

#### public void setSources​(
Vector
<
Object
> sources)

Sets the entire Vector of sources to a given Vector.

**Parameters:**
- sources

- the

Vector

of source images

**See Also:**
- getSources()

---

#### public void removeSources()

Clears the list of source images.

---

#### public int getNumParameters()

Returns the number of parameters (not including source images).

**Returns:**
- the number of parameters in the

parameters

Vector

.

---

#### public
Vector
<
Object
> getParameters()

Returns the entire Vector of parameters.

**Returns:**
- the

parameters Vector

.

**See Also:**
- setParameters(Vector)

---

#### public void setParameters​(
Vector
<
Object
> parameters)

Sets the entire Vector of parameters to a given Vector.

**Parameters:**
- parameters

- the specified

Vector

of
parameters

**See Also:**
- getParameters()

---

#### public void removeParameters()

Clears the list of parameters.

---

#### public
ParameterBlock
add​(
Object
obj)

Adds an object to the list of parameters.

**Parameters:**
- obj

- the

Object

to add to the

parameters Vector

**Returns:**
- a new

ParameterBlock

containing
the specified parameter.

---

#### public
ParameterBlock
add​(byte b)

Adds a Byte to the list of parameters.

**Parameters:**
- b

- the byte to add to the

parameters Vector

**Returns:**
- a new

ParameterBlock

containing
the specified parameter.

---

#### public
ParameterBlock
add​(char c)

Adds a Character to the list of parameters.

**Parameters:**
- c

- the char to add to the

parameters Vector

**Returns:**
- a new

ParameterBlock

containing
the specified parameter.

---

#### public
ParameterBlock
add​(short s)

Adds a Short to the list of parameters.

**Parameters:**
- s

- the short to add to the

parameters Vector

**Returns:**
- a new

ParameterBlock

containing
the specified parameter.

---

#### public
ParameterBlock
add​(int i)

Adds a Integer to the list of parameters.

**Parameters:**
- i

- the int to add to the

parameters Vector

**Returns:**
- a new

ParameterBlock

containing
the specified parameter.

---

#### public
ParameterBlock
add​(long l)

Adds a Long to the list of parameters.

**Parameters:**
- l

- the long to add to the

parameters Vector

**Returns:**
- a new

ParameterBlock

containing
the specified parameter.

---

#### public
ParameterBlock
add​(float f)

Adds a Float to the list of parameters.

**Parameters:**
- f

- the float to add to the

parameters Vector

**Returns:**
- a new

ParameterBlock

containing
the specified parameter.

---

#### public
ParameterBlock
add​(double d)

Adds a Double to the list of parameters.

**Parameters:**
- d

- the double to add to the

parameters Vector

**Returns:**
- a new

ParameterBlock

containing
the specified parameter.

---

#### public
ParameterBlock
set​(
Object
obj,
int index)

Replaces an Object in the list of parameters.
If the index lies beyond the current source list,
the list is extended with nulls as needed.

**Parameters:**
- obj

- the parameter that replaces the
parameter at the specified index in the

parameters Vector
- index

- the index of the parameter to be
replaced with the specified parameter

**Returns:**
- a new

ParameterBlock

containing
the specified parameter.

---

#### public
ParameterBlock
set​(byte b,
int index)

Replaces an Object in the list of parameters with a Byte.
If the index lies beyond the current source list,
the list is extended with nulls as needed.

**Parameters:**
- b

- the parameter that replaces the
parameter at the specified index in the

parameters Vector
- index

- the index of the parameter to be
replaced with the specified parameter

**Returns:**
- a new

ParameterBlock

containing
the specified parameter.

---

#### public
ParameterBlock
set​(char c,
int index)

Replaces an Object in the list of parameters with a Character.
If the index lies beyond the current source list,
the list is extended with nulls as needed.

**Parameters:**
- c

- the parameter that replaces the
parameter at the specified index in the

parameters Vector
- index

- the index of the parameter to be
replaced with the specified parameter

**Returns:**
- a new

ParameterBlock

containing
the specified parameter.

---

#### public
ParameterBlock
set​(short s,
int index)

Replaces an Object in the list of parameters with a Short.
If the index lies beyond the current source list,
the list is extended with nulls as needed.

**Parameters:**
- s

- the parameter that replaces the
parameter at the specified index in the

parameters Vector
- index

- the index of the parameter to be
replaced with the specified parameter

**Returns:**
- a new

ParameterBlock

containing
the specified parameter.

---

#### public
ParameterBlock
set​(int i,
int index)

Replaces an Object in the list of parameters with an Integer.
If the index lies beyond the current source list,
the list is extended with nulls as needed.

**Parameters:**
- i

- the parameter that replaces the
parameter at the specified index in the

parameters Vector
- index

- the index of the parameter to be
replaced with the specified parameter

**Returns:**
- a new

ParameterBlock

containing
the specified parameter.

---

#### public
ParameterBlock
set​(long l,
int index)

Replaces an Object in the list of parameters with a Long.
If the index lies beyond the current source list,
the list is extended with nulls as needed.

**Parameters:**
- l

- the parameter that replaces the
parameter at the specified index in the

parameters Vector
- index

- the index of the parameter to be
replaced with the specified parameter

**Returns:**
- a new

ParameterBlock

containing
the specified parameter.

---

#### public
ParameterBlock
set​(float f,
int index)

Replaces an Object in the list of parameters with a Float.
If the index lies beyond the current source list,
the list is extended with nulls as needed.

**Parameters:**
- f

- the parameter that replaces the
parameter at the specified index in the

parameters Vector
- index

- the index of the parameter to be
replaced with the specified parameter

**Returns:**
- a new

ParameterBlock

containing
the specified parameter.

---

#### public
ParameterBlock
set​(double d,
int index)

Replaces an Object in the list of parameters with a Double.
If the index lies beyond the current source list,
the list is extended with nulls as needed.

**Parameters:**
- d

- the parameter that replaces the
parameter at the specified index in the

parameters Vector
- index

- the index of the parameter to be
replaced with the specified parameter

**Returns:**
- a new

ParameterBlock

containing
the specified parameter.

---

#### public
Object
getObjectParameter​(int index)

Gets a parameter as an object.

**Parameters:**
- index

- the index of the parameter to get

**Returns:**
- an

Object

representing the
the parameter at the specified index
into the

parameters

Vector

.

---

#### public byte getByteParameter​(int index)

A convenience method to return a parameter as a byte. An
exception is thrown if the parameter is

null

or not a

Byte

.

**Parameters:**
- index

- the index of the parameter to be returned.

**Returns:**
- the parameter at the specified index
as a

byte

value.

**Throws:**
- ClassCastException

- if the parameter at the
specified index is not a

Byte
- NullPointerException

- if the parameter at the specified
index is

null
- ArrayIndexOutOfBoundsException

- if

index

is negative or not less than the current size of this

ParameterBlock

object

---

#### public char getCharParameter​(int index)

A convenience method to return a parameter as a char. An
exception is thrown if the parameter is

null

or not a

Character

.

**Parameters:**
- index

- the index of the parameter to be returned.

**Returns:**
- the parameter at the specified index
as a

char

value.

**Throws:**
- ClassCastException

- if the parameter at the
specified index is not a

Character
- NullPointerException

- if the parameter at the specified
index is

null
- ArrayIndexOutOfBoundsException

- if

index

is negative or not less than the current size of this

ParameterBlock

object

---

#### public short getShortParameter​(int index)

A convenience method to return a parameter as a short. An
exception is thrown if the parameter is

null

or not a

Short

.

**Parameters:**
- index

- the index of the parameter to be returned.

**Returns:**
- the parameter at the specified index
as a

short

value.

**Throws:**
- ClassCastException

- if the parameter at the
specified index is not a

Short
- NullPointerException

- if the parameter at the specified
index is

null
- ArrayIndexOutOfBoundsException

- if

index

is negative or not less than the current size of this

ParameterBlock

object

---

#### public int getIntParameter​(int index)

A convenience method to return a parameter as an int. An
exception is thrown if the parameter is

null

or not an

Integer

.

**Parameters:**
- index

- the index of the parameter to be returned.

**Returns:**
- the parameter at the specified index
as an

int

value.

**Throws:**
- ClassCastException

- if the parameter at the
specified index is not an

Integer
- NullPointerException

- if the parameter at the specified
index is

null
- ArrayIndexOutOfBoundsException

- if

index

is negative or not less than the current size of this

ParameterBlock

object

---

#### public long getLongParameter​(int index)

A convenience method to return a parameter as a long. An
exception is thrown if the parameter is

null

or not a

Long

.

**Parameters:**
- index

- the index of the parameter to be returned.

**Returns:**
- the parameter at the specified index
as a

long

value.

**Throws:**
- ClassCastException

- if the parameter at the
specified index is not a

Long
- NullPointerException

- if the parameter at the specified
index is

null
- ArrayIndexOutOfBoundsException

- if

index

is negative or not less than the current size of this

ParameterBlock

object

---

#### public float getFloatParameter​(int index)

A convenience method to return a parameter as a float. An
exception is thrown if the parameter is

null

or not a

Float

.

**Parameters:**
- index

- the index of the parameter to be returned.

**Returns:**
- the parameter at the specified index
as a

float

value.

**Throws:**
- ClassCastException

- if the parameter at the
specified index is not a

Float
- NullPointerException

- if the parameter at the specified
index is

null
- ArrayIndexOutOfBoundsException

- if

index

is negative or not less than the current size of this

ParameterBlock

object

---

#### public double getDoubleParameter​(int index)

A convenience method to return a parameter as a double. An
exception is thrown if the parameter is

null

or not a

Double

.

**Parameters:**
- index

- the index of the parameter to be returned.

**Returns:**
- the parameter at the specified index
as a

double

value.

**Throws:**
- ClassCastException

- if the parameter at the
specified index is not a

Double
- NullPointerException

- if the parameter at the specified
index is

null
- ArrayIndexOutOfBoundsException

- if

index

is negative or not less than the current size of this

ParameterBlock

object

---

#### public
Class
<?>[] getParamClasses()

Returns an array of Class objects describing the types
of the parameters.

**Returns:**
- an array of

Class

objects.

---

### Additional Sections

#### Class ParameterBlock

java.lang.Object

- java.awt.image.renderable.ParameterBlock

java.awt.image.renderable.ParameterBlock

**All Implemented Interfaces:** Serializable

,

Cloneable

```java
public class
ParameterBlock

extends
Object

implements
Cloneable
,
Serializable
```

A

ParameterBlock

encapsulates all the information about sources and
parameters (Objects) required by a RenderableImageOp, or other
classes that process images.

Although it is possible to place arbitrary objects in the
source Vector, users of this class may impose semantic constraints
such as requiring all sources to be RenderedImages or
RenderableImage.

ParameterBlock

itself is merely a container and
performs no checking on source or parameter types.

All parameters in a

ParameterBlock

are objects; convenience
add and set methods are available that take arguments of base type and
construct the appropriate subclass of Number (such as
Integer or Float). Corresponding get methods perform a
downward cast and have return values of base type; an exception
will be thrown if the stored values do not have the correct type.
There is no way to distinguish between the results of
"short s; add(s)" and "add(new Short(s))".

Note that the get and set methods operate on references.
Therefore, one must be careful not to share references between

ParameterBlock

s when this is inappropriate. For example, to create
a new

ParameterBlock

that is equal to an old one except for an
added source, one might be tempted to write:

```java
ParameterBlock addSource(ParameterBlock pb, RenderableImage im) {
ParameterBlock pb1 = new ParameterBlock(pb.getSources());
pb1.addSource(im);
return pb1;
}
```

This code will have the side effect of altering the original

ParameterBlock

, since the getSources operation returned a reference
to its source Vector. Both pb and pb1 share their source Vector,
and a change in either is visible to both.

A correct way to write the addSource function is to clone
the source Vector:

```java
ParameterBlock addSource (ParameterBlock pb, RenderableImage im) {
ParameterBlock pb1 = new ParameterBlock(pb.getSources().clone());
pb1.addSource(im);
return pb1;
}
```

The clone method of

ParameterBlock

has been defined to
perform a clone of both the source and parameter Vectors for
this reason. A standard, shallow clone is available as
shallowClone.

The addSource, setSource, add, and set methods are
defined to return 'this' after adding their argument. This allows
use of syntax like:

```java
ParameterBlock pb = new ParameterBlock();
op = new RenderableImageOp("operation", pb.add(arg1).add(arg2));
```

**See Also:** Serialized Form

public class

ParameterBlock

extends

Object

implements

Cloneable

,

Serializable

A

ParameterBlock

encapsulates all the information about sources and
parameters (Objects) required by a RenderableImageOp, or other
classes that process images.

Although it is possible to place arbitrary objects in the
source Vector, users of this class may impose semantic constraints
such as requiring all sources to be RenderedImages or
RenderableImage.

ParameterBlock

itself is merely a container and
performs no checking on source or parameter types.

All parameters in a

ParameterBlock

are objects; convenience
add and set methods are available that take arguments of base type and
construct the appropriate subclass of Number (such as
Integer or Float). Corresponding get methods perform a
downward cast and have return values of base type; an exception
will be thrown if the stored values do not have the correct type.
There is no way to distinguish between the results of
"short s; add(s)" and "add(new Short(s))".

Note that the get and set methods operate on references.
Therefore, one must be careful not to share references between

ParameterBlock

s when this is inappropriate. For example, to create
a new

ParameterBlock

that is equal to an old one except for an
added source, one might be tempted to write:

```java
ParameterBlock addSource(ParameterBlock pb, RenderableImage im) {
ParameterBlock pb1 = new ParameterBlock(pb.getSources());
pb1.addSource(im);
return pb1;
}
```

This code will have the side effect of altering the original

ParameterBlock

, since the getSources operation returned a reference
to its source Vector. Both pb and pb1 share their source Vector,
and a change in either is visible to both.

A correct way to write the addSource function is to clone
the source Vector:

```java
ParameterBlock addSource (ParameterBlock pb, RenderableImage im) {
ParameterBlock pb1 = new ParameterBlock(pb.getSources().clone());
pb1.addSource(im);
return pb1;
}
```

The clone method of

ParameterBlock

has been defined to
perform a clone of both the source and parameter Vectors for
this reason. A standard, shallow clone is available as
shallowClone.

The addSource, setSource, add, and set methods are
defined to return 'this' after adding their argument. This allows
use of syntax like:

```java
ParameterBlock pb = new ParameterBlock();
op = new RenderableImageOp("operation", pb.add(arg1).add(arg2));
```

Although it is possible to place arbitrary objects in the
source Vector, users of this class may impose semantic constraints
such as requiring all sources to be RenderedImages or
RenderableImage.

ParameterBlock

itself is merely a container and
performs no checking on source or parameter types.

All parameters in a

ParameterBlock

are objects; convenience
add and set methods are available that take arguments of base type and
construct the appropriate subclass of Number (such as
Integer or Float). Corresponding get methods perform a
downward cast and have return values of base type; an exception
will be thrown if the stored values do not have the correct type.
There is no way to distinguish between the results of
"short s; add(s)" and "add(new Short(s))".

Note that the get and set methods operate on references.
Therefore, one must be careful not to share references between

ParameterBlock

s when this is inappropriate. For example, to create
a new

ParameterBlock

that is equal to an old one except for an
added source, one might be tempted to write:

```java
ParameterBlock addSource(ParameterBlock pb, RenderableImage im) {
ParameterBlock pb1 = new ParameterBlock(pb.getSources());
pb1.addSource(im);
return pb1;
}
```

This code will have the side effect of altering the original

ParameterBlock

, since the getSources operation returned a reference
to its source Vector. Both pb and pb1 share their source Vector,
and a change in either is visible to both.

A correct way to write the addSource function is to clone
the source Vector:

```java
ParameterBlock addSource (ParameterBlock pb, RenderableImage im) {
ParameterBlock pb1 = new ParameterBlock(pb.getSources().clone());
pb1.addSource(im);
return pb1;
}
```

The clone method of

ParameterBlock

has been defined to
perform a clone of both the source and parameter Vectors for
this reason. A standard, shallow clone is available as
shallowClone.

The addSource, setSource, add, and set methods are
defined to return 'this' after adding their argument. This allows
use of syntax like:

```java
ParameterBlock pb = new ParameterBlock();
op = new RenderableImageOp("operation", pb.add(arg1).add(arg2));
```

All parameters in a

ParameterBlock

are objects; convenience
add and set methods are available that take arguments of base type and
construct the appropriate subclass of Number (such as
Integer or Float). Corresponding get methods perform a
downward cast and have return values of base type; an exception
will be thrown if the stored values do not have the correct type.
There is no way to distinguish between the results of
"short s; add(s)" and "add(new Short(s))".

Note that the get and set methods operate on references.
Therefore, one must be careful not to share references between

ParameterBlock

s when this is inappropriate. For example, to create
a new

ParameterBlock

that is equal to an old one except for an
added source, one might be tempted to write:

```java
ParameterBlock addSource(ParameterBlock pb, RenderableImage im) {
ParameterBlock pb1 = new ParameterBlock(pb.getSources());
pb1.addSource(im);
return pb1;
}
```

This code will have the side effect of altering the original

ParameterBlock

, since the getSources operation returned a reference
to its source Vector. Both pb and pb1 share their source Vector,
and a change in either is visible to both.

A correct way to write the addSource function is to clone
the source Vector:

```java
ParameterBlock addSource (ParameterBlock pb, RenderableImage im) {
ParameterBlock pb1 = new ParameterBlock(pb.getSources().clone());
pb1.addSource(im);
return pb1;
}
```

The clone method of

ParameterBlock

has been defined to
perform a clone of both the source and parameter Vectors for
this reason. A standard, shallow clone is available as
shallowClone.

The addSource, setSource, add, and set methods are
defined to return 'this' after adding their argument. This allows
use of syntax like:

```java
ParameterBlock pb = new ParameterBlock();
op = new RenderableImageOp("operation", pb.add(arg1).add(arg2));
```

Note that the get and set methods operate on references.
Therefore, one must be careful not to share references between

ParameterBlock

s when this is inappropriate. For example, to create
a new

ParameterBlock

that is equal to an old one except for an
added source, one might be tempted to write:

```java
ParameterBlock addSource(ParameterBlock pb, RenderableImage im) {
ParameterBlock pb1 = new ParameterBlock(pb.getSources());
pb1.addSource(im);
return pb1;
}
```

This code will have the side effect of altering the original

ParameterBlock

, since the getSources operation returned a reference
to its source Vector. Both pb and pb1 share their source Vector,
and a change in either is visible to both.

A correct way to write the addSource function is to clone
the source Vector:

```java
ParameterBlock addSource (ParameterBlock pb, RenderableImage im) {
ParameterBlock pb1 = new ParameterBlock(pb.getSources().clone());
pb1.addSource(im);
return pb1;
}
```

The clone method of

ParameterBlock

has been defined to
perform a clone of both the source and parameter Vectors for
this reason. A standard, shallow clone is available as
shallowClone.

The addSource, setSource, add, and set methods are
defined to return 'this' after adding their argument. This allows
use of syntax like:

```java
ParameterBlock pb = new ParameterBlock();
op = new RenderableImageOp("operation", pb.add(arg1).add(arg2));
```

ParameterBlock addSource(ParameterBlock pb, RenderableImage im) {
ParameterBlock pb1 = new ParameterBlock(pb.getSources());
pb1.addSource(im);
return pb1;
}

This code will have the side effect of altering the original

ParameterBlock

, since the getSources operation returned a reference
to its source Vector. Both pb and pb1 share their source Vector,
and a change in either is visible to both.

A correct way to write the addSource function is to clone
the source Vector:

```java
ParameterBlock addSource (ParameterBlock pb, RenderableImage im) {
ParameterBlock pb1 = new ParameterBlock(pb.getSources().clone());
pb1.addSource(im);
return pb1;
}
```

The clone method of

ParameterBlock

has been defined to
perform a clone of both the source and parameter Vectors for
this reason. A standard, shallow clone is available as
shallowClone.

The addSource, setSource, add, and set methods are
defined to return 'this' after adding their argument. This allows
use of syntax like:

```java
ParameterBlock pb = new ParameterBlock();
op = new RenderableImageOp("operation", pb.add(arg1).add(arg2));
```

A correct way to write the addSource function is to clone
the source Vector:

```java
ParameterBlock addSource (ParameterBlock pb, RenderableImage im) {
ParameterBlock pb1 = new ParameterBlock(pb.getSources().clone());
pb1.addSource(im);
return pb1;
}
```

The clone method of

ParameterBlock

has been defined to
perform a clone of both the source and parameter Vectors for
this reason. A standard, shallow clone is available as
shallowClone.

The addSource, setSource, add, and set methods are
defined to return 'this' after adding their argument. This allows
use of syntax like:

```java
ParameterBlock pb = new ParameterBlock();
op = new RenderableImageOp("operation", pb.add(arg1).add(arg2));
```

ParameterBlock addSource (ParameterBlock pb, RenderableImage im) {
ParameterBlock pb1 = new ParameterBlock(pb.getSources().clone());
pb1.addSource(im);
return pb1;
}

The clone method of

ParameterBlock

has been defined to
perform a clone of both the source and parameter Vectors for
this reason. A standard, shallow clone is available as
shallowClone.

The addSource, setSource, add, and set methods are
defined to return 'this' after adding their argument. This allows
use of syntax like:

```java
ParameterBlock pb = new ParameterBlock();
op = new RenderableImageOp("operation", pb.add(arg1).add(arg2));
```

The addSource, setSource, add, and set methods are
defined to return 'this' after adding their argument. This allows
use of syntax like:

```java
ParameterBlock pb = new ParameterBlock();
op = new RenderableImageOp("operation", pb.add(arg1).add(arg2));
```

ParameterBlock pb = new ParameterBlock();
op = new RenderableImageOp("operation", pb.add(arg1).add(arg2));

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

Vector

<

Object

>

parameters

A Vector of non-source parameters, stored as arbitrary Objects.

protected

Vector

<

Object

>

sources

A Vector of sources, stored as arbitrary Objects.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ParameterBlock

()

A dummy constructor.

ParameterBlock

​(

Vector

<

Object

> sources)

Constructs a

ParameterBlock

with a given Vector
of sources.

ParameterBlock

​(

Vector

<

Object

> sources,

Vector

<

Object

> parameters)

Constructs a

ParameterBlock

with a given Vector of sources and
Vector of parameters.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

ParameterBlock

add

​(byte b)

Adds a Byte to the list of parameters.

ParameterBlock

add

​(char c)

Adds a Character to the list of parameters.

ParameterBlock

add

​(double d)

Adds a Double to the list of parameters.

ParameterBlock

add

​(float f)

Adds a Float to the list of parameters.

ParameterBlock

add

​(int i)

Adds a Integer to the list of parameters.

ParameterBlock

add

​(long l)

Adds a Long to the list of parameters.

ParameterBlock

add

​(short s)

Adds a Short to the list of parameters.

ParameterBlock

add

​(

Object

obj)

Adds an object to the list of parameters.

ParameterBlock

addSource

​(

Object

source)

Adds an image to end of the list of sources.

Object

clone

()

Creates a copy of a

ParameterBlock

.

byte

getByteParameter

​(int index)

A convenience method to return a parameter as a byte.

char

getCharParameter

​(int index)

A convenience method to return a parameter as a char.

double

getDoubleParameter

​(int index)

A convenience method to return a parameter as a double.

float

getFloatParameter

​(int index)

A convenience method to return a parameter as a float.

int

getIntParameter

​(int index)

A convenience method to return a parameter as an int.

long

getLongParameter

​(int index)

A convenience method to return a parameter as a long.

int

getNumParameters

()

Returns the number of parameters (not including source images).

int

getNumSources

()

Returns the number of source images.

Object

getObjectParameter

​(int index)

Gets a parameter as an object.

Class

<?>[]

getParamClasses

()

Returns an array of Class objects describing the types
of the parameters.

Vector

<

Object

>

getParameters

()

Returns the entire Vector of parameters.

RenderableImage

getRenderableSource

​(int index)

Returns a source as a RenderableImage.

RenderedImage

getRenderedSource

​(int index)

Returns a source as a

RenderedImage

.

short

getShortParameter

​(int index)

A convenience method to return a parameter as a short.

Object

getSource

​(int index)

Returns a source as a general Object.

Vector

<

Object

>

getSources

()

Returns the entire Vector of sources.

void

removeParameters

()

Clears the list of parameters.

void

removeSources

()

Clears the list of source images.

ParameterBlock

set

​(byte b,
int index)

Replaces an Object in the list of parameters with a Byte.

ParameterBlock

set

​(char c,
int index)

Replaces an Object in the list of parameters with a Character.

ParameterBlock

set

​(double d,
int index)

Replaces an Object in the list of parameters with a Double.

ParameterBlock

set

​(float f,
int index)

Replaces an Object in the list of parameters with a Float.

ParameterBlock

set

​(int i,
int index)

Replaces an Object in the list of parameters with an Integer.

ParameterBlock

set

​(long l,
int index)

Replaces an Object in the list of parameters with a Long.

ParameterBlock

set

​(short s,
int index)

Replaces an Object in the list of parameters with a Short.

ParameterBlock

set

​(

Object

obj,
int index)

Replaces an Object in the list of parameters.

void

setParameters

​(

Vector

<

Object

> parameters)

Sets the entire Vector of parameters to a given Vector.

ParameterBlock

setSource

​(

Object

source,
int index)

Replaces an entry in the list of source with a new source.

void

setSources

​(

Vector

<

Object

> sources)

Sets the entire Vector of sources to a given Vector.

Object

shallowClone

()

Creates a shallow copy of a

ParameterBlock

.

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

Fields

Modifier and Type

Field

Description

protected

Vector

<

Object

>

parameters

A Vector of non-source parameters, stored as arbitrary Objects.

protected

Vector

<

Object

>

sources

A Vector of sources, stored as arbitrary Objects.

---

#### Field Summary

A Vector of non-source parameters, stored as arbitrary Objects.

A Vector of sources, stored as arbitrary Objects.

Constructor Summary

Constructors

Constructor

Description

ParameterBlock

()

A dummy constructor.

ParameterBlock

​(

Vector

<

Object

> sources)

Constructs a

ParameterBlock

with a given Vector
of sources.

ParameterBlock

​(

Vector

<

Object

> sources,

Vector

<

Object

> parameters)

Constructs a

ParameterBlock

with a given Vector of sources and
Vector of parameters.

---

#### Constructor Summary

A dummy constructor.

Constructs a

ParameterBlock

with a given Vector
of sources.

Constructs a

ParameterBlock

with a given Vector of sources and
Vector of parameters.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

ParameterBlock

add

​(byte b)

Adds a Byte to the list of parameters.

ParameterBlock

add

​(char c)

Adds a Character to the list of parameters.

ParameterBlock

add

​(double d)

Adds a Double to the list of parameters.

ParameterBlock

add

​(float f)

Adds a Float to the list of parameters.

ParameterBlock

add

​(int i)

Adds a Integer to the list of parameters.

ParameterBlock

add

​(long l)

Adds a Long to the list of parameters.

ParameterBlock

add

​(short s)

Adds a Short to the list of parameters.

ParameterBlock

add

​(

Object

obj)

Adds an object to the list of parameters.

ParameterBlock

addSource

​(

Object

source)

Adds an image to end of the list of sources.

Object

clone

()

Creates a copy of a

ParameterBlock

.

byte

getByteParameter

​(int index)

A convenience method to return a parameter as a byte.

char

getCharParameter

​(int index)

A convenience method to return a parameter as a char.

double

getDoubleParameter

​(int index)

A convenience method to return a parameter as a double.

float

getFloatParameter

​(int index)

A convenience method to return a parameter as a float.

int

getIntParameter

​(int index)

A convenience method to return a parameter as an int.

long

getLongParameter

​(int index)

A convenience method to return a parameter as a long.

int

getNumParameters

()

Returns the number of parameters (not including source images).

int

getNumSources

()

Returns the number of source images.

Object

getObjectParameter

​(int index)

Gets a parameter as an object.

Class

<?>[]

getParamClasses

()

Returns an array of Class objects describing the types
of the parameters.

Vector

<

Object

>

getParameters

()

Returns the entire Vector of parameters.

RenderableImage

getRenderableSource

​(int index)

Returns a source as a RenderableImage.

RenderedImage

getRenderedSource

​(int index)

Returns a source as a

RenderedImage

.

short

getShortParameter

​(int index)

A convenience method to return a parameter as a short.

Object

getSource

​(int index)

Returns a source as a general Object.

Vector

<

Object

>

getSources

()

Returns the entire Vector of sources.

void

removeParameters

()

Clears the list of parameters.

void

removeSources

()

Clears the list of source images.

ParameterBlock

set

​(byte b,
int index)

Replaces an Object in the list of parameters with a Byte.

ParameterBlock

set

​(char c,
int index)

Replaces an Object in the list of parameters with a Character.

ParameterBlock

set

​(double d,
int index)

Replaces an Object in the list of parameters with a Double.

ParameterBlock

set

​(float f,
int index)

Replaces an Object in the list of parameters with a Float.

ParameterBlock

set

​(int i,
int index)

Replaces an Object in the list of parameters with an Integer.

ParameterBlock

set

​(long l,
int index)

Replaces an Object in the list of parameters with a Long.

ParameterBlock

set

​(short s,
int index)

Replaces an Object in the list of parameters with a Short.

ParameterBlock

set

​(

Object

obj,
int index)

Replaces an Object in the list of parameters.

void

setParameters

​(

Vector

<

Object

> parameters)

Sets the entire Vector of parameters to a given Vector.

ParameterBlock

setSource

​(

Object

source,
int index)

Replaces an entry in the list of source with a new source.

void

setSources

​(

Vector

<

Object

> sources)

Sets the entire Vector of sources to a given Vector.

Object

shallowClone

()

Creates a shallow copy of a

ParameterBlock

.

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

Adds a Byte to the list of parameters.

Adds a Character to the list of parameters.

Adds a Double to the list of parameters.

Adds a Float to the list of parameters.

Adds a Integer to the list of parameters.

Adds a Long to the list of parameters.

Adds a Short to the list of parameters.

Adds an object to the list of parameters.

Adds an image to end of the list of sources.

Creates a copy of a

ParameterBlock

.

A convenience method to return a parameter as a byte.

A convenience method to return a parameter as a char.

A convenience method to return a parameter as a double.

A convenience method to return a parameter as a float.

A convenience method to return a parameter as an int.

A convenience method to return a parameter as a long.

Returns the number of parameters (not including source images).

Returns the number of source images.

Gets a parameter as an object.

Returns an array of Class objects describing the types
of the parameters.

Returns the entire Vector of parameters.

Returns a source as a RenderableImage.

Returns a source as a

RenderedImage

.

A convenience method to return a parameter as a short.

Returns a source as a general Object.

Returns the entire Vector of sources.

Clears the list of parameters.

Clears the list of source images.

Replaces an Object in the list of parameters with a Byte.

Replaces an Object in the list of parameters with a Character.

Replaces an Object in the list of parameters with a Double.

Replaces an Object in the list of parameters with a Float.

Replaces an Object in the list of parameters with an Integer.

Replaces an Object in the list of parameters with a Long.

Replaces an Object in the list of parameters with a Short.

Replaces an Object in the list of parameters.

Sets the entire Vector of parameters to a given Vector.

Replaces an entry in the list of source with a new source.

Sets the entire Vector of sources to a given Vector.

Creates a shallow copy of a

ParameterBlock

.

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

============ FIELD DETAIL ===========

- Field Detail

- sources

```java
protected
Vector
<
Object
> sources
```

A Vector of sources, stored as arbitrary Objects.

- parameters

```java
protected
Vector
<
Object
> parameters
```

A Vector of non-source parameters, stored as arbitrary Objects.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ParameterBlock

```java
public ParameterBlock()
```

A dummy constructor.

- ParameterBlock

```java
public ParameterBlock​(
Vector
<
Object
> sources)
```

Constructs a

ParameterBlock

with a given Vector
of sources.

**Parameters:** sources

- a

Vector

of source images

- ParameterBlock

```java
public ParameterBlock​(
Vector
<
Object
> sources,

Vector
<
Object
> parameters)
```

Constructs a

ParameterBlock

with a given Vector of sources and
Vector of parameters.

**Parameters:** sources

- a

Vector

of source images
**Parameters:** parameters

- a

Vector

of parameters to be used in the
rendering operation

============ METHOD DETAIL ==========

- Method Detail

- shallowClone

```java
public
Object
shallowClone()
```

Creates a shallow copy of a

ParameterBlock

. The source and
parameter Vectors are copied by reference -- additions or
changes will be visible to both versions.

**Returns:** an Object clone of the

ParameterBlock

.

- clone

```java
public
Object
clone()
```

Creates a copy of a

ParameterBlock

. The source and parameter
Vectors are cloned, but the actual sources and parameters are
copied by reference. This allows modifications to the order
and number of sources and parameters in the clone to be invisible
to the original

ParameterBlock

. Changes to the shared sources or
parameters themselves will still be visible.

**Overrides:** clone

in class

Object
**Returns:** an Object clone of the

ParameterBlock

.
**See Also:** Cloneable

- addSource

```java
public
ParameterBlock
addSource​(
Object
source)
```

Adds an image to end of the list of sources. The image is
stored as an object in order to allow new node types in the
future.

**Parameters:** source

- an image object to be stored in the source list.
**Returns:** a new

ParameterBlock

containing the specified

source

.

- getSource

```java
public
Object
getSource​(int index)
```

Returns a source as a general Object. The caller must cast it into
an appropriate type.

**Parameters:** index

- the index of the source to be returned.
**Returns:** an

Object

that represents the source located
at the specified index in the

sources

Vector

.
**See Also:** setSource(Object, int)

- setSource

```java
public
ParameterBlock
setSource​(
Object
source,
int index)
```

Replaces an entry in the list of source with a new source.
If the index lies beyond the current source list,
the list is extended with nulls as needed.

**Parameters:** source

- the specified source image
**Parameters:** index

- the index into the

sources

Vector

at which to
insert the specified

source
**Returns:** a new

ParameterBlock

that contains the
specified

source

at the specified

index

.
**See Also:** getSource(int)

- getRenderedSource

```java
public
RenderedImage
getRenderedSource​(int index)
```

Returns a source as a

RenderedImage

. This method is
a convenience method.
An exception will be thrown if the source is not a RenderedImage.

**Parameters:** index

- the index of the source to be returned
**Returns:** a

RenderedImage

that represents the source
image that is at the specified index in the

sources Vector

.

- getRenderableSource

```java
public
RenderableImage
getRenderableSource​(int index)
```

Returns a source as a RenderableImage. This method is a
convenience method.
An exception will be thrown if the sources is not a RenderableImage.

**Parameters:** index

- the index of the source to be returned
**Returns:** a

RenderableImage

that represents the source
image that is at the specified index in the

sources Vector

.

- getNumSources

```java
public int getNumSources()
```

Returns the number of source images.

**Returns:** the number of source images in the

sources

Vector

.

- getSources

```java
public
Vector
<
Object
> getSources()
```

Returns the entire Vector of sources.

**Returns:** the

sources Vector

.
**See Also:** setSources(Vector)

- setSources

```java
public void setSources​(
Vector
<
Object
> sources)
```

Sets the entire Vector of sources to a given Vector.

**Parameters:** sources

- the

Vector

of source images
**See Also:** getSources()

- removeSources

```java
public void removeSources()
```

Clears the list of source images.

- getNumParameters

```java
public int getNumParameters()
```

Returns the number of parameters (not including source images).

**Returns:** the number of parameters in the

parameters

Vector

.

- getParameters

```java
public
Vector
<
Object
> getParameters()
```

Returns the entire Vector of parameters.

**Returns:** the

parameters Vector

.
**See Also:** setParameters(Vector)

- setParameters

```java
public void setParameters​(
Vector
<
Object
> parameters)
```

Sets the entire Vector of parameters to a given Vector.

**Parameters:** parameters

- the specified

Vector

of
parameters
**See Also:** getParameters()

- removeParameters

```java
public void removeParameters()
```

Clears the list of parameters.

- add

```java
public
ParameterBlock
add​(
Object
obj)
```

Adds an object to the list of parameters.

**Parameters:** obj

- the

Object

to add to the

parameters Vector
**Returns:** a new

ParameterBlock

containing
the specified parameter.

- add

```java
public
ParameterBlock
add​(byte b)
```

Adds a Byte to the list of parameters.

**Parameters:** b

- the byte to add to the

parameters Vector
**Returns:** a new

ParameterBlock

containing
the specified parameter.

- add

```java
public
ParameterBlock
add​(char c)
```

Adds a Character to the list of parameters.

**Parameters:** c

- the char to add to the

parameters Vector
**Returns:** a new

ParameterBlock

containing
the specified parameter.

- add

```java
public
ParameterBlock
add​(short s)
```

Adds a Short to the list of parameters.

**Parameters:** s

- the short to add to the

parameters Vector
**Returns:** a new

ParameterBlock

containing
the specified parameter.

- add

```java
public
ParameterBlock
add​(int i)
```

Adds a Integer to the list of parameters.

**Parameters:** i

- the int to add to the

parameters Vector
**Returns:** a new

ParameterBlock

containing
the specified parameter.

- add

```java
public
ParameterBlock
add​(long l)
```

Adds a Long to the list of parameters.

**Parameters:** l

- the long to add to the

parameters Vector
**Returns:** a new

ParameterBlock

containing
the specified parameter.

- add

```java
public
ParameterBlock
add​(float f)
```

Adds a Float to the list of parameters.

**Parameters:** f

- the float to add to the

parameters Vector
**Returns:** a new

ParameterBlock

containing
the specified parameter.

- add

```java
public
ParameterBlock
add​(double d)
```

Adds a Double to the list of parameters.

**Parameters:** d

- the double to add to the

parameters Vector
**Returns:** a new

ParameterBlock

containing
the specified parameter.

- set

```java
public
ParameterBlock
set​(
Object
obj,
int index)
```

Replaces an Object in the list of parameters.
If the index lies beyond the current source list,
the list is extended with nulls as needed.

**Parameters:** obj

- the parameter that replaces the
parameter at the specified index in the

parameters Vector
**Parameters:** index

- the index of the parameter to be
replaced with the specified parameter
**Returns:** a new

ParameterBlock

containing
the specified parameter.

- set

```java
public
ParameterBlock
set​(byte b,
int index)
```

Replaces an Object in the list of parameters with a Byte.
If the index lies beyond the current source list,
the list is extended with nulls as needed.

**Parameters:** b

- the parameter that replaces the
parameter at the specified index in the

parameters Vector
**Parameters:** index

- the index of the parameter to be
replaced with the specified parameter
**Returns:** a new

ParameterBlock

containing
the specified parameter.

- set

```java
public
ParameterBlock
set​(char c,
int index)
```

Replaces an Object in the list of parameters with a Character.
If the index lies beyond the current source list,
the list is extended with nulls as needed.

**Parameters:** c

- the parameter that replaces the
parameter at the specified index in the

parameters Vector
**Parameters:** index

- the index of the parameter to be
replaced with the specified parameter
**Returns:** a new

ParameterBlock

containing
the specified parameter.

- set

```java
public
ParameterBlock
set​(short s,
int index)
```

Replaces an Object in the list of parameters with a Short.
If the index lies beyond the current source list,
the list is extended with nulls as needed.

**Parameters:** s

- the parameter that replaces the
parameter at the specified index in the

parameters Vector
**Parameters:** index

- the index of the parameter to be
replaced with the specified parameter
**Returns:** a new

ParameterBlock

containing
the specified parameter.

- set

```java
public
ParameterBlock
set​(int i,
int index)
```

Replaces an Object in the list of parameters with an Integer.
If the index lies beyond the current source list,
the list is extended with nulls as needed.

**Parameters:** i

- the parameter that replaces the
parameter at the specified index in the

parameters Vector
**Parameters:** index

- the index of the parameter to be
replaced with the specified parameter
**Returns:** a new

ParameterBlock

containing
the specified parameter.

- set

```java
public
ParameterBlock
set​(long l,
int index)
```

Replaces an Object in the list of parameters with a Long.
If the index lies beyond the current source list,
the list is extended with nulls as needed.

**Parameters:** l

- the parameter that replaces the
parameter at the specified index in the

parameters Vector
**Parameters:** index

- the index of the parameter to be
replaced with the specified parameter
**Returns:** a new

ParameterBlock

containing
the specified parameter.

- set

```java
public
ParameterBlock
set​(float f,
int index)
```

Replaces an Object in the list of parameters with a Float.
If the index lies beyond the current source list,
the list is extended with nulls as needed.

**Parameters:** f

- the parameter that replaces the
parameter at the specified index in the

parameters Vector
**Parameters:** index

- the index of the parameter to be
replaced with the specified parameter
**Returns:** a new

ParameterBlock

containing
the specified parameter.

- set

```java
public
ParameterBlock
set​(double d,
int index)
```

Replaces an Object in the list of parameters with a Double.
If the index lies beyond the current source list,
the list is extended with nulls as needed.

**Parameters:** d

- the parameter that replaces the
parameter at the specified index in the

parameters Vector
**Parameters:** index

- the index of the parameter to be
replaced with the specified parameter
**Returns:** a new

ParameterBlock

containing
the specified parameter.

- getObjectParameter

```java
public
Object
getObjectParameter​(int index)
```

Gets a parameter as an object.

**Parameters:** index

- the index of the parameter to get
**Returns:** an

Object

representing the
the parameter at the specified index
into the

parameters

Vector

.

- getByteParameter

```java
public byte getByteParameter​(int index)
```

A convenience method to return a parameter as a byte. An
exception is thrown if the parameter is

null

or not a

Byte

.

**Parameters:** index

- the index of the parameter to be returned.
**Returns:** the parameter at the specified index
as a

byte

value.
**Throws:** ClassCastException

- if the parameter at the
specified index is not a

Byte
**Throws:** NullPointerException

- if the parameter at the specified
index is

null
**Throws:** ArrayIndexOutOfBoundsException

- if

index

is negative or not less than the current size of this

ParameterBlock

object

- getCharParameter

```java
public char getCharParameter​(int index)
```

A convenience method to return a parameter as a char. An
exception is thrown if the parameter is

null

or not a

Character

.

**Parameters:** index

- the index of the parameter to be returned.
**Returns:** the parameter at the specified index
as a

char

value.
**Throws:** ClassCastException

- if the parameter at the
specified index is not a

Character
**Throws:** NullPointerException

- if the parameter at the specified
index is

null
**Throws:** ArrayIndexOutOfBoundsException

- if

index

is negative or not less than the current size of this

ParameterBlock

object

- getShortParameter

```java
public short getShortParameter​(int index)
```

A convenience method to return a parameter as a short. An
exception is thrown if the parameter is

null

or not a

Short

.

**Parameters:** index

- the index of the parameter to be returned.
**Returns:** the parameter at the specified index
as a

short

value.
**Throws:** ClassCastException

- if the parameter at the
specified index is not a

Short
**Throws:** NullPointerException

- if the parameter at the specified
index is

null
**Throws:** ArrayIndexOutOfBoundsException

- if

index

is negative or not less than the current size of this

ParameterBlock

object

- getIntParameter

```java
public int getIntParameter​(int index)
```

A convenience method to return a parameter as an int. An
exception is thrown if the parameter is

null

or not an

Integer

.

**Parameters:** index

- the index of the parameter to be returned.
**Returns:** the parameter at the specified index
as an

int

value.
**Throws:** ClassCastException

- if the parameter at the
specified index is not an

Integer
**Throws:** NullPointerException

- if the parameter at the specified
index is

null
**Throws:** ArrayIndexOutOfBoundsException

- if

index

is negative or not less than the current size of this

ParameterBlock

object

- getLongParameter

```java
public long getLongParameter​(int index)
```

A convenience method to return a parameter as a long. An
exception is thrown if the parameter is

null

or not a

Long

.

**Parameters:** index

- the index of the parameter to be returned.
**Returns:** the parameter at the specified index
as a

long

value.
**Throws:** ClassCastException

- if the parameter at the
specified index is not a

Long
**Throws:** NullPointerException

- if the parameter at the specified
index is

null
**Throws:** ArrayIndexOutOfBoundsException

- if

index

is negative or not less than the current size of this

ParameterBlock

object

- getFloatParameter

```java
public float getFloatParameter​(int index)
```

A convenience method to return a parameter as a float. An
exception is thrown if the parameter is

null

or not a

Float

.

**Parameters:** index

- the index of the parameter to be returned.
**Returns:** the parameter at the specified index
as a

float

value.
**Throws:** ClassCastException

- if the parameter at the
specified index is not a

Float
**Throws:** NullPointerException

- if the parameter at the specified
index is

null
**Throws:** ArrayIndexOutOfBoundsException

- if

index

is negative or not less than the current size of this

ParameterBlock

object

- getDoubleParameter

```java
public double getDoubleParameter​(int index)
```

A convenience method to return a parameter as a double. An
exception is thrown if the parameter is

null

or not a

Double

.

**Parameters:** index

- the index of the parameter to be returned.
**Returns:** the parameter at the specified index
as a

double

value.
**Throws:** ClassCastException

- if the parameter at the
specified index is not a

Double
**Throws:** NullPointerException

- if the parameter at the specified
index is

null
**Throws:** ArrayIndexOutOfBoundsException

- if

index

is negative or not less than the current size of this

ParameterBlock

object

- getParamClasses

```java
public
Class
<?>[] getParamClasses()
```

Returns an array of Class objects describing the types
of the parameters.

**Returns:** an array of

Class

objects.

Field Detail

- sources

```java
protected
Vector
<
Object
> sources
```

A Vector of sources, stored as arbitrary Objects.

- parameters

```java
protected
Vector
<
Object
> parameters
```

A Vector of non-source parameters, stored as arbitrary Objects.

---

#### Field Detail

sources

```java
protected
Vector
<
Object
> sources
```

A Vector of sources, stored as arbitrary Objects.

---

#### sources

protected

Vector

<

Object

> sources

A Vector of sources, stored as arbitrary Objects.

parameters

```java
protected
Vector
<
Object
> parameters
```

A Vector of non-source parameters, stored as arbitrary Objects.

---

#### parameters

protected

Vector

<

Object

> parameters

A Vector of non-source parameters, stored as arbitrary Objects.

Constructor Detail

- ParameterBlock

```java
public ParameterBlock()
```

A dummy constructor.

- ParameterBlock

```java
public ParameterBlock​(
Vector
<
Object
> sources)
```

Constructs a

ParameterBlock

with a given Vector
of sources.

**Parameters:** sources

- a

Vector

of source images

- ParameterBlock

```java
public ParameterBlock​(
Vector
<
Object
> sources,

Vector
<
Object
> parameters)
```

Constructs a

ParameterBlock

with a given Vector of sources and
Vector of parameters.

**Parameters:** sources

- a

Vector

of source images
**Parameters:** parameters

- a

Vector

of parameters to be used in the
rendering operation

---

#### Constructor Detail

ParameterBlock

```java
public ParameterBlock()
```

A dummy constructor.

---

#### ParameterBlock

public ParameterBlock()

A dummy constructor.

ParameterBlock

```java
public ParameterBlock​(
Vector
<
Object
> sources)
```

Constructs a

ParameterBlock

with a given Vector
of sources.

**Parameters:** sources

- a

Vector

of source images

---

#### ParameterBlock

public ParameterBlock​(

Vector

<

Object

> sources)

Constructs a

ParameterBlock

with a given Vector
of sources.

ParameterBlock

```java
public ParameterBlock​(
Vector
<
Object
> sources,

Vector
<
Object
> parameters)
```

Constructs a

ParameterBlock

with a given Vector of sources and
Vector of parameters.

**Parameters:** sources

- a

Vector

of source images
**Parameters:** parameters

- a

Vector

of parameters to be used in the
rendering operation

---

#### ParameterBlock

public ParameterBlock​(

Vector

<

Object

> sources,

Vector

<

Object

> parameters)

Constructs a

ParameterBlock

with a given Vector of sources and
Vector of parameters.

Method Detail

- shallowClone

```java
public
Object
shallowClone()
```

Creates a shallow copy of a

ParameterBlock

. The source and
parameter Vectors are copied by reference -- additions or
changes will be visible to both versions.

**Returns:** an Object clone of the

ParameterBlock

.

- clone

```java
public
Object
clone()
```

Creates a copy of a

ParameterBlock

. The source and parameter
Vectors are cloned, but the actual sources and parameters are
copied by reference. This allows modifications to the order
and number of sources and parameters in the clone to be invisible
to the original

ParameterBlock

. Changes to the shared sources or
parameters themselves will still be visible.

**Overrides:** clone

in class

Object
**Returns:** an Object clone of the

ParameterBlock

.
**See Also:** Cloneable

- addSource

```java
public
ParameterBlock
addSource​(
Object
source)
```

Adds an image to end of the list of sources. The image is
stored as an object in order to allow new node types in the
future.

**Parameters:** source

- an image object to be stored in the source list.
**Returns:** a new

ParameterBlock

containing the specified

source

.

- getSource

```java
public
Object
getSource​(int index)
```

Returns a source as a general Object. The caller must cast it into
an appropriate type.

**Parameters:** index

- the index of the source to be returned.
**Returns:** an

Object

that represents the source located
at the specified index in the

sources

Vector

.
**See Also:** setSource(Object, int)

- setSource

```java
public
ParameterBlock
setSource​(
Object
source,
int index)
```

Replaces an entry in the list of source with a new source.
If the index lies beyond the current source list,
the list is extended with nulls as needed.

**Parameters:** source

- the specified source image
**Parameters:** index

- the index into the

sources

Vector

at which to
insert the specified

source
**Returns:** a new

ParameterBlock

that contains the
specified

source

at the specified

index

.
**See Also:** getSource(int)

- getRenderedSource

```java
public
RenderedImage
getRenderedSource​(int index)
```

Returns a source as a

RenderedImage

. This method is
a convenience method.
An exception will be thrown if the source is not a RenderedImage.

**Parameters:** index

- the index of the source to be returned
**Returns:** a

RenderedImage

that represents the source
image that is at the specified index in the

sources Vector

.

- getRenderableSource

```java
public
RenderableImage
getRenderableSource​(int index)
```

Returns a source as a RenderableImage. This method is a
convenience method.
An exception will be thrown if the sources is not a RenderableImage.

**Parameters:** index

- the index of the source to be returned
**Returns:** a

RenderableImage

that represents the source
image that is at the specified index in the

sources Vector

.

- getNumSources

```java
public int getNumSources()
```

Returns the number of source images.

**Returns:** the number of source images in the

sources

Vector

.

- getSources

```java
public
Vector
<
Object
> getSources()
```

Returns the entire Vector of sources.

**Returns:** the

sources Vector

.
**See Also:** setSources(Vector)

- setSources

```java
public void setSources​(
Vector
<
Object
> sources)
```

Sets the entire Vector of sources to a given Vector.

**Parameters:** sources

- the

Vector

of source images
**See Also:** getSources()

- removeSources

```java
public void removeSources()
```

Clears the list of source images.

- getNumParameters

```java
public int getNumParameters()
```

Returns the number of parameters (not including source images).

**Returns:** the number of parameters in the

parameters

Vector

.

- getParameters

```java
public
Vector
<
Object
> getParameters()
```

Returns the entire Vector of parameters.

**Returns:** the

parameters Vector

.
**See Also:** setParameters(Vector)

- setParameters

```java
public void setParameters​(
Vector
<
Object
> parameters)
```

Sets the entire Vector of parameters to a given Vector.

**Parameters:** parameters

- the specified

Vector

of
parameters
**See Also:** getParameters()

- removeParameters

```java
public void removeParameters()
```

Clears the list of parameters.

- add

```java
public
ParameterBlock
add​(
Object
obj)
```

Adds an object to the list of parameters.

**Parameters:** obj

- the

Object

to add to the

parameters Vector
**Returns:** a new

ParameterBlock

containing
the specified parameter.

- add

```java
public
ParameterBlock
add​(byte b)
```

Adds a Byte to the list of parameters.

**Parameters:** b

- the byte to add to the

parameters Vector
**Returns:** a new

ParameterBlock

containing
the specified parameter.

- add

```java
public
ParameterBlock
add​(char c)
```

Adds a Character to the list of parameters.

**Parameters:** c

- the char to add to the

parameters Vector
**Returns:** a new

ParameterBlock

containing
the specified parameter.

- add

```java
public
ParameterBlock
add​(short s)
```

Adds a Short to the list of parameters.

**Parameters:** s

- the short to add to the

parameters Vector
**Returns:** a new

ParameterBlock

containing
the specified parameter.

- add

```java
public
ParameterBlock
add​(int i)
```

Adds a Integer to the list of parameters.

**Parameters:** i

- the int to add to the

parameters Vector
**Returns:** a new

ParameterBlock

containing
the specified parameter.

- add

```java
public
ParameterBlock
add​(long l)
```

Adds a Long to the list of parameters.

**Parameters:** l

- the long to add to the

parameters Vector
**Returns:** a new

ParameterBlock

containing
the specified parameter.

- add

```java
public
ParameterBlock
add​(float f)
```

Adds a Float to the list of parameters.

**Parameters:** f

- the float to add to the

parameters Vector
**Returns:** a new

ParameterBlock

containing
the specified parameter.

- add

```java
public
ParameterBlock
add​(double d)
```

Adds a Double to the list of parameters.

**Parameters:** d

- the double to add to the

parameters Vector
**Returns:** a new

ParameterBlock

containing
the specified parameter.

- set

```java
public
ParameterBlock
set​(
Object
obj,
int index)
```

Replaces an Object in the list of parameters.
If the index lies beyond the current source list,
the list is extended with nulls as needed.

**Parameters:** obj

- the parameter that replaces the
parameter at the specified index in the

parameters Vector
**Parameters:** index

- the index of the parameter to be
replaced with the specified parameter
**Returns:** a new

ParameterBlock

containing
the specified parameter.

- set

```java
public
ParameterBlock
set​(byte b,
int index)
```

Replaces an Object in the list of parameters with a Byte.
If the index lies beyond the current source list,
the list is extended with nulls as needed.

**Parameters:** b

- the parameter that replaces the
parameter at the specified index in the

parameters Vector
**Parameters:** index

- the index of the parameter to be
replaced with the specified parameter
**Returns:** a new

ParameterBlock

containing
the specified parameter.

- set

```java
public
ParameterBlock
set​(char c,
int index)
```

Replaces an Object in the list of parameters with a Character.
If the index lies beyond the current source list,
the list is extended with nulls as needed.

**Parameters:** c

- the parameter that replaces the
parameter at the specified index in the

parameters Vector
**Parameters:** index

- the index of the parameter to be
replaced with the specified parameter
**Returns:** a new

ParameterBlock

containing
the specified parameter.

- set

```java
public
ParameterBlock
set​(short s,
int index)
```

Replaces an Object in the list of parameters with a Short.
If the index lies beyond the current source list,
the list is extended with nulls as needed.

**Parameters:** s

- the parameter that replaces the
parameter at the specified index in the

parameters Vector
**Parameters:** index

- the index of the parameter to be
replaced with the specified parameter
**Returns:** a new

ParameterBlock

containing
the specified parameter.

- set

```java
public
ParameterBlock
set​(int i,
int index)
```

Replaces an Object in the list of parameters with an Integer.
If the index lies beyond the current source list,
the list is extended with nulls as needed.

**Parameters:** i

- the parameter that replaces the
parameter at the specified index in the

parameters Vector
**Parameters:** index

- the index of the parameter to be
replaced with the specified parameter
**Returns:** a new

ParameterBlock

containing
the specified parameter.

- set

```java
public
ParameterBlock
set​(long l,
int index)
```

Replaces an Object in the list of parameters with a Long.
If the index lies beyond the current source list,
the list is extended with nulls as needed.

**Parameters:** l

- the parameter that replaces the
parameter at the specified index in the

parameters Vector
**Parameters:** index

- the index of the parameter to be
replaced with the specified parameter
**Returns:** a new

ParameterBlock

containing
the specified parameter.

- set

```java
public
ParameterBlock
set​(float f,
int index)
```

Replaces an Object in the list of parameters with a Float.
If the index lies beyond the current source list,
the list is extended with nulls as needed.

**Parameters:** f

- the parameter that replaces the
parameter at the specified index in the

parameters Vector
**Parameters:** index

- the index of the parameter to be
replaced with the specified parameter
**Returns:** a new

ParameterBlock

containing
the specified parameter.

- set

```java
public
ParameterBlock
set​(double d,
int index)
```

Replaces an Object in the list of parameters with a Double.
If the index lies beyond the current source list,
the list is extended with nulls as needed.

**Parameters:** d

- the parameter that replaces the
parameter at the specified index in the

parameters Vector
**Parameters:** index

- the index of the parameter to be
replaced with the specified parameter
**Returns:** a new

ParameterBlock

containing
the specified parameter.

- getObjectParameter

```java
public
Object
getObjectParameter​(int index)
```

Gets a parameter as an object.

**Parameters:** index

- the index of the parameter to get
**Returns:** an

Object

representing the
the parameter at the specified index
into the

parameters

Vector

.

- getByteParameter

```java
public byte getByteParameter​(int index)
```

A convenience method to return a parameter as a byte. An
exception is thrown if the parameter is

null

or not a

Byte

.

**Parameters:** index

- the index of the parameter to be returned.
**Returns:** the parameter at the specified index
as a

byte

value.
**Throws:** ClassCastException

- if the parameter at the
specified index is not a

Byte
**Throws:** NullPointerException

- if the parameter at the specified
index is

null
**Throws:** ArrayIndexOutOfBoundsException

- if

index

is negative or not less than the current size of this

ParameterBlock

object

- getCharParameter

```java
public char getCharParameter​(int index)
```

A convenience method to return a parameter as a char. An
exception is thrown if the parameter is

null

or not a

Character

.

**Parameters:** index

- the index of the parameter to be returned.
**Returns:** the parameter at the specified index
as a

char

value.
**Throws:** ClassCastException

- if the parameter at the
specified index is not a

Character
**Throws:** NullPointerException

- if the parameter at the specified
index is

null
**Throws:** ArrayIndexOutOfBoundsException

- if

index

is negative or not less than the current size of this

ParameterBlock

object

- getShortParameter

```java
public short getShortParameter​(int index)
```

A convenience method to return a parameter as a short. An
exception is thrown if the parameter is

null

or not a

Short

.

**Parameters:** index

- the index of the parameter to be returned.
**Returns:** the parameter at the specified index
as a

short

value.
**Throws:** ClassCastException

- if the parameter at the
specified index is not a

Short
**Throws:** NullPointerException

- if the parameter at the specified
index is

null
**Throws:** ArrayIndexOutOfBoundsException

- if

index

is negative or not less than the current size of this

ParameterBlock

object

- getIntParameter

```java
public int getIntParameter​(int index)
```

A convenience method to return a parameter as an int. An
exception is thrown if the parameter is

null

or not an

Integer

.

**Parameters:** index

- the index of the parameter to be returned.
**Returns:** the parameter at the specified index
as an

int

value.
**Throws:** ClassCastException

- if the parameter at the
specified index is not an

Integer
**Throws:** NullPointerException

- if the parameter at the specified
index is

null
**Throws:** ArrayIndexOutOfBoundsException

- if

index

is negative or not less than the current size of this

ParameterBlock

object

- getLongParameter

```java
public long getLongParameter​(int index)
```

A convenience method to return a parameter as a long. An
exception is thrown if the parameter is

null

or not a

Long

.

**Parameters:** index

- the index of the parameter to be returned.
**Returns:** the parameter at the specified index
as a

long

value.
**Throws:** ClassCastException

- if the parameter at the
specified index is not a

Long
**Throws:** NullPointerException

- if the parameter at the specified
index is

null
**Throws:** ArrayIndexOutOfBoundsException

- if

index

is negative or not less than the current size of this

ParameterBlock

object

- getFloatParameter

```java
public float getFloatParameter​(int index)
```

A convenience method to return a parameter as a float. An
exception is thrown if the parameter is

null

or not a

Float

.

**Parameters:** index

- the index of the parameter to be returned.
**Returns:** the parameter at the specified index
as a

float

value.
**Throws:** ClassCastException

- if the parameter at the
specified index is not a

Float
**Throws:** NullPointerException

- if the parameter at the specified
index is

null
**Throws:** ArrayIndexOutOfBoundsException

- if

index

is negative or not less than the current size of this

ParameterBlock

object

- getDoubleParameter

```java
public double getDoubleParameter​(int index)
```

A convenience method to return a parameter as a double. An
exception is thrown if the parameter is

null

or not a

Double

.

**Parameters:** index

- the index of the parameter to be returned.
**Returns:** the parameter at the specified index
as a

double

value.
**Throws:** ClassCastException

- if the parameter at the
specified index is not a

Double
**Throws:** NullPointerException

- if the parameter at the specified
index is

null
**Throws:** ArrayIndexOutOfBoundsException

- if

index

is negative or not less than the current size of this

ParameterBlock

object

- getParamClasses

```java
public
Class
<?>[] getParamClasses()
```

Returns an array of Class objects describing the types
of the parameters.

**Returns:** an array of

Class

objects.

---

#### Method Detail

shallowClone

```java
public
Object
shallowClone()
```

Creates a shallow copy of a

ParameterBlock

. The source and
parameter Vectors are copied by reference -- additions or
changes will be visible to both versions.

**Returns:** an Object clone of the

ParameterBlock

.

---

#### shallowClone

public

Object

shallowClone()

Creates a shallow copy of a

ParameterBlock

. The source and
parameter Vectors are copied by reference -- additions or
changes will be visible to both versions.

clone

```java
public
Object
clone()
```

Creates a copy of a

ParameterBlock

. The source and parameter
Vectors are cloned, but the actual sources and parameters are
copied by reference. This allows modifications to the order
and number of sources and parameters in the clone to be invisible
to the original

ParameterBlock

. Changes to the shared sources or
parameters themselves will still be visible.

**Overrides:** clone

in class

Object
**Returns:** an Object clone of the

ParameterBlock

.
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Creates a copy of a

ParameterBlock

. The source and parameter
Vectors are cloned, but the actual sources and parameters are
copied by reference. This allows modifications to the order
and number of sources and parameters in the clone to be invisible
to the original

ParameterBlock

. Changes to the shared sources or
parameters themselves will still be visible.

addSource

```java
public
ParameterBlock
addSource​(
Object
source)
```

Adds an image to end of the list of sources. The image is
stored as an object in order to allow new node types in the
future.

**Parameters:** source

- an image object to be stored in the source list.
**Returns:** a new

ParameterBlock

containing the specified

source

.

---

#### addSource

public

ParameterBlock

addSource​(

Object

source)

Adds an image to end of the list of sources. The image is
stored as an object in order to allow new node types in the
future.

getSource

```java
public
Object
getSource​(int index)
```

Returns a source as a general Object. The caller must cast it into
an appropriate type.

**Parameters:** index

- the index of the source to be returned.
**Returns:** an

Object

that represents the source located
at the specified index in the

sources

Vector

.
**See Also:** setSource(Object, int)

---

#### getSource

public

Object

getSource​(int index)

Returns a source as a general Object. The caller must cast it into
an appropriate type.

setSource

```java
public
ParameterBlock
setSource​(
Object
source,
int index)
```

Replaces an entry in the list of source with a new source.
If the index lies beyond the current source list,
the list is extended with nulls as needed.

**Parameters:** source

- the specified source image
**Parameters:** index

- the index into the

sources

Vector

at which to
insert the specified

source
**Returns:** a new

ParameterBlock

that contains the
specified

source

at the specified

index

.
**See Also:** getSource(int)

---

#### setSource

public

ParameterBlock

setSource​(

Object

source,
int index)

Replaces an entry in the list of source with a new source.
If the index lies beyond the current source list,
the list is extended with nulls as needed.

getRenderedSource

```java
public
RenderedImage
getRenderedSource​(int index)
```

Returns a source as a

RenderedImage

. This method is
a convenience method.
An exception will be thrown if the source is not a RenderedImage.

**Parameters:** index

- the index of the source to be returned
**Returns:** a

RenderedImage

that represents the source
image that is at the specified index in the

sources Vector

.

---

#### getRenderedSource

public

RenderedImage

getRenderedSource​(int index)

Returns a source as a

RenderedImage

. This method is
a convenience method.
An exception will be thrown if the source is not a RenderedImage.

getRenderableSource

```java
public
RenderableImage
getRenderableSource​(int index)
```

Returns a source as a RenderableImage. This method is a
convenience method.
An exception will be thrown if the sources is not a RenderableImage.

**Parameters:** index

- the index of the source to be returned
**Returns:** a

RenderableImage

that represents the source
image that is at the specified index in the

sources Vector

.

---

#### getRenderableSource

public

RenderableImage

getRenderableSource​(int index)

Returns a source as a RenderableImage. This method is a
convenience method.
An exception will be thrown if the sources is not a RenderableImage.

getNumSources

```java
public int getNumSources()
```

Returns the number of source images.

**Returns:** the number of source images in the

sources

Vector

.

---

#### getNumSources

public int getNumSources()

Returns the number of source images.

getSources

```java
public
Vector
<
Object
> getSources()
```

Returns the entire Vector of sources.

**Returns:** the

sources Vector

.
**See Also:** setSources(Vector)

---

#### getSources

public

Vector

<

Object

> getSources()

Returns the entire Vector of sources.

setSources

```java
public void setSources​(
Vector
<
Object
> sources)
```

Sets the entire Vector of sources to a given Vector.

**Parameters:** sources

- the

Vector

of source images
**See Also:** getSources()

---

#### setSources

public void setSources​(

Vector

<

Object

> sources)

Sets the entire Vector of sources to a given Vector.

removeSources

```java
public void removeSources()
```

Clears the list of source images.

---

#### removeSources

public void removeSources()

Clears the list of source images.

getNumParameters

```java
public int getNumParameters()
```

Returns the number of parameters (not including source images).

**Returns:** the number of parameters in the

parameters

Vector

.

---

#### getNumParameters

public int getNumParameters()

Returns the number of parameters (not including source images).

getParameters

```java
public
Vector
<
Object
> getParameters()
```

Returns the entire Vector of parameters.

**Returns:** the

parameters Vector

.
**See Also:** setParameters(Vector)

---

#### getParameters

public

Vector

<

Object

> getParameters()

Returns the entire Vector of parameters.

setParameters

```java
public void setParameters​(
Vector
<
Object
> parameters)
```

Sets the entire Vector of parameters to a given Vector.

**Parameters:** parameters

- the specified

Vector

of
parameters
**See Also:** getParameters()

---

#### setParameters

public void setParameters​(

Vector

<

Object

> parameters)

Sets the entire Vector of parameters to a given Vector.

removeParameters

```java
public void removeParameters()
```

Clears the list of parameters.

---

#### removeParameters

public void removeParameters()

Clears the list of parameters.

add

```java
public
ParameterBlock
add​(
Object
obj)
```

Adds an object to the list of parameters.

**Parameters:** obj

- the

Object

to add to the

parameters Vector
**Returns:** a new

ParameterBlock

containing
the specified parameter.

---

#### add

public

ParameterBlock

add​(

Object

obj)

Adds an object to the list of parameters.

add

```java
public
ParameterBlock
add​(byte b)
```

Adds a Byte to the list of parameters.

**Parameters:** b

- the byte to add to the

parameters Vector
**Returns:** a new

ParameterBlock

containing
the specified parameter.

---

#### add

public

ParameterBlock

add​(byte b)

Adds a Byte to the list of parameters.

add

```java
public
ParameterBlock
add​(char c)
```

Adds a Character to the list of parameters.

**Parameters:** c

- the char to add to the

parameters Vector
**Returns:** a new

ParameterBlock

containing
the specified parameter.

---

#### add

public

ParameterBlock

add​(char c)

Adds a Character to the list of parameters.

add

```java
public
ParameterBlock
add​(short s)
```

Adds a Short to the list of parameters.

**Parameters:** s

- the short to add to the

parameters Vector
**Returns:** a new

ParameterBlock

containing
the specified parameter.

---

#### add

public

ParameterBlock

add​(short s)

Adds a Short to the list of parameters.

add

```java
public
ParameterBlock
add​(int i)
```

Adds a Integer to the list of parameters.

**Parameters:** i

- the int to add to the

parameters Vector
**Returns:** a new

ParameterBlock

containing
the specified parameter.

---

#### add

public

ParameterBlock

add​(int i)

Adds a Integer to the list of parameters.

add

```java
public
ParameterBlock
add​(long l)
```

Adds a Long to the list of parameters.

**Parameters:** l

- the long to add to the

parameters Vector
**Returns:** a new

ParameterBlock

containing
the specified parameter.

---

#### add

public

ParameterBlock

add​(long l)

Adds a Long to the list of parameters.

add

```java
public
ParameterBlock
add​(float f)
```

Adds a Float to the list of parameters.

**Parameters:** f

- the float to add to the

parameters Vector
**Returns:** a new

ParameterBlock

containing
the specified parameter.

---

#### add

public

ParameterBlock

add​(float f)

Adds a Float to the list of parameters.

add

```java
public
ParameterBlock
add​(double d)
```

Adds a Double to the list of parameters.

**Parameters:** d

- the double to add to the

parameters Vector
**Returns:** a new

ParameterBlock

containing
the specified parameter.

---

#### add

public

ParameterBlock

add​(double d)

Adds a Double to the list of parameters.

set

```java
public
ParameterBlock
set​(
Object
obj,
int index)
```

Replaces an Object in the list of parameters.
If the index lies beyond the current source list,
the list is extended with nulls as needed.

**Parameters:** obj

- the parameter that replaces the
parameter at the specified index in the

parameters Vector
**Parameters:** index

- the index of the parameter to be
replaced with the specified parameter
**Returns:** a new

ParameterBlock

containing
the specified parameter.

---

#### set

public

ParameterBlock

set​(

Object

obj,
int index)

Replaces an Object in the list of parameters.
If the index lies beyond the current source list,
the list is extended with nulls as needed.

set

```java
public
ParameterBlock
set​(byte b,
int index)
```

Replaces an Object in the list of parameters with a Byte.
If the index lies beyond the current source list,
the list is extended with nulls as needed.

**Parameters:** b

- the parameter that replaces the
parameter at the specified index in the

parameters Vector
**Parameters:** index

- the index of the parameter to be
replaced with the specified parameter
**Returns:** a new

ParameterBlock

containing
the specified parameter.

---

#### set

public

ParameterBlock

set​(byte b,
int index)

Replaces an Object in the list of parameters with a Byte.
If the index lies beyond the current source list,
the list is extended with nulls as needed.

set

```java
public
ParameterBlock
set​(char c,
int index)
```

Replaces an Object in the list of parameters with a Character.
If the index lies beyond the current source list,
the list is extended with nulls as needed.

**Parameters:** c

- the parameter that replaces the
parameter at the specified index in the

parameters Vector
**Parameters:** index

- the index of the parameter to be
replaced with the specified parameter
**Returns:** a new

ParameterBlock

containing
the specified parameter.

---

#### set

public

ParameterBlock

set​(char c,
int index)

Replaces an Object in the list of parameters with a Character.
If the index lies beyond the current source list,
the list is extended with nulls as needed.

set

```java
public
ParameterBlock
set​(short s,
int index)
```

Replaces an Object in the list of parameters with a Short.
If the index lies beyond the current source list,
the list is extended with nulls as needed.

**Parameters:** s

- the parameter that replaces the
parameter at the specified index in the

parameters Vector
**Parameters:** index

- the index of the parameter to be
replaced with the specified parameter
**Returns:** a new

ParameterBlock

containing
the specified parameter.

---

#### set

public

ParameterBlock

set​(short s,
int index)

Replaces an Object in the list of parameters with a Short.
If the index lies beyond the current source list,
the list is extended with nulls as needed.

set

```java
public
ParameterBlock
set​(int i,
int index)
```

Replaces an Object in the list of parameters with an Integer.
If the index lies beyond the current source list,
the list is extended with nulls as needed.

**Parameters:** i

- the parameter that replaces the
parameter at the specified index in the

parameters Vector
**Parameters:** index

- the index of the parameter to be
replaced with the specified parameter
**Returns:** a new

ParameterBlock

containing
the specified parameter.

---

#### set

public

ParameterBlock

set​(int i,
int index)

Replaces an Object in the list of parameters with an Integer.
If the index lies beyond the current source list,
the list is extended with nulls as needed.

set

```java
public
ParameterBlock
set​(long l,
int index)
```

Replaces an Object in the list of parameters with a Long.
If the index lies beyond the current source list,
the list is extended with nulls as needed.

**Parameters:** l

- the parameter that replaces the
parameter at the specified index in the

parameters Vector
**Parameters:** index

- the index of the parameter to be
replaced with the specified parameter
**Returns:** a new

ParameterBlock

containing
the specified parameter.

---

#### set

public

ParameterBlock

set​(long l,
int index)

Replaces an Object in the list of parameters with a Long.
If the index lies beyond the current source list,
the list is extended with nulls as needed.

set

```java
public
ParameterBlock
set​(float f,
int index)
```

Replaces an Object in the list of parameters with a Float.
If the index lies beyond the current source list,
the list is extended with nulls as needed.

**Parameters:** f

- the parameter that replaces the
parameter at the specified index in the

parameters Vector
**Parameters:** index

- the index of the parameter to be
replaced with the specified parameter
**Returns:** a new

ParameterBlock

containing
the specified parameter.

---

#### set

public

ParameterBlock

set​(float f,
int index)

Replaces an Object in the list of parameters with a Float.
If the index lies beyond the current source list,
the list is extended with nulls as needed.

set

```java
public
ParameterBlock
set​(double d,
int index)
```

Replaces an Object in the list of parameters with a Double.
If the index lies beyond the current source list,
the list is extended with nulls as needed.

**Parameters:** d

- the parameter that replaces the
parameter at the specified index in the

parameters Vector
**Parameters:** index

- the index of the parameter to be
replaced with the specified parameter
**Returns:** a new

ParameterBlock

containing
the specified parameter.

---

#### set

public

ParameterBlock

set​(double d,
int index)

Replaces an Object in the list of parameters with a Double.
If the index lies beyond the current source list,
the list is extended with nulls as needed.

getObjectParameter

```java
public
Object
getObjectParameter​(int index)
```

Gets a parameter as an object.

**Parameters:** index

- the index of the parameter to get
**Returns:** an

Object

representing the
the parameter at the specified index
into the

parameters

Vector

.

---

#### getObjectParameter

public

Object

getObjectParameter​(int index)

Gets a parameter as an object.

getByteParameter

```java
public byte getByteParameter​(int index)
```

A convenience method to return a parameter as a byte. An
exception is thrown if the parameter is

null

or not a

Byte

.

**Parameters:** index

- the index of the parameter to be returned.
**Returns:** the parameter at the specified index
as a

byte

value.
**Throws:** ClassCastException

- if the parameter at the
specified index is not a

Byte
**Throws:** NullPointerException

- if the parameter at the specified
index is

null
**Throws:** ArrayIndexOutOfBoundsException

- if

index

is negative or not less than the current size of this

ParameterBlock

object

---

#### getByteParameter

public byte getByteParameter​(int index)

A convenience method to return a parameter as a byte. An
exception is thrown if the parameter is

null

or not a

Byte

.

getCharParameter

```java
public char getCharParameter​(int index)
```

A convenience method to return a parameter as a char. An
exception is thrown if the parameter is

null

or not a

Character

.

**Parameters:** index

- the index of the parameter to be returned.
**Returns:** the parameter at the specified index
as a

char

value.
**Throws:** ClassCastException

- if the parameter at the
specified index is not a

Character
**Throws:** NullPointerException

- if the parameter at the specified
index is

null
**Throws:** ArrayIndexOutOfBoundsException

- if

index

is negative or not less than the current size of this

ParameterBlock

object

---

#### getCharParameter

public char getCharParameter​(int index)

A convenience method to return a parameter as a char. An
exception is thrown if the parameter is

null

or not a

Character

.

getShortParameter

```java
public short getShortParameter​(int index)
```

A convenience method to return a parameter as a short. An
exception is thrown if the parameter is

null

or not a

Short

.

**Parameters:** index

- the index of the parameter to be returned.
**Returns:** the parameter at the specified index
as a

short

value.
**Throws:** ClassCastException

- if the parameter at the
specified index is not a

Short
**Throws:** NullPointerException

- if the parameter at the specified
index is

null
**Throws:** ArrayIndexOutOfBoundsException

- if

index

is negative or not less than the current size of this

ParameterBlock

object

---

#### getShortParameter

public short getShortParameter​(int index)

A convenience method to return a parameter as a short. An
exception is thrown if the parameter is

null

or not a

Short

.

getIntParameter

```java
public int getIntParameter​(int index)
```

A convenience method to return a parameter as an int. An
exception is thrown if the parameter is

null

or not an

Integer

.

**Parameters:** index

- the index of the parameter to be returned.
**Returns:** the parameter at the specified index
as an

int

value.
**Throws:** ClassCastException

- if the parameter at the
specified index is not an

Integer
**Throws:** NullPointerException

- if the parameter at the specified
index is

null
**Throws:** ArrayIndexOutOfBoundsException

- if

index

is negative or not less than the current size of this

ParameterBlock

object

---

#### getIntParameter

public int getIntParameter​(int index)

A convenience method to return a parameter as an int. An
exception is thrown if the parameter is

null

or not an

Integer

.

getLongParameter

```java
public long getLongParameter​(int index)
```

A convenience method to return a parameter as a long. An
exception is thrown if the parameter is

null

or not a

Long

.

**Parameters:** index

- the index of the parameter to be returned.
**Returns:** the parameter at the specified index
as a

long

value.
**Throws:** ClassCastException

- if the parameter at the
specified index is not a

Long
**Throws:** NullPointerException

- if the parameter at the specified
index is

null
**Throws:** ArrayIndexOutOfBoundsException

- if

index

is negative or not less than the current size of this

ParameterBlock

object

---

#### getLongParameter

public long getLongParameter​(int index)

A convenience method to return a parameter as a long. An
exception is thrown if the parameter is

null

or not a

Long

.

getFloatParameter

```java
public float getFloatParameter​(int index)
```

A convenience method to return a parameter as a float. An
exception is thrown if the parameter is

null

or not a

Float

.

**Parameters:** index

- the index of the parameter to be returned.
**Returns:** the parameter at the specified index
as a

float

value.
**Throws:** ClassCastException

- if the parameter at the
specified index is not a

Float
**Throws:** NullPointerException

- if the parameter at the specified
index is

null
**Throws:** ArrayIndexOutOfBoundsException

- if

index

is negative or not less than the current size of this

ParameterBlock

object

---

#### getFloatParameter

public float getFloatParameter​(int index)

A convenience method to return a parameter as a float. An
exception is thrown if the parameter is

null

or not a

Float

.

getDoubleParameter

```java
public double getDoubleParameter​(int index)
```

A convenience method to return a parameter as a double. An
exception is thrown if the parameter is

null

or not a

Double

.

**Parameters:** index

- the index of the parameter to be returned.
**Returns:** the parameter at the specified index
as a

double

value.
**Throws:** ClassCastException

- if the parameter at the
specified index is not a

Double
**Throws:** NullPointerException

- if the parameter at the specified
index is

null
**Throws:** ArrayIndexOutOfBoundsException

- if

index

is negative or not less than the current size of this

ParameterBlock

object

---

#### getDoubleParameter

public double getDoubleParameter​(int index)

A convenience method to return a parameter as a double. An
exception is thrown if the parameter is

null

or not a

Double

.

getParamClasses

```java
public
Class
<?>[] getParamClasses()
```

Returns an array of Class objects describing the types
of the parameters.

**Returns:** an array of

Class

objects.

---

#### getParamClasses

public

Class

<?>[] getParamClasses()

Returns an array of Class objects describing the types
of the parameters.

---

