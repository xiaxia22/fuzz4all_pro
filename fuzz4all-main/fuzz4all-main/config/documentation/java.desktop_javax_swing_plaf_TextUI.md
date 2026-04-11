# Class TextUI

**Source:** `java.desktop\javax\swing\plaf\TextUI.html`

### Class Description

```java
public abstract class
TextUI

extends
ComponentUI
```

Text editor user interface

**Direct Known Subclasses:** BasicTextUI

,

MultiTextUI

---

### Field Details

*No entries found.*

### Constructor Details

#### public TextUI()

*No description found.*

---

### Method Details

#### @Deprecated
(
since
="9")
public abstract
Rectangle
modelToView​(
JTextComponent
t,
int pos)
throws
BadLocationException

Converts the given location in the model to a place in
the view coordinate system.

**Parameters:**
- t

- the text component for which this UI is installed
- pos

- the local location in the model to translate >= 0

**Returns:**
- the coordinates as a

Rectangle

**Throws:**
- BadLocationException

- if the given position does not
represent a valid location in the associated document

---

#### @Deprecated
(
since
="9")
public abstract
Rectangle
modelToView​(
JTextComponent
t,
int pos,

Position.Bias
bias)
throws
BadLocationException

Converts the given location in the model to a place in
the view coordinate system.

**Parameters:**
- t

- the text component for which this UI is installed
- pos

- the local location in the model to translate >= 0
- bias

- the bias for the position

**Returns:**
- the coordinates as a

Rectangle

**Throws:**
- BadLocationException

- if the given position does not
represent a valid location in the associated document

---

#### public
Rectangle2D
modelToView2D​(
JTextComponent
t,
int pos,

Position.Bias
bias)
throws
BadLocationException

Converts the given location in the model to a place in
the view coordinate system.

**Parameters:**
- t

- the text component for which this UI is installed
- pos

- the local location in the model to translate

>= 0
- bias

- the bias for the position

**Returns:**
- the coordinates as a

Rectangle2D

**Throws:**
- BadLocationException

- if the given position does not
represent a valid location in the associated document

**Since:**
- 9

**Implementation Requirements:**
- This implementation calls

modelToView(t, pos, bias)

.

---

#### @Deprecated
(
since
="9")
public abstract int viewToModel​(
JTextComponent
t,

Point
pt)

Converts the given place in the view coordinate system
to the nearest representative location in the model.

**Parameters:**
- t

- the text component for which this UI is installed
- pt

- the location in the view to translate. This
should be in the same coordinate system as the mouse
events.

**Returns:**
- the offset from the start of the document >= 0

---

#### @Deprecated
(
since
="9")
public abstract int viewToModel​(
JTextComponent
t,

Point
pt,

Position.Bias
[] biasReturn)

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

**Parameters:**
- t

- the text component for which this UI is installed
- pt

- the location in the view to translate.
This should be in the same coordinate system
as the mouse events.
- biasReturn

- filled in by this method to indicate whether
the point given is closer to the previous or the next
character in the model

**Returns:**
- the location within the model that best represents the
given point in the view >= 0

---

#### public int viewToModel2D​(
JTextComponent
t,

Point2D
pt,

Position.Bias
[] biasReturn)

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

**Parameters:**
- t

- the text component for which this UI is installed
- pt

- the location in the view to translate.
- biasReturn

- filled in by this method to indicate whether
the point given is closer to the previous or the next
character in the model

**Returns:**
- the location within the model that best represents the
given point in the view

>= 0

**Since:**
- 9

**Implementation Requirements:**
- This implementation calls

viewToModel(t, new Point((int) pt.getX(), (int) pt.getY()),
biasReturn)

.

---

#### public abstract int getNextVisualPositionFrom​(
JTextComponent
t,
int pos,

Position.Bias
b,
int direction,

Position.Bias
[] biasRet)
throws
BadLocationException

Provides a way to determine the next visually represented model
location that one might place a caret. Some views may not be visible,
they might not be in the same order found in the model, or they just
might not allow access to some of the locations in the model.

**Parameters:**
- t

- the text component for which this UI is installed
- pos

- the position to convert >= 0
- b

- the bias for the position
- direction

- the direction from the current position that can
be thought of as the arrow keys typically found on a keyboard.
This may be SwingConstants.WEST, SwingConstants.EAST,
SwingConstants.NORTH, or SwingConstants.SOUTH
- biasRet

- an array to contain the bias for the returned position

**Returns:**
- the location within the model that best represents the next
location visual position

**Throws:**
- BadLocationException

- for a bad location within a document model
- IllegalArgumentException

- for an invalid direction

---

#### public abstract void damageRange​(
JTextComponent
t,
int p0,
int p1)

Causes the portion of the view responsible for the
given part of the model to be repainted.

**Parameters:**
- t

- the text component for which this UI is installed
- p0

- the beginning of the range >= 0
- p1

