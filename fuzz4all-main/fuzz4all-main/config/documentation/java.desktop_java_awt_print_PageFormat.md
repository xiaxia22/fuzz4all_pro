# Class PageFormat

**Source:** `java.desktop\java\awt\print\PageFormat.html`

### Class Description

```java
public class
PageFormat

extends
Object

implements
Cloneable
```

The

PageFormat

class describes the size and
orientation of a page to be printed.

**All Implemented Interfaces:** Cloneable

---

### Field Details

#### @Native

public static final int LANDSCAPE

The origin is at the bottom left of the paper with
x running bottom to top and y running left to right.
Note that this is not the Macintosh landscape but
is the Window's and PostScript landscape.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int PORTRAIT

The origin is at the top left of the paper with
x running to the right and y running down the
paper.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int REVERSE_LANDSCAPE

The origin is at the top right of the paper with x
running top to bottom and y running right to left.
Note that this is the Macintosh landscape.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public PageFormat()

Creates a default, portrait-oriented

PageFormat

.

---

### Method Details

#### public
Object
clone()

Makes a copy of this

PageFormat

with the same
contents as this

PageFormat

.

**Overrides:**
- clone

in class

Object

**Returns:**
- a copy of this

PageFormat

.

**See Also:**
- Cloneable

---

#### public double getWidth()

Returns the width, in 1/72nds of an inch, of the page.
This method takes into account the orientation of the
page when determining the width.

**Returns:**
- the width of the page.

---

#### public double getHeight()

Returns the height, in 1/72nds of an inch, of the page.
This method takes into account the orientation of the
page when determining the height.

**Returns:**
- the height of the page.

---

#### public double getImageableX()

Returns the x coordinate of the upper left point of the
imageable area of the

Paper

object
associated with this

PageFormat

.
This method takes into account the
orientation of the page.

**Returns:**
- the x coordinate of the upper left point of the
imageable area of the

Paper

object
associated with this

PageFormat

.

---

#### public double getImageableY()

Returns the y coordinate of the upper left point of the
imageable area of the

Paper

object
associated with this

PageFormat

.
This method takes into account the
orientation of the page.

**Returns:**
- the y coordinate of the upper left point of the
imageable area of the

Paper

object
associated with this

PageFormat

.

---

#### public double getImageableWidth()

Returns the width, in 1/72nds of an inch, of the imageable
area of the page. This method takes into account the orientation
of the page.

**Returns:**
- the width of the page.

---

#### public double getImageableHeight()

Return the height, in 1/72nds of an inch, of the imageable
area of the page. This method takes into account the orientation
of the page.

**Returns:**
- the height of the page.

---

#### public
Paper
getPaper()

Returns a copy of the

Paper

object associated
with this

PageFormat

. Changes made to the

Paper

object returned from this method do not
affect the

Paper

object of this

PageFormat

. To update the

Paper

object of this

PageFormat

, create a new

Paper

object and set it into this

PageFormat

by using the

setPaper(Paper)

method.

**Returns:**
- a copy of the

Paper

object associated
with this

PageFormat

.

**See Also:**
- setPaper(java.awt.print.Paper)

---

#### public void setPaper​(
Paper
paper)

Sets the

Paper

object for this

PageFormat

.

**Parameters:**
- paper

- the

Paper

object to which to set
the

Paper

object for this

PageFormat

.

**Throws:**
- NullPointerException

- a null paper instance was passed as a parameter.

**See Also:**
- getPaper()

---

#### public void setOrientation​(int orientation)
throws
IllegalArgumentException

Sets the page orientation.

orientation

must be
one of the constants: PORTRAIT, LANDSCAPE,
or REVERSE_LANDSCAPE.

**Parameters:**
- orientation

- the new orientation for the page

**Throws:**
- IllegalArgumentException

- if
an unknown orientation was requested

**See Also:**
- getOrientation()

---

#### public int getOrientation()

Returns the orientation of this

PageFormat

.

**Returns:**
- this

PageFormat

object's orientation.

**See Also:**
- setOrientation(int)

---

#### public double[] getMatrix()

Returns a transformation matrix that translates user
space rendering to the requested orientation
of the page. The values are placed into the
array as
{ m00, m10, m01, m11, m02, m12} in
the form required by the

