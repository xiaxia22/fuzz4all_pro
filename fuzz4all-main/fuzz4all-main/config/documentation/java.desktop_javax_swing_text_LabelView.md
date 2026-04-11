# Class LabelView

**Source:** `java.desktop\javax\swing\text\LabelView.html`

### Class Description

```java
public class
LabelView

extends
GlyphView

implements
TabableView
```

A

LabelView

is a styled chunk of text
that represents a view mapped over an element in the
text model. It caches the character level attributes
used for rendering.

**All Implemented Interfaces:** Cloneable

,

SwingConstants

,

TabableView

---

### Field Details

*No entries found.*

### Constructor Details

#### public LabelView​(
Element
elem)

Constructs a new view wrapped on an element.

**Parameters:**
- elem

- the element

---

### Method Details

#### protected void setUnderline​(boolean u)

Sets whether or not the view is underlined.
Note that this setter is protected and is really
only meant if you need to update some additional
state when set.

**Parameters:**
- u

- true if the view is underlined, otherwise
false

**See Also:**
- isUnderline()

---

#### protected void setStrikeThrough​(boolean s)

Sets whether or not the view has a strike/line
through it.
Note that this setter is protected and is really
only meant if you need to update some additional
state when set.

**Parameters:**
- s

- true if the view has a strike/line
through it, otherwise false

**See Also:**
- isStrikeThrough()

---

#### protected void setSuperscript​(boolean s)

Sets whether or not the view represents a
superscript.
Note that this setter is protected and is really
only meant if you need to update some additional
state when set.

**Parameters:**
- s

- true if the view represents a
superscript, otherwise false

**See Also:**
- isSuperscript()

---

#### protected void setSubscript​(boolean s)

Sets whether or not the view represents a
subscript.
Note that this setter is protected and is really
only meant if you need to update some additional
state when set.

**Parameters:**
- s

- true if the view represents a
subscript, otherwise false

**See Also:**
- isSubscript()

---

#### protected void setBackground​(
Color
bg)

Sets the background color for the view. This method is typically
invoked as part of configuring this

View

. If you need
to customize the background color you should override

setPropertiesFromAttributes

and invoke this method. A
value of null indicates no background should be rendered, so that the
background of the parent

View

will show through.

**Parameters:**
- bg

- background color, or null

**See Also:**
- setPropertiesFromAttributes()

**Since:**
- 1.5

---

#### protected void setPropertiesFromAttributes()

Sets the cached properties from the attributes.

---

#### @Deprecated

protected
FontMetrics
getFontMetrics()

Fetches the

FontMetrics

used for this view.

**Returns:**
- the

FontMetrics

used for this view

---

#### public
Color
getBackground()

Fetches the background color to use to render the glyphs.
This is implemented to return a cached background color,
which defaults to

null

.

**Overrides:**
- getBackground

in class

GlyphView

**Returns:**
- the cached background color

**Since:**
- 1.3

---

#### public
Color
getForeground()

Fetches the foreground color to use to render the glyphs.
This is implemented to return a cached foreground color,
which defaults to

null

.

**Overrides:**
- getForeground

in class

GlyphView

**Returns:**
- the cached foreground color

**Since:**
- 1.3

---

#### public
Font
getFont()

Fetches the font that the glyphs should be based upon.
This is implemented to return a cached font.

**Overrides:**
- getFont

in class

GlyphView

**Returns:**
- the cached font

---

#### public boolean isUnderline()

Determines if the glyphs should be underlined. If true,
an underline should be drawn through the baseline. This
is implemented to return the cached underline property.

When you request this property,

LabelView

re-syncs its state with the properties of the

Element

's

AttributeSet

.
If

Element

's

AttributeSet

does not have this property set, it will revert to false.

**Overrides:**
- isUnderline

in class

GlyphView

**Returns:**
- the value of the cached

underline

property

**Since:**
- 1.3

---

#### public boolean isStrikeThrough()

Determines if the glyphs should have a strikethrough
line. If true, a line should be drawn through the center
of the glyphs. This is implemented to return the
cached

strikeThrough

property.

When you request this property,

LabelView