- the end of the range >= p0

---

#### public abstract void damageRange​(
JTextComponent
t,
int p0,
int p1,

Position.Bias
firstBias,

Position.Bias
secondBias)

Causes the portion of the view responsible for the
given part of the model to be repainted.

**Parameters:**
- t

- the text component for which this UI is installed
- p0

- the beginning of the range >= 0
- p1

- the end of the range >= p0
- firstBias

- the bias of the first character position, toward the
previous character or the next character
- secondBias

- the bias of the second character position, toward the
previous character or the next character

---

#### public abstract
EditorKit
getEditorKit​(
JTextComponent
t)

Fetches the binding of services that set a policy
for the type of document being edited. This contains
things like the commands available, stream readers and
writers, etc.

**Parameters:**
- t

- the text component for which this UI is installed

**Returns:**
- the editor kit binding

---

#### public abstract
View
getRootView​(
JTextComponent
t)

Fetches a View with the allocation of the associated
text component (i.e. the root of the hierarchy) that
can be traversed to determine how the model is being
represented spatially.

**Parameters:**
- t

- the text component for which this UI is installed

**Returns:**
- a

View

with the allocation of the associated
text component

---

#### @Deprecated
(
since
="9")
public
String
getToolTipText​(
JTextComponent
t,

Point
pt)

Returns the string to be used as the tooltip at the passed in location.

**Parameters:**
- t

- the text component for which this UI is installed
- pt

- a

Point

specifying location for which to get a tooltip

**Returns:**
- a

String

containing the tooltip

**See Also:**
- JTextComponent.getToolTipText(java.awt.event.MouseEvent)

**Since:**
- 1.4

---

#### public
String
getToolTipText2D​(
JTextComponent
t,

Point2D
pt)

Returns the string to be used as the tooltip at the passed in location.

**Parameters:**
- t

- the text component for which this UI is installed
- pt

- a

Point

specifying location for which to get a tooltip

**Returns:**
- a

String

containing the tooltip

**See Also:**
- JTextComponent.getToolTipText(java.awt.event.MouseEvent)

**Since:**
- 9

**Implementation Requirements:**
- This implementation calls

getToolTipText(t, new Point((int) pt.getX(), (int) pt.getY())))

.

---

### Additional Sections

#### Class TextUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.TextUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.TextUI

javax.swing.plaf.TextUI

**Direct Known Subclasses:** BasicTextUI

,

MultiTextUI

```java
public abstract class
TextUI

extends
ComponentUI
```

Text editor user interface

public abstract class

TextUI

extends

ComponentUI

Text editor user interface

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

TextUI

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

abstract void

damageRange

​(

JTextComponent

t,
int p0,
int p1)

Causes the portion of the view responsible for the
given part of the model to be repainted.

abstract void

damageRange

​(

JTextComponent

t,
int p0,
int p1,

Position.Bias

firstBias,

Position.Bias

secondBias)

Causes the portion of the view responsible for the
given part of the model to be repainted.

abstract

EditorKit

getEditorKit

​(

JTextComponent

t)

Fetches the binding of services that set a policy
for the type of document being edited.

abstract int

getNextVisualPositionFrom

​(

JTextComponent

t,
int pos,

Position.Bias

b,
int direction,

Position.Bias

[] biasRet)

Provides a way to determine the next visually represented model
location that one might place a caret.

abstract

View

getRootView

​(

JTextComponent

t)

Fetches a View with the allocation of the associated
text component (i.e. the root of the hierarchy) that
can be traversed to determine how the model is being
represented spatially.

String

getToolTipText

​(

JTextComponent

t,

Point

pt)

Deprecated.

replaced by

getToolTipText2D(JTextComponent, Point2D)

String

getToolTipText2D

​(

JTextComponent

t,

Point2D

pt)

Returns the string to be used as the tooltip at the passed in location.

abstract

Rectangle

modelToView

​(

JTextComponent

t,
int pos)

Deprecated.

replaced by

modelToView2D(JTextComponent, int, Position.Bias)

abstract

Rectangle

modelToView

​(

JTextComponent

t,
int pos,

Position.Bias

bias)

Deprecated.

replaced by

modelToView2D(JTextComponent, int, Position.Bias)

Rectangle2D

modelToView2D

​(

JTextComponent

t,
int pos,

Position.Bias

bias)

Converts the given location in the model to a place in
the view coordinate system.

abstract int

viewToModel

​(

JTextComponent

t,

Point

pt)

Deprecated.

replaced by

viewToModel2D(JTextComponent, Point2D, Position.Bias[])

abstract int

viewToModel

​(

JTextComponent

t,

Point

pt,

Position.Bias

[] biasReturn)

Deprecated.

replaced by

viewToModel2D(JTextComponent, Point2D, Position.Bias[])

int

viewToModel2D

​(

JTextComponent

t,

Point2D

pt,

Position.Bias

[] biasReturn)

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

