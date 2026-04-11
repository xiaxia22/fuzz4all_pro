# Class EtchedBorder

**Source:** `java.desktop\javax\swing\border\EtchedBorder.html`

### Class Description

```java
public class
EtchedBorder

extends
AbstractBorder
```

A class which implements a simple etched border which can
either be etched-in or etched-out. If no highlight/shadow
colors are initialized when the border is created, then
these colors will be dynamically derived from the background
color of the component argument passed into the paintBorder()
method.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**All Implemented Interfaces:** Serializable

,

Border

---

### Field Details

#### public static final int RAISED

Raised etched type.

**See Also:**
- Constant Field Values

---

#### public static final int LOWERED

Lowered etched type.

**See Also:**
- Constant Field Values

---

#### protected int etchType

The type of etch to be drawn by the border.

---

#### protected
Color
highlight

The color to use for the etched highlight.

---

#### protected
Color
shadow

The color to use for the etched shadow.

---

### Constructor Details

#### public EtchedBorder()

Creates a lowered etched border whose colors will be derived
from the background color of the component passed into
the paintBorder method.

---

#### public EtchedBorder​(int etchType)

Creates an etched border with the specified etch-type
whose colors will be derived
from the background color of the component passed into
the paintBorder method.

**Parameters:**
- etchType

- the type of etch to be drawn by the border

---

#### public EtchedBorder​(
Color
highlight,

Color
shadow)

Creates a lowered etched border with the specified highlight and
shadow colors.

**Parameters:**
- highlight

- the color to use for the etched highlight
- shadow

- the color to use for the etched shadow

---

#### @ConstructorProperties
({"etchType","highlightColor","shadowColor"})
public EtchedBorder​(int etchType,

Color
highlight,

Color
shadow)

Creates an etched border with the specified etch-type,
highlight and shadow colors.

**Parameters:**
- etchType

- the type of etch to be drawn by the border
- highlight

- the color to use for the etched highlight
- shadow

- the color to use for the etched shadow

---

### Method Details

#### public void paintBorder​(
Component
c,

Graphics
g,
int x,
int y,
int width,
int height)

Paints the border for the specified component with the
specified position and size.

**Specified by:**
- paintBorder

in interface

Border

**Overrides:**
- paintBorder

in class

AbstractBorder

**Parameters:**
- c

- the component for which this border is being painted
- g

- the paint graphics
- x

- the x position of the painted border
- y

- the y position of the painted border
- width

- the width of the painted border
- height

- the height of the painted border

---

#### public
Insets
getBorderInsets​(
Component
c,

Insets
insets)

Reinitialize the insets parameter with this Border's current Insets.

**Overrides:**
- getBorderInsets

in class

AbstractBorder

**Parameters:**
- c

- the component for which this border insets value applies
- insets

- the object to be reinitialized

**Returns:**
- the

insets

object

---

#### public boolean isBorderOpaque()

Returns whether or not the border is opaque.
This implementation returns true.

**Specified by:**
- isBorderOpaque

in interface

Border

**Overrides:**
- isBorderOpaque

in class

AbstractBorder

**Returns:**
- true

---

#### public int getEtchType()

Returns which etch-type is set on the etched border.

**Returns:**
- the etched border type, either

RAISED

or

LOWERED

---

#### public
Color
getHighlightColor​(
Component
c)

Returns the highlight color of the etched border
when rendered on the specified component. If no highlight
color was specified at instantiation, the highlight color
is derived from the specified component's background color.

**Parameters:**
- c

- the component for which the highlight may be derived

**Returns:**
- the highlight

Color

of this

EtchedBorder

**Since:**
- 1.3

---

#### public
Color
getHighlightColor()

Returns the highlight color of the etched border.
Will return null if no highlight color was specified
at instantiation.

**Returns:**
- the highlight

Color

of this

EtchedBorder

or null
if none was specified

**Since:**
- 1.3

---

#### public
Color
getShadowColor​(
Component
c)

Returns the shadow color of the etched border
when rendered on the specified component. If no shadow
color was specified at instantiation, the shadow color
is derived from the specified component's background color.

**Parameters:**
- c

- the component for which the shadow may be derived

**Returns:**
- the shadow

Color

of this

EtchedBorder

**Since:**
- 1.3

---

#### public
Color
getShadowColor()