AffineTransform

constructor.

**Returns:**
- the matrix used to translate user space rendering
to the orientation of the page.

**See Also:**
- AffineTransform

---

### Additional Sections

#### Class PageFormat

java.lang.Object

- java.awt.print.PageFormat

java.awt.print.PageFormat

**All Implemented Interfaces:** Cloneable

```java
public class
PageFormat

extends
Object

implements
Cloneable
```

The

PageFormat

class describes the size and
orientation of a page to be printed.

public class

PageFormat

extends

Object

implements

Cloneable

The

PageFormat

class describes the size and
orientation of a page to be printed.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

LANDSCAPE

The origin is at the bottom left of the paper with
x running bottom to top and y running left to right.

static int

PORTRAIT

The origin is at the top left of the paper with
x running to the right and y running down the
paper.

static int

REVERSE_LANDSCAPE

The origin is at the top right of the paper with x
running top to bottom and y running right to left.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

PageFormat

()

Creates a default, portrait-oriented

PageFormat

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Makes a copy of this

PageFormat

with the same
contents as this

PageFormat

.

double

getHeight

()

Returns the height, in 1/72nds of an inch, of the page.

double

getImageableHeight

()

Return the height, in 1/72nds of an inch, of the imageable
area of the page.

double

getImageableWidth

()

Returns the width, in 1/72nds of an inch, of the imageable
area of the page.

double

getImageableX

()

Returns the x coordinate of the upper left point of the
imageable area of the

Paper

object
associated with this

PageFormat

.

double

getImageableY

()

Returns the y coordinate of the upper left point of the
imageable area of the

Paper

object
associated with this

PageFormat

.

double[]

getMatrix

()

Returns a transformation matrix that translates user
space rendering to the requested orientation
of the page.

int

getOrientation

()

Returns the orientation of this

PageFormat

.

Paper

getPaper

()

Returns a copy of the

Paper

object associated
with this

PageFormat

.

double

getWidth

()

Returns the width, in 1/72nds of an inch, of the page.

void

setOrientation

​(int orientation)

Sets the page orientation.

void

setPaper

​(

Paper

paper)

Sets the

Paper

object for this

PageFormat

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

static int

LANDSCAPE

The origin is at the bottom left of the paper with
x running bottom to top and y running left to right.

static int

PORTRAIT

The origin is at the top left of the paper with
x running to the right and y running down the
paper.

static int

REVERSE_LANDSCAPE

The origin is at the top right of the paper with x
running top to bottom and y running right to left.

---

#### Field Summary

The origin is at the bottom left of the paper with
x running bottom to top and y running left to right.

The origin is at the top left of the paper with
x running to the right and y running down the
paper.

The origin is at the top right of the paper with x
running top to bottom and y running right to left.

Constructor Summary

Constructors

Constructor

Description

PageFormat

()

Creates a default, portrait-oriented

PageFormat

.

---

#### Constructor Summary

Creates a default, portrait-oriented

PageFormat

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Makes a copy of this

PageFormat

with the same
contents as this

PageFormat

.

double

getHeight

()

Returns the height, in 1/72nds of an inch, of the page.

double

getImageableHeight

()

Return the height, in 1/72nds of an inch, of the imageable
area of the page.

double

getImageableWidth

()

Returns the width, in 1/72nds of an inch, of the imageable
area of the page.

double

getImageableX

()

Returns the x coordinate of the upper left point of the
imageable area of the

Paper

object
associated with this

PageFormat

.

double

getImageableY

()

Returns the y coordinate of the upper left point of the
imageable area of the

Paper

object
associated with this

PageFormat

.

double[]

getMatrix

()

Returns a transformation matrix that translates user
space rendering to the requested orientation
of the page.

int

getOrientation

()

Returns the orientation of this

PageFormat

.

Paper

getPaper

()

Returns a copy of the

Paper

object associated
with this

PageFormat

.

double

getWidth

()

Returns the width, in 1/72nds of an inch, of the page.

void

setOrientation

​(int orientation)

Sets the page orientation.

void

setPaper

​(

Paper

paper)

Sets the

Paper

object for this

PageFormat

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

Makes a copy of this