createUI

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getBaseline

,

getBaselineResizeBehavior

,

getMaximumSize

,

getMinimumSize

,

getPreferredSize

,

installUI

,

paint

,

uninstallUI

,

update

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

TextUI

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

abstract void

damageRange

​(

JTextComponent

t,
int p0,
int p1)

Causes the portion of the view responsible for the
given part of the model to be repainted.

abstract void

damageRange

​(

JTextComponent

t,
int p0,
int p1,

Position.Bias

firstBias,

Position.Bias

secondBias)

Causes the portion of the view responsible for the
given part of the model to be repainted.

abstract

EditorKit

getEditorKit

​(

JTextComponent

t)

Fetches the binding of services that set a policy
for the type of document being edited.

abstract int

getNextVisualPositionFrom

​(

JTextComponent

t,
int pos,

Position.Bias

b,
int direction,

Position.Bias

[] biasRet)

Provides a way to determine the next visually represented model
location that one might place a caret.

abstract

View

getRootView

​(

JTextComponent

t)

Fetches a View with the allocation of the associated
text component (i.e. the root of the hierarchy) that
can be traversed to determine how the model is being
represented spatially.

String

getToolTipText

​(

JTextComponent

t,

Point

pt)

Deprecated.

replaced by

getToolTipText2D(JTextComponent, Point2D)

String

getToolTipText2D

​(

JTextComponent

t,

Point2D

pt)

Returns the string to be used as the tooltip at the passed in location.

abstract

Rectangle

modelToView

​(

JTextComponent

t,
int pos)

Deprecated.

replaced by

modelToView2D(JTextComponent, int, Position.Bias)

abstract

Rectangle

modelToView

​(

JTextComponent

t,
int pos,

Position.Bias

bias)

Deprecated.

replaced by

modelToView2D(JTextComponent, int, Position.Bias)

Rectangle2D

modelToView2D

​(

JTextComponent

t,
int pos,

Position.Bias

bias)

Converts the given location in the model to a place in
the view coordinate system.

abstract int

viewToModel

​(

JTextComponent

t,

Point

pt)

Deprecated.

replaced by

viewToModel2D(JTextComponent, Point2D, Position.Bias[])

abstract int

viewToModel

​(

JTextComponent

t,

Point

pt,

Position.Bias

[] biasReturn)

Deprecated.

replaced by

viewToModel2D(JTextComponent, Point2D, Position.Bias[])

int

viewToModel2D

​(

JTextComponent

t,

Point2D

pt,

Position.Bias

[] biasReturn)

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

createUI

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getBaseline

,

getBaselineResizeBehavior

,

getMaximumSize

,

getMinimumSize

,

getPreferredSize

,

installUI

,

paint

,

uninstallUI

,

update

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

Causes the portion of the view responsible for the
given part of the model to be repainted.

Fetches the binding of services that set a policy
for the type of document being edited.

Provides a way to determine the next visually represented model
location that one might place a caret.

Fetches a View with the allocation of the associated
text component (i.e. the root of the hierarchy) that
can be traversed to determine how the model is being
represented spatially.

Deprecated.

replaced by

getToolTipText2D(JTextComponent, Point2D)

Returns the string to be used as the tooltip at the passed in location.

Deprecated.

replaced by

modelToView2D(JTextComponent, int, Position.Bias)

Converts the given location in the model to a place in
the view coordinate system.

Deprecated.

replaced by

viewToModel2D(JTextComponent, Point2D, Position.Bias[])

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

createUI

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getBaseline

,

getBaselineResizeBehavior

,

getMaximumSize

,

getMinimumSize

,

getPreferredSize

,

installUI

,

paint

,

uninstallUI

,

update

---

#### Methods declared in class javax.swing.plaf. ComponentUI

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

- TextUI

```java
public TextUI()
```

============ METHOD DETAIL ==========

- Method Detail

- modelToView

```java
@Deprecated
(
since
="9")
public abstract
Rectangle
modelToView​(
JTextComponent
t,
int pos)
throws
BadLocationException
```

Deprecated.

replaced by

modelToView2D(JTextComponent, int, Position.Bias)

Converts the given location in the model to a place in
the view coordinate system.

**Parameters:** t

- the text component for which this UI is installed
**Parameters:** pos

- the local location in the model to translate >= 0
**Returns:** the coordinates as a

Rectangle
**Throws:** BadLocationException

- if the given position does not
represent a valid location in the associated document

- modelToView

```java
@Deprecated
(
since
="9")
public abstract
Rectangle
modelToView​(
JTextComponent
t,
int pos,

Position.Bias
bias)
throws
BadLocationException
```

Deprecated.

replaced by

modelToView2D(JTextComponent, int, Position.Bias)

Converts the given location in the model to a place in
the view coordinate system.

**Parameters:** t

- the text component for which this UI is installed
**Parameters:** pos