re-syncs its state with the properties of the

Element

's

AttributeSet

.
If

Element

's

AttributeSet

does not have this property set, it will revert to false.

**Overrides:**
- isStrikeThrough

in class

GlyphView

**Returns:**
- the value of the cached

strikeThrough

property

**Since:**
- 1.3

---

#### public boolean isSubscript()

Determines if the glyphs should be rendered as superscript.

**Overrides:**
- isSubscript

in class

GlyphView

**Returns:**
- the value of the cached subscript property

When you request this property,

LabelView

re-syncs its state with the properties of the

Element

's

AttributeSet

.
If

Element

's

AttributeSet

does not have this property set, it will revert to false.

**Since:**
- 1.3

---

#### public boolean isSuperscript()

Determines if the glyphs should be rendered as subscript.

When you request this property,

LabelView

re-syncs its state with the properties of the

Element

's

AttributeSet

.
If

Element

's

AttributeSet

does not have this property set, it will revert to false.

**Overrides:**
- isSuperscript

in class

GlyphView

**Returns:**
- the value of the cached

superscript

property

**Since:**
- 1.3

---

#### public void changedUpdate​(
DocumentEvent
e,

Shape
a,

ViewFactory
f)

Gives notification from the document that attributes were changed
in a location that this view is responsible for.

**Overrides:**
- changedUpdate

in class

GlyphView

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

### Additional Sections

#### Class LabelView

java.lang.Object

- javax.swing.text.View
- - javax.swing.text.GlyphView
- - javax.swing.text.LabelView

javax.swing.text.View

- javax.swing.text.GlyphView
- - javax.swing.text.LabelView

javax.swing.text.GlyphView

- javax.swing.text.LabelView

javax.swing.text.LabelView

**All Implemented Interfaces:** Cloneable

,

SwingConstants

,

TabableView

**Direct Known Subclasses:** InlineView

```java
public class
LabelView

extends
GlyphView

implements
TabableView
```

A

LabelView

is a styled chunk of text
that represents a view mapped over an element in the
text model. It caches the character level attributes
used for rendering.

public class

LabelView

extends

GlyphView

implements

TabableView

A

LabelView

is a styled chunk of text
that represents a view mapped over an element in the
text model. It caches the character level attributes
used for rendering.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in class javax.swing.text.

GlyphView

GlyphView.GlyphPainter

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

LabelView

​(

Element

elem)

Constructs a new view wrapped on an element.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

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

Gives notification from the document that attributes were changed
in a location that this view is responsible for.

Color

getBackground

()

Fetches the background color to use to render the glyphs.

Font

getFont

()

Fetches the font that the glyphs should be based upon.

protected

FontMetrics

getFontMetrics

()

Deprecated.

FontMetrics are not used for glyph rendering
when running in the JDK.

Color

getForeground

()

Fetches the foreground color to use to render the glyphs.

boolean

isStrikeThrough

()

Determines if the glyphs should have a strikethrough
line.

boolean

isSubscript

()

Determines if the glyphs should be rendered as superscript.

boolean

isSuperscript

()

Determines if the glyphs should be rendered as subscript.

boolean

isUnderline

()

Determines if the glyphs should be underlined.

protected void

setBackground

​(

Color

bg)

Sets the background color for the view.

protected void

setPropertiesFromAttributes

()

Sets the cached properties from the attributes.

protected void

setStrikeThrough

​(boolean s)

Sets whether or not the view has a strike/line
through it.

protected void

setSubscript

​(boolean s)

Sets whether or not the view represents a
subscript.

protected void

setSuperscript

​(boolean s)

Sets whether or not the view represents a
superscript.

protected void

setUnderline

​(boolean u)

Sets whether or not the view is underlined.

- Methods declared in class javax.swing.text.

GlyphView

breakView

,

checkPainter

,

clone

,

createFragment

,

getAlignment

,

getBreakWeight

,

getEndOffset

,

getGlyphPainter

,

getMinimumSpan

,

getNextVisualPositionFrom

,

getPartialSpan

,

getPreferredSpan

,

getStartOffset

,

getTabbedSpan

,

getTabExpander