Returns the shadow color of the etched border.
Will return null if no shadow color was specified
at instantiation.

**Returns:**
- the shadow

Color

of this

EtchedBorder

or null
if none was specified

**Since:**
- 1.3

---

### Additional Sections

#### Class EtchedBorder

java.lang.Object

- javax.swing.border.AbstractBorder
- - javax.swing.border.EtchedBorder

javax.swing.border.AbstractBorder

- javax.swing.border.EtchedBorder

javax.swing.border.EtchedBorder

**All Implemented Interfaces:** Serializable

,

Border

**Direct Known Subclasses:** BorderUIResource.EtchedBorderUIResource

```java
public class
EtchedBorder

extends
AbstractBorder
```

A class which implements a simple etched border which can
either be etched-in or etched-out. If no highlight/shadow
colors are initialized when the border is created, then
these colors will be dynamically derived from the background
color of the component argument passed into the paintBorder()
method.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**See Also:** Serialized Form

public class

EtchedBorder

extends

AbstractBorder

A class which implements a simple etched border which can
either be etched-in or etched-out. If no highlight/shadow
colors are initialized when the border is created, then
these colors will be dynamically derived from the background
color of the component argument passed into the paintBorder()
method.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected int

etchType

The type of etch to be drawn by the border.

protected

Color

highlight

The color to use for the etched highlight.

static int

LOWERED

Lowered etched type.

static int

RAISED

Raised etched type.

protected

Color

shadow

The color to use for the etched shadow.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

EtchedBorder

()

Creates a lowered etched border whose colors will be derived
from the background color of the component passed into
the paintBorder method.

EtchedBorder

​(int etchType)

Creates an etched border with the specified etch-type
whose colors will be derived
from the background color of the component passed into
the paintBorder method.

EtchedBorder

​(int etchType,

Color

highlight,

Color

shadow)

Creates an etched border with the specified etch-type,
highlight and shadow colors.

EtchedBorder

​(

Color

highlight,

Color

shadow)

Creates a lowered etched border with the specified highlight and
shadow colors.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Insets

getBorderInsets

​(

Component

c,

Insets

insets)

Reinitialize the insets parameter with this Border's current Insets.

int

getEtchType

()

Returns which etch-type is set on the etched border.

Color

getHighlightColor

()

Returns the highlight color of the etched border.

Color

getHighlightColor

​(

Component

c)

Returns the highlight color of the etched border
when rendered on the specified component.

Color

getShadowColor

()

Returns the shadow color of the etched border.

Color

getShadowColor

​(

Component

c)

Returns the shadow color of the etched border
when rendered on the specified component.

boolean

isBorderOpaque

()

Returns whether or not the border is opaque.

void

paintBorder

​(

Component

c,

Graphics

g,
int x,
int y,
int width,
int height)

Paints the border for the specified component with the
specified position and size.

- Methods declared in class javax.swing.border.

AbstractBorder

getBaseline

,

getBaselineResizeBehavior

,

getBorderInsets

,

getInteriorRectangle

,

getInteriorRectangle

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

protected int

etchType

The type of etch to be drawn by the border.

protected

Color

highlight

The color to use for the etched highlight.

static int

LOWERED

Lowered etched type.

static int

RAISED

Raised etched type.

protected

Color

shadow

The color to use for the etched shadow.

---

#### Field Summary

The type of etch to be drawn by the border.

The color to use for the etched highlight.

Lowered etched type.

Raised etched type.

The color to use for the etched shadow.

Constructor Summary

Constructors

Constructor

Description

EtchedBorder

()

Creates a lowered etched border whose colors will be derived
from the background color of the component passed into
the paintBorder method.

EtchedBorder

​(int etchType)

Creates an etched border with the specified etch-type
whose colors will be derived
from the background color of the component passed into
the paintBorder method.

EtchedBorder

​(int etchType,

Color

highlight,

Color

shadow)

Creates an etched border with the specified etch-type,
highlight and shadow colors.

EtchedBorder

​(

Color

highlight,

Color

shadow)

Creates a lowered etched border with the specified highlight and
shadow colors.

---

#### Constructor Summary

Creates a lowered etched border whose colors will be derived
from the background color of the component passed into
the paintBorder method.

Creates an etched border with the specified etch-type
whose colors will be derived
from the background color of the component passed into
the paintBorder method.