- the local location in the model to translate >= 0
**Parameters:** bias

- the bias for the position
**Returns:** the coordinates as a

Rectangle
**Throws:** BadLocationException

- if the given position does not
represent a valid location in the associated document

- modelToView2D

```java
public
Rectangle2D
modelToView2D​(
JTextComponent
t,
int pos,

Position.Bias
bias)
throws
BadLocationException
```

Converts the given location in the model to a place in
the view coordinate system.

**Implementation Requirements:** This implementation calls

modelToView(t, pos, bias)

.
**Parameters:** t

- the text component for which this UI is installed
**Parameters:** pos

- the local location in the model to translate

>= 0
**Parameters:** bias

- the bias for the position
**Returns:** the coordinates as a

Rectangle2D
**Throws:** BadLocationException

- if the given position does not
represent a valid location in the associated document
**Since:** 9

- viewToModel

```java
@Deprecated
(
since
="9")
public abstract int viewToModel​(
JTextComponent
t,

Point
pt)
```

Deprecated.

replaced by

viewToModel2D(JTextComponent, Point2D, Position.Bias[])

Converts the given place in the view coordinate system
to the nearest representative location in the model.

**Parameters:** t

- the text component for which this UI is installed
**Parameters:** pt

- the location in the view to translate. This
should be in the same coordinate system as the mouse
events.
**Returns:** the offset from the start of the document >= 0

- viewToModel

```java
@Deprecated
(
since
="9")
public abstract int viewToModel​(
JTextComponent
t,

Point
pt,

Position.Bias
[] biasReturn)
```

Deprecated.

replaced by

viewToModel2D(JTextComponent, Point2D, Position.Bias[])

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

**Parameters:** t

- the text component for which this UI is installed
**Parameters:** pt

- the location in the view to translate.
This should be in the same coordinate system
as the mouse events.
**Parameters:** biasReturn

- filled in by this method to indicate whether
the point given is closer to the previous or the next
character in the model
**Returns:** the location within the model that best represents the
given point in the view >= 0

- viewToModel2D

```java
public int viewToModel2D​(
JTextComponent
t,

Point2D
pt,

Position.Bias
[] biasReturn)
```

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

**Implementation Requirements:** This implementation calls

viewToModel(t, new Point((int) pt.getX(), (int) pt.getY()),
biasReturn)

.
**Parameters:** t

- the text component for which this UI is installed
**Parameters:** pt

- the location in the view to translate.
**Parameters:** biasReturn

- filled in by this method to indicate whether
the point given is closer to the previous or the next
character in the model
**Returns:** the location within the model that best represents the
given point in the view

>= 0
**Since:** 9

- getNextVisualPositionFrom

```java
public abstract int getNextVisualPositionFrom​(
JTextComponent
t,
int pos,

Position.Bias
b,
int direction,

Position.Bias
[] biasRet)
throws
BadLocationException
```

Provides a way to determine the next visually represented model
location that one might place a caret. Some views may not be visible,
they might not be in the same order found in the model, or they just
might not allow access to some of the locations in the model.

**Parameters:** t

- the text component for which this UI is installed
**Parameters:** pos

- the position to convert >= 0
**Parameters:** b

- the bias for the position
**Parameters:** direction

- the direction from the current position that can
be thought of as the arrow keys typically found on a keyboard.
This may be SwingConstants.WEST, SwingConstants.EAST,
SwingConstants.NORTH, or SwingConstants.SOUTH
**Parameters:** biasRet

- an array to contain the bias for the returned position
**Returns:** the location within the model that best represents the next
location visual position
**Throws:** BadLocationException

- for a bad location within a document model
**Throws:** IllegalArgumentException

- for an invalid direction

- damageRange

```java
public abstract void damageRange​(
JTextComponent
t,
int p0,
int p1)
```

Causes the portion of the view responsible for the
given part of the model to be repainted.

**Parameters:** t

- the text component for which this UI is installed
**Parameters:** p0

- the beginning of the range >= 0
**Parameters:** p1

- the end of the range >= p0

- damageRange

```java
public abstract void damageRange​(
JTextComponent
t,
int p0,
int p1,

Position.Bias
firstBias,

Position.Bias
secondBias)
```

Causes the portion of the view responsible for the
given part of the model to be repainted.

**Parameters:** t

- the text component for which this UI is installed
**Parameters:** p0

- the beginning of the range >= 0
**Parameters:** p1

- the end of the range >= p0
**Parameters:** firstBias

- the bias of the first character position, toward the
previous character or the next character
**Parameters:** secondBias

- the bias of the second character position, toward the
previous character or the next character

- getEditorKit

```java
public abstract
EditorKit
getEditorKit​(
JTextComponent
t)
```

Fetches the binding of services that set a policy
for the type of document being edited. This contains
things like the commands available, stream readers and
writers, etc.

**Parameters:** t

