# Class ImageView

**Source:** `java.desktop\javax\swing\text\html\ImageView.html`

### Class Description

```java
public class
ImageView

extends
View
```

View of an Image, intended to support the HTML <IMG> tag.
Supports scaling via the HEIGHT and WIDTH attributes of the tag.
If the image is unable to be loaded any text specified via the

ALT

attribute will be rendered.

While this class has been part of swing for a while now, it is public
as of 1.4.

**All Implemented Interfaces:** SwingConstants

---

### Field Details

*No entries found.*

### Constructor Details

#### public ImageView​(
Element
elem)

Creates a new view that represents an IMG element.

**Parameters:**
- elem

- the element to create a view for

---

### Method Details

#### public
String
getAltText()

Returns the text to display if the image cannot be loaded. This is
obtained from the Elements attribute set with the attribute name

HTML.Attribute.ALT

.

**Returns:**
- the test to display if the image cannot be loaded.

---

#### public
URL
getImageURL()

Return a URL for the image source,
or null if it could not be determined.

**Returns:**
- the URL for the image source, or null if it could not be determined.

---

#### public
Icon
getNoImageIcon()

Returns the icon to use if the image could not be found.

**Returns:**
- the icon to use if the image could not be found.

---

#### public
Icon
getLoadingImageIcon()

Returns the icon to use while in the process of loading the image.

**Returns:**
- the icon to use while in the process of loading the image.

---

#### public
Image
getImage()

Returns the image to render.

**Returns:**
- the image to render.

---

#### public void setLoadsSynchronously​(boolean newValue)

Sets how the image is loaded. If

newValue

is true,
the image will be loaded when first asked for, otherwise it will
be loaded asynchronously. The default is to not load synchronously,
that is to load the image asynchronously.

**Parameters:**
- newValue

- if

true

the image will be loaded when first asked for,
otherwise it will be asynchronously.

---

#### public boolean getLoadsSynchronously()

Returns

true

if the image should be loaded when first asked for.

**Returns:**
- true

if the image should be loaded when first asked for.

---

#### protected
StyleSheet
getStyleSheet()

Convenient method to get the StyleSheet.

**Returns:**
- the StyleSheet

---

#### public
AttributeSet
getAttributes()

Fetches the attributes to use when rendering. This is
implemented to multiplex the attributes specified in the
model with a StyleSheet.

**Overrides:**
- getAttributes

in class

View

**Returns:**
- the attributes to use when rendering

---

#### public
String
getToolTipText​(float x,
float y,

Shape
allocation)

For images the tooltip text comes from text specified with the

ALT

attribute. This is overriden to return

getAltText

.

**Overrides:**
- getToolTipText

in class

View

**Parameters:**
- x

- the x coordinate
- y

- the y coordinate
- allocation

- current allocation of the View.

**Returns:**
- the tooltip text at the specified location

**See Also:**
- JTextComponent.getToolTipText(java.awt.event.MouseEvent)

---

#### protected void setPropertiesFromAttributes()

Update any cached values that come from attributes.

---

#### public void setParent​(
View
parent)

Establishes the parent view for this view.
Seize this moment to cache the AWT Container I'm in.

**Overrides:**
- setParent

in class

View

**Parameters:**
- parent

- the new parent, or

null

if the view is
being removed from a parent

---

#### public void changedUpdate​(
DocumentEvent
e,

Shape
a,

ViewFactory
f)

Invoked when the Elements attributes have changed. Recreates the image.

**Overrides:**
- changedUpdate

in class

View

**Parameters:**
- e

- the change information from the associated document
- a

- the current allocation of the view
- f

- the factory to use to rebuild if the view has children

**See Also:**
- View.changedUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

---

#### public void paint​(
Graphics
g,

Shape
a)

Paints the View.

**Specified by:**
- paint

in class

View

**Parameters:**
- g

- the rendering surface to use
- a

- the allocated region to render into

**See Also:**
- View.paint(java.awt.Graphics, java.awt.Shape)

---

#### public float getPreferredSpan​(int axis)

Determines the preferred span for this view along an
axis.

**Specified by:**
- getPreferredSpan

in class

View

**Parameters:**
- axis

- may be either X_AXIS or Y_AXIS

**Returns:**
- the span the view would like to be rendered into;
typically the view is told to render into the span
that is returned, although there is no guarantee;
the parent may choose to resize or break the view

**See Also:**
- View.getPreferredSpan(int)

---

#### public float getAlignment​(int axis)

Determines the desired alignment for this view along an
axis. This is implemented to give the alignment to the
bottom of the icon along the y axis, and the default
along the x axis.

**Overrides:**
- getAlignment

in class

View

**Parameters:**
- axis

- may be either X_AXIS or Y_AXIS