PageFormat

with the same
contents as this

PageFormat

.

Returns the height, in 1/72nds of an inch, of the page.

Return the height, in 1/72nds of an inch, of the imageable
area of the page.

Returns the width, in 1/72nds of an inch, of the imageable
area of the page.

Returns the x coordinate of the upper left point of the
imageable area of the

Paper

object
associated with this

PageFormat

.

Returns the y coordinate of the upper left point of the
imageable area of the

Paper

object
associated with this

PageFormat

.

Returns a transformation matrix that translates user
space rendering to the requested orientation
of the page.

Returns the orientation of this

PageFormat

.

Returns a copy of the

Paper

object associated
with this

PageFormat

.

Returns the width, in 1/72nds of an inch, of the page.

Sets the page orientation.

Sets the

Paper

object for this

PageFormat

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

- LANDSCAPE

```java
@Native

public static final int LANDSCAPE
```

The origin is at the bottom left of the paper with
x running bottom to top and y running left to right.
Note that this is not the Macintosh landscape but
is the Window's and PostScript landscape.

**See Also:** Constant Field Values

- PORTRAIT

```java
@Native

public static final int PORTRAIT
```

The origin is at the top left of the paper with
x running to the right and y running down the
paper.

**See Also:** Constant Field Values

- REVERSE_LANDSCAPE

```java
@Native

public static final int REVERSE_LANDSCAPE
```

The origin is at the top right of the paper with x
running top to bottom and y running right to left.
Note that this is the Macintosh landscape.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- PageFormat

```java
public PageFormat()
```

Creates a default, portrait-oriented

PageFormat

.

============ METHOD DETAIL ==========

- Method Detail

- clone

```java
public
Object
clone()
```

Makes a copy of this

PageFormat

with the same
contents as this

PageFormat

.

**Overrides:** clone

in class

Object
**Returns:** a copy of this

PageFormat

.
**See Also:** Cloneable

- getWidth

```java
public double getWidth()
```

Returns the width, in 1/72nds of an inch, of the page.
This method takes into account the orientation of the
page when determining the width.

**Returns:** the width of the page.

- getHeight

```java
public double getHeight()
```

Returns the height, in 1/72nds of an inch, of the page.
This method takes into account the orientation of the
page when determining the height.

**Returns:** the height of the page.

- getImageableX

```java
public double getImageableX()
```

Returns the x coordinate of the upper left point of the
imageable area of the

Paper

object
associated with this

PageFormat

.
This method takes into account the
orientation of the page.

**Returns:** the x coordinate of the upper left point of the
imageable area of the

Paper

object
associated with this

PageFormat

.

- getImageableY

```java
public double getImageableY()
```

Returns the y coordinate of the upper left point of the
imageable area of the

Paper

object
associated with this

PageFormat

.
This method takes into account the
orientation of the page.

**Returns:** the y coordinate of the upper left point of the
imageable area of the

Paper

object
associated with this

PageFormat

.

- getImageableWidth

```java
public double getImageableWidth()
```

Returns the width, in 1/72nds of an inch, of the imageable
area of the page. This method takes into account the orientation
of the page.

**Returns:** the width of the page.

- getImageableHeight

```java
public double getImageableHeight()
```

Return the height, in 1/72nds of an inch, of the imageable
area of the page. This method takes into account the orientation
of the page.

**Returns:** the height of the page.

- getPaper

```java
public
Paper
getPaper()
```

Returns a copy of the

Paper

object associated
with this

PageFormat

. Changes made to the

Paper

object returned from this method do not
affect the

Paper

object of this

PageFormat

. To update the

Paper

object of this

PageFormat

, create a new

Paper

object and set it into this

PageFormat

by using the

setPaper(Paper)

method.

**Returns:** a copy of the

Paper

object associated
with this

PageFormat

.
**See Also:** setPaper(java.awt.print.Paper)

- setPaper

```java
public void setPaper​(
Paper
paper)
```

Sets the

Paper

object for this

PageFormat

.

**Parameters:** paper

- the

Paper

object to which to set
the

Paper

object for this

PageFormat

.
**Throws:** NullPointerException

- a null paper instance was passed as a parameter.
**See Also:** getPaper()