- the text component for which this UI is installed
**Returns:** the editor kit binding

- getRootView

```java
public abstract
View
getRootView​(
JTextComponent
t)
```

Fetches a View with the allocation of the associated
text component (i.e. the root of the hierarchy) that
can be traversed to determine how the model is being
represented spatially.

**Parameters:** t

- the text component for which this UI is installed
**Returns:** a

View

with the allocation of the associated
text component

- getToolTipText

```java
@Deprecated
(
since
="9")
public
String
getToolTipText​(
JTextComponent
t,

Point
pt)
```

Deprecated.

replaced by

getToolTipText2D(JTextComponent, Point2D)

Returns the string to be used as the tooltip at the passed in location.

**Parameters:** t

- the text component for which this UI is installed
**Parameters:** pt

- a

Point

specifying location for which to get a tooltip
**Returns:** a

String

containing the tooltip
**Since:** 1.4
**See Also:** JTextComponent.getToolTipText(java.awt.event.MouseEvent)

- getToolTipText2D

```java
public
String
getToolTipText2D​(
JTextComponent
t,

Point2D
pt)
```

Returns the string to be used as the tooltip at the passed in location.

**Implementation Requirements:** This implementation calls

getToolTipText(t, new Point((int) pt.getX(), (int) pt.getY())))

.
**Parameters:** t

- the text component for which this UI is installed
**Parameters:** pt

- a

Point

specifying location for which to get a tooltip
**Returns:** a

String

containing the tooltip
**Since:** 9
**See Also:** JTextComponent.getToolTipText(java.awt.event.MouseEvent)

Constructor Detail

- TextUI

```java
public TextUI()
```

---

#### Constructor Detail

TextUI

```java
public TextUI()
```

---

#### TextUI

public TextUI()

Method Detail

- modelToView

```java
@Deprecated
(
since
="9")
public abstract
Rectangle
modelToView​(
JTextComponent
t,
int pos)
throws
BadLocationException
```

Deprecated.

replaced by

modelToView2D(JTextComponent, int, Position.Bias)

Converts the given location in the model to a place in
the view coordinate system.

**Parameters:** t

- the text component for which this UI is installed
**Parameters:** pos

- the local location in the model to translate >= 0
**Returns:** the coordinates as a

Rectangle
**Throws:** BadLocationException

- if the given position does not
represent a valid location in the associated document

- modelToView

```java
@Deprecated
(
since
="9")
public abstract
Rectangle
modelToView​(
JTextComponent
t,
int pos,

Position.Bias
bias)
throws
BadLocationException
```

Deprecated.

replaced by

modelToView2D(JTextComponent, int, Position.Bias)

Converts the given location in the model to a place in
the view coordinate system.

**Parameters:** t

- the text component for which this UI is installed
**Parameters:** pos

- the local location in the model to translate >= 0
**Parameters:** bias

- the bias for the position
**Returns:** the coordinates as a

Rectangle
**Throws:** BadLocationException

- if the given position does not
represent a valid location in the associated document

- modelToView2D

```java
public
Rectangle2D
modelToView2D​(
JTextComponent
t,
int pos,

Position.Bias
bias)
throws
BadLocationException
```

Converts the given location in the model to a place in
the view coordinate system.

**Implementation Requirements:** This implementation calls

modelToView(t, pos, bias)

.
**Parameters:** t

- the text component for which this UI is installed
**Parameters:** pos

- the local location in the model to translate

>= 0
**Parameters:** bias

- the bias for the position
**Returns:** the coordinates as a

Rectangle2D
**Throws:** BadLocationException

- if the given position does not
represent a valid location in the associated document
**Since:** 9

- viewToModel

```java
@Deprecated
(
since
="9")
public abstract int viewToModel​(
JTextComponent
t,

Point
pt)
```

Deprecated.

replaced by

viewToModel2D(JTextComponent, Point2D, Position.Bias[])

Converts the given place in the view coordinate system
to the nearest representative location in the model.

**Parameters:** t

- the text component for which this UI is installed
**Parameters:** pt

- the location in the view to translate. This
should be in the same coordinate system as the mouse
events.
**Returns:** the offset from the start of the document >= 0

- viewToModel

```java
@Deprecated
(
since
="9")
public abstract int viewToModel​(
JTextComponent
t,

Point
pt,

Position.Bias
[] biasReturn)
```

Deprecated.

replaced by

viewToModel2D(JTextComponent, Point2D, Position.Bias[])

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

**Parameters:** t

- the text component for which this UI is installed
**Parameters:** pt

- the location in the view to translate.
This should be in the same coordinate system
as the mouse events.
**Parameters:** biasReturn

- filled in by this method to indicate whether
the point given is closer to the previous or the next
character in the model
**Returns:** the location within the model that best represents the
given point in the view >= 0

- viewToModel2D

```java
public int viewToModel2D​(
JTextComponent
t,

Point2D
pt,

Position.Bias
[] biasReturn)
```

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

