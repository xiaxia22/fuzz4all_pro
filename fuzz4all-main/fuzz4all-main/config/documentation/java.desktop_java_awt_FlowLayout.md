# Class FlowLayout

**Source:** `java.desktop\java\awt\FlowLayout.html`

### Class Description

```java
public class
FlowLayout

extends
Object

implements
LayoutManager
,
Serializable
```

A flow layout arranges components in a directional flow, much
like lines of text in a paragraph. The flow direction is
determined by the container's

componentOrientation

property and may be one of two values:

- ComponentOrientation.LEFT_TO_RIGHT

ComponentOrientation.RIGHT_TO_LEFT

Flow layouts are typically used
to arrange buttons in a panel. It arranges buttons
horizontally until no more buttons fit on the same line.
The line alignment is determined by the

align

property. The possible values are:

- LEFT

RIGHT

CENTER

LEADING

TRAILING

For example, the following picture shows an applet using the flow
layout manager (its default layout manager) to position three buttons:

Here is the code for this applet:

```java
import java.awt.*;
import java.applet.Applet;

public class myButtons extends Applet {
Button button1, button2, button3;
public void init() {
button1 = new Button("Ok");
button2 = new Button("Open");
button3 = new Button("Close");
add(button1);
add(button2);
add(button3);
}
}
```

A flow layout lets each component assume its natural (preferred) size.

**All Implemented Interfaces:** LayoutManager

,

Serializable

---

### Field Details

#### public static final int LEFT

This value indicates that each row of components
should be left-justified.

**See Also:**
- Constant Field Values

---

#### public static final int CENTER

This value indicates that each row of components
should be centered.

**See Also:**
- Constant Field Values

---

#### public static final int RIGHT

This value indicates that each row of components
should be right-justified.

**See Also:**
- Constant Field Values

---

#### public static final int LEADING

This value indicates that each row of components
should be justified to the leading edge of the container's
orientation, for example, to the left in left-to-right orientations.

**See Also:**
- Component.getComponentOrientation()

,

ComponentOrientation

,

Constant Field Values

**Since:**
- 1.2

---

#### public static final int TRAILING

This value indicates that each row of components
should be justified to the trailing edge of the container's
orientation, for example, to the right in left-to-right orientations.

**See Also:**
- Component.getComponentOrientation()

,

ComponentOrientation

,

Constant Field Values

**Since:**
- 1.2

---

### Constructor Details

#### public FlowLayout()

Constructs a new

FlowLayout

with a centered alignment and a
default 5-unit horizontal and vertical gap.

---

#### public FlowLayout​(int align)

Constructs a new

FlowLayout

with the specified
alignment and a default 5-unit horizontal and vertical gap.
The value of the alignment argument must be one of

FlowLayout.LEFT

,

FlowLayout.RIGHT

,

FlowLayout.CENTER

,

FlowLayout.LEADING

,
or

FlowLayout.TRAILING

.

**Parameters:**
- align

- the alignment value

---

#### public FlowLayout​(int align,
int hgap,
int vgap)

Creates a new flow layout manager with the indicated alignment
and the indicated horizontal and vertical gaps.

The value of the alignment argument must be one of

FlowLayout.LEFT

,

FlowLayout.RIGHT

,

FlowLayout.CENTER

,

FlowLayout.LEADING

,
or

FlowLayout.TRAILING

.

**Parameters:**
- align

- the alignment value
- hgap

- the horizontal gap between components
and between the components and the
borders of the

Container
- vgap

- the vertical gap between components
and between the components and the
borders of the

Container

---

### Method Details

#### public int getAlignment()

Gets the alignment for this layout.
Possible values are

FlowLayout.LEFT

,

FlowLayout.RIGHT

,

FlowLayout.CENTER

,

FlowLayout.LEADING

,
or

FlowLayout.TRAILING

.

**Returns:**
- the alignment value for this layout

**See Also:**
- setAlignment(int)

**Since:**
- 1.1

---

#### public void setAlignment​(int align)

Sets the alignment for this layout.
Possible values are

- FlowLayout.LEFT

FlowLayout.RIGHT

FlowLayout.CENTER

FlowLayout.LEADING

FlowLayout.TRAILING

**Parameters:**
- align

- one of the alignment values shown above

**See Also:**
- getAlignment()

**Since:**
- 1.1

---

#### public int getHgap()

Gets the horizontal gap between components
and between the components and the borders
of the

Container

**Returns:**
- the horizontal gap between components
and between the components and the borders
of the

Container

**See Also:**
- setHgap(int)

**Since:**
- 1.1

---

#### public void setHgap​(int hgap)

Sets the horizontal gap between components and
between the components and the borders of the

Container

.

**Parameters:**
- hgap

- the horizontal gap between components
and between the components and the borders
of the

Container

**See Also:**
- getHgap()

**Since:**
- 1.1

---

#### public int getVgap()

Gets the vertical gap between components and
between the components and the borders of the

Container

.

**Returns:**
- the vertical gap between components
and between the components and the borders
of the

Container

**See Also:**
- setVgap(int)

**Since:**
- 1.1

---

#### public void setVgap​(int vgap)

Sets the vertical gap between components and between
the components and the borders of the

Container

.

**Parameters:**
- vgap

- the vertical gap between components
and between the components and the borders
of the

Container