- setOrientation

```java
public void setOrientation​(int orientation)
throws
IllegalArgumentException
```

Sets the page orientation.

orientation

must be
one of the constants: PORTRAIT, LANDSCAPE,
or REVERSE_LANDSCAPE.

**Parameters:** orientation

- the new orientation for the page
**Throws:** IllegalArgumentException

- if
an unknown orientation was requested
**See Also:** getOrientation()

- getOrientation

```java
public int getOrientation()
```

Returns the orientation of this

PageFormat

.

**Returns:** this

PageFormat

object's orientation.
**See Also:** setOrientation(int)

- getMatrix

```java
public double[] getMatrix()
```

Returns a transformation matrix that translates user
space rendering to the requested orientation
of the page. The values are placed into the
array as
{ m00, m10, m01, m11, m02, m12} in
the form required by the

AffineTransform

constructor.

**Returns:** the matrix used to translate user space rendering
to the orientation of the page.
**See Also:** AffineTransform

Field Detail

- LANDSCAPE

```java
@Native

public static final int LANDSCAPE
```

The origin is at the bottom left of the paper with
x running bottom to top and y running left to right.
Note that this is not the Macintosh landscape but
is the Window's and PostScript landscape.

**See Also:** Constant Field Values

- PORTRAIT

```java
@Native

public static final int PORTRAIT
```

The origin is at the top left of the paper with
x running to the right and y running down the
paper.

**See Also:** Constant Field Values

- REVERSE_LANDSCAPE

```java
@Native

public static final int REVERSE_LANDSCAPE
```

The origin is at the top right of the paper with x
running top to bottom and y running right to left.
Note that this is the Macintosh landscape.

**See Also:** Constant Field Values

---

#### Field Detail

LANDSCAPE

```java
@Native

public static final int LANDSCAPE
```

The origin is at the bottom left of the paper with
x running bottom to top and y running left to right.
Note that this is not the Macintosh landscape but
is the Window's and PostScript landscape.

**See Also:** Constant Field Values

---

#### LANDSCAPE

@Native

public static final int LANDSCAPE

The origin is at the bottom left of the paper with
x running bottom to top and y running left to right.
Note that this is not the Macintosh landscape but
is the Window's and PostScript landscape.

PORTRAIT

```java
@Native

public static final int PORTRAIT
```

The origin is at the top left of the paper with
x running to the right and y running down the
paper.

**See Also:** Constant Field Values

---

#### PORTRAIT

@Native

public static final int PORTRAIT

The origin is at the top left of the paper with
x running to the right and y running down the
paper.

REVERSE_LANDSCAPE

```java
@Native

public static final int REVERSE_LANDSCAPE
```

The origin is at the top right of the paper with x
running top to bottom and y running right to left.
Note that this is the Macintosh landscape.

**See Also:** Constant Field Values

---

#### REVERSE_LANDSCAPE

@Native

public static final int REVERSE_LANDSCAPE

The origin is at the top right of the paper with x
running top to bottom and y running right to left.
Note that this is the Macintosh landscape.

Constructor Detail

- PageFormat

```java
public PageFormat()
```

Creates a default, portrait-oriented

PageFormat

.

---

#### Constructor Detail

PageFormat

```java
public PageFormat()
```

Creates a default, portrait-oriented

PageFormat

.

---

#### PageFormat

public PageFormat()

Creates a default, portrait-oriented

PageFormat

.

Method Detail

- clone

```java
public
Object
clone()
```

Makes a copy of this

PageFormat

with the same
contents as this

PageFormat

.

**Overrides:** clone

in class

Object
**Returns:** a copy of this

PageFormat

.
**See Also:** Cloneable

- getWidth

```java
public double getWidth()
```

Returns the width, in 1/72nds of an inch, of the page.
This method takes into account the orientation of the
page when determining the width.

**Returns:** the width of the page.

- getHeight

```java
public double getHeight()
```

Returns the height, in 1/72nds of an inch, of the page.
This method takes into account the orientation of the
page when determining the height.

**Returns:** the height of the page.

- getImageableX

```java
public double getImageableX()
```

Returns the x coordinate of the upper left point of the
imageable area of the

Paper

object
associated with this