Creates an etched border with the specified etch-type,
highlight and shadow colors.

Creates a lowered etched border with the specified highlight and
shadow colors.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Insets

getBorderInsets

​(

Component

c,

Insets

insets)

Reinitialize the insets parameter with this Border's current Insets.

int

getEtchType

()

Returns which etch-type is set on the etched border.

Color

getHighlightColor

()

Returns the highlight color of the etched border.

Color

getHighlightColor

​(

Component

c)

Returns the highlight color of the etched border
when rendered on the specified component.

Color

getShadowColor

()

Returns the shadow color of the etched border.

Color

getShadowColor

​(

Component

c)

Returns the shadow color of the etched border
when rendered on the specified component.

boolean

isBorderOpaque

()

Returns whether or not the border is opaque.

void

paintBorder

​(

Component

c,

Graphics

g,
int x,
int y,
int width,
int height)

Paints the border for the specified component with the
specified position and size.

- Methods declared in class javax.swing.border.

AbstractBorder

getBaseline

,

getBaselineResizeBehavior

,

getBorderInsets

,

getInteriorRectangle

,

getInteriorRectangle

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

Reinitialize the insets parameter with this Border's current Insets.

Returns which etch-type is set on the etched border.

Returns the highlight color of the etched border.

Returns the highlight color of the etched border
when rendered on the specified component.

Returns the shadow color of the etched border.

Returns the shadow color of the etched border
when rendered on the specified component.

Returns whether or not the border is opaque.

Paints the border for the specified component with the
specified position and size.

Methods declared in class javax.swing.border.

AbstractBorder

getBaseline

,

getBaselineResizeBehavior

,

getBorderInsets

,

getInteriorRectangle

,

getInteriorRectangle

---

#### Methods declared in class javax.swing.border. AbstractBorder

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

- RAISED

```java
public static final int RAISED
```

Raised etched type.

**See Also:** Constant Field Values

- LOWERED

```java
public static final int LOWERED
```

Lowered etched type.

**See Also:** Constant Field Values

- etchType

```java
protected int etchType
```

The type of etch to be drawn by the border.

- highlight

```java
protected
Color
highlight
```

The color to use for the etched highlight.

- shadow

```java
protected
Color
shadow
```

The color to use for the etched shadow.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- EtchedBorder

```java
public EtchedBorder()
```

Creates a lowered etched border whose colors will be derived
from the background color of the component passed into
the paintBorder method.

- EtchedBorder

```java
public EtchedBorder​(int etchType)
```

Creates an etched border with the specified etch-type
whose colors will be derived
from the background color of the component passed into
the paintBorder method.

**Parameters:** etchType

- the type of etch to be drawn by the border

- EtchedBorder

```java
public EtchedBorder​(
Color
highlight,

Color
shadow)
```

Creates a lowered etched border with the specified highlight and
shadow colors.

**Parameters:** highlight

- the color to use for the etched highlight
**Parameters:** shadow

- the color to use for the etched shadow

- EtchedBorder

```java
@ConstructorProperties
({"etchType","highlightColor","shadowColor"})
public EtchedBorder​(int etchType,

Color
highlight,

Color
shadow)
```

Creates an etched border with the specified etch-type,
highlight and shadow colors.

**Parameters:** etchType

- the type of etch to be drawn by the border
**Parameters:** highlight

- the color to use for the etched highlight
**Parameters:** shadow

- the color to use for the etched shadow

============ METHOD DETAIL ==========

- Method Detail

- paintBorder

```java
public void paintBorder​(
Component
c,

Graphics
g,
int x,
int y,
int width,
int height)
```

Paints the border for the specified component with the
specified position and size.

**Specified by:** paintBorder

in interface

Border
**Overrides:** paintBorder

in class

AbstractBorder
**Parameters:** c

- the component for which this border is being painted
**Parameters:** g

- the paint graphics
**Parameters:** x

- the x position of the painted border
**Parameters:** y

- the y position of the painted border
**Parameters:** width

- the width of the painted border
**Parameters:** height

- the height of the painted border

- getBorderInsets

```java
public
Insets
getBorderInsets​(
Component
c,

Insets
insets)
```

Reinitialize the insets parameter with this Border's current Insets.

**Overrides:** getBorderInsets

in class

AbstractBorder
**Parameters:** c

- the component for which this border insets value applies
**Parameters:** insets