**Returns:**
- the desired alignment; this should be a value
between 0.0 and 1.0 where 0 indicates alignment at the
origin and 1.0 indicates alignment to the full span
away from the origin; an alignment of 0.5 would be the
center of the view

---

#### public
Shape
modelToView​(int pos,

Shape
a,

Position.Bias
b)
throws
BadLocationException

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.

**Specified by:**
- modelToView

in class

View

**Parameters:**
- pos

- the position to convert
- a

- the allocated region to render into
- b

- the bias toward the previous character or the
next character represented by the offset, in case the
position is a boundary of two views;

b

will have one
of these values:

- Position.Bias.Forward

Position.Bias.Backward

**Returns:**
- the bounding box of the given position

**Throws:**
- BadLocationException

- if the given position does not represent a
valid location in the associated document

**See Also:**
- View.modelToView(int, java.awt.Shape, javax.swing.text.Position.Bias)

---

#### public int viewToModel​(float x,
float y,

Shape
a,

Position.Bias
[] bias)

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

**Specified by:**
- viewToModel

in class

View

**Parameters:**
- x

- the X coordinate
- y

- the Y coordinate
- a

- the allocated region to render into
- bias

- the returned bias

**Returns:**
- the location within the model that best represents the
given point of view

**See Also:**
- View.viewToModel(float, float, java.awt.Shape, javax.swing.text.Position.Bias[])

---

#### public void setSize​(float width,
float height)

Sets the size of the view. This should cause
layout of the view if it has any layout duties.

**Overrides:**
- setSize

in class

View

**Parameters:**
- width

- the width >= 0
- height

- the height >= 0

---

### Additional Sections

#### Class ImageView

java.lang.Object

- javax.swing.text.View
- - javax.swing.text.html.ImageView

javax.swing.text.View

- javax.swing.text.html.ImageView

javax.swing.text.html.ImageView

**All Implemented Interfaces:** SwingConstants

```java
public class
ImageView

extends
View
```

View of an Image, intended to support the HTML <IMG> tag.
Supports scaling via the HEIGHT and WIDTH attributes of the tag.
If the image is unable to be loaded any text specified via the

ALT

attribute will be rendered.

While this class has been part of swing for a while now, it is public
as of 1.4.

**Since:** 1.4
**See Also:** IconView

public class

ImageView

extends

View

View of an Image, intended to support the HTML <IMG> tag.
Supports scaling via the HEIGHT and WIDTH attributes of the tag.
If the image is unable to be loaded any text specified via the

ALT

attribute will be rendered.

While this class has been part of swing for a while now, it is public
as of 1.4.

While this class has been part of swing for a while now, it is public
as of 1.4.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.swing.text.

View

BadBreakWeight

,

ExcellentBreakWeight

,

ForcedBreakWeight

,

GoodBreakWeight

,

X_AXIS

,

Y_AXIS

- Fields declared in interface javax.swing.

SwingConstants

BOTTOM

,

CENTER

,

EAST

,

HORIZONTAL

,

LEADING

,

LEFT

,

NEXT

,

NORTH

,

NORTH_EAST

,

NORTH_WEST

,

PREVIOUS

,

RIGHT

,

SOUTH

,

SOUTH_EAST

,

SOUTH_WEST

,

TOP

,

TRAILING

,

VERTICAL

,

WEST

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ImageView

​(

Element

elem)

Creates a new view that represents an IMG element.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

changedUpdate

​(

DocumentEvent

e,

Shape

a,

ViewFactory

f)

Invoked when the Elements attributes have changed.

float

getAlignment

​(int axis)

Determines the desired alignment for this view along an
axis.

String

getAltText

()

Returns the text to display if the image cannot be loaded.

AttributeSet

getAttributes

()

Fetches the attributes to use when rendering.

Image

getImage

()

Returns the image to render.

URL

getImageURL

()

Return a URL for the image source,
or null if it could not be determined.

Icon

getLoadingImageIcon

()

Returns the icon to use while in the process of loading the image.

boolean

getLoadsSynchronously

()

Returns

true

if the image should be loaded when first asked for.

Icon

getNoImageIcon

()

Returns the icon to use if the image could not be found.

float

getPreferredSpan

​(int axis)

Determines the preferred span for this view along an
axis.

protected

StyleSheet

getStyleSheet

()

Convenient method to get the StyleSheet.

String

getToolTipText

​(float x,
float y,

Shape

allocation)

For images the tooltip text comes from text specified with the

ALT

attribute.

Shape

modelToView

​(int pos,

Shape

a,

Position.Bias

b)

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.

void

paint

​(

Graphics

g,

Shape

a)

Paints the View.

void

setLoadsSynchronously

​(boolean newValue)

Sets how the image is loaded.

void

setParent