,

getText

,

insertUpdate

,

modelToView

,

paint

,

removeUpdate

,

setGlyphPainter

,

viewToModel

- Methods declared in class javax.swing.text.

View

append

,

forwardUpdate

,

forwardUpdateToView

,

getAttributes

,

getChildAllocation

,

getContainer

,

getDocument

,

getElement

,

getGraphics

,

getMaximumSpan

,

getParent

,

getResizeWeight

,

getToolTipText

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

replace

,

setParent

,

setSize

,

updateChildren

,

updateLayout

,

viewToModel

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

- Methods declared in interface javax.swing.text.

TabableView

getPartialSpan

,

getTabbedSpan

Nested Class Summary

- Nested classes/interfaces declared in class javax.swing.text.

GlyphView

GlyphView.GlyphPainter

---

#### Nested Class Summary

Nested classes/interfaces declared in class javax.swing.text.

GlyphView

GlyphView.GlyphPainter

---

#### Nested classes/interfaces declared in class javax.swing.text. GlyphView

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

LabelView

​(

Element

elem)

Constructs a new view wrapped on an element.

---

#### Constructor Summary

Constructs a new view wrapped on an element.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

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

Gives notification from the document that attributes were changed
in a location that this view is responsible for.

Color

getBackground

()

Fetches the background color to use to render the glyphs.

Font

getFont

()

Fetches the font that the glyphs should be based upon.

protected

FontMetrics

getFontMetrics

()

Deprecated.

FontMetrics are not used for glyph rendering
when running in the JDK.

Color

getForeground

()

Fetches the foreground color to use to render the glyphs.

boolean

isStrikeThrough

()

Determines if the glyphs should have a strikethrough
line.

boolean

isSubscript

()

Determines if the glyphs should be rendered as superscript.

boolean

isSuperscript

()

Determines if the glyphs should be rendered as subscript.

boolean

isUnderline

()

Determines if the glyphs should be underlined.

protected void

setBackground

​(

Color

bg)

Sets the background color for the view.

protected void

setPropertiesFromAttributes

()

Sets the cached properties from the attributes.

protected void

setStrikeThrough

​(boolean s)

Sets whether or not the view has a strike/line
through it.

protected void

setSubscript

​(boolean s)

Sets whether or not the view represents a
subscript.

protected void

setSuperscript

​(boolean s)

Sets whether or not the view represents a
superscript.

protected void

setUnderline

​(boolean u)

Sets whether or not the view is underlined.

- Methods declared in class javax.swing.text.

GlyphView

breakView

,

checkPainter

,

clone

,

createFragment

,

getAlignment

,

getBreakWeight

,

getEndOffset

,

getGlyphPainter

,

getMinimumSpan

,

getNextVisualPositionFrom

,

getPartialSpan

,

getPreferredSpan

,

getStartOffset

,

getTabbedSpan

,

getTabExpander

,

getText

,

insertUpdate

,

modelToView

,

paint

,

removeUpdate

,

setGlyphPainter

,

viewToModel

- Methods declared in class javax.swing.text.

View

append

,

forwardUpdate

,

forwardUpdateToView

,

getAttributes

,

getChildAllocation

,

getContainer

,

getDocument

,

getElement

,

getGraphics

,

getMaximumSpan

,

getParent

,

getResizeWeight

,

getToolTipText

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

replace

,

setParent

,

setSize

,

updateChildren

,

updateLayout

,

viewToModel

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

- Methods declared in interface javax.swing.text.

TabableView

getPartialSpan

,

getTabbedSpan

---

#### Method Summary

Gives notification from the document that attributes were changed
in a location that this view is responsible for.

Fetches the background color to use to render the glyphs.

Fetches the font that the glyphs should be based upon.

Deprecated.

FontMetrics are not used for glyph rendering
when running in the JDK.

Fetches the foreground color to use to render the glyphs.

Determines if the glyphs should have a strikethrough
line.

Determines if the glyphs should be rendered as superscript.

Determines if the glyphs should be rendered as subscript.

Determines if the glyphs should be underlined.

Sets the background color for the view.

Sets the cached properties from the attributes.