**See Also:**
- getVgap()

**Since:**
- 1.1

---

#### public void setAlignOnBaseline​(boolean alignOnBaseline)

Sets whether or not components should be vertically aligned along their
baseline. Components that do not have a baseline will be centered.
The default is false.

**Parameters:**
- alignOnBaseline

- whether or not components should be
vertically aligned on their baseline

**Since:**
- 1.6

---

#### public boolean getAlignOnBaseline()

Returns true if components are to be vertically aligned along
their baseline. The default is false.

**Returns:**
- true if components are to be vertically aligned along
their baseline

**Since:**
- 1.6

---

#### public void addLayoutComponent​(
String
name,

Component
comp)

Adds the specified component to the layout.
Not used by this class.

**Specified by:**
- addLayoutComponent

in interface

LayoutManager

**Parameters:**
- name

- the name of the component
- comp

- the component to be added

---

#### public void removeLayoutComponent​(
Component
comp)

Removes the specified component from the layout.
Not used by this class.

**Specified by:**
- removeLayoutComponent

in interface

LayoutManager

**Parameters:**
- comp

- the component to remove

**See Also:**
- Container.removeAll()

---

#### public
Dimension
preferredLayoutSize​(
Container
target)

Returns the preferred dimensions for this layout given the

visible

components in the specified target container.

**Specified by:**
- preferredLayoutSize

in interface

LayoutManager

**Parameters:**
- target

- the container that needs to be laid out

**Returns:**
- the preferred dimensions to lay out the
subcomponents of the specified container

**See Also:**
- Container

,

minimumLayoutSize(java.awt.Container)

,

Container.getPreferredSize()

---

#### public
Dimension
minimumLayoutSize​(
Container
target)

Returns the minimum dimensions needed to layout the

visible

components contained in the specified target container.

**Specified by:**
- minimumLayoutSize

in interface

LayoutManager

**Parameters:**
- target

- the container that needs to be laid out

**Returns:**
- the minimum dimensions to lay out the
subcomponents of the specified container

**See Also:**
- preferredLayoutSize(java.awt.Container)

,

Container

,

Container.doLayout()

---

#### public void layoutContainer​(
Container
target)

Lays out the container. This method lets each

visible

component take
its preferred size by reshaping the components in the
target container in order to satisfy the alignment of
this

FlowLayout

object.

**Specified by:**
- layoutContainer

in interface

LayoutManager

**Parameters:**
- target

- the specified component being laid out

**See Also:**
- Container

,

Container.doLayout()

---

#### public
String
toString()

Returns a string representation of this

FlowLayout

object and its values.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this layout

---

### Additional Sections

#### Class FlowLayout

java.lang.Object

- java.awt.FlowLayout

java.awt.FlowLayout

**All Implemented Interfaces:** LayoutManager

,

Serializable

```java
public class
FlowLayout

extends
Object

implements
LayoutManager
,
Serializable
```

A flow layout arranges components in a directional flow, much
like lines of text in a paragraph. The flow direction is
determined by the container's

componentOrientation

property and may be one of two values:

- ComponentOrientation.LEFT_TO_RIGHT

ComponentOrientation.RIGHT_TO_LEFT

Flow layouts are typically used
to arrange buttons in a panel. It arranges buttons
horizontally until no more buttons fit on the same line.
The line alignment is determined by the

align

property. The possible values are:

- LEFT

RIGHT

CENTER

LEADING

TRAILING

For example, the following picture shows an applet using the flow
layout manager (its default layout manager) to position three buttons:

Here is the code for this applet:

```java
import java.awt.*;
import java.applet.Applet;

public class myButtons extends Applet {
Button button1, button2, button3;
public void init() {
button1 = new Button("Ok");
button2 = new Button("Open");
button3 = new Button("Close");
add(button1);
add(button2);
add(button3);
}
}
```

A flow layout lets each component assume its natural (preferred) size.

**Since:** 1.0
**See Also:** ComponentOrientation

,

Serialized Form

public class

FlowLayout

extends

Object

implements

LayoutManager

,

Serializable

A flow layout arranges components in a directional flow, much
like lines of text in a paragraph. The flow direction is
determined by the container's

componentOrientation

property and may be one of two values:

- ComponentOrientation.LEFT_TO_RIGHT

ComponentOrientation.RIGHT_TO_LEFT

Flow layouts are typically used
to arrange buttons in a panel. It arranges buttons
horizontally until no more buttons fit on the same line.
The line alignment is determined by the

align

property. The possible values are:

- LEFT

RIGHT

CENTER

LEADING

TRAILING

For example, the following picture shows an applet using the flow
layout manager (its default layout manager) to position three buttons:

Here is the code for this applet:

```java
import java.awt.*;
import java.applet.Applet;

public class myButtons extends Applet {
Button button1, button2, button3;
public void init() {
button1 = new Button("Ok");
button2 = new Button("Open");
button3 = new Button("Close");
add(button1);
add(button2);
add(button3);
}
}
```

A flow layout lets each component assume its natural (preferred) size.

ComponentOrientation.LEFT_TO_RIGHT

ComponentOrientation.RIGHT_TO_LEFT

LEFT

RIGHT

CENTER

LEADING

TRAILING

For example, the following picture shows an applet using the flow
layout manager (its default layout manager) to position three buttons:

Here is the code for this applet:

```java
import java.awt.*;
import java.applet.Applet;

public class myButtons extends Applet {
Button button1, button2, button3;
public void init() {
button1 = new Button("Ok");
button2 = new Button("Open");
button3 = new Button("Close");
add(button1);
add(button2);
add(button3);
}
}
```

A flow layout lets each component assume its natural (preferred) size.

Here is the code for this applet:

```java
import java.awt.*;
import java.applet.Applet;

public class myButtons extends Applet {
Button button1, button2, button3;
public void init() {
button1 = new Button("Ok");
button2 = new Button("Open");
button3 = new Button("Close");
add(button1);
add(button2);
add(button3);
}
}
```

A flow layout lets each component assume its natural (preferred) size.

import java.awt.*;
import java.applet.Applet;

public class myButtons extends Applet {
Button button1, button2, button3;
public void init() {
button1 = new Button("Ok");
button2 = new Button("Open");
button3 = new Button("Close");
add(button1);
add(button2);
add(button3);
}
}

A flow layout lets each component assume its natural (preferred) size.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

CENTER

This value indicates that each row of components
should be centered.

static int

LEADING

This value indicates that each row of components
should be justified to the leading edge of the container's
orientation, for example, to the left in left-to-right orientations.

static int

LEFT

This value indicates that each row of components
should be left-justified.

static int

RIGHT

This value indicates that each row of components
should be right-justified.

static int

TRAILING

This value indicates that each row of components
should be justified to the trailing edge of the container's
orientation, for example, to the right in left-to-right orientations.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

FlowLayout

()

Constructs a new

FlowLayout

with a centered alignment and a
default 5-unit horizontal and vertical gap.

FlowLayout

​(int align)

Constructs a new

FlowLayout

with the specified
alignment and a default 5-unit horizontal and vertical gap.

FlowLayout

​(int align,
int hgap,
int vgap)

Creates a new flow layout manager with the indicated alignment
and the indicated horizontal and vertical gaps.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addLayoutComponent

​(

String

name,

Component

comp)

Adds the specified component to the layout.

int

getAlignment

()

Gets the alignment for this layout.

boolean

getAlignOnBaseline

()

Returns true if components are to be vertically aligned along
their baseline.

int

getHgap

()

Gets the horizontal gap between components
and between the components and the borders
of the

Container

int

getVgap

()

Gets the vertical gap between components and
between the components and the borders of the

Container

.

void

layoutContainer

​(

Container

target)

Lays out the container.

Dimension

minimumLayoutSize

​(

Container

target)

Returns the minimum dimensions needed to layout the

visible

components contained in the specified target container.

Dimension

preferredLayoutSize

​(

Container

target)

Returns the preferred dimensions for this layout given the

visible

components in the specified target container.

void

removeLayoutComponent

​(

Component

comp)

Removes the specified component from the layout.

void

setAlignment

​(int align)

Sets the alignment for this layout.

void

setAlignOnBaseline

​(boolean alignOnBaseline)

Sets whether or not components should be vertically aligned along their
baseline.

void

setHgap

​(int hgap)

Sets the horizontal gap between components and
between the components and the borders of the

Container

.

void

setVgap

​(int vgap)

Sets the vertical gap between components and between
the components and the borders of the

Container

.

String

toString

()

Returns a string representation of this

FlowLayout

object and its values.

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

CENTER

This value indicates that each row of components
should be centered.

static int

LEADING

This value indicates that each row of components
should be justified to the leading edge of the container's
orientation, for example, to the left in left-to-right orientations.

static int

LEFT

This value indicates that each row of components
should be left-justified.

static int

RIGHT

This value indicates that each row of components
should be right-justified.

static int

TRAILING

This value indicates that each row of components
should be justified to the trailing edge of the container's
orientation, for example, to the right in left-to-right orientations.

---

#### Field Summary

This value indicates that each row of components
should be centered.

This value indicates that each row of components
should be justified to the leading edge of the container's
orientation, for example, to the left in left-to-right orientations.

This value indicates that each row of components
should be left-justified.

This value indicates that each row of components
should be right-justified.

This value indicates that each row of components
should be justified to the trailing edge of the container's
orientation, for example, to the right in left-to-right orientations.

Constructor Summary

Constructors

Constructor

Description

FlowLayout

()

Constructs a new

FlowLayout

with a centered alignment and a
default 5-unit horizontal and vertical gap.

FlowLayout

​(int align)

Constructs a new

FlowLayout

with the specified
alignment and a default 5-unit horizontal and vertical gap.

FlowLayout

​(int align,
int hgap,
int vgap)

Creates a new flow layout manager with the indicated alignment
and the indicated horizontal and vertical gaps.

---

#### Constructor Summary

Constructs a new

FlowLayout

with a centered alignment and a
default 5-unit horizontal and vertical gap.

Constructs a new

FlowLayout

with the specified
alignment and a default 5-unit horizontal and vertical gap.

Creates a new flow layout manager with the indicated alignment
and the indicated horizontal and vertical gaps.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addLayoutComponent

​(

String

name,

Component

comp)

Adds the specified component to the layout.

int

getAlignment

()

Gets the alignment for this layout.

boolean

getAlignOnBaseline

()

Returns true if components are to be vertically aligned along
their baseline.

int

getHgap

()