​(

View

parent)

Establishes the parent view for this view.

protected void

setPropertiesFromAttributes

()

Update any cached values that come from attributes.

void

setSize

​(float width,
float height)

Sets the size of the view.

int

viewToModel

​(float x,
float y,

Shape

a,

Position.Bias

[] bias)

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

- Methods declared in class javax.swing.text.

View

append

,

breakView

,

createFragment

,

forwardUpdate

,

forwardUpdateToView

,

getBreakWeight

,

getChildAllocation

,

getContainer

,

getDocument

,

getElement

,

getEndOffset

,

getGraphics

,

getMaximumSpan

,

getMinimumSpan

,

getNextVisualPositionFrom

,

getParent

,

getResizeWeight

,

getStartOffset

,

getView

,

getViewCount

,

getViewFactory

,

getViewIndex

,

getViewIndex

,

insert

,

insertUpdate

,

isVisible

,

modelToView

,

modelToView

,

preferenceChanged

,

remove

,

removeAll

,

removeUpdate

,

replace

,

updateChildren

,

updateLayout

,

viewToModel

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

- Fields declared in class javax.swing.text.

View

BadBreakWeight

,

ExcellentBreakWeight

,

ForcedBreakWeight

,

GoodBreakWeight

,

X_AXIS

,

Y_AXIS

- Fields declared in interface javax.swing.

SwingConstants

BOTTOM

,

CENTER

,

EAST

,

HORIZONTAL

,

LEADING

,

LEFT

,

NEXT

,

NORTH

,

NORTH_EAST

,

NORTH_WEST

,

PREVIOUS

,

RIGHT

,

SOUTH

,

SOUTH_EAST

,

SOUTH_WEST

,

TOP

,

TRAILING

,

VERTICAL

,

WEST

---

#### Field Summary

Fields declared in class javax.swing.text.

View

BadBreakWeight

,

ExcellentBreakWeight

,

ForcedBreakWeight

,

GoodBreakWeight

,

X_AXIS

,

Y_AXIS

---

#### Fields declared in class javax.swing.text. View

Fields declared in interface javax.swing.

SwingConstants

BOTTOM

,

CENTER

,

EAST

,

HORIZONTAL

,

LEADING

,

LEFT

,

NEXT

,

NORTH

,

NORTH_EAST

,

NORTH_WEST

,

PREVIOUS

,

RIGHT

,

SOUTH

,

SOUTH_EAST

,

SOUTH_WEST

,

TOP

,

TRAILING

,

VERTICAL

,

WEST

---

#### Fields declared in interface javax.swing. SwingConstants

Constructor Summary

Constructors

Constructor

Description

ImageView

​(

Element

elem)

Creates a new view that represents an IMG element.

---

#### Constructor Summary

Creates a new view that represents an IMG element.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

changedUpdate

​(

DocumentEvent

e,

Shape

a,

ViewFactory

f)

Invoked when the Elements attributes have changed.

float

getAlignment

​(int axis)

Determines the desired alignment for this view along an
axis.

String

getAltText

()

Returns the text to display if the image cannot be loaded.

AttributeSet

getAttributes

()

Fetches the attributes to use when rendering.

Image

getImage

()

Returns the image to render.

URL

getImageURL

()

Return a URL for the image source,
or null if it could not be determined.

Icon

getLoadingImageIcon

()

Returns the icon to use while in the process of loading the image.

boolean

getLoadsSynchronously

()

Returns

true

if the image should be loaded when first asked for.

Icon

getNoImageIcon

()

Returns the icon to use if the image could not be found.

float

getPreferredSpan

​(int axis)

Determines the preferred span for this view along an
axis.

protected

StyleSheet

getStyleSheet

()

Convenient method to get the StyleSheet.

String

getToolTipText

​(float x,
float y,

Shape

allocation)

For images the tooltip text comes from text specified with the

ALT

attribute.

Shape

modelToView

​(int pos,

Shape

a,

Position.Bias

b)

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.

void

paint

​(

Graphics

g,

Shape

a)

Paints the View.

void

setLoadsSynchronously

​(boolean newValue)

Sets how the image is loaded.

void

setParent

​(

View

parent)

Establishes the parent view for this view.

protected void

setPropertiesFromAttributes

()

Update any cached values that come from attributes.

void

setSize

​(float width,
float height)

Sets the size of the view.

int

viewToModel

​(float x,
float y,

Shape

a,

Position.Bias

[] bias)

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

- Methods declared in class javax.swing.text.

View

append

,

breakView

,

createFragment

,

forwardUpdate

,

forwardUpdateToView

,

getBreakWeight

,

getChildAllocation

,

getContainer

,

getDocument

,

getElement

,

getEndOffset

,

getGraphics

,

getMaximumSpan