Sets whether or not the view has a strike/line
through it.

Sets whether or not the view represents a
subscript.

Sets whether or not the view represents a
superscript.

Sets whether or not the view is underlined.

Methods declared in class javax.swing.text.

GlyphView

breakView

,

checkPainter

,

clone

,

createFragment

,

getAlignment

,

getBreakWeight

,

getEndOffset

,

getGlyphPainter

,

getMinimumSpan

,

getNextVisualPositionFrom

,

getPartialSpan

,

getPreferredSpan

,

getStartOffset

,

getTabbedSpan

,

getTabExpander

,

getText

,

insertUpdate

,

modelToView

,

paint

,

removeUpdate

,

setGlyphPainter

,

viewToModel

---

#### Methods declared in class javax.swing.text. GlyphView

Methods declared in class javax.swing.text.

View

append

,

forwardUpdate

,

forwardUpdateToView

,

getAttributes

,

getChildAllocation

,

getContainer

,

getDocument

,

getElement

,

getGraphics

,

getMaximumSpan

,

getParent

,

getResizeWeight

,

getToolTipText

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

replace

,

setParent

,

setSize

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

Methods declared in interface javax.swing.text.

TabableView

getPartialSpan

,

getTabbedSpan

---

#### Methods declared in interface javax.swing.text. TabableView

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- LabelView

```java
public LabelView​(
Element
elem)
```

Constructs a new view wrapped on an element.

**Parameters:** elem

- the element

============ METHOD DETAIL ==========

- Method Detail

- setUnderline

```java
protected void setUnderline​(boolean u)
```

Sets whether or not the view is underlined.
Note that this setter is protected and is really
only meant if you need to update some additional
state when set.

**Parameters:** u

- true if the view is underlined, otherwise
false
**See Also:** isUnderline()

- setStrikeThrough

```java
protected void setStrikeThrough​(boolean s)
```

Sets whether or not the view has a strike/line
through it.
Note that this setter is protected and is really
only meant if you need to update some additional
state when set.

**Parameters:** s

- true if the view has a strike/line
through it, otherwise false
**See Also:** isStrikeThrough()

- setSuperscript

```java
protected void setSuperscript​(boolean s)
```

Sets whether or not the view represents a
superscript.
Note that this setter is protected and is really
only meant if you need to update some additional
state when set.

**Parameters:** s

- true if the view represents a
superscript, otherwise false
**See Also:** isSuperscript()

- setSubscript

```java
protected void setSubscript​(boolean s)
```

Sets whether or not the view represents a
subscript.
Note that this setter is protected and is really
only meant if you need to update some additional
state when set.

**Parameters:** s

- true if the view represents a
subscript, otherwise false
**See Also:** isSubscript()

- setBackground

```java
protected void setBackground​(
Color
bg)
```

Sets the background color for the view. This method is typically
invoked as part of configuring this

View

. If you need
to customize the background color you should override

setPropertiesFromAttributes

and invoke this method. A
value of null indicates no background should be rendered, so that the
background of the parent

View

will show through.

**Parameters:** bg

- background color, or null
**Since:** 1.5
**See Also:** setPropertiesFromAttributes()

- setPropertiesFromAttributes

```java
protected void setPropertiesFromAttributes()
```

Sets the cached properties from the attributes.

- getFontMetrics

```java
@Deprecated

protected
FontMetrics
getFontMetrics()
```

Deprecated.

FontMetrics are not used for glyph rendering
when running in the JDK.

Fetches the

FontMetrics

used for this view.

**Returns:** the

FontMetrics

used for this view

- getBackground

```java
public
Color
getBackground()
```

Fetches the background color to use to render the glyphs.
This is implemented to return a cached background color,
which defaults to

null

.

**Overrides:** getBackground

in class

GlyphView
**Returns:** the cached background color
**Since:** 1.3

- getForeground

```java
public
Color
getForeground()
```

Fetches the foreground color to use to render the glyphs.
This is implemented to return a cached foreground color,
which defaults to

null

.

**Overrides:** getForeground

in class

GlyphView
**Returns:** the cached foreground color
**Since:** 1.3