- the object to be reinitialized
**Returns:** the

insets

object

- isBorderOpaque

```java
public boolean isBorderOpaque()
```

Returns whether or not the border is opaque.
This implementation returns true.

**Specified by:** isBorderOpaque

in interface

Border
**Overrides:** isBorderOpaque

in class

AbstractBorder
**Returns:** true

- getEtchType

```java
public int getEtchType()
```

Returns which etch-type is set on the etched border.

**Returns:** the etched border type, either

RAISED

or

LOWERED

- getHighlightColor

```java
public
Color
getHighlightColor​(
Component
c)
```

Returns the highlight color of the etched border
when rendered on the specified component. If no highlight
color was specified at instantiation, the highlight color
is derived from the specified component's background color.

**Parameters:** c

- the component for which the highlight may be derived
**Returns:** the highlight

Color

of this

EtchedBorder
**Since:** 1.3

- getHighlightColor

```java
public
Color
getHighlightColor()
```

Returns the highlight color of the etched border.
Will return null if no highlight color was specified
at instantiation.

**Returns:** the highlight

Color

of this

EtchedBorder

or null
if none was specified
**Since:** 1.3

- getShadowColor

```java
public
Color
getShadowColor​(
Component
c)
```

Returns the shadow color of the etched border
when rendered on the specified component. If no shadow
color was specified at instantiation, the shadow color
is derived from the specified component's background color.

**Parameters:** c

- the component for which the shadow may be derived
**Returns:** the shadow

Color

of this

EtchedBorder
**Since:** 1.3

- getShadowColor

```java
public
Color
getShadowColor()
```

Returns the shadow color of the etched border.
Will return null if no shadow color was specified
at instantiation.

**Returns:** the shadow

Color

of this

EtchedBorder

or null
if none was specified
**Since:** 1.3

Field Detail

- RAISED

```java
public static final int RAISED
```

Raised etched type.

**See Also:** Constant Field Values

- LOWERED

```java
public static final int LOWERED
```

Lowered etched type.

**See Also:** Constant Field Values

- etchType

```java
protected int etchType
```

The type of etch to be drawn by the border.

- highlight

```java
protected
Color
highlight
```

The color to use for the etched highlight.

- shadow

```java
protected
Color
shadow
```

The color to use for the etched shadow.

---

#### Field Detail

RAISED

```java
public static final int RAISED
```

Raised etched type.

**See Also:** Constant Field Values

---

#### RAISED

public static final int RAISED

Raised etched type.

LOWERED

```java
public static final int LOWERED
```

Lowered etched type.

**See Also:** Constant Field Values

---

#### LOWERED

public static final int LOWERED

Lowered etched type.

etchType

```java
protected int etchType
```

The type of etch to be drawn by the border.

---

#### etchType

protected int etchType

The type of etch to be drawn by the border.

highlight

```java
protected
Color
highlight
```

The color to use for the etched highlight.

---

#### highlight

protected

Color

highlight

The color to use for the etched highlight.

shadow

```java
protected
Color
shadow
```

The color to use for the etched shadow.

---

#### shadow

protected

Color

shadow

The color to use for the etched shadow.

Constructor Detail

- EtchedBorder

```java
public EtchedBorder()
```

Creates a lowered etched border whose colors will be derived
from the background color of the component passed into
the paintBorder method.

- EtchedBorder

```java
public EtchedBorder​(int etchType)
```

Creates an etched border with the specified etch-type
whose colors will be derived
from the background color of the component passed into
the paintBorder method.

**Parameters:** etchType

- the type of etch to be drawn by the border

- EtchedBorder

```java
public EtchedBorder​(
Color
highlight,

Color
shadow)
```

Creates a lowered etched border with the specified highlight and
shadow colors.

**Parameters:** highlight

- the color to use for the etched highlight
**Parameters:** shadow

- the color to use for the etched shadow

- EtchedBorder

```java
@ConstructorProperties
({"etchType","highlightColor","shadowColor"})
public EtchedBorder​(int etchType,

Color
highlight,

Color
shadow)
```

Creates an etched border with the specified etch-type,
highlight and shadow colors.

**Parameters:** etchType

- the type of etch to be drawn by the border
**Parameters:** highlight

- the color to use for the etched highlight
**Parameters:** shadow

- the color to use for the etched shadow

---