,

getMinimumSpan

,

getNextVisualPositionFrom

,

getParent

,

getResizeWeight

,

getStartOffset

,

getView

,

getViewCount

,

getViewFactory

,

getViewIndex

,

getViewIndex

,

insert

,

insertUpdate

,

isVisible

,

modelToView

,

modelToView

,

preferenceChanged

,

remove

,

removeAll

,

removeUpdate

,

replace

,

updateChildren

,

updateLayout

,

viewToModel

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

Invoked when the Elements attributes have changed.

Determines the desired alignment for this view along an
axis.

Returns the text to display if the image cannot be loaded.

Fetches the attributes to use when rendering.

Returns the image to render.

Return a URL for the image source,
or null if it could not be determined.

Returns the icon to use while in the process of loading the image.

Returns

true

if the image should be loaded when first asked for.

Returns the icon to use if the image could not be found.

Determines the preferred span for this view along an
axis.

Convenient method to get the StyleSheet.

For images the tooltip text comes from text specified with the

ALT

attribute.

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.

Paints the View.

Sets how the image is loaded.

Establishes the parent view for this view.

Update any cached values that come from attributes.

Sets the size of the view.

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

Methods declared in class javax.swing.text.

View

append

,

breakView

,

createFragment

,

forwardUpdate

,

forwardUpdateToView

,

getBreakWeight

,

getChildAllocation

,

getContainer

,

getDocument

,

getElement

,

getEndOffset

,

getGraphics

,

getMaximumSpan

,

getMinimumSpan

,

getNextVisualPositionFrom

,

getParent

,

getResizeWeight

,

getStartOffset

,

getView

,

getViewCount

,

getViewFactory

,

getViewIndex

,

getViewIndex

,

insert

,

insertUpdate

,

isVisible

,

modelToView

,

modelToView

,

preferenceChanged

,

remove

,

removeAll

,

removeUpdate

,

replace

,

updateChildren

,

updateLayout

,

viewToModel

---

#### Methods declared in class javax.swing.text. View

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

- ImageView

```java
public ImageView​(
Element
elem)
```

Creates a new view that represents an IMG element.

**Parameters:** elem

- the element to create a view for

============ METHOD DETAIL ==========

- Method Detail

- getAltText

```java
public
String
getAltText()
```

Returns the text to display if the image cannot be loaded. This is
obtained from the Elements attribute set with the attribute name

HTML.Attribute.ALT

.

**Returns:** the test to display if the image cannot be loaded.

- getImageURL

```java
public
URL
getImageURL()
```

Return a URL for the image source,
or null if it could not be determined.

**Returns:** the URL for the image source, or null if it could not be determined.

- getNoImageIcon

```java
public
Icon
getNoImageIcon()
```

Returns the icon to use if the image could not be found.

**Returns:** the icon to use if the image could not be found.

- getLoadingImageIcon

```java
public
Icon
getLoadingImageIcon()
```

Returns the icon to use while in the process of loading the image.

**Returns:** the icon to use while in the process of loading the image.

- getImage

```java
public
Image
getImage()
```

Returns the image to render.

**Returns:** the image to render.

- setLoadsSynchronously

```java
public void setLoadsSynchronously​(boolean newValue)
```

Sets how the image is loaded. If

newValue

is true,
the image will be loaded when first asked for, otherwise it will
be loaded asynchronously. The default is to not load synchronously,
that is to load the image asynchronously.

**Parameters:** newValue

- if

true

the image will be loaded when first asked for,
otherwise it will be asynchronously.

- getLoadsSynchronously

```java
public boolean getLoadsSynchronously()
```

Returns

true

if the image should be loaded when first asked for.

**Returns:** true

if the image should be loaded when first asked for.

- getStyleSheet

```java
protected
StyleSheet
getStyleSheet()
```

Convenient method to get the StyleSheet.

**Returns:** the StyleSheet

- getAttributes

```java
public
AttributeSet
getAttributes()
```

Fetches the attributes to use when rendering. This is
implemented to multiplex the attributes specified in the
model with a StyleSheet.

**Overrides:** getAttributes

in class

View
**Returns:** the attributes to use when rendering

- getToolTipText

```java
public
String
getToolTipText​(float x,
float y,

Shape
allocation)
```

For images the tooltip text comes from text specified with the

ALT

attribute. This is overriden to return

getAltText

.

**Overrides:** getToolTipText

in class

View
**Parameters:** x

- the x coordinate
**Parameters:** y

- the y coordinate
**Parameters:** allocation

- current allocation of the View.
**Returns:** the tooltip text at the specified location
**See Also:** JTextComponent.getToolTipText(java.awt.event.MouseEvent)

- setPropertiesFromAttributes

```java
protected void setPropertiesFromAttributes()
```