- getFont

```java
public
Font
getFont()
```

Fetches the font that the glyphs should be based upon.
This is implemented to return a cached font.

**Overrides:** getFont

in class

GlyphView
**Returns:** the cached font

- isUnderline

```java
public boolean isUnderline()
```

Determines if the glyphs should be underlined. If true,
an underline should be drawn through the baseline. This
is implemented to return the cached underline property.

When you request this property,

LabelView

re-syncs its state with the properties of the

Element

's

AttributeSet

.
If

Element

's

AttributeSet

does not have this property set, it will revert to false.

**Overrides:** isUnderline

in class

GlyphView
**Returns:** the value of the cached

underline

property
**Since:** 1.3

- isStrikeThrough

```java
public boolean isStrikeThrough()
```

Determines if the glyphs should have a strikethrough
line. If true, a line should be drawn through the center
of the glyphs. This is implemented to return the
cached

strikeThrough

property.

When you request this property,

LabelView

re-syncs its state with the properties of the

Element

's

AttributeSet

.
If

Element

's

AttributeSet

does not have this property set, it will revert to false.

**Overrides:** isStrikeThrough

in class

GlyphView
**Returns:** the value of the cached

strikeThrough

property
**Since:** 1.3

- isSubscript

```java
public boolean isSubscript()
```

Determines if the glyphs should be rendered as superscript.

**Overrides:** isSubscript

in class

GlyphView
**Returns:** the value of the cached subscript property

When you request this property,

LabelView

re-syncs its state with the properties of the

Element

's

AttributeSet

.
If

Element

's

AttributeSet

does not have this property set, it will revert to false.
**Since:** 1.3

- isSuperscript

```java
public boolean isSuperscript()
```

Determines if the glyphs should be rendered as subscript.

When you request this property,

LabelView

re-syncs its state with the properties of the

Element

's

AttributeSet

.
If

Element

's

AttributeSet

does not have this property set, it will revert to false.

**Overrides:** isSuperscript

in class

GlyphView
**Returns:** the value of the cached

superscript

property
**Since:** 1.3

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

Gives notification from the document that attributes were changed
in a location that this view is responsible for.

**Overrides:** changedUpdate

in class

GlyphView
**Parameters:** e

- the change information from the associated document
**Parameters:** a

- the current allocation of the view
**Parameters:** f

- the factory to use to rebuild if the view has children
**See Also:** View.changedUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

Constructor Detail

- LabelView

```java
public LabelView​(
Element
elem)
```

Constructs a new view wrapped on an element.

**Parameters:** elem

- the element

---

#### Constructor Detail

LabelView

```java
public LabelView​(
Element
elem)
```

Constructs a new view wrapped on an element.

**Parameters:** elem

- the element

---

#### LabelView

public LabelView​(

Element

elem)

Constructs a new view wrapped on an element.

Method Detail

- setUnderline

```java
protected void setUnderline​(boolean u)
```

Sets whether or not the view is underlined.
Note that this setter is protected and is really
only meant if you need to update some additional
state when set.

**Parameters:** u

- true if the view is underlined, otherwise
false
**See Also:** isUnderline()

- setStrikeThrough

```java
protected void setStrikeThrough​(boolean s)
```

Sets whether or not the view has a strike/line
through it.
Note that this setter is protected and is really
only meant if you need to update some additional
state when set.

**Parameters:** s

- true if the view has a strike/line
through it, otherwise false
**See Also:** isStrikeThrough()

- setSuperscript

```java
protected void setSuperscript​(boolean s)
```

Sets whether or not the view represents a
superscript.
Note that this setter is protected and is really
only meant if you need to update some additional
state when set.

**Parameters:** s

- true if the view represents a
superscript, otherwise false
**See Also:** isSuperscript()

- setSubscript

```java
protected void setSubscript​(boolean s)
```

Sets whether or not the view represents a
subscript.
Note that this setter is protected and is really
only meant if you need to update some additional
state when set.

**Parameters:** s

- true if the view represents a
subscript, otherwise false
**See Also:** isSubscript()

- setBackground

```java
protected void setBackground​(
Color
bg)
```