#### Constructor Detail

EtchedBorder

```java
public EtchedBorder()
```

Creates a lowered etched border whose colors will be derived
from the background color of the component passed into
the paintBorder method.

---

#### EtchedBorder

public EtchedBorder()

Creates a lowered etched border whose colors will be derived
from the background color of the component passed into
the paintBorder method.

EtchedBorder

```java
public EtchedBorder​(int etchType)
```

Creates an etched border with the specified etch-type
whose colors will be derived
from the background color of the component passed into
the paintBorder method.

**Parameters:** etchType

- the type of etch to be drawn by the border

---

#### EtchedBorder

public EtchedBorder​(int etchType)

Creates an etched border with the specified etch-type
whose colors will be derived
from the background color of the component passed into
the paintBorder method.

EtchedBorder

```java
public EtchedBorder​(
Color
highlight,

Color
shadow)
```

Creates a lowered etched border with the specified highlight and
shadow colors.

**Parameters:** highlight

- the color to use for the etched highlight
**Parameters:** shadow

- the color to use for the etched shadow

---

#### EtchedBorder

public EtchedBorder​(

Color

highlight,

Color

shadow)

Creates a lowered etched border with the specified highlight and
shadow colors.

EtchedBorder

```java
@ConstructorProperties
({"etchType","highlightColor","shadowColor"})
public EtchedBorder​(int etchType,

Color
highlight,

Color
shadow)
```

Creates an etched border with the specified etch-type,
highlight and shadow colors.

**Parameters:** etchType

- the type of etch to be drawn by the border
**Parameters:** highlight

- the color to use for the etched highlight
**Parameters:** shadow

- the color to use for the etched shadow

---

#### EtchedBorder

@ConstructorProperties

({"etchType","highlightColor","shadowColor"})
public EtchedBorder​(int etchType,

Color

highlight,

Color

shadow)

Creates an etched border with the specified etch-type,
highlight and shadow colors.

Method Detail

- paintBorder

```java
public void paintBorder​(
Component
c,

Graphics
g,
int x,
int y,
int width,
int height)
```

Paints the border for the specified component with the
specified position and size.

**Specified by:** paintBorder

in interface

Border
**Overrides:** paintBorder

in class

AbstractBorder
**Parameters:** c

- the component for which this border is being painted
**Parameters:** g

- the paint graphics
**Parameters:** x

- the x position of the painted border
**Parameters:** y

- the y position of the painted border
**Parameters:** width

- the width of the painted border
**Parameters:** height

- the height of the painted border

- getBorderInsets

```java
public
Insets
getBorderInsets​(
Component
c,

Insets
insets)
```

Reinitialize the insets parameter with this Border's current Insets.

**Overrides:** getBorderInsets

in class

AbstractBorder
**Parameters:** c

- the component for which this border insets value applies
**Parameters:** insets

- the object to be reinitialized
**Returns:** the

insets

object

- isBorderOpaque

```java
public boolean isBorderOpaque()
```

Returns whether or not the border is opaque.
This implementation returns true.

**Specified by:** isBorderOpaque

in interface

Border
**Overrides:** isBorderOpaque

in class

AbstractBorder
**Returns:** true

- getEtchType

```java
public int getEtchType()
```

Returns which etch-type is set on the etched border.

**Returns:** the etched border type, either

RAISED

or

LOWERED

- getHighlightColor

```java
public
Color
getHighlightColor​(
Component
c)
```

Returns the highlight color of the etched border
when rendered on the specified component. If no highlight
color was specified at instantiation, the highlight color
is derived from the specified component's background color.

**Parameters:** c

- the component for which the highlight may be derived
**Returns:** the highlight

Color

of this

EtchedBorder
**Since:** 1.3

- getHighlightColor

```java
public
Color
getHighlightColor()
```

Returns the highlight color of the etched border.
Will return null if no highlight color was specified
at instantiation.

**Returns:** the highlight

Color

of this

EtchedBorder

or null
if none was specified
**Since:** 1.3

- getShadowColor

```java
public
Color
getShadowColor​(
Component
c)
```

Returns the shadow color of the etched border
when rendered on the specified component. If no shadow
color was specified at instantiation, the shadow color
is derived from the specified component's background color.

**Parameters:** c

- the component for which the shadow may be derived
**Returns:** the shadow

Color

of this