Update any cached values that come from attributes.

- setParent

```java
public void setParent​(
View
parent)
```

Establishes the parent view for this view.
Seize this moment to cache the AWT Container I'm in.

**Overrides:** setParent

in class

View
**Parameters:** parent

- the new parent, or

null

if the view is
being removed from a parent

- changedUpdate

```java
public void changedUpdate​(
DocumentEvent
e,

Shape
a,

ViewFactory
f)
```

Invoked when the Elements attributes have changed. Recreates the image.

**Overrides:** changedUpdate

in class

View
**Parameters:** e

- the change information from the associated document
**Parameters:** a

- the current allocation of the view
**Parameters:** f

- the factory to use to rebuild if the view has children
**See Also:** View.changedUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

- paint

```java
public void paint​(
Graphics
g,

Shape
a)
```

Paints the View.

**Specified by:** paint

in class

View
**Parameters:** g

- the rendering surface to use
**Parameters:** a

- the allocated region to render into
**See Also:** View.paint(java.awt.Graphics, java.awt.Shape)

- getPreferredSpan

```java
public float getPreferredSpan​(int axis)
```

Determines the preferred span for this view along an
axis.

**Specified by:** getPreferredSpan

in class

View
**Parameters:** axis

- may be either X_AXIS or Y_AXIS
**Returns:** the span the view would like to be rendered into;
typically the view is told to render into the span
that is returned, although there is no guarantee;
the parent may choose to resize or break the view
**See Also:** View.getPreferredSpan(int)

- getAlignment

```java
public float getAlignment​(int axis)
```

Determines the desired alignment for this view along an
axis. This is implemented to give the alignment to the
bottom of the icon along the y axis, and the default
along the x axis.

**Overrides:** getAlignment

in class

View
**Parameters:** axis

- may be either X_AXIS or Y_AXIS
**Returns:** the desired alignment; this should be a value
between 0.0 and 1.0 where 0 indicates alignment at the
origin and 1.0 indicates alignment to the full span
away from the origin; an alignment of 0.5 would be the
center of the view

- modelToView

```java
public
Shape
modelToView​(int pos,

Shape
a,

Position.Bias
b)
throws
BadLocationException
```

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.

**Specified by:** modelToView

in class

View
**Parameters:** pos

- the position to convert
**Parameters:** a

- the allocated region to render into
**Parameters:** b

- the bias toward the previous character or the
next character represented by the offset, in case the
position is a boundary of two views;

b

will have one
of these values:

- Position.Bias.Forward

Position.Bias.Backward
**Returns:** the bounding box of the given position
**Throws:** BadLocationException

- if the given position does not represent a
valid location in the associated document
**See Also:** View.modelToView(int, java.awt.Shape, javax.swing.text.Position.Bias)

- viewToModel

```java
public int viewToModel​(float x,
float y,

Shape
a,

Position.Bias
[] bias)
```

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

**Specified by:** viewToModel

in class

View
**Parameters:** x

- the X coordinate
**Parameters:** y

- the Y coordinate
**Parameters:** a

- the allocated region to render into
**Parameters:** bias

- the returned bias
**Returns:** the location within the model that best represents the
given point of view
**See Also:** View.viewToModel(float, float, java.awt.Shape, javax.swing.text.Position.Bias[])

- setSize

```java
public void setSize​(float width,
float height)
```

Sets the size of the view. This should cause
layout of the view if it has any layout duties.

**Overrides:** setSize

in class

View
**Parameters:** width

- the width >= 0
**Parameters:** height

- the height >= 0

Constructor Detail

- ImageView

```java
public ImageView​(
Element
elem)
```

Creates a new view that represents an IMG element.

**Parameters:** elem

- the element to create a view for

---

#### Constructor Detail

ImageView

```java
public ImageView​(
Element
elem)
```

Creates a new view that represents an IMG element.

**Parameters:** elem

- the element to create a view for

---

#### ImageView

public ImageView​(

Element

elem)

Creates a new view that represents an IMG element.

Method Detail

- getAltText

```java
public
String
getAltText()
```

Returns the text to display if the image cannot be loaded. This is
obtained from the Elements attribute set with the attribute name

HTML.Attribute.ALT

.

**Returns:** the test to display if the image cannot be loaded.

- getImageURL

```java
public
URL
getImageURL()
```

Return a URL for the image source,
or null if it could not be determined.

**Returns:** the URL for the image source, or null if it could not be determined.

- getNoImageIcon

```java
public
Icon
getNoImageIcon()
```

Returns the icon to use if the image could not be found.

**Returns:** the icon to use if the image could not be found.

- getLoadingImageIcon

```java
public
Icon
getLoadingImageIcon()
```

Returns the icon to use while in the process of loading the image.