**Implementation Requirements:** This implementation calls

viewToModel(t, new Point((int) pt.getX(), (int) pt.getY()),
biasReturn)

.
**Parameters:** t

- the text component for which this UI is installed
**Parameters:** pt

- the location in the view to translate.
**Parameters:** biasReturn

- filled in by this method to indicate whether
the point given is closer to the previous or the next
character in the model
**Returns:** the location within the model that best represents the
given point in the view

>= 0
**Since:** 9

- getNextVisualPositionFrom

```java
public abstract int getNextVisualPositionFrom​(
JTextComponent
t,
int pos,

Position.Bias
b,
int direction,

Position.Bias
[] biasRet)
throws
BadLocationException
```

Provides a way to determine the next visually represented model
location that one might place a caret. Some views may not be visible,
they might not be in the same order found in the model, or they just
might not allow access to some of the locations in the model.

**Parameters:** t

- the text component for which this UI is installed
**Parameters:** pos

- the position to convert >= 0
**Parameters:** b

- the bias for the position
**Parameters:** direction

- the direction from the current position that can
be thought of as the arrow keys typically found on a keyboard.
This may be SwingConstants.WEST, SwingConstants.EAST,
SwingConstants.NORTH, or SwingConstants.SOUTH
**Parameters:** biasRet

- an array to contain the bias for the returned position
**Returns:** the location within the model that best represents the next
location visual position
**Throws:** BadLocationException

- for a bad location within a document model
**Throws:** IllegalArgumentException

- for an invalid direction

- damageRange

```java
public abstract void damageRange​(
JTextComponent
t,
int p0,
int p1)
```

Causes the portion of the view responsible for the
given part of the model to be repainted.

**Parameters:** t

- the text component for which this UI is installed
**Parameters:** p0

- the beginning of the range >= 0
**Parameters:** p1

- the end of the range >= p0

- damageRange

```java
public abstract void damageRange​(
JTextComponent
t,
int p0,
int p1,

Position.Bias
firstBias,

Position.Bias
secondBias)
```

Causes the portion of the view responsible for the
given part of the model to be repainted.

**Parameters:** t

- the text component for which this UI is installed
**Parameters:** p0

- the beginning of the range >= 0
**Parameters:** p1

- the end of the range >= p0
**Parameters:** firstBias

- the bias of the first character position, toward the
previous character or the next character
**Parameters:** secondBias

- the bias of the second character position, toward the
previous character or the next character

- getEditorKit

```java
public abstract
EditorKit
getEditorKit​(
JTextComponent
t)
```

Fetches the binding of services that set a policy
for the type of document being edited. This contains
things like the commands available, stream readers and
writers, etc.

**Parameters:** t

- the text component for which this UI is installed
**Returns:** the editor kit binding

- getRootView

```java
public abstract
View
getRootView​(
JTextComponent
t)
```

Fetches a View with the allocation of the associated
text component (i.e. the root of the hierarchy) that
can be traversed to determine how the model is being
represented spatially.

**Parameters:** t

- the text component for which this UI is installed
**Returns:** a

View

with the allocation of the associated
text component

- getToolTipText

```java
@Deprecated
(
since
="9")
public
String
getToolTipText​(
JTextComponent
t,

Point
pt)
```

Deprecated.

replaced by

getToolTipText2D(JTextComponent, Point2D)

Returns the string to be used as the tooltip at the passed in location.

**Parameters:** t

- the text component for which this UI is installed
**Parameters:** pt

- a

Point

specifying location for which to get a tooltip
**Returns:** a

String

containing the tooltip
**Since:** 1.4
**See Also:** JTextComponent.getToolTipText(java.awt.event.MouseEvent)

- getToolTipText2D

```java
public
String
getToolTipText2D​(
JTextComponent
t,

Point2D
pt)
```

Returns the string to be used as the tooltip at the passed in location.

**Implementation Requirements:** This implementation calls

getToolTipText(t, new Point((int) pt.getX(), (int) pt.getY())))

.
**Parameters:** t

- the text component for which this UI is installed
**Parameters:** pt

- a

Point

specifying location for which to get a tooltip
**Returns:** a

String

containing the tooltip
**Since:** 9
**See Also:** JTextComponent.getToolTipText(java.awt.event.MouseEvent)

---

#### Method Detail

modelToView

```java
@Deprecated
(
since
="9")
public abstract
Rectangle
modelToView​(
JTextComponent
t,
int pos)
throws
BadLocationException
```

Deprecated.

replaced by

modelToView2D(JTextComponent, int, Position.Bias)

Converts the given location in the model to a place in
the view coordinate system.

**Parameters:** t

- the text component for which this UI is installed
**Parameters:** pos

- the local location in the model to translate >= 0
**Returns:** the coordinates as a

Rectangle
**Throws:** BadLocationException