Sets the background color for the view. This method is typically
invoked as part of configuring this

View

. If you need
to customize the background color you should override

setPropertiesFromAttributes

and invoke this method. A
value of null indicates no background should be rendered, so that the
background of the parent

View

will show through.

**Parameters:** bg

- background color, or null
**Since:** 1.5
**See Also:** setPropertiesFromAttributes()

- setPropertiesFromAttributes

```java
protected void setPropertiesFromAttributes()
```

Sets the cached properties from the attributes.

- getFontMetrics

```java
@Deprecated

protected
FontMetrics
getFontMetrics()
```

Deprecated.

FontMetrics are not used for glyph rendering
when running in the JDK.

Fetches the

FontMetrics

used for this view.

**Returns:** the

FontMetrics

used for this view

- getBackground

```java
public
Color
getBackground()
```

Fetches the background color to use to render the glyphs.
This is implemented to return a cached background color,
which defaults to

null

.

**Overrides:** getBackground

in class

GlyphView
**Returns:** the cached background color
**Since:** 1.3

- getForeground

```java
public
Color
getForeground()
```

Fetches the foreground color to use to render the glyphs.
This is implemented to return a cached foreground color,
which defaults to

null

.

**Overrides:** getForeground

in class

GlyphView
**Returns:** the cached foreground color
**Since:** 1.3

- getFont

```java
public
Font
getFont()
```

Fetches the font that the glyphs should be based upon.
This is implemented to return a cached font.

**Overrides:** getFont

in class

GlyphView
**Returns:** the cached font

- isUnderline

```java
public boolean isUnderline()
```

Determines if the glyphs should be underlined. If true,
an underline should be drawn through the baseline. This
is implemented to return the cached underline property.

When you request this property,

LabelView

re-syncs its state with the properties of the

Element

's

AttributeSet

.
If

Element

's

AttributeSet

does not have this property set, it will revert to false.

**Overrides:** isUnderline

in class

GlyphView
**Returns:** the value of the cached

underline

property
**Since:** 1.3

- isStrikeThrough

```java
public boolean isStrikeThrough()
```

Determines if the glyphs should have a strikethrough
line. If true, a line should be drawn through the center
of the glyphs. This is implemented to return the
cached

strikeThrough

property.

When you request this property,

LabelView

re-syncs its state with the properties of the

Element

's

AttributeSet

.
If

Element

's

AttributeSet

does not have this property set, it will revert to false.

**Overrides:** isStrikeThrough

in class

GlyphView
**Returns:** the value of the cached

strikeThrough

property
**Since:** 1.3

- isSubscript

```java
public boolean isSubscript()
```

Determines if the glyphs should be rendered as superscript.

**Overrides:** isSubscript

in class

GlyphView
**Returns:** the value of the cached subscript property

When you request this property,

LabelView

re-syncs its state with the properties of the

Element

's

AttributeSet

.
If

Element

's

AttributeSet

does not have this property set, it will revert to false.
**Since:** 1.3

- isSuperscript

```java
public boolean isSuperscript()
```

Determines if the glyphs should be rendered as subscript.

When you request this property,

LabelView

re-syncs its state with the properties of the

Element

's

AttributeSet

.
If

Element

's

AttributeSet

does not have this property set, it will revert to false.

**Overrides:** isSuperscript

in class

GlyphView
**Returns:** the value of the cached

superscript

property
**Since:** 1.3

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

Gives notification from the document that attributes were changed
in a location that this view is responsible for.

**Overrides:** changedUpdate

in class

GlyphView
**Parameters:** e

- the change information from the associated document
**Parameters:** a

- the current allocation of the view
**Parameters:** f

- the factory to use to rebuild if the view has children
**See Also:** View.changedUpdate(javax.swing.event.DocumentEvent, java.awt.Shape, javax.swing.text.ViewFactory)

---

#### Method Detail

setUnderline

```java
protected void setUnderline​(boolean u)
```

Sets whether or not the view is underlined.
Note that this setter is protected and is really
only meant if you need to update some additional
state when set.

**Parameters:** u

- true if the view is underlined, otherwise
false
**See Also:** isUnderline()