**Returns:** the icon to use while in the process of loading the image.

- getImage

```java
public
Image
getImage()
```

Returns the image to render.

**Returns:** the image to render.

- setLoadsSynchronously

```java
public void setLoadsSynchronously​(boolean newValue)
```

Sets how the image is loaded. If

newValue

is true,
the image will be loaded when first asked for, otherwise it will
be loaded asynchronously. The default is to not load synchronously,
that is to load the image asynchronously.

**Parameters:** newValue

- if

true

the image will be loaded when first asked for,
otherwise it will be asynchronously.

- getLoadsSynchronously

```java
public boolean getLoadsSynchronously()
```

Returns

true

if the image should be loaded when first asked for.

**Returns:** true

if the image should be loaded when first asked for.

- getStyleSheet

```java
protected
StyleSheet
getStyleSheet()
```

Convenient method to get the StyleSheet.

**Returns:** the StyleSheet

- getAttributes

```java
public
AttributeSet
getAttributes()
```

Fetches the attributes to use when rendering. This is
implemented to multiplex the attributes specified in the
model with a StyleSheet.

**Overrides:** getAttributes

in class

View
**Returns:** the attributes to use when rendering

- getToolTipText

```java
public
String
getToolTipText​(float x,
float y,

Shape
allocation)
```

For images the tooltip text comes from text specified with the

ALT

attribute. This is overriden to return

getAltText

.

**Overrides:** getToolTipText

in class

View
**Parameters:** x

- the x coordinate
**Parameters:** y

- the y coordinate
**Parameters:** allocation

- current allocation of the View.
**Returns:** the tooltip text at the specified location
**See Also:** JTextComponent.getToolTipText(java.awt.event.MouseEvent)

- setPropertiesFromAttributes

```java
protected void setPropertiesFromAttributes()
```

Update any cached values that come from attributes.

- setParent

```java
public void setParent​(
View
parent)
```

Establishes the parent view for this view.
Seize this moment to cache the AWT Container I'm in.

**Overrides:** setParent

in class

View
**Parameters:** parent

- the new parent, or

null

if the view is
being removed from a parent

- changedUpdate

```java
public void changedUpdate​(
DocumentEvent
e,

Shape
a,

ViewFactory
f)
```

Invoked when the Elements attributes have changed. Recreates the image.

**Overrides:** changedUpdate

in class

View
**Parameters:** e

- the change information from the associated document
**Parameters:** a

- the current allocation of the view
**Parameters:** f

- the factory to use to rebuild if the view has children
**See Also:** View.changedUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

- paint

```java
public void paint​(
Graphics
g,

Shape
a)
```

Paints the View.

**Specified by:** paint

in class

View
**Parameters:** g

- the rendering surface to use
**Parameters:** a

- the allocated region to render into
**See Also:** View.paint(java.awt.Graphics, java.awt.Shape)

- getPreferredSpan

```java
public float getPreferredSpan​(int axis)
```

Determines the preferred span for this view along an
axis.

**Specified by:** getPreferredSpan

in class

View
**Parameters:** axis

- may be either X_AXIS or Y_AXIS
**Returns:** the span the view would like to be rendered into;
typically the view is told to render into the span
that is returned, although there is no guarantee;
the parent may choose to resize or break the view
**See Also:** View.getPreferredSpan(int)

- getAlignment

```java
public float getAlignment​(int axis)
```

Determines the desired alignment for this view along an
axis. This is implemented to give the alignment to the
bottom of the icon along the y axis, and the default
along the x axis.

**Overrides:** getAlignment

in class

View
**Parameters:** axis

- may be either X_AXIS or Y_AXIS
**Returns:** the desired alignment; this should be a value
between 0.0 and 1.0 where 0 indicates alignment at the
origin and 1.0 indicates alignment to the full span
away from the origin; an alignment of 0.5 would be the
center of the view

- modelToView

```java
public
Shape
modelToView​(int pos,

Shape
a,

Position.Bias
b)
throws
BadLocationException
```

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.

**Specified by:** modelToView

in class

View
**Parameters:** pos

- the position to convert
**Parameters:** a

- the allocated region to render into
**Parameters:** b

- the bias toward the previous character or the
next character represented by the offset, in case the
position is a boundary of two views;

b

will have one
of these values:

- Position.Bias.Forward

Position.Bias.Backward
**Returns:** the bounding box of the given position
**Throws:** BadLocationException

- if the given position does not represent a
valid location in the associated document
**See Also:** View.modelToView(int, java.awt.Shape, javax.swing.text.Position.Bias)

- viewToModel

```java
public int viewToModel​(float x,
float y,

Shape
a,

Position.Bias
[] bias)
```

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

**Specified by:** viewToModel

in class