Gets the horizontal gap between components
and between the components and the borders
of the

Container

int

getVgap

()

Gets the vertical gap between components and
between the components and the borders of the

Container

.

void

layoutContainer

​(

Container

target)

Lays out the container.

Dimension

minimumLayoutSize

​(

Container

target)

Returns the minimum dimensions needed to layout the

visible

components contained in the specified target container.

Dimension

preferredLayoutSize

​(

Container

target)

Returns the preferred dimensions for this layout given the

visible

components in the specified target container.

void

removeLayoutComponent

​(

Component

comp)

Removes the specified component from the layout.

void

setAlignment

​(int align)

Sets the alignment for this layout.

void

setAlignOnBaseline

​(boolean alignOnBaseline)

Sets whether or not components should be vertically aligned along their
baseline.

void

setHgap

​(int hgap)

Sets the horizontal gap between components and
between the components and the borders of the

Container

.

void

setVgap

​(int vgap)

Sets the vertical gap between components and between
the components and the borders of the

Container

.

String

toString

()

Returns a string representation of this

FlowLayout

object and its values.

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

wait

,

wait

,

wait

---

#### Method Summary

Adds the specified component to the layout.

Gets the alignment for this layout.

Returns true if components are to be vertically aligned along
their baseline.

Gets the horizontal gap between components
and between the components and the borders
of the

Container

Gets the vertical gap between components and
between the components and the borders of the

Container

.

Lays out the container.

Returns the minimum dimensions needed to layout the

visible

components contained in the specified target container.

Returns the preferred dimensions for this layout given the

visible

components in the specified target container.

Removes the specified component from the layout.

Sets the alignment for this layout.

Sets whether or not components should be vertically aligned along their
baseline.

Sets the horizontal gap between components and
between the components and the borders of the

Container

.

Sets the vertical gap between components and between
the components and the borders of the

Container

.

Returns a string representation of this

FlowLayout

object and its values.

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ FIELD DETAIL ===========

- Field Detail

- LEFT

```java
public static final int LEFT
```

This value indicates that each row of components
should be left-justified.

**See Also:** Constant Field Values

- CENTER

```java
public static final int CENTER
```

This value indicates that each row of components
should be centered.

**See Also:** Constant Field Values

- RIGHT

```java
public static final int RIGHT
```

This value indicates that each row of components
should be right-justified.

**See Also:** Constant Field Values

- LEADING

```java
public static final int LEADING
```

This value indicates that each row of components
should be justified to the leading edge of the container's
orientation, for example, to the left in left-to-right orientations.

**Since:** 1.2
**See Also:** Component.getComponentOrientation()

,

ComponentOrientation

,

Constant Field Values

- TRAILING

```java
public static final int TRAILING
```

This value indicates that each row of components
should be justified to the trailing edge of the container's
orientation, for example, to the right in left-to-right orientations.

**Since:** 1.2
**See Also:** Component.getComponentOrientation()

,

ComponentOrientation

,

Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- FlowLayout

```java
public FlowLayout()
```

Constructs a new

FlowLayout

with a centered alignment and a
default 5-unit horizontal and vertical gap.

- FlowLayout

```java
public FlowLayout​(int align)
```

Constructs a new

FlowLayout

with the specified
alignment and a default 5-unit horizontal and vertical gap.
The value of the alignment argument must be one of

FlowLayout.LEFT

,

FlowLayout.RIGHT

,

FlowLayout.CENTER

,

FlowLayout.LEADING

,
or

FlowLayout.TRAILING

.

**Parameters:** align

- the alignment value

- FlowLayout

```java
public FlowLayout​(int align,
int hgap,
int vgap)
```

Creates a new flow layout manager with the indicated alignment
and the indicated horizontal and vertical gaps.

The value of the alignment argument must be one of

FlowLayout.LEFT

,

FlowLayout.RIGHT

,

FlowLayout.CENTER

,

FlowLayout.LEADING

,
or

FlowLayout.TRAILING

.

**Parameters:** align

- the alignment value
**Parameters:** hgap

- the horizontal gap between components
and between the components and the
borders of the

Container
**Parameters:** vgap

- the vertical gap between components
and between the components and the
borders of the

Container

============ METHOD DETAIL ==========

- Method Detail

- getAlignment

```java
public int getAlignment()
```

Gets the alignment for this layout.
Possible values are

FlowLayout.LEFT

,

FlowLayout.RIGHT

,

FlowLayout.CENTER

,

FlowLayout.LEADING

,
or

FlowLayout.TRAILING

.

**Returns:** the alignment value for this layout
**Since:** 1.1
**See Also:** setAlignment(int)

- setAlignment

```java
public void setAlignment​(int align)
```

Sets the alignment for this layout.
Possible values are

- FlowLayout.LEFT

FlowLayout.RIGHT

FlowLayout.CENTER

FlowLayout.LEADING

FlowLayout.TRAILING

**Parameters:** align

- one of the alignment values shown above
**Since:** 1.1
**See Also:** getAlignment()

- getHgap

```java
public int getHgap()
```

Gets the horizontal gap between components
and between the components and the borders
of the

Container

**Returns:** the horizontal gap between components
and between the components and the borders
of the

Container
**Since:** 1.1
**See Also:** setHgap(int)

- setHgap

```java
public void setHgap​(int hgap)
```