---

#### setUnderline

protected void setUnderline​(boolean u)

Sets whether or not the view is underlined.
Note that this setter is protected and is really
only meant if you need to update some additional
state when set.

setStrikeThrough

```java
protected void setStrikeThrough​(boolean s)
```

Sets whether or not the view has a strike/line
through it.
Note that this setter is protected and is really
only meant if you need to update some additional
state when set.

**Parameters:** s

- true if the view has a strike/line
through it, otherwise false
**See Also:** isStrikeThrough()

---

#### setStrikeThrough

protected void setStrikeThrough​(boolean s)

Sets whether or not the view has a strike/line
through it.
Note that this setter is protected and is really
only meant if you need to update some additional
state when set.

setSuperscript

```java
protected void setSuperscript​(boolean s)
```

Sets whether or not the view represents a
superscript.
Note that this setter is protected and is really
only meant if you need to update some additional
state when set.

**Parameters:** s

- true if the view represents a
superscript, otherwise false
**See Also:** isSuperscript()

---

#### setSuperscript

protected void setSuperscript​(boolean s)

Sets whether or not the view represents a
superscript.
Note that this setter is protected and is really
only meant if you need to update some additional
state when set.

setSubscript

```java
protected void setSubscript​(boolean s)
```

Sets whether or not the view represents a
subscript.
Note that this setter is protected and is really
only meant if you need to update some additional
state when set.

**Parameters:** s

- true if the view represents a
subscript, otherwise false
**See Also:** isSubscript()

---

#### setSubscript

protected void setSubscript​(boolean s)

Sets whether or not the view represents a
subscript.
Note that this setter is protected and is really
only meant if you need to update some additional
state when set.

setBackground

```java
protected void setBackground​(
Color
bg)
```

Sets the background color for the view. This method is typically
invoked as part of configuring this

View

. If you need
to customize the background color you should override

setPropertiesFromAttributes

and invoke this method. A
value of null indicates no background should be rendered, so that the
background of the parent

View

will show through.

**Parameters:** bg

- background color, or null
**Since:** 1.5
**See Also:** setPropertiesFromAttributes()

---

#### setBackground

protected void setBackground​(

Color

bg)

Sets the background color for the view. This method is typically
invoked as part of configuring this

View

. If you need
to customize the background color you should override

setPropertiesFromAttributes

and invoke this method. A
value of null indicates no background should be rendered, so that the
background of the parent

View

will show through.

setPropertiesFromAttributes

```java
protected void setPropertiesFromAttributes()
```

Sets the cached properties from the attributes.

---

#### setPropertiesFromAttributes

protected void setPropertiesFromAttributes()

Sets the cached properties from the attributes.

getFontMetrics

```java
@Deprecated

protected
FontMetrics
getFontMetrics()
```

Deprecated.

FontMetrics are not used for glyph rendering
when running in the JDK.

Fetches the

FontMetrics

used for this view.

**Returns:** the

FontMetrics

used for this view

---

#### getFontMetrics

@Deprecated

protected

FontMetrics

getFontMetrics()

Fetches the

FontMetrics

used for this view.

getBackground

```java
public
Color
getBackground()
```

Fetches the background color to use to render the glyphs.
This is implemented to return a cached background color,
which defaults to

null

.

**Overrides:** getBackground

in class

GlyphView
**Returns:** the cached background color
**Since:** 1.3

---

#### getBackground

public

Color

getBackground()

Fetches the background color to use to render the glyphs.
This is implemented to return a cached background color,
which defaults to

null

.

getForeground

```java
public
Color
getForeground()
```

Fetches the foreground color to use to render the glyphs.
This is implemented to return a cached foreground color,
which defaults to

null

.

**Overrides:** getForeground

in class

GlyphView
**Returns:** the cached foreground color
**Since:** 1.3

---

#### getForeground

public

Color

getForeground()

Fetches the foreground color to use to render the glyphs.
This is implemented to return a cached foreground color,
which defaults to

null

.

getFont

```java
public
Font
getFont()
```

Fetches the font that the glyphs should be based upon.
This is implemented to return a cached font.