View
**Parameters:** x

- the X coordinate
**Parameters:** y

- the Y coordinate
**Parameters:** a

- the allocated region to render into
**Parameters:** bias

- the returned bias
**Returns:** the location within the model that best represents the
given point of view
**See Also:** View.viewToModel(float, float, java.awt.Shape, javax.swing.text.Position.Bias[])

- setSize

```java
public void setSize​(float width,
float height)
```

Sets the size of the view. This should cause
layout of the view if it has any layout duties.

**Overrides:** setSize

in class

View
**Parameters:** width

- the width >= 0
**Parameters:** height

- the height >= 0

---

#### Method Detail

getAltText

```java
public
String
getAltText()
```

Returns the text to display if the image cannot be loaded. This is
obtained from the Elements attribute set with the attribute name

HTML.Attribute.ALT

.

**Returns:** the test to display if the image cannot be loaded.

---

#### getAltText

public

String

getAltText()

Returns the text to display if the image cannot be loaded. This is
obtained from the Elements attribute set with the attribute name

HTML.Attribute.ALT

.

getImageURL

```java
public
URL
getImageURL()
```

Return a URL for the image source,
or null if it could not be determined.

**Returns:** the URL for the image source, or null if it could not be determined.

---

#### getImageURL

public

URL

getImageURL()

Return a URL for the image source,
or null if it could not be determined.

getNoImageIcon

```java
public
Icon
getNoImageIcon()
```

Returns the icon to use if the image could not be found.

**Returns:** the icon to use if the image could not be found.

---

#### getNoImageIcon

public

Icon

getNoImageIcon()

Returns the icon to use if the image could not be found.

getLoadingImageIcon

```java
public
Icon
getLoadingImageIcon()
```

Returns the icon to use while in the process of loading the image.

**Returns:** the icon to use while in the process of loading the image.

---

#### getLoadingImageIcon

public

Icon

getLoadingImageIcon()

Returns the icon to use while in the process of loading the image.

getImage

```java
public
Image
getImage()
```

Returns the image to render.

**Returns:** the image to render.

---

#### getImage

public

Image

getImage()

Returns the image to render.

setLoadsSynchronously

```java
public void setLoadsSynchronously​(boolean newValue)
```

Sets how the image is loaded. If

newValue

is true,
the image will be loaded when first asked for, otherwise it will
be loaded asynchronously. The default is to not load synchronously,
that is to load the image asynchronously.

**Parameters:** newValue

- if

true

the image will be loaded when first asked for,
otherwise it will be asynchronously.

---

#### setLoadsSynchronously

public void setLoadsSynchronously​(boolean newValue)

Sets how the image is loaded. If

newValue

is true,
the image will be loaded when first asked for, otherwise it will
be loaded asynchronously. The default is to not load synchronously,
that is to load the image asynchronously.

getLoadsSynchronously

```java
public boolean getLoadsSynchronously()
```

Returns

true

if the image should be loaded when first asked for.

**Returns:** true

if the image should be loaded when first asked for.

---

#### getLoadsSynchronously

public boolean getLoadsSynchronously()

Returns

true

if the image should be loaded when first asked for.

getStyleSheet

```java
protected
StyleSheet
getStyleSheet()
```

Convenient method to get the StyleSheet.

**Returns:** the StyleSheet

---

#### getStyleSheet

protected

StyleSheet

getStyleSheet()

Convenient method to get the StyleSheet.

getAttributes

```java
public
AttributeSet
getAttributes()
```

Fetches the attributes to use when rendering. This is
implemented to multiplex the attributes specified in the
model with a StyleSheet.

**Overrides:** getAttributes

in class

View
**Returns:** the attributes to use when rendering

---

#### getAttributes

public

AttributeSet

getAttributes()

Fetches the attributes to use when rendering. This is
implemented to multiplex the attributes specified in the
model with a StyleSheet.

getToolTipText

```java
public
String
getToolTipText​(float x,
float y,

Shape
allocation)
```

For images the tooltip text comes from text specified with the

ALT

attribute. This is overriden to return

getAltText

.

**Overrides:** getToolTipText

in class

View
**Parameters:** x

- the x coordinate
**Parameters:** y

- the y coordinate
**Parameters:** allocation

- current allocation of the View.
**Returns:** the tooltip text at the specified location
**See Also:** JTextComponent.getToolTipText(java.awt.event.MouseEvent)

---

#### getToolTipText

public

String

getToolTipText​(float x,
float y,

Shape

allocation)

For images the tooltip text comes from text specified with the

ALT

attribute. This is overriden to return

getAltText

.

setPropertiesFromAttributes

```java
protected void setPropertiesFromAttributes()
```

Update any cached values that come from attributes.

---

#### setPropertiesFromAttributes