PageFormat

.
This method takes into account the
orientation of the page.

**Returns:** the x coordinate of the upper left point of the
imageable area of the

Paper

object
associated with this

PageFormat

.

- getImageableY

```java
public double getImageableY()
```

Returns the y coordinate of the upper left point of the
imageable area of the

Paper

object
associated with this

PageFormat

.
This method takes into account the
orientation of the page.

**Returns:** the y coordinate of the upper left point of the
imageable area of the

Paper

object
associated with this

PageFormat

.

- getImageableWidth

```java
public double getImageableWidth()
```

Returns the width, in 1/72nds of an inch, of the imageable
area of the page. This method takes into account the orientation
of the page.

**Returns:** the width of the page.

- getImageableHeight

```java
public double getImageableHeight()
```

Return the height, in 1/72nds of an inch, of the imageable
area of the page. This method takes into account the orientation
of the page.

**Returns:** the height of the page.

- getPaper

```java
public
Paper
getPaper()
```

Returns a copy of the

Paper

object associated
with this

PageFormat

. Changes made to the

Paper

object returned from this method do not
affect the

Paper

object of this

PageFormat

. To update the

Paper

object of this

PageFormat

, create a new

Paper

object and set it into this

PageFormat

by using the

setPaper(Paper)

method.

**Returns:** a copy of the

Paper

object associated
with this

PageFormat

.
**See Also:** setPaper(java.awt.print.Paper)

- setPaper

```java
public void setPaper​(
Paper
paper)
```

Sets the

Paper

object for this

PageFormat

.

**Parameters:** paper

- the

Paper

object to which to set
the

Paper

object for this

PageFormat

.
**Throws:** NullPointerException

- a null paper instance was passed as a parameter.
**See Also:** getPaper()

- setOrientation

```java
public void setOrientation​(int orientation)
throws
IllegalArgumentException
```

Sets the page orientation.

orientation

must be
one of the constants: PORTRAIT, LANDSCAPE,
or REVERSE_LANDSCAPE.

**Parameters:** orientation

- the new orientation for the page
**Throws:** IllegalArgumentException

- if
an unknown orientation was requested
**See Also:** getOrientation()

- getOrientation

```java
public int getOrientation()
```

Returns the orientation of this

PageFormat

.

**Returns:** this

PageFormat

object's orientation.
**See Also:** setOrientation(int)

- getMatrix

```java
public double[] getMatrix()
```

Returns a transformation matrix that translates user
space rendering to the requested orientation
of the page. The values are placed into the
array as
{ m00, m10, m01, m11, m02, m12} in
the form required by the

AffineTransform

constructor.

**Returns:** the matrix used to translate user space rendering
to the orientation of the page.
**See Also:** AffineTransform

---

#### Method Detail

clone

```java
public
Object
clone()
```

Makes a copy of this

PageFormat

with the same
contents as this

PageFormat

.

**Overrides:** clone

in class

Object
**Returns:** a copy of this

PageFormat

.
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Makes a copy of this

PageFormat

with the same
contents as this

PageFormat

.

getWidth

```java
public double getWidth()
```

Returns the width, in 1/72nds of an inch, of the page.
This method takes into account the orientation of the
page when determining the width.

**Returns:** the width of the page.

---

#### getWidth

public double getWidth()

Returns the width, in 1/72nds of an inch, of the page.
This method takes into account the orientation of the
page when determining the width.

getHeight

```java
public double getHeight()
```

Returns the height, in 1/72nds of an inch, of the page.
This method takes into account the orientation of the
page when determining the height.

**Returns:** the height of the page.

---

#### getHeight

public double getHeight()

Returns the height, in 1/72nds of an inch, of the page.
This method takes into account the orientation of the
page when determining the height.

getImageableX

```java
public double getImageableX()
```

Returns the x coordinate of the upper left point of the
imageable area of the

Paper

object
associated with this

PageFormat

.
This method takes into account the
orientation of the page.

**Returns:** the x coordinate of the upper left point of the
imageable area of the

Paper

object
associated with this

PageFormat

.

---

#### getImageableX

public double getImageableX()

Returns the x coordinate of the upper left point of the
imageable area of the

Paper

object
associated with this

PageFormat