Sets the horizontal gap between components and
between the components and the borders of the

Container

.

**Parameters:** hgap

- the horizontal gap between components
and between the components and the borders
of the

Container
**Since:** 1.1
**See Also:** getHgap()

- getVgap

```java
public int getVgap()
```

Gets the vertical gap between components and
between the components and the borders of the

Container

.

**Returns:** the vertical gap between components
and between the components and the borders
of the

Container
**Since:** 1.1
**See Also:** setVgap(int)

- setVgap

```java
public void setVgap​(int vgap)
```

Sets the vertical gap between components and between
the components and the borders of the

Container

.

**Parameters:** vgap

- the vertical gap between components
and between the components and the borders
of the

Container
**Since:** 1.1
**See Also:** getVgap()

- setAlignOnBaseline

```java
public void setAlignOnBaseline​(boolean alignOnBaseline)
```

Sets whether or not components should be vertically aligned along their
baseline. Components that do not have a baseline will be centered.
The default is false.

**Parameters:** alignOnBaseline

- whether or not components should be
vertically aligned on their baseline
**Since:** 1.6

- getAlignOnBaseline

```java
public boolean getAlignOnBaseline()
```

Returns true if components are to be vertically aligned along
their baseline. The default is false.

**Returns:** true if components are to be vertically aligned along
their baseline
**Since:** 1.6

- addLayoutComponent

```java
public void addLayoutComponent​(
String
name,

Component
comp)
```

Adds the specified component to the layout.
Not used by this class.

**Specified by:** addLayoutComponent

in interface

LayoutManager
**Parameters:** name

- the name of the component
**Parameters:** comp

- the component to be added

- removeLayoutComponent

```java
public void removeLayoutComponent​(
Component
comp)
```

Removes the specified component from the layout.
Not used by this class.

**Specified by:** removeLayoutComponent

in interface

LayoutManager
**Parameters:** comp

- the component to remove
**See Also:** Container.removeAll()

- preferredLayoutSize

```java
public
Dimension
preferredLayoutSize​(
Container
target)
```

Returns the preferred dimensions for this layout given the

visible

components in the specified target container.

**Specified by:** preferredLayoutSize

in interface

LayoutManager
**Parameters:** target

- the container that needs to be laid out
**Returns:** the preferred dimensions to lay out the
subcomponents of the specified container
**See Also:** Container

,

minimumLayoutSize(java.awt.Container)

,

Container.getPreferredSize()

- minimumLayoutSize

```java
public
Dimension
minimumLayoutSize​(
Container
target)
```

Returns the minimum dimensions needed to layout the

visible

components contained in the specified target container.

**Specified by:** minimumLayoutSize

in interface

LayoutManager
**Parameters:** target

- the container that needs to be laid out
**Returns:** the minimum dimensions to lay out the
subcomponents of the specified container
**See Also:** preferredLayoutSize(java.awt.Container)

,

Container

,

Container.doLayout()

- layoutContainer

```java
public void layoutContainer​(
Container
target)
```

Lays out the container. This method lets each

visible

component take
its preferred size by reshaping the components in the
target container in order to satisfy the alignment of
this

FlowLayout

object.

**Specified by:** layoutContainer

in interface

LayoutManager
**Parameters:** target

- the specified component being laid out
**See Also:** Container

,

Container.doLayout()

- toString

```java
public
String
toString()
```

Returns a string representation of this

FlowLayout

object and its values.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this layout

Field Detail

- LEFT

```java
public static final int LEFT
```

This value indicates that each row of components
should be left-justified.

**See Also:** Constant Field Values

- CENTER

```java
public static final int CENTER
```

This value indicates that each row of components
should be centered.

**See Also:** Constant Field Values

- RIGHT

```java
public static final int RIGHT
```

This value indicates that each row of components
should be right-justified.

**See Also:** Constant Field Values

- LEADING

```java
public static final int LEADING
```

This value indicates that each row of components
should be justified to the leading edge of the container's
orientation, for example, to the left in left-to-right orientations.

**Since:** 1.2
**See Also:** Component.getComponentOrientation()

,

ComponentOrientation

,

Constant Field Values

- TRAILING

```java
public static final int TRAILING
```

This value indicates that each row of components
should be justified to the trailing edge of the container's
orientation, for example, to the right in left-to-right orientations.

**Since:** 1.2
**See Also:** Component.getComponentOrientation()

,

ComponentOrientation

,

Constant Field Values

---

#### Field Detail

LEFT

```java
public static final int LEFT
```

This value indicates that each row of components
should be left-justified.

**See Also:** Constant Field Values

---

#### LEFT

public static final int LEFT

This value indicates that each row of components
should be left-justified.

CENTER

```java
public static final int CENTER
```

This value indicates that each row of components
should be centered.

**See Also:** Constant Field Values

---

#### CENTER

public static final int CENTER

This value indicates that each row of components
should be centered.

RIGHT

```java
public static final int RIGHT
```

This value indicates that each row of components
should be right-justified.

**See Also:** Constant Field Values

---

#### RIGHT

public static final int RIGHT

This value indicates that each row of components
should be right-justified.

LEADING

```java
public static final int LEADING
```

This value indicates that each row of components
should be justified to the leading edge of the container's
orientation, for example, to the left in left-to-right orientations.