- if the given position does not
represent a valid location in the associated document

---

#### modelToView

@Deprecated

(

since

="9")
public abstract

Rectangle

modelToView​(

JTextComponent

t,
int pos)
throws

BadLocationException

Converts the given location in the model to a place in
the view coordinate system.

modelToView

```java
@Deprecated
(
since
="9")
public abstract
Rectangle
modelToView​(
JTextComponent
t,
int pos,

Position.Bias
bias)
throws
BadLocationException
```

Deprecated.

replaced by

modelToView2D(JTextComponent, int, Position.Bias)

Converts the given location in the model to a place in
the view coordinate system.

**Parameters:** t

- the text component for which this UI is installed
**Parameters:** pos

- the local location in the model to translate >= 0
**Parameters:** bias

- the bias for the position
**Returns:** the coordinates as a

Rectangle
**Throws:** BadLocationException

- if the given position does not
represent a valid location in the associated document

---

#### modelToView

@Deprecated

(

since

="9")
public abstract

Rectangle

modelToView​(

JTextComponent

t,
int pos,

Position.Bias

bias)
throws

BadLocationException

Converts the given location in the model to a place in
the view coordinate system.

modelToView2D

```java
public
Rectangle2D
modelToView2D​(
JTextComponent
t,
int pos,

Position.Bias
bias)
throws
BadLocationException
```

Converts the given location in the model to a place in
the view coordinate system.

**Implementation Requirements:** This implementation calls

modelToView(t, pos, bias)

.
**Parameters:** t

- the text component for which this UI is installed
**Parameters:** pos

- the local location in the model to translate

>= 0
**Parameters:** bias

- the bias for the position
**Returns:** the coordinates as a

Rectangle2D
**Throws:** BadLocationException

- if the given position does not
represent a valid location in the associated document
**Since:** 9

---

#### modelToView2D

public

Rectangle2D

modelToView2D​(

JTextComponent

t,
int pos,

Position.Bias

bias)
throws

BadLocationException

Converts the given location in the model to a place in
the view coordinate system.

viewToModel

```java
@Deprecated
(
since
="9")
public abstract int viewToModel​(
JTextComponent
t,

Point
pt)
```

Deprecated.

replaced by

viewToModel2D(JTextComponent, Point2D, Position.Bias[])

Converts the given place in the view coordinate system
to the nearest representative location in the model.

**Parameters:** t

- the text component for which this UI is installed
**Parameters:** pt

- the location in the view to translate. This
should be in the same coordinate system as the mouse
events.
**Returns:** the offset from the start of the document >= 0

---

#### viewToModel

@Deprecated

(

since

="9")
public abstract int viewToModel​(

JTextComponent

t,

Point

pt)

Converts the given place in the view coordinate system
to the nearest representative location in the model.

viewToModel

```java
@Deprecated
(
since
="9")
public abstract int viewToModel​(
JTextComponent
t,

Point
pt,

Position.Bias
[] biasReturn)
```

Deprecated.

replaced by

viewToModel2D(JTextComponent, Point2D, Position.Bias[])

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

**Parameters:** t

- the text component for which this UI is installed
**Parameters:** pt

- the location in the view to translate.
This should be in the same coordinate system
as the mouse events.
**Parameters:** biasReturn

- filled in by this method to indicate whether
the point given is closer to the previous or the next
character in the model
**Returns:** the location within the model that best represents the
given point in the view >= 0

---

#### viewToModel

@Deprecated

(

since

="9")
public abstract int viewToModel​(

JTextComponent

t,

Point

pt,

Position.Bias

[] biasReturn)

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

viewToModel2D

```java
public int viewToModel2D​(
JTextComponent
t,

Point2D
pt,

Position.Bias
[] biasReturn)
```

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

**Implementation Requirements:** This implementation calls

viewToModel(t, new Point((int) pt.getX(), (int) pt.getY()),
biasReturn)

.
**Parameters:** t

- the text component for which this UI is installed
**Parameters:** pt

- the location in the view to translate.
**Parameters:** biasReturn

- filled in by this method to indicate whether
the point given is closer to the previous or the next
character in the model
**Returns:** the location within the model that best represents the
given point in the view

>= 0
**Since:** 9

---

#### viewToModel2D

public int viewToModel2D​(

JTextComponent

t,

Point2D

pt,

Position.Bias

[] biasReturn)

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

getNextVisualPositionFrom

```java
public abstract int getNextVisualPositionFrom​(
JTextComponent
t,
int pos,

Position.Bias
b,
int direction,

Position.Bias
[] biasRet)
throws
BadLocationException
```

Provides a way to determine the next visually represented model
location that one might place a caret. Some views may not be visible,
they might not be in the same order found in the model, or they just
might not allow access to some of the locations in the model.

**Parameters:** t

- the text component for which this UI is installed
**Parameters:** pos

- the position to convert >= 0
**Parameters:** b