protected void setPropertiesFromAttributes()

Update any cached values that come from attributes.

setParent

```java
public void setParent​(
View
parent)
```

Establishes the parent view for this view.
Seize this moment to cache the AWT Container I'm in.

**Overrides:** setParent

in class

View
**Parameters:** parent

- the new parent, or

null

if the view is
being removed from a parent

---

#### setParent

public void setParent​(

View

parent)

Establishes the parent view for this view.
Seize this moment to cache the AWT Container I'm in.

changedUpdate

```java
public void changedUpdate​(
DocumentEvent
e,

Shape
a,

ViewFactory
f)
```

Invoked when the Elements attributes have changed. Recreates the image.

**Overrides:** changedUpdate

in class

View
**Parameters:** e

- the change information from the associated document
**Parameters:** a

- the current allocation of the view
**Parameters:** f

- the factory to use to rebuild if the view has children
**See Also:** View.changedUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

---

#### changedUpdate

public void changedUpdate​(

DocumentEvent

e,

Shape

a,

ViewFactory

f)

Invoked when the Elements attributes have changed. Recreates the image.

paint

```java
public void paint​(
Graphics
g,

Shape
a)
```

Paints the View.

**Specified by:** paint

in class

View
**Parameters:** g

- the rendering surface to use
**Parameters:** a

- the allocated region to render into
**See Also:** View.paint(java.awt.Graphics, java.awt.Shape)

---

#### paint

public void paint​(

Graphics

g,

Shape

a)

Paints the View.

getPreferredSpan

```java
public float getPreferredSpan​(int axis)
```

Determines the preferred span for this view along an
axis.

**Specified by:** getPreferredSpan

in class

View
**Parameters:** axis

- may be either X_AXIS or Y_AXIS
**Returns:** the span the view would like to be rendered into;
typically the view is told to render into the span
that is returned, although there is no guarantee;
the parent may choose to resize or break the view
**See Also:** View.getPreferredSpan(int)

---

#### getPreferredSpan

public float getPreferredSpan​(int axis)

Determines the preferred span for this view along an
axis.

getAlignment

```java
public float getAlignment​(int axis)
```

Determines the desired alignment for this view along an
axis. This is implemented to give the alignment to the
bottom of the icon along the y axis, and the default
along the x axis.

**Overrides:** getAlignment

in class

View
**Parameters:** axis

- may be either X_AXIS or Y_AXIS
**Returns:** the desired alignment; this should be a value
between 0.0 and 1.0 where 0 indicates alignment at the
origin and 1.0 indicates alignment to the full span
away from the origin; an alignment of 0.5 would be the
center of the view

---

#### getAlignment

public float getAlignment​(int axis)

Determines the desired alignment for this view along an
axis. This is implemented to give the alignment to the
bottom of the icon along the y axis, and the default
along the x axis.

modelToView

```java
public
Shape
modelToView​(int pos,

Shape
a,

Position.Bias
b)
throws
BadLocationException
```

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.

**Specified by:** modelToView

in class

View
**Parameters:** pos

- the position to convert
**Parameters:** a

- the allocated region to render into
**Parameters:** b

- the bias toward the previous character or the
next character represented by the offset, in case the
position is a boundary of two views;

b

will have one
of these values:

- Position.Bias.Forward

Position.Bias.Backward
**Returns:** the bounding box of the given position
**Throws:** BadLocationException

- if the given position does not represent a
valid location in the associated document
**See Also:** View.modelToView(int, java.awt.Shape, javax.swing.text.Position.Bias)

---

#### modelToView

public

Shape

modelToView​(int pos,

Shape

a,

Position.Bias

b)
throws

BadLocationException

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.

Position.Bias.Forward

Position.Bias.Backward

viewToModel

```java
public int viewToModel​(float x,
float y,

Shape
a,

Position.Bias
[] bias)
```

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

**Specified by:** viewToModel

in class

View
**Parameters:** x

- the X coordinate
**Parameters:** y

- the Y coordinate
**Parameters:** a

- the allocated region to render into
**Parameters:** bias

- the returned bias
**Returns:** the location within the model that best represents the
given point of view
**See Also:** View.viewToModel(float, float, java.awt.Shape, javax.swing.text.Position.Bias[])

---

#### viewToModel

public int viewToModel​(float x,
float y,

Shape

a,

Position.Bias

[] bias)

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

setSize

```java
public void setSize​(float width,
float height)
```

Sets the size of the view. This should cause
layout of the view if it has any layout duties.

**Overrides:** setSize

in class

View
**Parameters:** width

- the width >= 0
**Parameters:** height

- the height >= 0

---

#### setSize

public void setSize​(float width,
float height)

Sets the size of the view. This should cause
layout of the view if it has any layout duties.

---