EtchedBorder
**Since:** 1.3

- getShadowColor

```java
public
Color
getShadowColor()
```

Returns the shadow color of the etched border.
Will return null if no shadow color was specified
at instantiation.

**Returns:** the shadow

Color

of this

EtchedBorder

or null
if none was specified
**Since:** 1.3

---

#### Method Detail

paintBorder

```java
public void paintBorder​(
Component
c,

Graphics
g,
int x,
int y,
int width,
int height)
```

Paints the border for the specified component with the
specified position and size.

**Specified by:** paintBorder

in interface

Border
**Overrides:** paintBorder

in class

AbstractBorder
**Parameters:** c

- the component for which this border is being painted
**Parameters:** g

- the paint graphics
**Parameters:** x

- the x position of the painted border
**Parameters:** y

- the y position of the painted border
**Parameters:** width

- the width of the painted border
**Parameters:** height

- the height of the painted border

---

#### paintBorder

public void paintBorder​(

Component

c,

Graphics

g,
int x,
int y,
int width,
int height)

Paints the border for the specified component with the
specified position and size.

getBorderInsets

```java
public
Insets
getBorderInsets​(
Component
c,

Insets
insets)
```

Reinitialize the insets parameter with this Border's current Insets.

**Overrides:** getBorderInsets

in class

AbstractBorder
**Parameters:** c

- the component for which this border insets value applies
**Parameters:** insets

- the object to be reinitialized
**Returns:** the

insets

object

---

#### getBorderInsets

public

Insets

getBorderInsets​(

Component

c,

Insets

insets)

Reinitialize the insets parameter with this Border's current Insets.

isBorderOpaque

```java
public boolean isBorderOpaque()
```

Returns whether or not the border is opaque.
This implementation returns true.

**Specified by:** isBorderOpaque

in interface

Border
**Overrides:** isBorderOpaque

in class

AbstractBorder
**Returns:** true

---

#### isBorderOpaque

public boolean isBorderOpaque()

Returns whether or not the border is opaque.
This implementation returns true.

getEtchType

```java
public int getEtchType()
```

Returns which etch-type is set on the etched border.

**Returns:** the etched border type, either

RAISED

or

LOWERED

---

#### getEtchType

public int getEtchType()

Returns which etch-type is set on the etched border.

getHighlightColor

```java
public
Color
getHighlightColor​(
Component
c)
```

Returns the highlight color of the etched border
when rendered on the specified component. If no highlight
color was specified at instantiation, the highlight color
is derived from the specified component's background color.

**Parameters:** c

- the component for which the highlight may be derived
**Returns:** the highlight

Color

of this

EtchedBorder
**Since:** 1.3

---

#### getHighlightColor

public

Color

getHighlightColor​(

Component

c)

Returns the highlight color of the etched border
when rendered on the specified component. If no highlight
color was specified at instantiation, the highlight color
is derived from the specified component's background color.

getHighlightColor

```java
public
Color
getHighlightColor()
```

Returns the highlight color of the etched border.
Will return null if no highlight color was specified
at instantiation.

**Returns:** the highlight

Color

of this

EtchedBorder

or null
if none was specified
**Since:** 1.3

---

#### getHighlightColor

public

Color

getHighlightColor()

Returns the highlight color of the etched border.
Will return null if no highlight color was specified
at instantiation.

getShadowColor

```java
public
Color
getShadowColor​(
Component
c)
```

Returns the shadow color of the etched border
when rendered on the specified component. If no shadow
color was specified at instantiation, the shadow color
is derived from the specified component's background color.

**Parameters:** c

- the component for which the shadow may be derived
**Returns:** the shadow

Color

of this

EtchedBorder
**Since:** 1.3

---

#### getShadowColor

public

Color

getShadowColor​(

Component

c)

Returns the shadow color of the etched border
when rendered on the specified component. If no shadow
color was specified at instantiation, the shadow color
is derived from the specified component's background color.

getShadowColor

```java
public
Color
getShadowColor()
```

Returns the shadow color of the etched border.
Will return null if no shadow color was specified
at instantiation.

**Returns:** the shadow

Color

of this

EtchedBorder

or null
if none was specified
**Since:** 1.3

---

#### getShadowColor

public

Color

getShadowColor()

Returns the shadow color of the etched border.
Will return null if no shadow color was specified
at instantiation.

---