**Since:** 1.2
**See Also:** Component.getComponentOrientation()

,

ComponentOrientation

,

Constant Field Values

---

#### LEADING

public static final int LEADING

This value indicates that each row of components
should be justified to the leading edge of the container's
orientation, for example, to the left in left-to-right orientations.

TRAILING

```java
public static final int TRAILING
```

This value indicates that each row of components
should be justified to the trailing edge of the container's
orientation, for example, to the right in left-to-right orientations.

**Since:** 1.2
**See Also:** Component.getComponentOrientation()

,

ComponentOrientation

,

Constant Field Values

---

#### TRAILING

public static final int TRAILING

This value indicates that each row of components
should be justified to the trailing edge of the container's
orientation, for example, to the right in left-to-right orientations.

Constructor Detail

- FlowLayout

```java
public FlowLayout()
```

Constructs a new

FlowLayout

with a centered alignment and a
default 5-unit horizontal and vertical gap.

- FlowLayout

```java
public FlowLayout​(int align)
```

Constructs a new

FlowLayout

with the specified
alignment and a default 5-unit horizontal and vertical gap.
The value of the alignment argument must be one of

FlowLayout.LEFT

,

FlowLayout.RIGHT

,

FlowLayout.CENTER

,

FlowLayout.LEADING

,
or

FlowLayout.TRAILING

.

**Parameters:** align

- the alignment value

- FlowLayout

```java
public FlowLayout​(int align,
int hgap,
int vgap)
```

Creates a new flow layout manager with the indicated alignment
and the indicated horizontal and vertical gaps.

The value of the alignment argument must be one of

FlowLayout.LEFT

,

FlowLayout.RIGHT

,

FlowLayout.CENTER

,

FlowLayout.LEADING

,
or

FlowLayout.TRAILING

.

**Parameters:** align

- the alignment value
**Parameters:** hgap

- the horizontal gap between components
and between the components and the
borders of the

Container
**Parameters:** vgap

- the vertical gap between components
and between the components and the
borders of the

Container

---

#### Constructor Detail

FlowLayout

```java
public FlowLayout()
```

Constructs a new

FlowLayout

with a centered alignment and a
default 5-unit horizontal and vertical gap.

---

#### FlowLayout

public FlowLayout()

Constructs a new

FlowLayout

with a centered alignment and a
default 5-unit horizontal and vertical gap.

FlowLayout

```java
public FlowLayout​(int align)
```

Constructs a new

FlowLayout

with the specified
alignment and a default 5-unit horizontal and vertical gap.
The value of the alignment argument must be one of

FlowLayout.LEFT

,

FlowLayout.RIGHT

,

FlowLayout.CENTER

,

FlowLayout.LEADING

,
or

FlowLayout.TRAILING

.

**Parameters:** align

- the alignment value

---

#### FlowLayout

public FlowLayout​(int align)

Constructs a new

FlowLayout

with the specified
alignment and a default 5-unit horizontal and vertical gap.
The value of the alignment argument must be one of

FlowLayout.LEFT

,

FlowLayout.RIGHT

,

FlowLayout.CENTER

,

FlowLayout.LEADING

,
or

FlowLayout.TRAILING

.

FlowLayout

```java
public FlowLayout​(int align,
int hgap,
int vgap)
```

Creates a new flow layout manager with the indicated alignment
and the indicated horizontal and vertical gaps.

The value of the alignment argument must be one of

FlowLayout.LEFT

,

FlowLayout.RIGHT

,

FlowLayout.CENTER

,

FlowLayout.LEADING

,
or

FlowLayout.TRAILING

.

**Parameters:** align

- the alignment value
**Parameters:** hgap

- the horizontal gap between components
and between the components and the
borders of the

Container
**Parameters:** vgap

- the vertical gap between components
and between the components and the
borders of the

Container

---

#### FlowLayout

public FlowLayout​(int align,
int hgap,
int vgap)

Creates a new flow layout manager with the indicated alignment
and the indicated horizontal and vertical gaps.

The value of the alignment argument must be one of

FlowLayout.LEFT

,

FlowLayout.RIGHT

,

FlowLayout.CENTER

,

FlowLayout.LEADING

,
or

FlowLayout.TRAILING

.

The value of the alignment argument must be one of

FlowLayout.LEFT

,

FlowLayout.RIGHT

,

FlowLayout.CENTER

,

FlowLayout.LEADING

,
or

FlowLayout.TRAILING

.

Method Detail

- getAlignment

```java
public int getAlignment()
```

Gets the alignment for this layout.
Possible values are

FlowLayout.LEFT

,

FlowLayout.RIGHT

,

FlowLayout.CENTER

,

FlowLayout.LEADING

,
or

FlowLayout.TRAILING

.

**Returns:** the alignment value for this layout
**Since:** 1.1
**See Also:** setAlignment(int)

- setAlignment

```java
public void setAlignment​(int align)
```

Sets the alignment for this layout.
Possible values are

- FlowLayout.LEFT

FlowLayout.RIGHT

FlowLayout.CENTER

FlowLayout.LEADING

FlowLayout.TRAILING

**Parameters:** align

- one of the alignment values shown above
**Since:** 1.1
**See Also:** getAlignment()

- getHgap

```java
public int getHgap()
```

Gets the horizontal gap between components
and between the components and the borders
of the

Container