- the bias for the position
**Parameters:** direction

- the direction from the current position that can
be thought of as the arrow keys typically found on a keyboard.
This may be SwingConstants.WEST, SwingConstants.EAST,
SwingConstants.NORTH, or SwingConstants.SOUTH
**Parameters:** biasRet

- an array to contain the bias for the returned position
**Returns:** the location within the model that best represents the next
location visual position
**Throws:** BadLocationException

- for a bad location within a document model
**Throws:** IllegalArgumentException

- for an invalid direction

---

#### getNextVisualPositionFrom

public abstract int getNextVisualPositionFrom​(

JTextComponent

t,
int pos,

Position.Bias

b,
int direction,

Position.Bias

[] biasRet)
throws

BadLocationException

Provides a way to determine the next visually represented model
location that one might place a caret. Some views may not be visible,
they might not be in the same order found in the model, or they just
might not allow access to some of the locations in the model.

damageRange

```java
public abstract void damageRange​(
JTextComponent
t,
int p0,
int p1)
```

Causes the portion of the view responsible for the
given part of the model to be repainted.

**Parameters:** t

- the text component for which this UI is installed
**Parameters:** p0

- the beginning of the range >= 0
**Parameters:** p1

- the end of the range >= p0

---

#### damageRange

public abstract void damageRange​(

JTextComponent

t,
int p0,
int p1)

Causes the portion of the view responsible for the
given part of the model to be repainted.

damageRange

```java
public abstract void damageRange​(
JTextComponent
t,
int p0,
int p1,

Position.Bias
firstBias,

Position.Bias
secondBias)
```

Causes the portion of the view responsible for the
given part of the model to be repainted.

**Parameters:** t

- the text component for which this UI is installed
**Parameters:** p0

- the beginning of the range >= 0
**Parameters:** p1

- the end of the range >= p0
**Parameters:** firstBias

- the bias of the first character position, toward the
previous character or the next character
**Parameters:** secondBias

- the bias of the second character position, toward the
previous character or the next character

---

#### damageRange

public abstract void damageRange​(

JTextComponent

t,
int p0,
int p1,

Position.Bias

firstBias,

Position.Bias

secondBias)

Causes the portion of the view responsible for the
given part of the model to be repainted.

getEditorKit

```java
public abstract
EditorKit
getEditorKit​(
JTextComponent
t)
```

Fetches the binding of services that set a policy
for the type of document being edited. This contains
things like the commands available, stream readers and
writers, etc.

**Parameters:** t

- the text component for which this UI is installed
**Returns:** the editor kit binding

---

#### getEditorKit

public abstract

EditorKit

getEditorKit​(

JTextComponent

t)

Fetches the binding of services that set a policy
for the type of document being edited. This contains
things like the commands available, stream readers and
writers, etc.

getRootView

```java
public abstract
View
getRootView​(
JTextComponent
t)
```

Fetches a View with the allocation of the associated
text component (i.e. the root of the hierarchy) that
can be traversed to determine how the model is being
represented spatially.

**Parameters:** t

- the text component for which this UI is installed
**Returns:** a

View

with the allocation of the associated
text component

---

#### getRootView

public abstract

View

getRootView​(

JTextComponent

t)

Fetches a View with the allocation of the associated
text component (i.e. the root of the hierarchy) that
can be traversed to determine how the model is being
represented spatially.

getToolTipText

```java
@Deprecated
(
since
="9")
public
String
getToolTipText​(
JTextComponent
t,

Point
pt)
```

Deprecated.

replaced by

getToolTipText2D(JTextComponent, Point2D)

Returns the string to be used as the tooltip at the passed in location.

**Parameters:** t

- the text component for which this UI is installed
**Parameters:** pt

- a

Point

specifying location for which to get a tooltip
**Returns:** a

String

containing the tooltip
**Since:** 1.4
**See Also:** JTextComponent.getToolTipText(java.awt.event.MouseEvent)

---

#### getToolTipText

@Deprecated

(

since

="9")
public

String

getToolTipText​(

JTextComponent

t,

Point

pt)

Returns the string to be used as the tooltip at the passed in location.

getToolTipText2D

```java
public
String
getToolTipText2D​(
JTextComponent
t,

Point2D
pt)
```

Returns the string to be used as the tooltip at the passed in location.

**Implementation Requirements:** This implementation calls

getToolTipText(t, new Point((int) pt.getX(), (int) pt.getY())))

.
**Parameters:** t

- the text component for which this UI is installed
**Parameters:** pt

- a

Point

specifying location for which to get a tooltip
**Returns:** a

String

containing the tooltip
**Since:** 9
**See Also:** JTextComponent.getToolTipText(java.awt.event.MouseEvent)

---

#### getToolTipText2D

public

String

getToolTipText2D​(

JTextComponent

t,

Point2D

pt)

Returns the string to be used as the tooltip at the passed in location.

---