**Overrides:** getFont

in class

GlyphView
**Returns:** the cached font

---

#### getFont

public

Font

getFont()

Fetches the font that the glyphs should be based upon.
This is implemented to return a cached font.

isUnderline

```java
public boolean isUnderline()
```

Determines if the glyphs should be underlined. If true,
an underline should be drawn through the baseline. This
is implemented to return the cached underline property.

When you request this property,

LabelView

re-syncs its state with the properties of the

Element

's

AttributeSet

.
If

Element

's

AttributeSet

does not have this property set, it will revert to false.

**Overrides:** isUnderline

in class

GlyphView
**Returns:** the value of the cached

underline

property
**Since:** 1.3

---

#### isUnderline

public boolean isUnderline()

Determines if the glyphs should be underlined. If true,
an underline should be drawn through the baseline. This
is implemented to return the cached underline property.

When you request this property,

LabelView

re-syncs its state with the properties of the

Element

's

AttributeSet

.
If

Element

's

AttributeSet

does not have this property set, it will revert to false.

When you request this property,

LabelView

re-syncs its state with the properties of the

Element

's

AttributeSet

.
If

Element

's

AttributeSet

does not have this property set, it will revert to false.

isStrikeThrough

```java
public boolean isStrikeThrough()
```

Determines if the glyphs should have a strikethrough
line. If true, a line should be drawn through the center
of the glyphs. This is implemented to return the
cached

strikeThrough

property.

When you request this property,

LabelView

re-syncs its state with the properties of the

Element

's

AttributeSet

.
If

Element

's

AttributeSet

does not have this property set, it will revert to false.

**Overrides:** isStrikeThrough

in class

GlyphView
**Returns:** the value of the cached

strikeThrough

property
**Since:** 1.3

---

#### isStrikeThrough

public boolean isStrikeThrough()

Determines if the glyphs should have a strikethrough
line. If true, a line should be drawn through the center
of the glyphs. This is implemented to return the
cached

strikeThrough

property.

When you request this property,

LabelView

re-syncs its state with the properties of the

Element

's

AttributeSet

.
If

Element

's

AttributeSet

does not have this property set, it will revert to false.

When you request this property,

LabelView

re-syncs its state with the properties of the

Element

's

AttributeSet

.
If

Element

's

AttributeSet

does not have this property set, it will revert to false.

isSubscript

```java
public boolean isSubscript()
```

Determines if the glyphs should be rendered as superscript.

**Overrides:** isSubscript

in class

GlyphView
**Returns:** the value of the cached subscript property

When you request this property,

LabelView

re-syncs its state with the properties of the

Element

's

AttributeSet

.
If

Element

's

AttributeSet

does not have this property set, it will revert to false.
**Since:** 1.3

---

#### isSubscript

public boolean isSubscript()

Determines if the glyphs should be rendered as superscript.

When you request this property,

LabelView

re-syncs its state with the properties of the

Element

's

AttributeSet

.
If

Element

's

AttributeSet

does not have this property set, it will revert to false.

isSuperscript

```java
public boolean isSuperscript()
```

Determines if the glyphs should be rendered as subscript.

When you request this property,

LabelView

re-syncs its state with the properties of the

Element

's

AttributeSet

.
If

Element

's

AttributeSet

does not have this property set, it will revert to false.

**Overrides:** isSuperscript

in class

GlyphView
**Returns:** the value of the cached

superscript

property
**Since:** 1.3

---

#### isSuperscript

public boolean isSuperscript()

Determines if the glyphs should be rendered as subscript.

When you request this property,

LabelView

re-syncs its state with the properties of the

Element

's

AttributeSet

.
If

Element

's

AttributeSet

does not have this property set, it will revert to false.

When you request this property,

LabelView

re-syncs its state with the properties of the

Element

's

AttributeSet

.
If

Element

's

AttributeSet

does not have this property set, it will revert to false.

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

Gives notification from the document that attributes were changed
in a location that this view is responsible for.

**Overrides:** changedUpdate

in class

GlyphView
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

Gives notification from the document that attributes were changed
in a location that this view is responsible for.

---