**Returns:** the horizontal gap between components
and between the components and the borders
of the

Container
**Since:** 1.1
**See Also:** setHgap(int)

- setHgap

```java
public void setHgap​(int hgap)
```

Sets the horizontal gap between components and
between the components and the borders of the

Container

.

**Parameters:** hgap

- the horizontal gap between components
and between the components and the borders
of the

Container
**Since:** 1.1
**See Also:** getHgap()

- getVgap

```java
public int getVgap()
```

Gets the vertical gap between components and
between the components and the borders of the

Container

.

**Returns:** the vertical gap between components
and between the components and the borders
of the

Container
**Since:** 1.1
**See Also:** setVgap(int)

- setVgap

```java
public void setVgap​(int vgap)
```

Sets the vertical gap between components and between
the components and the borders of the

Container

.

**Parameters:** vgap

- the vertical gap between components
and between the components and the borders
of the

Container
**Since:** 1.1
**See Also:** getVgap()

- setAlignOnBaseline

```java
public void setAlignOnBaseline​(boolean alignOnBaseline)
```

Sets whether or not components should be vertically aligned along their
baseline. Components that do not have a baseline will be centered.
The default is false.

**Parameters:** alignOnBaseline

- whether or not components should be
vertically aligned on their baseline
**Since:** 1.6

- getAlignOnBaseline

```java
public boolean getAlignOnBaseline()
```

Returns true if components are to be vertically aligned along
their baseline. The default is false.

**Returns:** true if components are to be vertically aligned along
their baseline
**Since:** 1.6

- addLayoutComponent

```java
public void addLayoutComponent​(
String
name,

Component
comp)
```

Adds the specified component to the layout.
Not used by this class.

**Specified by:** addLayoutComponent

in interface

LayoutManager
**Parameters:** name

- the name of the component
**Parameters:** comp

- the component to be added

- removeLayoutComponent

```java
public void removeLayoutComponent​(
Component
comp)
```

Removes the specified component from the layout.
Not used by this class.

**Specified by:** removeLayoutComponent

in interface

LayoutManager
**Parameters:** comp

- the component to remove
**See Also:** Container.removeAll()

- preferredLayoutSize

```java
public
Dimension
preferredLayoutSize​(
Container
target)
```

Returns the preferred dimensions for this layout given the

visible

components in the specified target container.

**Specified by:** preferredLayoutSize

in interface

LayoutManager
**Parameters:** target

- the container that needs to be laid out
**Returns:** the preferred dimensions to lay out the
subcomponents of the specified container
**See Also:** Container

,

minimumLayoutSize(java.awt.Container)

,

Container.getPreferredSize()

- minimumLayoutSize

```java
public
Dimension
minimumLayoutSize​(
Container
target)
```

Returns the minimum dimensions needed to layout the

visible

components contained in the specified target container.

**Specified by:** minimumLayoutSize

in interface

LayoutManager
**Parameters:** target

- the container that needs to be laid out
**Returns:** the minimum dimensions to lay out the
subcomponents of the specified container
**See Also:** preferredLayoutSize(java.awt.Container)

,

Container

,

Container.doLayout()

- layoutContainer

```java
public void layoutContainer​(
Container
target)
```

Lays out the container. This method lets each

visible

component take
its preferred size by reshaping the components in the
target container in order to satisfy the alignment of
this

FlowLayout

object.

**Specified by:** layoutContainer

in interface

LayoutManager
**Parameters:** target

- the specified component being laid out
**See Also:** Container

,

Container.doLayout()

- toString

```java
public
String
toString()
```

Returns a string representation of this

FlowLayout

object and its values.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this layout

---

#### Method Detail

getAlignment

```java
public int getAlignment()
```

Gets the alignment for this layout.
Possible values are

FlowLayout.LEFT

,

FlowLayout.RIGHT

,

FlowLayout.CENTER

,

FlowLayout.LEADING

,
or

FlowLayout.TRAILING

.

**Returns:** the alignment value for this layout
**Since:** 1.1
**See Also:** setAlignment(int)

---

#### getAlignment

public int getAlignment()

Gets the alignment for this layout.
Possible values are

FlowLayout.LEFT

,

FlowLayout.RIGHT

,

FlowLayout.CENTER

,

FlowLayout.LEADING

,
or

FlowLayout.TRAILING

.

setAlignment

```java
public void setAlignment​(int align)
```

Sets the alignment for this layout.
Possible values are

- FlowLayout.LEFT

FlowLayout.RIGHT

FlowLayout.CENTER

FlowLayout.LEADING

FlowLayout.TRAILING

**Parameters:** align

- one of the alignment values shown above
**Since:** 1.1
**See Also:** getAlignment()

---

#### setAlignment

public void setAlignment​(int align)

Sets the alignment for this layout.
Possible values are

- FlowLayout.LEFT

FlowLayout.RIGHT

FlowLayout.CENTER

FlowLayout.LEADING

FlowLayout.TRAILING

FlowLayout.LEFT

FlowLayout.RIGHT

FlowLayout.CENTER

FlowLayout.LEADING

FlowLayout.TRAILING

getHgap

```java
public int getHgap()
```

Gets the horizontal gap between components
and between the components and the borders
of the

Container

**Returns:** the horizontal gap between components
and between the components and the borders
of the