.
This method takes into account the
orientation of the page.

getImageableY

```java
public double getImageableY()
```

Returns the y coordinate of the upper left point of the
imageable area of the

Paper

object
associated with this

PageFormat

.
This method takes into account the
orientation of the page.

**Returns:** the y coordinate of the upper left point of the
imageable area of the

Paper

object
associated with this

PageFormat

.

---

#### getImageableY

public double getImageableY()

Returns the y coordinate of the upper left point of the
imageable area of the

Paper

object
associated with this

PageFormat

.
This method takes into account the
orientation of the page.

getImageableWidth

```java
public double getImageableWidth()
```

Returns the width, in 1/72nds of an inch, of the imageable
area of the page. This method takes into account the orientation
of the page.

**Returns:** the width of the page.

---

#### getImageableWidth

public double getImageableWidth()

Returns the width, in 1/72nds of an inch, of the imageable
area of the page. This method takes into account the orientation
of the page.

getImageableHeight

```java
public double getImageableHeight()
```

Return the height, in 1/72nds of an inch, of the imageable
area of the page. This method takes into account the orientation
of the page.

**Returns:** the height of the page.

---

#### getImageableHeight

public double getImageableHeight()

Return the height, in 1/72nds of an inch, of the imageable
area of the page. This method takes into account the orientation
of the page.

getPaper

```java
public
Paper
getPaper()
```

Returns a copy of the

Paper

object associated
with this

PageFormat

. Changes made to the

Paper

object returned from this method do not
affect the

Paper

object of this

PageFormat

. To update the

Paper

object of this

PageFormat

, create a new

Paper

object and set it into this

PageFormat

by using the

setPaper(Paper)

method.

**Returns:** a copy of the

Paper

object associated
with this

PageFormat

.
**See Also:** setPaper(java.awt.print.Paper)

---

#### getPaper

public

Paper

getPaper()

Returns a copy of the

Paper

object associated
with this

PageFormat

. Changes made to the

Paper

object returned from this method do not
affect the

Paper

object of this

PageFormat

. To update the

Paper

object of this

PageFormat

, create a new

Paper

object and set it into this

PageFormat

by using the

setPaper(Paper)

method.

setPaper

```java
public void setPaper​(
Paper
paper)
```

Sets the

Paper

object for this

PageFormat

.

**Parameters:** paper

- the

Paper

object to which to set
the

Paper

object for this

PageFormat

.
**Throws:** NullPointerException

- a null paper instance was passed as a parameter.
**See Also:** getPaper()

---

#### setPaper

public void setPaper​(

Paper

paper)

Sets the

Paper

object for this

PageFormat

.

setOrientation

```java
public void setOrientation​(int orientation)
throws
IllegalArgumentException
```

Sets the page orientation.

orientation

must be
one of the constants: PORTRAIT, LANDSCAPE,
or REVERSE_LANDSCAPE.

**Parameters:** orientation

- the new orientation for the page
**Throws:** IllegalArgumentException

- if
an unknown orientation was requested
**See Also:** getOrientation()

---

#### setOrientation

public void setOrientation​(int orientation)
throws

IllegalArgumentException

Sets the page orientation.

orientation

must be
one of the constants: PORTRAIT, LANDSCAPE,
or REVERSE_LANDSCAPE.

getOrientation

```java
public int getOrientation()
```

Returns the orientation of this

PageFormat

.

**Returns:** this

PageFormat

object's orientation.
**See Also:** setOrientation(int)

---

#### getOrientation

public int getOrientation()

Returns the orientation of this

PageFormat

.

getMatrix

```java
public double[] getMatrix()
```

Returns a transformation matrix that translates user
space rendering to the requested orientation
of the page. The values are placed into the
array as
{ m00, m10, m01, m11, m02, m12} in
the form required by the

AffineTransform

constructor.

**Returns:** the matrix used to translate user space rendering
to the orientation of the page.
**See Also:** AffineTransform

---

#### getMatrix

public double[] getMatrix()

Returns a transformation matrix that translates user
space rendering to the requested orientation
of the page. The values are placed into the
array as
{ m00, m10, m01, m11, m02, m12} in
the form required by the

AffineTransform

constructor.

---