Container
**Since:** 1.1
**See Also:** setHgap(int)

---

#### getHgap

public int getHgap()

Gets the horizontal gap between components
and between the components and the borders
of the

Container

setHgap

```java
public void setHgap​(int hgap)
```

Sets the horizontal gap between components and
between the components and the borders of the

Container

.

**Parameters:** hgap

- the horizontal gap between components
and between the components and the borders
of the

Container
**Since:** 1.1
**See Also:** getHgap()

---

#### setHgap

public void setHgap​(int hgap)

Sets the horizontal gap between components and
between the components and the borders of the

Container

.

getVgap

```java
public int getVgap()
```

Gets the vertical gap between components and
between the components and the borders of the

Container

.

**Returns:** the vertical gap between components
and between the components and the borders
of the

Container
**Since:** 1.1
**See Also:** setVgap(int)

---

#### getVgap

public int getVgap()

Gets the vertical gap between components and
between the components and the borders of the

Container

.

setVgap

```java
public void setVgap​(int vgap)
```

Sets the vertical gap between components and between
the components and the borders of the

Container

.

**Parameters:** vgap

- the vertical gap between components
and between the components and the borders
of the

Container
**Since:** 1.1
**See Also:** getVgap()

---

#### setVgap

public void setVgap​(int vgap)

Sets the vertical gap between components and between
the components and the borders of the

Container

.

setAlignOnBaseline

```java
public void setAlignOnBaseline​(boolean alignOnBaseline)
```

Sets whether or not components should be vertically aligned along their
baseline. Components that do not have a baseline will be centered.
The default is false.

**Parameters:** alignOnBaseline

- whether or not components should be
vertically aligned on their baseline
**Since:** 1.6

---

#### setAlignOnBaseline

public void setAlignOnBaseline​(boolean alignOnBaseline)

Sets whether or not components should be vertically aligned along their
baseline. Components that do not have a baseline will be centered.
The default is false.

getAlignOnBaseline

```java
public boolean getAlignOnBaseline()
```

Returns true if components are to be vertically aligned along
their baseline. The default is false.

**Returns:** true if components are to be vertically aligned along
their baseline
**Since:** 1.6

---

#### getAlignOnBaseline

public boolean getAlignOnBaseline()

Returns true if components are to be vertically aligned along
their baseline. The default is false.

addLayoutComponent

```java
public void addLayoutComponent​(
String
name,

Component
comp)
```

Adds the specified component to the layout.
Not used by this class.

**Specified by:** addLayoutComponent

in interface

LayoutManager
**Parameters:** name

- the name of the component
**Parameters:** comp

- the component to be added

---

#### addLayoutComponent

public void addLayoutComponent​(

String

name,

Component

comp)

Adds the specified component to the layout.
Not used by this class.

removeLayoutComponent

```java
public void removeLayoutComponent​(
Component
comp)
```

Removes the specified component from the layout.
Not used by this class.

**Specified by:** removeLayoutComponent

in interface

LayoutManager
**Parameters:** comp

- the component to remove
**See Also:** Container.removeAll()

---

#### removeLayoutComponent

public void removeLayoutComponent​(

Component

comp)

Removes the specified component from the layout.
Not used by this class.

preferredLayoutSize

```java
public
Dimension
preferredLayoutSize​(
Container
target)
```

Returns the preferred dimensions for this layout given the

visible

components in the specified target container.

**Specified by:** preferredLayoutSize

in interface

LayoutManager
**Parameters:** target

- the container that needs to be laid out
**Returns:** the preferred dimensions to lay out the
subcomponents of the specified container
**See Also:** Container

,

minimumLayoutSize(java.awt.Container)

,

Container.getPreferredSize()

---

#### preferredLayoutSize

public

Dimension

preferredLayoutSize​(

Container

target)

Returns the preferred dimensions for this layout given the

visible

components in the specified target container.

minimumLayoutSize

```java
public
Dimension
minimumLayoutSize​(
Container
target)
```

Returns the minimum dimensions needed to layout the

visible

components contained in the specified target container.

**Specified by:** minimumLayoutSize

in interface

LayoutManager
**Parameters:** target

- the container that needs to be laid out
**Returns:** the minimum dimensions to lay out the
subcomponents of the specified container
**See Also:** preferredLayoutSize(java.awt.Container)

,

Container

,

Container.doLayout()

---

#### minimumLayoutSize

public

Dimension

minimumLayoutSize​(

Container

target)

Returns the minimum dimensions needed to layout the

visible

components contained in the specified target container.

layoutContainer

```java
public void layoutContainer​(
Container
target)
```

Lays out the container. This method lets each

visible

component take
its preferred size by reshaping the components in the
target container in order to satisfy the alignment of
this

FlowLayout

object.

**Specified by:** layoutContainer

in interface

LayoutManager
**Parameters:** target

- the specified component being laid out
**See Also:** Container

,

Container.doLayout()

---

#### layoutContainer

public void layoutContainer​(

Container

target)

Lays out the container. This method lets each

visible

component take
its preferred size by reshaping the components in the
target container in order to satisfy the alignment of
this

FlowLayout

object.

toString

```java
public
String
toString()
```

Returns a string representation of this

FlowLayout

object and its values.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this layout

---

#### toString

public

String

toString()

Returns a string representation of this

FlowLayout

object and its values.

---

