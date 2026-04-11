# Class JLabel

**Source:** `java.desktop\javax\swing\JLabel.html`

### Class Description

```java
@JavaBean
(
defaultProperty
="UI",

description
="A component that displays a short string and an icon.")
public class
JLabel

extends
JComponent

implements
SwingConstants
,
Accessible
```

A display area for a short text string or an image,
or both.
A label does not react to input events.
As a result, it cannot get the keyboard focus.
A label can, however, display a keyboard alternative
as a convenience for a nearby component
that has a keyboard alternative but can't display it.

A

JLabel

object can display
either text, an image, or both.
You can specify where in the label's display area
the label's contents are aligned
by setting the vertical and horizontal alignment.
By default, labels are vertically centered
in their display area.
Text-only labels are leading edge aligned, by default;
image-only labels are horizontally centered, by default.

You can also specify the position of the text
relative to the image.
By default, text is on the trailing edge of the image,
with the text and image vertically aligned.

A label's leading and trailing edge are determined from the value of its

ComponentOrientation

property. At present, the default
ComponentOrientation setting maps the leading edge to left and the trailing
edge to right.

Finally, you can use the

setIconTextGap

method
to specify how many pixels
should appear between the text and the image.
The default is 4 pixels.

See

How to Use Labels

in

The Java Tutorial

for further documentation.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

,

SwingConstants

---

### Field Details

#### protected
Component
labelFor

The Component this label is for; null if the label
is not the label for a component

---

### Constructor Details

#### public JLabel​(
String
text,

Icon
icon,
int horizontalAlignment)

Creates a

JLabel

instance with the specified
text, image, and horizontal alignment.
The label is centered vertically in its display area.
The text is on the trailing edge of the image.

**Parameters:**
- text

- The text to be displayed by the label.
- icon

- The image to be displayed by the label.
- horizontalAlignment

- One of the following constants
defined in

SwingConstants

:

LEFT

,

CENTER

,

RIGHT

,

LEADING

or

TRAILING

.

---

#### public JLabel​(
String
text,
int horizontalAlignment)

Creates a

JLabel

instance with the specified
text and horizontal alignment.
The label is centered vertically in its display area.

**Parameters:**
- text

- The text to be displayed by the label.
- horizontalAlignment

- One of the following constants
defined in

SwingConstants

:

LEFT

,

CENTER

,

RIGHT

,

LEADING

or

TRAILING

.

---

#### public JLabel​(
String
text)

Creates a

JLabel

instance with the specified text.
The label is aligned against the leading edge of its display area,
and centered vertically.

**Parameters:**
- text

- The text to be displayed by the label.

---

#### public JLabel​(
Icon
image,
int horizontalAlignment)

Creates a

JLabel

instance with the specified
image and horizontal alignment.
The label is centered vertically in its display area.

**Parameters:**
- image

- The image to be displayed by the label.
- horizontalAlignment

- One of the following constants
defined in

SwingConstants

:

LEFT

,

CENTER

,

RIGHT

,

LEADING

or

TRAILING

.

---

#### public JLabel​(
Icon
image)

Creates a

JLabel

instance with the specified image.
The label is centered vertically and horizontally
in its display area.

**Parameters:**
- image

- The image to be displayed by the label.

---

#### public JLabel()

Creates a

JLabel

instance with
no image and with an empty string for the title.
The label is centered vertically
in its display area.
The label's contents, once set, will be displayed on the leading edge
of the label's display area.

---

### Method Details

#### public
LabelUI
getUI()

Returns the L&F object that renders this component.

**Overrides:**
- getUI

in class

JComponent

**Returns:**
- LabelUI object

---

#### @BeanProperty
(
hidden
=true,

visualUpdate
=true,

description
="The UI object that implements the Component\'s LookAndFeel.")
public void setUI​(
LabelUI
ui)

Sets the L&F object that renders this component.

**Parameters:**
- ui

- the LabelUI L&F object

**See Also:**
- UIDefaults.getUI(javax.swing.JComponent)

---

#### public void updateUI()

Resets the UI property to a value from the current look and feel.

**Overrides:**
- updateUI

in class

JComponent

**See Also:**
- JComponent.updateUI()

---

#### @BeanProperty
(
bound
=false)
public
String
getUIClassID()

Returns a string that specifies the name of the l&f class
that renders this component.

**Overrides:**
- getUIClassID

in class

JComponent

**Returns:**
- String "LabelUI"

**See Also:**
- JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

---

#### public
String
getText()

Returns the text string that the label displays.

**Returns:**
- a String

**See Also:**
- setText(java.lang.String)

---

#### @BeanProperty
(
preferred
=true,

visualUpdate
=true,

description
="Defines the single line of text this component will display.")
public void setText​(
String
text)

Defines the single line of text this component will display. If
the value of text is null or empty string, nothing is displayed.

The default value of this property is null.

This is a JavaBeans bound property.

**Parameters:**
- text

- the single line of text this component will display

**See Also:**
- setVerticalTextPosition(int)

,

setHorizontalTextPosition(int)

,

setIcon(javax.swing.Icon)

---

#### public
Icon
getIcon()

Returns the graphic image (glyph, icon) that the label displays.

**Returns:**
- an Icon

**See Also:**
- setIcon(javax.swing.Icon)

---

#### @BeanProperty
(
preferred
=true,

visualUpdate
=true,

description
="The icon this component will display.")
public void setIcon​(
Icon
icon)

Defines the icon this component will display. If
the value of icon is null, nothing is displayed.

The default value of this property is null.

This is a JavaBeans bound property.

**Parameters:**
- icon

- the default icon this component will display

**See Also:**
- setVerticalTextPosition(int)

,

setHorizontalTextPosition(int)

,

getIcon()

---

#### public
Icon
getDisabledIcon()

Returns the icon used by the label when it's disabled.
If no disabled icon has been set this will forward the call to
the look and feel to construct an appropriate disabled Icon.

Some look and feels might not render the disabled Icon, in which
case they will ignore this.

**Returns:**
- the

disabledIcon

property

**See Also:**
- setDisabledIcon(javax.swing.Icon)

,

LookAndFeel.getDisabledIcon(javax.swing.JComponent, javax.swing.Icon)

,

ImageIcon

---

#### @BeanProperty
(
visualUpdate
=true,

description
="The icon to display if the label is disabled.")
public void setDisabledIcon​(
Icon
disabledIcon)

Set the icon to be displayed if this JLabel is "disabled"
(JLabel.setEnabled(false)).

The default value of this property is null.

**Parameters:**
- disabledIcon

- the Icon to display when the component is disabled

**See Also:**
- getDisabledIcon()

,

JComponent.setEnabled(boolean)

---

#### @BeanProperty
(
visualUpdate
=true,

description
="The mnemonic keycode.")
public void setDisplayedMnemonic​(int key)

Specify a keycode that indicates a mnemonic key.
This property is used when the label is part of a larger component.
If the labelFor property of the label is not null, the label will
call the requestFocus method of the component specified by the
labelFor property when the mnemonic is activated.

**Parameters:**
- key

- a keycode that indicates a mnemonic key

**See Also:**
- getLabelFor()

,

setLabelFor(java.awt.Component)

---

#### public void setDisplayedMnemonic​(char aChar)

Specifies the displayedMnemonic as a char value.

**Parameters:**
- aChar

- a char specifying the mnemonic to display

**See Also:**
- setDisplayedMnemonic(int)

---

#### public int getDisplayedMnemonic()

Return the keycode that indicates a mnemonic key.
This property is used when the label is part of a larger component.
If the labelFor property of the label is not null, the label will
call the requestFocus method of the component specified by the
labelFor property when the mnemonic is activated.

**Returns:**
- int value for the mnemonic key

**See Also:**
- getLabelFor()

,

setLabelFor(java.awt.Component)

---

#### @BeanProperty
(
visualUpdate
=true,

description
="the index into the String to draw the keyboard character mnemonic at")
public void setDisplayedMnemonicIndex​(int index)
throws
IllegalArgumentException

Provides a hint to the look and feel as to which character in the
text should be decorated to represent the mnemonic. Not all look and
feels may support this. A value of -1 indicates either there is no
mnemonic, the mnemonic character is not contained in the string, or
the developer does not wish the mnemonic to be displayed.

The value of this is updated as the properties relating to the
mnemonic change (such as the mnemonic itself, the text...).
You should only ever have to call this if
you do not wish the default character to be underlined. For example, if
the text was 'Save As', with a mnemonic of 'a', and you wanted the 'A'
to be decorated, as 'Save

A

s', you would have to invoke

setDisplayedMnemonicIndex(5)

after invoking

setDisplayedMnemonic(KeyEvent.VK_A)

.

**Parameters:**
- index

- Index into the String to underline

**Throws:**
- IllegalArgumentException

- will be thrown if

index

is >= length of the text, or < -1

**Since:**
- 1.4

---

#### public int getDisplayedMnemonicIndex()

Returns the character, as an index, that the look and feel should
provide decoration for as representing the mnemonic character.

**Returns:**
- index representing mnemonic character

**See Also:**
- setDisplayedMnemonicIndex(int)

**Since:**
- 1.4

---

#### protected int checkHorizontalKey​(int key,

String
message)

Verify that key is a legal value for the horizontalAlignment properties.

**Parameters:**
- key

- the property value to check
- message

- the IllegalArgumentException detail message

**Returns:**
- the key value if

key

is a a legal value for the
horizontalAlignment properties

**Throws:**
- IllegalArgumentException

- if key isn't LEFT, CENTER, RIGHT,
LEADING or TRAILING.

**See Also:**
- setHorizontalTextPosition(int)

,

setHorizontalAlignment(int)

---

#### protected int checkVerticalKey​(int key,

String
message)

Verify that key is a legal value for the
verticalAlignment or verticalTextPosition properties.

**Parameters:**
- key

- the property value to check
- message

- the IllegalArgumentException detail message

**Returns:**
- the key value if

key

is a legal value for the
verticalAlignment or verticalTextPosition properties

**Throws:**
- IllegalArgumentException

- if key isn't TOP, CENTER, or BOTTOM.

**See Also:**
- setVerticalAlignment(int)

,

setVerticalTextPosition(int)

---

#### public int getIconTextGap()

Returns the amount of space between the text and the icon
displayed in this label.

**Returns:**
- an int equal to the number of pixels between the text
and the icon.

**See Also:**
- setIconTextGap(int)

---

#### @BeanProperty
(
visualUpdate
=true,

description
="If both the icon and text properties are set, this property defines the space between them.")
public void setIconTextGap​(int iconTextGap)

If both the icon and text properties are set, this property
defines the space between them.

The default value of this property is 4 pixels.

This is a JavaBeans bound property.

**Parameters:**
- iconTextGap

- the space between the icon and text properties

**See Also:**
- getIconTextGap()

---

#### public int getVerticalAlignment()

Returns the alignment of the label's contents along the Y axis.

**Returns:**
- The value of the verticalAlignment property, one of the
following constants defined in

SwingConstants

:

TOP

,

CENTER

, or

BOTTOM

.

**See Also:**
- SwingConstants

,

setVerticalAlignment(int)

---

#### @BeanProperty
(
visualUpdate
=true,

enumerationValues
={"SwingConstants.TOP","SwingConstants.CENTER","SwingConstants.BOTTOM"},

description
="The alignment of the label\'s contents along the Y axis.")
public void setVerticalAlignment​(int alignment)

Sets the alignment of the label's contents along the Y axis.

The default value of this property is CENTER.

**Parameters:**
- alignment

- One of the following constants
defined in

SwingConstants

:

TOP

,

CENTER

(the default), or

BOTTOM

.

**See Also:**
- SwingConstants

,

getVerticalAlignment()

---

#### public int getHorizontalAlignment()

Returns the alignment of the label's contents along the X axis.

**Returns:**
- The value of the horizontalAlignment property, one of the
following constants defined in

SwingConstants

:

LEFT

,

CENTER

,

RIGHT

,

LEADING

or

TRAILING

.

**See Also:**
- setHorizontalAlignment(int)

,

SwingConstants

---

#### @BeanProperty
(
visualUpdate
=true,

enumerationValues
={"SwingConstants.LEFT","SwingConstants.CENTER","SwingConstants.RIGHT","SwingConstants.LEADING","SwingConstants.TRAILING"},

description
="The alignment of the label\'s content along the X axis.")
public void setHorizontalAlignment​(int alignment)

Sets the alignment of the label's contents along the X axis.

This is a JavaBeans bound property.

**Parameters:**
- alignment

- One of the following constants
defined in

SwingConstants

:

LEFT

,

CENTER

(the default for image-only labels),

RIGHT

,

LEADING

(the default for text-only labels) or

TRAILING

.

**See Also:**
- SwingConstants

,

getHorizontalAlignment()

---

#### public int getVerticalTextPosition()

Returns the vertical position of the label's text,
relative to its image.

**Returns:**
- One of the following constants
defined in

SwingConstants

:

TOP

,

CENTER

, or

BOTTOM

.

**See Also:**
- setVerticalTextPosition(int)

,

SwingConstants

---

#### @BeanProperty
(
expert
=true,

visualUpdate
=true,

enumerationValues
={"SwingConstants.TOP","SwingConstants.CENTER","SwingConstants.BOTTOM"},

description
="The vertical position of the text relative to it\'s image.")
public void setVerticalTextPosition​(int textPosition)

Sets the vertical position of the label's text,
relative to its image.

The default value of this property is CENTER.

This is a JavaBeans bound property.

**Parameters:**
- textPosition

- One of the following constants
defined in

SwingConstants

:

TOP

,

CENTER

(the default), or

BOTTOM

.

**See Also:**
- SwingConstants

,

getVerticalTextPosition()

---

#### public int getHorizontalTextPosition()

Returns the horizontal position of the label's text,
relative to its image.

**Returns:**
- One of the following constants
defined in

SwingConstants

:

LEFT

,

CENTER

,

RIGHT

,

LEADING

or

TRAILING

.

**See Also:**
- SwingConstants

---

#### @BeanProperty
(
expert
=true,

visualUpdate
=true,

enumerationValues
={"SwingConstants.LEFT","SwingConstants.CENTER","SwingConstants.RIGHT","SwingConstants.LEADING","SwingConstants.TRAILING"},

description
="The horizontal position of the label\'s text, relative to its image.")
public void setHorizontalTextPosition​(int textPosition)

Sets the horizontal position of the label's text,
relative to its image.

**Parameters:**
- textPosition

- One of the following constants
defined in

SwingConstants

:

LEFT

,

CENTER

,

RIGHT

,

LEADING

, or

TRAILING

(the default).

**See Also:**
- SwingConstants

---

#### public boolean imageUpdate​(
Image
img,
int infoflags,
int x,
int y,
int w,
int h)

This is overridden to return false if the current Icon's Image is
not equal to the passed in Image

img

.

**Specified by:**
- imageUpdate

in interface

ImageObserver

**Overrides:**
- imageUpdate

in class

Component

**Parameters:**
- img

- the image being observed
- infoflags

- see

imageUpdate

for more information
- x

- the

x

coordinate
- y

- the

y

coordinate
- w

- the width
- h

- the height

**Returns:**
- false

if the infoflags indicate that the
image is completely loaded;

true

otherwise.

**See Also:**
- ImageObserver

,

Component.imageUpdate(java.awt.Image, int, int, int, int, int)

---

#### protected
String
paramString()

Returns a string representation of this JLabel. This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:**
- paramString

in class

JComponent

**Returns:**
- a string representation of this JLabel.

---

#### public
Component
getLabelFor()

Get the component this is labelling.

**Returns:**
- the Component this is labelling. Can be null if this
does not label a Component. If the displayedMnemonic
property is set and the labelFor property is also set, the label
will call the requestFocus method of the component specified by the
labelFor property when the mnemonic is activated.

**See Also:**
- getDisplayedMnemonic()

,

setDisplayedMnemonic(int)

---

#### @BeanProperty
(
description
="The component this is labelling.")
public void setLabelFor​(
Component
c)

Set the component this is labelling. Can be null if this does not
label a Component. If the displayedMnemonic property is set
and the labelFor property is also set, the label will
call the requestFocus method of the component specified by the
labelFor property when the mnemonic is activated.

**Parameters:**
- c

- the Component this label is for, or null if the label is
not the label for a component

**See Also:**
- getDisplayedMnemonic()

,

setDisplayedMnemonic(int)

---

#### @BeanProperty
(
bound
=false,

expert
=true,

description
="The AccessibleContext associated with this Label.")
public
AccessibleContext
getAccessibleContext()

Get the AccessibleContext of this object

**Specified by:**
- getAccessibleContext

in interface

Accessible

**Overrides:**
- getAccessibleContext

in class

Component

**Returns:**
- the AccessibleContext of this object

---

### Additional Sections

#### Class JLabel

java.lang.Object

- java.awt.Component
- - java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JLabel

java.awt.Component

- java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JLabel

java.awt.Container

- javax.swing.JComponent
- - javax.swing.JLabel

javax.swing.JComponent

- javax.swing.JLabel

javax.swing.JLabel

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

,

SwingConstants

**Direct Known Subclasses:** BasicComboBoxRenderer

,

DefaultListCellRenderer

,

DefaultTableCellRenderer

,

DefaultTreeCellRenderer

```java
@JavaBean
(
defaultProperty
="UI",

description
="A component that displays a short string and an icon.")
public class
JLabel

extends
JComponent

implements
SwingConstants
,
Accessible
```

A display area for a short text string or an image,
or both.
A label does not react to input events.
As a result, it cannot get the keyboard focus.
A label can, however, display a keyboard alternative
as a convenience for a nearby component
that has a keyboard alternative but can't display it.

A

JLabel

object can display
either text, an image, or both.
You can specify where in the label's display area
the label's contents are aligned
by setting the vertical and horizontal alignment.
By default, labels are vertically centered
in their display area.
Text-only labels are leading edge aligned, by default;
image-only labels are horizontally centered, by default.

You can also specify the position of the text
relative to the image.
By default, text is on the trailing edge of the image,
with the text and image vertically aligned.

A label's leading and trailing edge are determined from the value of its

ComponentOrientation

property. At present, the default
ComponentOrientation setting maps the leading edge to left and the trailing
edge to right.

Finally, you can use the

setIconTextGap

method
to specify how many pixels
should appear between the text and the image.
The default is 4 pixels.

See

How to Use Labels

in

The Java Tutorial

for further documentation.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

**Since:** 1.2
**See Also:** Serialized Form

@JavaBean

(

defaultProperty

="UI",

description

="A component that displays a short string and an icon.")
public class

JLabel

extends

JComponent

implements

SwingConstants

,

Accessible

A display area for a short text string or an image,
or both.
A label does not react to input events.
As a result, it cannot get the keyboard focus.
A label can, however, display a keyboard alternative
as a convenience for a nearby component
that has a keyboard alternative but can't display it.

A

JLabel

object can display
either text, an image, or both.
You can specify where in the label's display area
the label's contents are aligned
by setting the vertical and horizontal alignment.
By default, labels are vertically centered
in their display area.
Text-only labels are leading edge aligned, by default;
image-only labels are horizontally centered, by default.

You can also specify the position of the text
relative to the image.
By default, text is on the trailing edge of the image,
with the text and image vertically aligned.

A label's leading and trailing edge are determined from the value of its

ComponentOrientation

property. At present, the default
ComponentOrientation setting maps the leading edge to left and the trailing
edge to right.

Finally, you can use the

setIconTextGap

method
to specify how many pixels
should appear between the text and the image.
The default is 4 pixels.

See

How to Use Labels

in

The Java Tutorial

for further documentation.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

A

JLabel

object can display
either text, an image, or both.
You can specify where in the label's display area
the label's contents are aligned
by setting the vertical and horizontal alignment.
By default, labels are vertically centered
in their display area.
Text-only labels are leading edge aligned, by default;
image-only labels are horizontally centered, by default.

You can also specify the position of the text
relative to the image.
By default, text is on the trailing edge of the image,
with the text and image vertically aligned.

A label's leading and trailing edge are determined from the value of its

ComponentOrientation

property. At present, the default
ComponentOrientation setting maps the leading edge to left and the trailing
edge to right.

Finally, you can use the

setIconTextGap

method
to specify how many pixels
should appear between the text and the image.
The default is 4 pixels.

See

How to Use Labels

in

The Java Tutorial

for further documentation.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

You can also specify the position of the text
relative to the image.
By default, text is on the trailing edge of the image,
with the text and image vertically aligned.

A label's leading and trailing edge are determined from the value of its

ComponentOrientation

property. At present, the default
ComponentOrientation setting maps the leading edge to left and the trailing
edge to right.

Finally, you can use the

setIconTextGap

method
to specify how many pixels
should appear between the text and the image.
The default is 4 pixels.

See

How to Use Labels

in

The Java Tutorial

for further documentation.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

A label's leading and trailing edge are determined from the value of its

ComponentOrientation

property. At present, the default
ComponentOrientation setting maps the leading edge to left and the trailing
edge to right.

Finally, you can use the

setIconTextGap

method
to specify how many pixels
should appear between the text and the image.
The default is 4 pixels.

See

How to Use Labels

in

The Java Tutorial

for further documentation.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

Finally, you can use the

setIconTextGap

method
to specify how many pixels
should appear between the text and the image.
The default is 4 pixels.

See

How to Use Labels

in

The Java Tutorial

for further documentation.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

See

How to Use Labels

in

The Java Tutorial

for further documentation.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

JLabel.AccessibleJLabel

The class used to obtain the accessible role for this object.

- Nested classes/interfaces declared in class javax.swing.

JComponent

JComponent.AccessibleJComponent

- Nested classes/interfaces declared in class java.awt.

Container

Container.AccessibleAWTContainer

- Nested classes/interfaces declared in class java.awt.

Component

Component.AccessibleAWTComponent

,

Component.BaselineResizeBehavior

,

Component.BltBufferStrategy

,

Component.FlipBufferStrategy

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

Component

labelFor

The Component this label is for; null if the label
is not the label for a component

- Fields declared in class javax.swing.

JComponent

listenerList

,

TOOL_TIP_TEXT_KEY

,

ui

,

UNDEFINED_CONDITION

,

WHEN_ANCESTOR_OF_FOCUSED_COMPONENT

,

WHEN_FOCUSED

,

WHEN_IN_FOCUSED_WINDOW

- Fields declared in class java.awt.

Component

accessibleContext

,

BOTTOM_ALIGNMENT

,

CENTER_ALIGNMENT

,

LEFT_ALIGNMENT

,

RIGHT_ALIGNMENT

,

TOP_ALIGNMENT

- Fields declared in interface java.awt.image.

ImageObserver

ABORT

,

ALLBITS

,

ERROR

,

FRAMEBITS

,

HEIGHT

,

PROPERTIES

,

SOMEBITS

,

WIDTH

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

JLabel

()

Creates a

JLabel

instance with
no image and with an empty string for the title.

JLabel

​(

String

text)

Creates a

JLabel

instance with the specified text.

JLabel

​(

String

text,
int horizontalAlignment)

Creates a

JLabel

instance with the specified
text and horizontal alignment.

JLabel

​(

String

text,

Icon

icon,
int horizontalAlignment)

Creates a

JLabel

instance with the specified
text, image, and horizontal alignment.

JLabel

​(

Icon

image)

Creates a

JLabel

instance with the specified image.

JLabel

​(

Icon

image,
int horizontalAlignment)

Creates a

JLabel

instance with the specified
image and horizontal alignment.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected int

checkHorizontalKey

​(int key,

String

message)

Verify that key is a legal value for the horizontalAlignment properties.

protected int

checkVerticalKey

​(int key,

String

message)

Verify that key is a legal value for the
verticalAlignment or verticalTextPosition properties.

AccessibleContext

getAccessibleContext

()

Get the AccessibleContext of this object

Icon

getDisabledIcon

()

Returns the icon used by the label when it's disabled.

int

getDisplayedMnemonic

()

Return the keycode that indicates a mnemonic key.

int

getDisplayedMnemonicIndex

()

Returns the character, as an index, that the look and feel should
provide decoration for as representing the mnemonic character.

int

getHorizontalAlignment

()

Returns the alignment of the label's contents along the X axis.

int

getHorizontalTextPosition

()

Returns the horizontal position of the label's text,
relative to its image.

Icon

getIcon

()

Returns the graphic image (glyph, icon) that the label displays.

int

getIconTextGap

()

Returns the amount of space between the text and the icon
displayed in this label.

Component

getLabelFor

()

Get the component this is labelling.

String

getText

()

Returns the text string that the label displays.

LabelUI

getUI

()

Returns the L&F object that renders this component.

String

getUIClassID

()

Returns a string that specifies the name of the l&f class
that renders this component.

int

getVerticalAlignment

()

Returns the alignment of the label's contents along the Y axis.

int

getVerticalTextPosition

()

Returns the vertical position of the label's text,
relative to its image.

boolean

imageUpdate

​(

Image

img,
int infoflags,
int x,
int y,
int w,
int h)

This is overridden to return false if the current Icon's Image is
not equal to the passed in Image

img

.

protected

String

paramString

()

Returns a string representation of this JLabel.

void

setDisabledIcon

​(

Icon

disabledIcon)

Set the icon to be displayed if this JLabel is "disabled"
(JLabel.setEnabled(false)).

void

setDisplayedMnemonic

​(char aChar)

Specifies the displayedMnemonic as a char value.

void

setDisplayedMnemonic

​(int key)

Specify a keycode that indicates a mnemonic key.

void

setDisplayedMnemonicIndex

​(int index)

Provides a hint to the look and feel as to which character in the
text should be decorated to represent the mnemonic.

void

setHorizontalAlignment

​(int alignment)

Sets the alignment of the label's contents along the X axis.

void

setHorizontalTextPosition

​(int textPosition)

Sets the horizontal position of the label's text,
relative to its image.

void

setIcon

​(

Icon

icon)

Defines the icon this component will display.

void

setIconTextGap

​(int iconTextGap)

If both the icon and text properties are set, this property
defines the space between them.

void

setLabelFor

​(

Component

c)

Set the component this is labelling.

void

setText

​(

String

text)

Defines the single line of text this component will display.

void

setUI

​(

LabelUI

ui)

Sets the L&F object that renders this component.

void

setVerticalAlignment

​(int alignment)

Sets the alignment of the label's contents along the Y axis.

void

setVerticalTextPosition

​(int textPosition)

Sets the vertical position of the label's text,
relative to its image.

void

updateUI

()

Resets the UI property to a value from the current look and feel.

- Methods declared in class javax.swing.

JComponent

addAncestorListener

,

addNotify

,

addVetoableChangeListener

,

computeVisibleRect

,

contains

,

createToolTip

,

disable

,

enable

,

firePropertyChange

,

firePropertyChange

,

fireVetoableChange

,

getActionForKeyStroke

,

getActionMap

,

getAlignmentX

,

getAlignmentY

,

getAncestorListeners

,

getAutoscrolls

,

getBaseline

,

getBaselineResizeBehavior

,

getBorder

,

getBounds

,

getClientProperty

,

getComponentGraphics

,

getComponentPopupMenu

,

getConditionForKeyStroke

,

getDebugGraphicsOptions

,

getDefaultLocale

,

getFontMetrics

,

getGraphics

,

getHeight

,

getInheritsPopupMenu

,

getInputMap

,

getInputMap

,

getInputVerifier

,

getInsets

,

getInsets

,

getListeners

,

getLocation

,

getMaximumSize

,

getMinimumSize

,

getNextFocusableComponent

,

getPopupLocation

,

getPreferredSize

,

getRegisteredKeyStrokes

,

getRootPane

,

getSize

,

getToolTipLocation

,

getToolTipText

,

getToolTipText

,

getTopLevelAncestor

,

getTransferHandler

,

getVerifyInputWhenFocusTarget

,

getVetoableChangeListeners

,

getVisibleRect

,

getWidth

,

getX

,

getY

,

grabFocus

,

isDoubleBuffered

,

isLightweightComponent

,

isManagingFocus

,

isOpaque

,

isOptimizedDrawingEnabled

,

isPaintingForPrint

,

isPaintingOrigin

,

isPaintingTile

,

isRequestFocusEnabled

,

isValidateRoot

,

paint

,

paintBorder

,

paintChildren

,

paintComponent

,

paintImmediately

,

paintImmediately

,

print

,

printAll

,

printBorder

,

printChildren

,

printComponent

,

processComponentKeyEvent

,

processKeyBinding

,

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

,

putClientProperty

,

registerKeyboardAction

,

registerKeyboardAction

,

removeAncestorListener

,

removeNotify

,

removeVetoableChangeListener

,

repaint

,

repaint

,

requestDefaultFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

resetKeyboardActions

,

reshape

,

revalidate

,

scrollRectToVisible

,

setActionMap

,

setAlignmentX

,

setAlignmentY

,

setAutoscrolls

,

setBackground

,

setBorder

,

setComponentPopupMenu

,

setDebugGraphicsOptions

,

setDefaultLocale

,

setDoubleBuffered

,

setEnabled

,

setFocusTraversalKeys

,

setFont

,

setForeground

,

setInheritsPopupMenu

,

setInputMap

,

setInputVerifier

,

setMaximumSize

,

setMinimumSize

,

setNextFocusableComponent

,

setOpaque

,

setPreferredSize

,

setRequestFocusEnabled

,

setToolTipText

,

setTransferHandler

,

setUI

,

setVerifyInputWhenFocusTarget

,

setVisible

,

unregisterKeyboardAction

,

update

- Methods declared in class java.awt.

Container

add

,

add

,

add

,

add

,

add

,

addContainerListener

,

addImpl

,

addPropertyChangeListener

,

addPropertyChangeListener

,

applyComponentOrientation

,

areFocusTraversalKeysSet

,

countComponents

,

deliverEvent

,

doLayout

,

findComponentAt

,

findComponentAt

,

getComponent

,

getComponentAt

,

getComponentAt

,

getComponentCount

,

getComponents

,

getComponentZOrder

,

getContainerListeners

,

getFocusTraversalKeys

,

getFocusTraversalPolicy

,

getLayout

,

getMousePosition

,

insets

,

invalidate

,

isAncestorOf

,

isFocusCycleRoot

,

isFocusCycleRoot

,

isFocusTraversalPolicyProvider

,

isFocusTraversalPolicySet

,

layout

,

list

,

list

,

locate

,

minimumSize

,

paintComponents

,

preferredSize

,

printComponents

,

processContainerEvent

,

processEvent

,

remove

,

remove

,

removeAll

,

removeContainerListener

,

setComponentZOrder

,

setFocusCycleRoot

,

setFocusTraversalPolicy

,

setFocusTraversalPolicyProvider

,

setLayout

,

transferFocusDownCycle

,

validate

,

validateTree

- Methods declared in class java.awt.

Component

action

,

add

,

addComponentListener

,

addFocusListener

,

addHierarchyBoundsListener

,

addHierarchyListener

,

addInputMethodListener

,

addKeyListener

,

addMouseListener

,

addMouseMotionListener

,

addMouseWheelListener

,

bounds

,

checkImage

,

checkImage

,

coalesceEvents

,

contains

,

createImage

,

createImage

,

createVolatileImage

,

createVolatileImage

,

disableEvents

,

dispatchEvent

,

enable

,

enableEvents

,

enableInputMethods

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

getBackground

,

getBounds

,

getColorModel

,

getComponentListeners

,

getComponentOrientation

,

getCursor

,

getDropTarget

,

getFocusCycleRootAncestor

,

getFocusListeners

,

getFocusTraversalKeysEnabled

,

getFont

,

getForeground

,

getGraphicsConfiguration

,

getHierarchyBoundsListeners

,

getHierarchyListeners

,

getIgnoreRepaint

,

getInputContext

,

getInputMethodListeners

,

getInputMethodRequests

,

getKeyListeners

,

getLocale

,

getLocation

,

getLocationOnScreen

,

getMouseListeners

,

getMouseMotionListeners

,

getMousePosition

,

getMouseWheelListeners

,

getName

,

getParent

,

getPropertyChangeListeners

,

getPropertyChangeListeners

,

getSize

,

getToolkit

,

getTreeLock

,

gotFocus

,

handleEvent

,

hasFocus

,

hide

,

inside

,

isBackgroundSet

,

isCursorSet

,

isDisplayable

,

isEnabled

,

isFocusable

,

isFocusOwner

,

isFocusTraversable

,

isFontSet

,

isForegroundSet

,

isLightweight

,

isMaximumSizeSet

,

isMinimumSizeSet

,

isPreferredSizeSet

,

isShowing

,

isValid

,

isVisible

,

keyDown

,

keyUp

,

list

,

list

,

list

,

location

,

lostFocus

,

mouseDown

,

mouseDrag

,

mouseEnter

,

mouseExit

,

mouseMove

,

mouseUp

,

move

,

nextFocus

,

paintAll

,

postEvent

,

prepareImage

,

prepareImage

,

processComponentEvent

,

processFocusEvent

,

processHierarchyBoundsEvent

,

processHierarchyEvent

,

processInputMethodEvent

,

processMouseWheelEvent

,

remove

,

removeComponentListener

,

removeFocusListener

,

removeHierarchyBoundsListener

,

removeHierarchyListener

,

removeInputMethodListener

,

removeKeyListener

,

removeMouseListener

,

removeMouseMotionListener

,

removeMouseWheelListener

,

removePropertyChangeListener

,

removePropertyChangeListener

,

repaint

,

repaint

,

repaint

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

resize

,

resize

,

setBounds

,

setBounds

,

setComponentOrientation

,

setCursor

,

setDropTarget

,

setFocusable

,

setFocusTraversalKeysEnabled

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMixingCutoutShape

,

setName

,

setSize

,

setSize

,

show

,

show

,

size

,

toString

,

transferFocus

,

transferFocusBackward

,

transferFocusUpCycle

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

JLabel.AccessibleJLabel

The class used to obtain the accessible role for this object.

- Nested classes/interfaces declared in class javax.swing.

JComponent

JComponent.AccessibleJComponent

- Nested classes/interfaces declared in class java.awt.

Container

Container.AccessibleAWTContainer

- Nested classes/interfaces declared in class java.awt.

Component

Component.AccessibleAWTComponent

,

Component.BaselineResizeBehavior

,

Component.BltBufferStrategy

,

Component.FlipBufferStrategy

---

#### Nested Class Summary

The class used to obtain the accessible role for this object.

Nested classes/interfaces declared in class javax.swing.

JComponent

JComponent.AccessibleJComponent

---

#### Nested classes/interfaces declared in class javax.swing. JComponent

Nested classes/interfaces declared in class java.awt.

Container

Container.AccessibleAWTContainer

---

#### Nested classes/interfaces declared in class java.awt. Container

Nested classes/interfaces declared in class java.awt.

Component

Component.AccessibleAWTComponent

,

Component.BaselineResizeBehavior

,

Component.BltBufferStrategy

,

Component.FlipBufferStrategy

---

#### Nested classes/interfaces declared in class java.awt. Component

Field Summary

Fields

Modifier and Type

Field

Description

protected

Component

labelFor

The Component this label is for; null if the label
is not the label for a component

- Fields declared in class javax.swing.

JComponent

listenerList

,

TOOL_TIP_TEXT_KEY

,

ui

,

UNDEFINED_CONDITION

,

WHEN_ANCESTOR_OF_FOCUSED_COMPONENT

,

WHEN_FOCUSED

,

WHEN_IN_FOCUSED_WINDOW

- Fields declared in class java.awt.

Component

accessibleContext

,

BOTTOM_ALIGNMENT

,

CENTER_ALIGNMENT

,

LEFT_ALIGNMENT

,

RIGHT_ALIGNMENT

,

TOP_ALIGNMENT

- Fields declared in interface java.awt.image.

ImageObserver

ABORT

,

ALLBITS

,

ERROR

,

FRAMEBITS

,

HEIGHT

,

PROPERTIES

,

SOMEBITS

,

WIDTH

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

The Component this label is for; null if the label
is not the label for a component

Fields declared in class javax.swing.

JComponent

listenerList

,

TOOL_TIP_TEXT_KEY

,

ui

,

UNDEFINED_CONDITION

,

WHEN_ANCESTOR_OF_FOCUSED_COMPONENT

,

WHEN_FOCUSED

,

WHEN_IN_FOCUSED_WINDOW

---

#### Fields declared in class javax.swing. JComponent

Fields declared in class java.awt.

Component

accessibleContext

,

BOTTOM_ALIGNMENT

,

CENTER_ALIGNMENT

,

LEFT_ALIGNMENT

,

RIGHT_ALIGNMENT

,

TOP_ALIGNMENT

---

#### Fields declared in class java.awt. Component

Fields declared in interface java.awt.image.

ImageObserver

ABORT

,

ALLBITS

,

ERROR

,

FRAMEBITS

,

HEIGHT

,

PROPERTIES

,

SOMEBITS

,

WIDTH

---

#### Fields declared in interface java.awt.image. ImageObserver

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

JLabel

()

Creates a

JLabel

instance with
no image and with an empty string for the title.

JLabel

​(

String

text)

Creates a

JLabel

instance with the specified text.

JLabel

​(

String

text,
int horizontalAlignment)

Creates a

JLabel

instance with the specified
text and horizontal alignment.

JLabel

​(

String

text,

Icon

icon,
int horizontalAlignment)

Creates a

JLabel

instance with the specified
text, image, and horizontal alignment.

JLabel

​(

Icon

image)

Creates a

JLabel

instance with the specified image.

JLabel

​(

Icon

image,
int horizontalAlignment)

Creates a

JLabel

instance with the specified
image and horizontal alignment.

---

#### Constructor Summary

Creates a

JLabel

instance with
no image and with an empty string for the title.

Creates a

JLabel

instance with the specified text.

Creates a

JLabel

instance with the specified
text and horizontal alignment.

Creates a

JLabel

instance with the specified
text, image, and horizontal alignment.

Creates a

JLabel

instance with the specified image.

Creates a

JLabel

instance with the specified
image and horizontal alignment.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected int

checkHorizontalKey

​(int key,

String

message)

Verify that key is a legal value for the horizontalAlignment properties.

protected int

checkVerticalKey

​(int key,

String

message)

Verify that key is a legal value for the
verticalAlignment or verticalTextPosition properties.

AccessibleContext

getAccessibleContext

()

Get the AccessibleContext of this object

Icon

getDisabledIcon

()

Returns the icon used by the label when it's disabled.

int

getDisplayedMnemonic

()

Return the keycode that indicates a mnemonic key.

int

getDisplayedMnemonicIndex

()

Returns the character, as an index, that the look and feel should
provide decoration for as representing the mnemonic character.

int

getHorizontalAlignment

()

Returns the alignment of the label's contents along the X axis.

int

getHorizontalTextPosition

()

Returns the horizontal position of the label's text,
relative to its image.

Icon

getIcon

()

Returns the graphic image (glyph, icon) that the label displays.

int

getIconTextGap

()

Returns the amount of space between the text and the icon
displayed in this label.

Component

getLabelFor

()

Get the component this is labelling.

String

getText

()

Returns the text string that the label displays.

LabelUI

getUI

()

Returns the L&F object that renders this component.

String

getUIClassID

()

Returns a string that specifies the name of the l&f class
that renders this component.

int

getVerticalAlignment

()

Returns the alignment of the label's contents along the Y axis.

int

getVerticalTextPosition

()

Returns the vertical position of the label's text,
relative to its image.

boolean

imageUpdate

​(

Image

img,
int infoflags,
int x,
int y,
int w,
int h)

This is overridden to return false if the current Icon's Image is
not equal to the passed in Image

img

.

protected

String

paramString

()

Returns a string representation of this JLabel.

void

setDisabledIcon

​(

Icon

disabledIcon)

Set the icon to be displayed if this JLabel is "disabled"
(JLabel.setEnabled(false)).

void

setDisplayedMnemonic

​(char aChar)

Specifies the displayedMnemonic as a char value.

void

setDisplayedMnemonic

​(int key)

Specify a keycode that indicates a mnemonic key.

void

setDisplayedMnemonicIndex

​(int index)

Provides a hint to the look and feel as to which character in the
text should be decorated to represent the mnemonic.

void

setHorizontalAlignment

​(int alignment)

Sets the alignment of the label's contents along the X axis.

void

setHorizontalTextPosition

​(int textPosition)

Sets the horizontal position of the label's text,
relative to its image.

void

setIcon

​(

Icon

icon)

Defines the icon this component will display.

void

setIconTextGap

​(int iconTextGap)

If both the icon and text properties are set, this property
defines the space between them.

void

setLabelFor

​(

Component

c)

Set the component this is labelling.

void

setText

​(

String

text)

Defines the single line of text this component will display.

void

setUI

​(

LabelUI

ui)

Sets the L&F object that renders this component.

void

setVerticalAlignment

​(int alignment)

Sets the alignment of the label's contents along the Y axis.

void

setVerticalTextPosition

​(int textPosition)

Sets the vertical position of the label's text,
relative to its image.

void

updateUI

()

Resets the UI property to a value from the current look and feel.

- Methods declared in class javax.swing.

JComponent

addAncestorListener

,

addNotify

,

addVetoableChangeListener

,

computeVisibleRect

,

contains

,

createToolTip

,

disable

,

enable

,

firePropertyChange

,

firePropertyChange

,

fireVetoableChange

,

getActionForKeyStroke

,

getActionMap

,

getAlignmentX

,

getAlignmentY

,

getAncestorListeners

,

getAutoscrolls

,

getBaseline

,

getBaselineResizeBehavior

,

getBorder

,

getBounds

,

getClientProperty

,

getComponentGraphics

,

getComponentPopupMenu

,

getConditionForKeyStroke

,

getDebugGraphicsOptions

,

getDefaultLocale

,

getFontMetrics

,

getGraphics

,

getHeight

,

getInheritsPopupMenu

,

getInputMap

,

getInputMap

,

getInputVerifier

,

getInsets

,

getInsets

,

getListeners

,

getLocation

,

getMaximumSize

,

getMinimumSize

,

getNextFocusableComponent

,

getPopupLocation

,

getPreferredSize

,

getRegisteredKeyStrokes

,

getRootPane

,

getSize

,

getToolTipLocation

,

getToolTipText

,

getToolTipText

,

getTopLevelAncestor

,

getTransferHandler

,

getVerifyInputWhenFocusTarget

,

getVetoableChangeListeners

,

getVisibleRect

,

getWidth

,

getX

,

getY

,

grabFocus

,

isDoubleBuffered

,

isLightweightComponent

,

isManagingFocus

,

isOpaque

,

isOptimizedDrawingEnabled

,

isPaintingForPrint

,

isPaintingOrigin

,

isPaintingTile

,

isRequestFocusEnabled

,

isValidateRoot

,

paint

,

paintBorder

,

paintChildren

,

paintComponent

,

paintImmediately

,

paintImmediately

,

print

,

printAll

,

printBorder

,

printChildren

,

printComponent

,

processComponentKeyEvent

,

processKeyBinding

,

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

,

putClientProperty

,

registerKeyboardAction

,

registerKeyboardAction

,

removeAncestorListener

,

removeNotify

,

removeVetoableChangeListener

,

repaint

,

repaint

,

requestDefaultFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

resetKeyboardActions

,

reshape

,

revalidate

,

scrollRectToVisible

,

setActionMap

,

setAlignmentX

,

setAlignmentY

,

setAutoscrolls

,

setBackground

,

setBorder

,

setComponentPopupMenu

,

setDebugGraphicsOptions

,

setDefaultLocale

,

setDoubleBuffered

,

setEnabled

,

setFocusTraversalKeys

,

setFont

,

setForeground

,

setInheritsPopupMenu

,

setInputMap

,

setInputVerifier

,

setMaximumSize

,

setMinimumSize

,

setNextFocusableComponent

,

setOpaque

,

setPreferredSize

,

setRequestFocusEnabled

,

setToolTipText

,

setTransferHandler

,

setUI

,

setVerifyInputWhenFocusTarget

,

setVisible

,

unregisterKeyboardAction

,

update

- Methods declared in class java.awt.

Container

add

,

add

,

add

,

add

,

add

,

addContainerListener

,

addImpl

,

addPropertyChangeListener

,

addPropertyChangeListener

,

applyComponentOrientation

,

areFocusTraversalKeysSet

,

countComponents

,

deliverEvent

,

doLayout

,

findComponentAt

,

findComponentAt

,

getComponent

,

getComponentAt

,

getComponentAt

,

getComponentCount

,

getComponents

,

getComponentZOrder

,

getContainerListeners

,

getFocusTraversalKeys

,

getFocusTraversalPolicy

,

getLayout

,

getMousePosition

,

insets

,

invalidate

,

isAncestorOf

,

isFocusCycleRoot

,

isFocusCycleRoot

,

isFocusTraversalPolicyProvider

,

isFocusTraversalPolicySet

,

layout

,

list

,

list

,

locate

,

minimumSize

,

paintComponents

,

preferredSize

,

printComponents

,

processContainerEvent

,

processEvent

,

remove

,

remove

,

removeAll

,

removeContainerListener

,

setComponentZOrder

,

setFocusCycleRoot

,

setFocusTraversalPolicy

,

setFocusTraversalPolicyProvider

,

setLayout

,

transferFocusDownCycle

,

validate

,

validateTree

- Methods declared in class java.awt.

Component

action

,

add

,

addComponentListener

,

addFocusListener

,

addHierarchyBoundsListener

,

addHierarchyListener

,

addInputMethodListener

,

addKeyListener

,

addMouseListener

,

addMouseMotionListener

,

addMouseWheelListener

,

bounds

,

checkImage

,

checkImage

,

coalesceEvents

,

contains

,

createImage

,

createImage

,

createVolatileImage

,

createVolatileImage

,

disableEvents

,

dispatchEvent

,

enable

,

enableEvents

,

enableInputMethods

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

getBackground

,

getBounds

,

getColorModel

,

getComponentListeners

,

getComponentOrientation

,

getCursor

,

getDropTarget

,

getFocusCycleRootAncestor

,

getFocusListeners

,

getFocusTraversalKeysEnabled

,

getFont

,

getForeground

,

getGraphicsConfiguration

,

getHierarchyBoundsListeners

,

getHierarchyListeners

,

getIgnoreRepaint

,

getInputContext

,

getInputMethodListeners

,

getInputMethodRequests

,

getKeyListeners

,

getLocale

,

getLocation

,

getLocationOnScreen

,

getMouseListeners

,

getMouseMotionListeners

,

getMousePosition

,

getMouseWheelListeners

,

getName

,

getParent

,

getPropertyChangeListeners

,

getPropertyChangeListeners

,

getSize

,

getToolkit

,

getTreeLock

,

gotFocus

,

handleEvent

,

hasFocus

,

hide

,

inside

,

isBackgroundSet

,

isCursorSet

,

isDisplayable

,

isEnabled

,

isFocusable

,

isFocusOwner

,

isFocusTraversable

,

isFontSet

,

isForegroundSet

,

isLightweight

,

isMaximumSizeSet

,

isMinimumSizeSet

,

isPreferredSizeSet

,

isShowing

,

isValid

,

isVisible

,

keyDown

,

keyUp

,

list

,

list

,

list

,

location

,

lostFocus

,

mouseDown

,

mouseDrag

,

mouseEnter

,

mouseExit

,

mouseMove

,

mouseUp

,

move

,

nextFocus

,

paintAll

,

postEvent

,

prepareImage

,

prepareImage

,

processComponentEvent

,

processFocusEvent

,

processHierarchyBoundsEvent

,

processHierarchyEvent

,

processInputMethodEvent

,

processMouseWheelEvent

,

remove

,

removeComponentListener

,

removeFocusListener

,

removeHierarchyBoundsListener

,

removeHierarchyListener

,

removeInputMethodListener

,

removeKeyListener

,

removeMouseListener

,

removeMouseMotionListener

,

removeMouseWheelListener

,

removePropertyChangeListener

,

removePropertyChangeListener

,

repaint

,

repaint

,

repaint

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

resize

,

resize

,

setBounds

,

setBounds

,

setComponentOrientation

,

setCursor

,

setDropTarget

,

setFocusable

,

setFocusTraversalKeysEnabled

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMixingCutoutShape

,

setName

,

setSize

,

setSize

,

show

,

show

,

size

,

toString

,

transferFocus

,

transferFocusBackward

,

transferFocusUpCycle

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

Verify that key is a legal value for the horizontalAlignment properties.

Verify that key is a legal value for the
verticalAlignment or verticalTextPosition properties.

Get the AccessibleContext of this object

Returns the icon used by the label when it's disabled.

Return the keycode that indicates a mnemonic key.

Returns the character, as an index, that the look and feel should
provide decoration for as representing the mnemonic character.

Returns the alignment of the label's contents along the X axis.

Returns the horizontal position of the label's text,
relative to its image.

Returns the graphic image (glyph, icon) that the label displays.

Returns the amount of space between the text and the icon
displayed in this label.

Get the component this is labelling.

Returns the text string that the label displays.

Returns the L&F object that renders this component.

Returns a string that specifies the name of the l&f class
that renders this component.

Returns the alignment of the label's contents along the Y axis.

Returns the vertical position of the label's text,
relative to its image.

This is overridden to return false if the current Icon's Image is
not equal to the passed in Image

img

.

Returns a string representation of this JLabel.

Set the icon to be displayed if this JLabel is "disabled"
(JLabel.setEnabled(false)).

Specifies the displayedMnemonic as a char value.

Specify a keycode that indicates a mnemonic key.

Provides a hint to the look and feel as to which character in the
text should be decorated to represent the mnemonic.

Sets the alignment of the label's contents along the X axis.

Sets the horizontal position of the label's text,
relative to its image.

Defines the icon this component will display.

If both the icon and text properties are set, this property
defines the space between them.

Set the component this is labelling.

Defines the single line of text this component will display.

Sets the L&F object that renders this component.

Sets the alignment of the label's contents along the Y axis.

Sets the vertical position of the label's text,
relative to its image.

Resets the UI property to a value from the current look and feel.

Methods declared in class javax.swing.

JComponent

addAncestorListener

,

addNotify

,

addVetoableChangeListener

,

computeVisibleRect

,

contains

,

createToolTip

,

disable

,

enable

,

firePropertyChange

,

firePropertyChange

,

fireVetoableChange

,

getActionForKeyStroke

,

getActionMap

,

getAlignmentX

,

getAlignmentY

,

getAncestorListeners

,

getAutoscrolls

,

getBaseline

,

getBaselineResizeBehavior

,

getBorder

,

getBounds

,

getClientProperty

,

getComponentGraphics

,

getComponentPopupMenu

,

getConditionForKeyStroke

,

getDebugGraphicsOptions

,

getDefaultLocale

,

getFontMetrics

,

getGraphics

,

getHeight

,

getInheritsPopupMenu

,

getInputMap

,

getInputMap

,

getInputVerifier

,

getInsets

,

getInsets

,

getListeners

,

getLocation

,

getMaximumSize

,

getMinimumSize

,

getNextFocusableComponent

,

getPopupLocation

,

getPreferredSize

,

getRegisteredKeyStrokes

,

getRootPane

,

getSize

,

getToolTipLocation

,

getToolTipText

,

getToolTipText

,

getTopLevelAncestor

,

getTransferHandler

,

getVerifyInputWhenFocusTarget

,

getVetoableChangeListeners

,

getVisibleRect

,

getWidth

,

getX

,

getY

,

grabFocus

,

isDoubleBuffered

,

isLightweightComponent

,

isManagingFocus

,

isOpaque

,

isOptimizedDrawingEnabled

,

isPaintingForPrint

,

isPaintingOrigin

,

isPaintingTile

,

isRequestFocusEnabled

,

isValidateRoot

,

paint

,

paintBorder

,

paintChildren

,

paintComponent

,

paintImmediately

,

paintImmediately

,

print

,

printAll

,

printBorder

,

printChildren

,

printComponent

,

processComponentKeyEvent

,

processKeyBinding

,

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

,

putClientProperty

,

registerKeyboardAction

,

registerKeyboardAction

,

removeAncestorListener

,

removeNotify

,

removeVetoableChangeListener

,

repaint

,

repaint

,

requestDefaultFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

resetKeyboardActions

,

reshape

,

revalidate

,

scrollRectToVisible

,

setActionMap

,

setAlignmentX

,

setAlignmentY

,

setAutoscrolls

,

setBackground

,

setBorder

,

setComponentPopupMenu

,

setDebugGraphicsOptions

,

setDefaultLocale

,

setDoubleBuffered

,

setEnabled

,

setFocusTraversalKeys

,

setFont

,

setForeground

,

setInheritsPopupMenu

,

setInputMap

,

setInputVerifier

,

setMaximumSize

,

setMinimumSize

,

setNextFocusableComponent

,

setOpaque

,

setPreferredSize

,

setRequestFocusEnabled

,

setToolTipText

,

setTransferHandler

,

setUI

,

setVerifyInputWhenFocusTarget

,

setVisible

,

unregisterKeyboardAction

,

update

---

#### Methods declared in class javax.swing. JComponent

Methods declared in class java.awt.

Container

add

,

add

,

add

,

add

,

add

,

addContainerListener

,

addImpl

,

addPropertyChangeListener

,

addPropertyChangeListener

,

applyComponentOrientation

,

areFocusTraversalKeysSet

,

countComponents

,

deliverEvent

,

doLayout

,

findComponentAt

,

findComponentAt

,

getComponent

,

getComponentAt

,

getComponentAt

,

getComponentCount

,

getComponents

,

getComponentZOrder

,

getContainerListeners

,

getFocusTraversalKeys

,

getFocusTraversalPolicy

,

getLayout

,

getMousePosition

,

insets

,

invalidate

,

isAncestorOf

,

isFocusCycleRoot

,

isFocusCycleRoot

,

isFocusTraversalPolicyProvider

,

isFocusTraversalPolicySet

,

layout

,

list

,

list

,

locate

,

minimumSize

,

paintComponents

,

preferredSize

,

printComponents

,

processContainerEvent

,

processEvent

,

remove

,

remove

,

removeAll

,

removeContainerListener

,

setComponentZOrder

,

setFocusCycleRoot

,

setFocusTraversalPolicy

,

setFocusTraversalPolicyProvider

,

setLayout

,

transferFocusDownCycle

,

validate

,

validateTree

---

#### Methods declared in class java.awt. Container

Methods declared in class java.awt.

Component

action

,

add

,

addComponentListener

,

addFocusListener

,

addHierarchyBoundsListener

,

addHierarchyListener

,

addInputMethodListener

,

addKeyListener

,

addMouseListener

,

addMouseMotionListener

,

addMouseWheelListener

,

bounds

,

checkImage

,

checkImage

,

coalesceEvents

,

contains

,

createImage

,

createImage

,

createVolatileImage

,

createVolatileImage

,

disableEvents

,

dispatchEvent

,

enable

,

enableEvents

,

enableInputMethods

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

getBackground

,

getBounds

,

getColorModel

,

getComponentListeners

,

getComponentOrientation

,

getCursor

,

getDropTarget

,

getFocusCycleRootAncestor

,

getFocusListeners

,

getFocusTraversalKeysEnabled

,

getFont

,

getForeground

,

getGraphicsConfiguration

,

getHierarchyBoundsListeners

,

getHierarchyListeners

,

getIgnoreRepaint

,

getInputContext

,

getInputMethodListeners

,

getInputMethodRequests

,

getKeyListeners

,

getLocale

,

getLocation

,

getLocationOnScreen

,

getMouseListeners

,

getMouseMotionListeners

,

getMousePosition

,

getMouseWheelListeners

,

getName

,

getParent

,

getPropertyChangeListeners

,

getPropertyChangeListeners

,

getSize

,

getToolkit

,

getTreeLock

,

gotFocus

,

handleEvent

,

hasFocus

,

hide

,

inside

,

isBackgroundSet

,

isCursorSet

,

isDisplayable

,

isEnabled

,

isFocusable

,

isFocusOwner

,

isFocusTraversable

,

isFontSet

,

isForegroundSet

,

isLightweight

,

isMaximumSizeSet

,

isMinimumSizeSet

,

isPreferredSizeSet

,

isShowing

,

isValid

,

isVisible

,

keyDown

,

keyUp

,

list

,

list

,

list

,

location

,

lostFocus

,

mouseDown

,

mouseDrag

,

mouseEnter

,

mouseExit

,

mouseMove

,

mouseUp

,

move

,

nextFocus

,

paintAll

,

postEvent

,

prepareImage

,

prepareImage

,

processComponentEvent

,

processFocusEvent

,

processHierarchyBoundsEvent

,

processHierarchyEvent

,

processInputMethodEvent

,

processMouseWheelEvent

,

remove

,

removeComponentListener

,

removeFocusListener

,

removeHierarchyBoundsListener

,

removeHierarchyListener

,

removeInputMethodListener

,

removeKeyListener

,

removeMouseListener

,

removeMouseMotionListener

,

removeMouseWheelListener

,

removePropertyChangeListener

,

removePropertyChangeListener

,

repaint

,

repaint

,

repaint

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

resize

,

resize

,

setBounds

,

setBounds

,

setComponentOrientation

,

setCursor

,

setDropTarget

,

setFocusable

,

setFocusTraversalKeysEnabled

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMixingCutoutShape

,

setName

,

setSize

,

setSize

,

show

,

show

,

size

,

toString

,

transferFocus

,

transferFocusBackward

,

transferFocusUpCycle

---

#### Methods declared in class java.awt. Component

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

- labelFor

```java
protected
Component
labelFor
```

The Component this label is for; null if the label
is not the label for a component

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- JLabel

```java
public JLabel​(
String
text,

Icon
icon,
int horizontalAlignment)
```

Creates a

JLabel

instance with the specified
text, image, and horizontal alignment.
The label is centered vertically in its display area.
The text is on the trailing edge of the image.

**Parameters:** text

- The text to be displayed by the label.
**Parameters:** icon

- The image to be displayed by the label.
**Parameters:** horizontalAlignment

- One of the following constants
defined in

SwingConstants

:

LEFT

,

CENTER

,

RIGHT

,

LEADING

or

TRAILING

.

- JLabel

```java
public JLabel​(
String
text,
int horizontalAlignment)
```

Creates a

JLabel

instance with the specified
text and horizontal alignment.
The label is centered vertically in its display area.

**Parameters:** text

- The text to be displayed by the label.
**Parameters:** horizontalAlignment

- One of the following constants
defined in

SwingConstants

:

LEFT

,

CENTER

,

RIGHT

,

LEADING

or

TRAILING

.

- JLabel

```java
public JLabel​(
String
text)
```

Creates a

JLabel

instance with the specified text.
The label is aligned against the leading edge of its display area,
and centered vertically.

**Parameters:** text

- The text to be displayed by the label.

- JLabel

```java
public JLabel​(
Icon
image,
int horizontalAlignment)
```

Creates a

JLabel

instance with the specified
image and horizontal alignment.
The label is centered vertically in its display area.

**Parameters:** image

- The image to be displayed by the label.
**Parameters:** horizontalAlignment

- One of the following constants
defined in

SwingConstants

:

LEFT

,

CENTER

,

RIGHT

,

LEADING

or

TRAILING

.

- JLabel

```java
public JLabel​(
Icon
image)
```

Creates a

JLabel

instance with the specified image.
The label is centered vertically and horizontally
in its display area.

**Parameters:** image

- The image to be displayed by the label.

- JLabel

```java
public JLabel()
```

Creates a

JLabel

instance with
no image and with an empty string for the title.
The label is centered vertically
in its display area.
The label's contents, once set, will be displayed on the leading edge
of the label's display area.

============ METHOD DETAIL ==========

- Method Detail

- getUI

```java
public
LabelUI
getUI()
```

Returns the L&F object that renders this component.

**Overrides:** getUI

in class

JComponent
**Returns:** LabelUI object

- setUI

```java
@BeanProperty
(
hidden
=true,

visualUpdate
=true,

description
="The UI object that implements the Component\'s LookAndFeel.")
public void setUI​(
LabelUI
ui)
```

Sets the L&F object that renders this component.

**Parameters:** ui

- the LabelUI L&F object
**See Also:** UIDefaults.getUI(javax.swing.JComponent)

- updateUI

```java
public void updateUI()
```

Resets the UI property to a value from the current look and feel.

**Overrides:** updateUI

in class

JComponent
**See Also:** JComponent.updateUI()

- getUIClassID

```java
@BeanProperty
(
bound
=false)
public
String
getUIClassID()
```

Returns a string that specifies the name of the l&f class
that renders this component.

**Overrides:** getUIClassID

in class

JComponent
**Returns:** String "LabelUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

- getText

```java
public
String
getText()
```

Returns the text string that the label displays.

**Returns:** a String
**See Also:** setText(java.lang.String)

- setText

```java
@BeanProperty
(
preferred
=true,

visualUpdate
=true,

description
="Defines the single line of text this component will display.")
public void setText​(
String
text)
```

Defines the single line of text this component will display. If
the value of text is null or empty string, nothing is displayed.

The default value of this property is null.

This is a JavaBeans bound property.

**Parameters:** text

- the single line of text this component will display
**See Also:** setVerticalTextPosition(int)

,

setHorizontalTextPosition(int)

,

setIcon(javax.swing.Icon)

- getIcon

```java
public
Icon
getIcon()
```

Returns the graphic image (glyph, icon) that the label displays.

**Returns:** an Icon
**See Also:** setIcon(javax.swing.Icon)

- setIcon

```java
@BeanProperty
(
preferred
=true,

visualUpdate
=true,

description
="The icon this component will display.")
public void setIcon​(
Icon
icon)
```

Defines the icon this component will display. If
the value of icon is null, nothing is displayed.

The default value of this property is null.

This is a JavaBeans bound property.

**Parameters:** icon

- the default icon this component will display
**See Also:** setVerticalTextPosition(int)

,

setHorizontalTextPosition(int)

,

getIcon()

- getDisabledIcon

```java
public
Icon
getDisabledIcon()
```

Returns the icon used by the label when it's disabled.
If no disabled icon has been set this will forward the call to
the look and feel to construct an appropriate disabled Icon.

Some look and feels might not render the disabled Icon, in which
case they will ignore this.

**Returns:** the

disabledIcon

property
**See Also:** setDisabledIcon(javax.swing.Icon)

,

LookAndFeel.getDisabledIcon(javax.swing.JComponent, javax.swing.Icon)

,

ImageIcon

- setDisabledIcon

```java
@BeanProperty
(
visualUpdate
=true,

description
="The icon to display if the label is disabled.")
public void setDisabledIcon​(
Icon
disabledIcon)
```

Set the icon to be displayed if this JLabel is "disabled"
(JLabel.setEnabled(false)).

The default value of this property is null.

**Parameters:** disabledIcon

- the Icon to display when the component is disabled
**See Also:** getDisabledIcon()

,

JComponent.setEnabled(boolean)

- setDisplayedMnemonic

```java
@BeanProperty
(
visualUpdate
=true,

description
="The mnemonic keycode.")
public void setDisplayedMnemonic​(int key)
```

Specify a keycode that indicates a mnemonic key.
This property is used when the label is part of a larger component.
If the labelFor property of the label is not null, the label will
call the requestFocus method of the component specified by the
labelFor property when the mnemonic is activated.

**Parameters:** key

- a keycode that indicates a mnemonic key
**See Also:** getLabelFor()

,

setLabelFor(java.awt.Component)

- setDisplayedMnemonic

```java
public void setDisplayedMnemonic​(char aChar)
```

Specifies the displayedMnemonic as a char value.

**Parameters:** aChar

- a char specifying the mnemonic to display
**See Also:** setDisplayedMnemonic(int)

- getDisplayedMnemonic

```java
public int getDisplayedMnemonic()
```

Return the keycode that indicates a mnemonic key.
This property is used when the label is part of a larger component.
If the labelFor property of the label is not null, the label will
call the requestFocus method of the component specified by the
labelFor property when the mnemonic is activated.

**Returns:** int value for the mnemonic key
**See Also:** getLabelFor()

,

setLabelFor(java.awt.Component)

- setDisplayedMnemonicIndex

```java
@BeanProperty
(
visualUpdate
=true,

description
="the index into the String to draw the keyboard character mnemonic at")
public void setDisplayedMnemonicIndex​(int index)
throws
IllegalArgumentException
```

Provides a hint to the look and feel as to which character in the
text should be decorated to represent the mnemonic. Not all look and
feels may support this. A value of -1 indicates either there is no
mnemonic, the mnemonic character is not contained in the string, or
the developer does not wish the mnemonic to be displayed.

The value of this is updated as the properties relating to the
mnemonic change (such as the mnemonic itself, the text...).
You should only ever have to call this if
you do not wish the default character to be underlined. For example, if
the text was 'Save As', with a mnemonic of 'a', and you wanted the 'A'
to be decorated, as 'Save

A

s', you would have to invoke

setDisplayedMnemonicIndex(5)

after invoking

setDisplayedMnemonic(KeyEvent.VK_A)

.

**Parameters:** index

- Index into the String to underline
**Throws:** IllegalArgumentException

- will be thrown if

index

is >= length of the text, or < -1
**Since:** 1.4

- getDisplayedMnemonicIndex

```java
public int getDisplayedMnemonicIndex()
```

Returns the character, as an index, that the look and feel should
provide decoration for as representing the mnemonic character.

**Returns:** index representing mnemonic character
**Since:** 1.4
**See Also:** setDisplayedMnemonicIndex(int)

- checkHorizontalKey

```java
protected int checkHorizontalKey​(int key,

String
message)
```

Verify that key is a legal value for the horizontalAlignment properties.

**Parameters:** key

- the property value to check
**Parameters:** message

- the IllegalArgumentException detail message
**Returns:** the key value if

key

is a a legal value for the
horizontalAlignment properties
**Throws:** IllegalArgumentException

- if key isn't LEFT, CENTER, RIGHT,
LEADING or TRAILING.
**See Also:** setHorizontalTextPosition(int)

,

setHorizontalAlignment(int)

- checkVerticalKey

```java
protected int checkVerticalKey​(int key,

String
message)
```

Verify that key is a legal value for the
verticalAlignment or verticalTextPosition properties.

**Parameters:** key

- the property value to check
**Parameters:** message

- the IllegalArgumentException detail message
**Returns:** the key value if

key

is a legal value for the
verticalAlignment or verticalTextPosition properties
**Throws:** IllegalArgumentException

- if key isn't TOP, CENTER, or BOTTOM.
**See Also:** setVerticalAlignment(int)

,

setVerticalTextPosition(int)

- getIconTextGap

```java
public int getIconTextGap()
```

Returns the amount of space between the text and the icon
displayed in this label.

**Returns:** an int equal to the number of pixels between the text
and the icon.
**See Also:** setIconTextGap(int)

- setIconTextGap

```java
@BeanProperty
(
visualUpdate
=true,

description
="If both the icon and text properties are set, this property defines the space between them.")
public void setIconTextGap​(int iconTextGap)
```

If both the icon and text properties are set, this property
defines the space between them.

The default value of this property is 4 pixels.

This is a JavaBeans bound property.

**Parameters:** iconTextGap

- the space between the icon and text properties
**See Also:** getIconTextGap()

- getVerticalAlignment

```java
public int getVerticalAlignment()
```

Returns the alignment of the label's contents along the Y axis.

**Returns:** The value of the verticalAlignment property, one of the
following constants defined in

SwingConstants

:

TOP

,

CENTER

, or

BOTTOM

.
**See Also:** SwingConstants

,

setVerticalAlignment(int)

- setVerticalAlignment

```java
@BeanProperty
(
visualUpdate
=true,

enumerationValues
={"SwingConstants.TOP","SwingConstants.CENTER","SwingConstants.BOTTOM"},

description
="The alignment of the label\'s contents along the Y axis.")
public void setVerticalAlignment​(int alignment)
```

Sets the alignment of the label's contents along the Y axis.

The default value of this property is CENTER.

**Parameters:** alignment

- One of the following constants
defined in

SwingConstants

:

TOP

,

CENTER

(the default), or

BOTTOM

.
**See Also:** SwingConstants

,

getVerticalAlignment()

- getHorizontalAlignment

```java
public int getHorizontalAlignment()
```

Returns the alignment of the label's contents along the X axis.

**Returns:** The value of the horizontalAlignment property, one of the
following constants defined in

SwingConstants

:

LEFT

,

CENTER

,

RIGHT

,

LEADING

or

TRAILING

.
**See Also:** setHorizontalAlignment(int)

,

SwingConstants

- setHorizontalAlignment

```java
@BeanProperty
(
visualUpdate
=true,

enumerationValues
={"SwingConstants.LEFT","SwingConstants.CENTER","SwingConstants.RIGHT","SwingConstants.LEADING","SwingConstants.TRAILING"},

description
="The alignment of the label\'s content along the X axis.")
public void setHorizontalAlignment​(int alignment)
```

Sets the alignment of the label's contents along the X axis.

This is a JavaBeans bound property.

**Parameters:** alignment

- One of the following constants
defined in

SwingConstants

:

LEFT

,

CENTER

(the default for image-only labels),

RIGHT

,

LEADING

(the default for text-only labels) or

TRAILING

.
**See Also:** SwingConstants

,

getHorizontalAlignment()

- getVerticalTextPosition

```java
public int getVerticalTextPosition()
```

Returns the vertical position of the label's text,
relative to its image.

**Returns:** One of the following constants
defined in

SwingConstants

:

TOP

,

CENTER

, or

BOTTOM

.
**See Also:** setVerticalTextPosition(int)

,

SwingConstants

- setVerticalTextPosition

```java
@BeanProperty
(
expert
=true,

visualUpdate
=true,

enumerationValues
={"SwingConstants.TOP","SwingConstants.CENTER","SwingConstants.BOTTOM"},

description
="The vertical position of the text relative to it\'s image.")
public void setVerticalTextPosition​(int textPosition)
```

Sets the vertical position of the label's text,
relative to its image.

The default value of this property is CENTER.

This is a JavaBeans bound property.

**Parameters:** textPosition

- One of the following constants
defined in

SwingConstants

:

TOP

,

CENTER

(the default), or

BOTTOM

.
**See Also:** SwingConstants

,

getVerticalTextPosition()

- getHorizontalTextPosition

```java
public int getHorizontalTextPosition()
```

Returns the horizontal position of the label's text,
relative to its image.

**Returns:** One of the following constants
defined in

SwingConstants

:

LEFT

,

CENTER

,

RIGHT

,

LEADING

or

TRAILING

.
**See Also:** SwingConstants

- setHorizontalTextPosition

```java
@BeanProperty
(
expert
=true,

visualUpdate
=true,

enumerationValues
={"SwingConstants.LEFT","SwingConstants.CENTER","SwingConstants.RIGHT","SwingConstants.LEADING","SwingConstants.TRAILING"},

description
="The horizontal position of the label\'s text, relative to its image.")
public void setHorizontalTextPosition​(int textPosition)
```

Sets the horizontal position of the label's text,
relative to its image.

**Parameters:** textPosition

- One of the following constants
defined in

SwingConstants

:

LEFT

,

CENTER

,

RIGHT

,

LEADING

, or

TRAILING

(the default).
**See Also:** SwingConstants

- imageUpdate

```java
public boolean imageUpdate​(
Image
img,
int infoflags,
int x,
int y,
int w,
int h)
```

This is overridden to return false if the current Icon's Image is
not equal to the passed in Image

img

.

**Specified by:** imageUpdate

in interface

ImageObserver
**Overrides:** imageUpdate

in class

Component
**Parameters:** img

- the image being observed
**Parameters:** infoflags

- see

imageUpdate

for more information
**Parameters:** x

- the

x

coordinate
**Parameters:** y

- the

y

coordinate
**Parameters:** w

- the width
**Parameters:** h

- the height
**Returns:** false

if the infoflags indicate that the
image is completely loaded;

true

otherwise.
**See Also:** ImageObserver

,

Component.imageUpdate(java.awt.Image, int, int, int, int, int)

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this JLabel. This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

JComponent
**Returns:** a string representation of this JLabel.

- getLabelFor

```java
public
Component
getLabelFor()
```

Get the component this is labelling.

**Returns:** the Component this is labelling. Can be null if this
does not label a Component. If the displayedMnemonic
property is set and the labelFor property is also set, the label
will call the requestFocus method of the component specified by the
labelFor property when the mnemonic is activated.
**See Also:** getDisplayedMnemonic()

,

setDisplayedMnemonic(int)

- setLabelFor

```java
@BeanProperty
(
description
="The component this is labelling.")
public void setLabelFor​(
Component
c)
```

Set the component this is labelling. Can be null if this does not
label a Component. If the displayedMnemonic property is set
and the labelFor property is also set, the label will
call the requestFocus method of the component specified by the
labelFor property when the mnemonic is activated.

**Parameters:** c

- the Component this label is for, or null if the label is
not the label for a component
**See Also:** getDisplayedMnemonic()

,

setDisplayedMnemonic(int)

- getAccessibleContext

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="The AccessibleContext associated with this Label.")
public
AccessibleContext
getAccessibleContext()
```

Get the AccessibleContext of this object

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** the AccessibleContext of this object

Field Detail

- labelFor

```java
protected
Component
labelFor
```

The Component this label is for; null if the label
is not the label for a component

---

#### Field Detail

labelFor

```java
protected
Component
labelFor
```

The Component this label is for; null if the label
is not the label for a component

---

#### labelFor

protected

Component

labelFor

The Component this label is for; null if the label
is not the label for a component

Constructor Detail

- JLabel

```java
public JLabel​(
String
text,

Icon
icon,
int horizontalAlignment)
```

Creates a

JLabel

instance with the specified
text, image, and horizontal alignment.
The label is centered vertically in its display area.
The text is on the trailing edge of the image.

**Parameters:** text

- The text to be displayed by the label.
**Parameters:** icon

- The image to be displayed by the label.
**Parameters:** horizontalAlignment

- One of the following constants
defined in

SwingConstants

:

LEFT

,

CENTER

,

RIGHT

,

LEADING

or

TRAILING

.

- JLabel

```java
public JLabel​(
String
text,
int horizontalAlignment)
```

Creates a

JLabel

instance with the specified
text and horizontal alignment.
The label is centered vertically in its display area.

**Parameters:** text

- The text to be displayed by the label.
**Parameters:** horizontalAlignment

- One of the following constants
defined in

SwingConstants

:

LEFT

,

CENTER

,

RIGHT

,

LEADING

or

TRAILING

.

- JLabel

```java
public JLabel​(
String
text)
```

Creates a

JLabel

instance with the specified text.
The label is aligned against the leading edge of its display area,
and centered vertically.

**Parameters:** text

- The text to be displayed by the label.

- JLabel

```java
public JLabel​(
Icon
image,
int horizontalAlignment)
```

Creates a

JLabel

instance with the specified
image and horizontal alignment.
The label is centered vertically in its display area.

**Parameters:** image

- The image to be displayed by the label.
**Parameters:** horizontalAlignment

- One of the following constants
defined in

SwingConstants

:

LEFT

,

CENTER

,

RIGHT

,

LEADING

or

TRAILING

.

- JLabel

```java
public JLabel​(
Icon
image)
```

Creates a

JLabel

instance with the specified image.
The label is centered vertically and horizontally
in its display area.

**Parameters:** image

- The image to be displayed by the label.

- JLabel

```java
public JLabel()
```

Creates a

JLabel

instance with
no image and with an empty string for the title.
The label is centered vertically
in its display area.
The label's contents, once set, will be displayed on the leading edge
of the label's display area.

---

#### Constructor Detail

JLabel

```java
public JLabel​(
String
text,

Icon
icon,
int horizontalAlignment)
```

Creates a

JLabel

instance with the specified
text, image, and horizontal alignment.
The label is centered vertically in its display area.
The text is on the trailing edge of the image.

**Parameters:** text

- The text to be displayed by the label.
**Parameters:** icon

- The image to be displayed by the label.
**Parameters:** horizontalAlignment

- One of the following constants
defined in

SwingConstants

:

LEFT

,

CENTER

,

RIGHT

,

LEADING

or

TRAILING

.

---

#### JLabel

public JLabel​(

String

text,

Icon

icon,
int horizontalAlignment)

Creates a

JLabel

instance with the specified
text, image, and horizontal alignment.
The label is centered vertically in its display area.
The text is on the trailing edge of the image.

JLabel

```java
public JLabel​(
String
text,
int horizontalAlignment)
```

Creates a

JLabel

instance with the specified
text and horizontal alignment.
The label is centered vertically in its display area.

**Parameters:** text

- The text to be displayed by the label.
**Parameters:** horizontalAlignment

- One of the following constants
defined in

SwingConstants

:

LEFT

,

CENTER

,

RIGHT

,

LEADING

or

TRAILING

.

---

#### JLabel

public JLabel​(

String

text,
int horizontalAlignment)

Creates a

JLabel

instance with the specified
text and horizontal alignment.
The label is centered vertically in its display area.

JLabel

```java
public JLabel​(
String
text)
```

Creates a

JLabel

instance with the specified text.
The label is aligned against the leading edge of its display area,
and centered vertically.

**Parameters:** text

- The text to be displayed by the label.

---

#### JLabel

public JLabel​(

String

text)

Creates a

JLabel

instance with the specified text.
The label is aligned against the leading edge of its display area,
and centered vertically.

JLabel

```java
public JLabel​(
Icon
image,
int horizontalAlignment)
```

Creates a

JLabel

instance with the specified
image and horizontal alignment.
The label is centered vertically in its display area.

**Parameters:** image

- The image to be displayed by the label.
**Parameters:** horizontalAlignment

- One of the following constants
defined in

SwingConstants

:

LEFT

,

CENTER

,

RIGHT

,

LEADING

or

TRAILING

.

---

#### JLabel

public JLabel​(

Icon

image,
int horizontalAlignment)

Creates a

JLabel

instance with the specified
image and horizontal alignment.
The label is centered vertically in its display area.

JLabel

```java
public JLabel​(
Icon
image)
```

Creates a

JLabel

instance with the specified image.
The label is centered vertically and horizontally
in its display area.

**Parameters:** image

- The image to be displayed by the label.

---

#### JLabel

public JLabel​(

Icon

image)

Creates a

JLabel

instance with the specified image.
The label is centered vertically and horizontally
in its display area.

JLabel

```java
public JLabel()
```

Creates a

JLabel

instance with
no image and with an empty string for the title.
The label is centered vertically
in its display area.
The label's contents, once set, will be displayed on the leading edge
of the label's display area.

---

#### JLabel

public JLabel()

Creates a

JLabel

instance with
no image and with an empty string for the title.
The label is centered vertically
in its display area.
The label's contents, once set, will be displayed on the leading edge
of the label's display area.

Method Detail

- getUI

```java
public
LabelUI
getUI()
```

Returns the L&F object that renders this component.

**Overrides:** getUI

in class

JComponent
**Returns:** LabelUI object

- setUI

```java
@BeanProperty
(
hidden
=true,

visualUpdate
=true,

description
="The UI object that implements the Component\'s LookAndFeel.")
public void setUI​(
LabelUI
ui)
```

Sets the L&F object that renders this component.

**Parameters:** ui

- the LabelUI L&F object
**See Also:** UIDefaults.getUI(javax.swing.JComponent)

- updateUI

```java
public void updateUI()
```

Resets the UI property to a value from the current look and feel.

**Overrides:** updateUI

in class

JComponent
**See Also:** JComponent.updateUI()

- getUIClassID

```java
@BeanProperty
(
bound
=false)
public
String
getUIClassID()
```

Returns a string that specifies the name of the l&f class
that renders this component.

**Overrides:** getUIClassID

in class

JComponent
**Returns:** String "LabelUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

- getText

```java
public
String
getText()
```

Returns the text string that the label displays.

**Returns:** a String
**See Also:** setText(java.lang.String)

- setText

```java
@BeanProperty
(
preferred
=true,

visualUpdate
=true,

description
="Defines the single line of text this component will display.")
public void setText​(
String
text)
```

Defines the single line of text this component will display. If
the value of text is null or empty string, nothing is displayed.

The default value of this property is null.

This is a JavaBeans bound property.

**Parameters:** text

- the single line of text this component will display
**See Also:** setVerticalTextPosition(int)

,

setHorizontalTextPosition(int)

,

setIcon(javax.swing.Icon)

- getIcon

```java
public
Icon
getIcon()
```

Returns the graphic image (glyph, icon) that the label displays.

**Returns:** an Icon
**See Also:** setIcon(javax.swing.Icon)

- setIcon

```java
@BeanProperty
(
preferred
=true,

visualUpdate
=true,

description
="The icon this component will display.")
public void setIcon​(
Icon
icon)
```

Defines the icon this component will display. If
the value of icon is null, nothing is displayed.

The default value of this property is null.

This is a JavaBeans bound property.

**Parameters:** icon

- the default icon this component will display
**See Also:** setVerticalTextPosition(int)

,

setHorizontalTextPosition(int)

,

getIcon()

- getDisabledIcon

```java
public
Icon
getDisabledIcon()
```

Returns the icon used by the label when it's disabled.
If no disabled icon has been set this will forward the call to
the look and feel to construct an appropriate disabled Icon.

Some look and feels might not render the disabled Icon, in which
case they will ignore this.

**Returns:** the

disabledIcon

property
**See Also:** setDisabledIcon(javax.swing.Icon)

,

LookAndFeel.getDisabledIcon(javax.swing.JComponent, javax.swing.Icon)

,

ImageIcon

- setDisabledIcon

```java
@BeanProperty
(
visualUpdate
=true,

description
="The icon to display if the label is disabled.")
public void setDisabledIcon​(
Icon
disabledIcon)
```

Set the icon to be displayed if this JLabel is "disabled"
(JLabel.setEnabled(false)).

The default value of this property is null.

**Parameters:** disabledIcon

- the Icon to display when the component is disabled
**See Also:** getDisabledIcon()

,

JComponent.setEnabled(boolean)

- setDisplayedMnemonic

```java
@BeanProperty
(
visualUpdate
=true,

description
="The mnemonic keycode.")
public void setDisplayedMnemonic​(int key)
```

Specify a keycode that indicates a mnemonic key.
This property is used when the label is part of a larger component.
If the labelFor property of the label is not null, the label will
call the requestFocus method of the component specified by the
labelFor property when the mnemonic is activated.

**Parameters:** key

- a keycode that indicates a mnemonic key
**See Also:** getLabelFor()

,

setLabelFor(java.awt.Component)

- setDisplayedMnemonic

```java
public void setDisplayedMnemonic​(char aChar)
```

Specifies the displayedMnemonic as a char value.

**Parameters:** aChar

- a char specifying the mnemonic to display
**See Also:** setDisplayedMnemonic(int)

- getDisplayedMnemonic

```java
public int getDisplayedMnemonic()
```

Return the keycode that indicates a mnemonic key.
This property is used when the label is part of a larger component.
If the labelFor property of the label is not null, the label will
call the requestFocus method of the component specified by the
labelFor property when the mnemonic is activated.

**Returns:** int value for the mnemonic key
**See Also:** getLabelFor()

,

setLabelFor(java.awt.Component)

- setDisplayedMnemonicIndex

```java
@BeanProperty
(
visualUpdate
=true,

description
="the index into the String to draw the keyboard character mnemonic at")
public void setDisplayedMnemonicIndex​(int index)
throws
IllegalArgumentException
```

Provides a hint to the look and feel as to which character in the
text should be decorated to represent the mnemonic. Not all look and
feels may support this. A value of -1 indicates either there is no
mnemonic, the mnemonic character is not contained in the string, or
the developer does not wish the mnemonic to be displayed.

The value of this is updated as the properties relating to the
mnemonic change (such as the mnemonic itself, the text...).
You should only ever have to call this if
you do not wish the default character to be underlined. For example, if
the text was 'Save As', with a mnemonic of 'a', and you wanted the 'A'
to be decorated, as 'Save

A

s', you would have to invoke

setDisplayedMnemonicIndex(5)

after invoking

setDisplayedMnemonic(KeyEvent.VK_A)

.

**Parameters:** index

- Index into the String to underline
**Throws:** IllegalArgumentException

- will be thrown if

index

is >= length of the text, or < -1
**Since:** 1.4

- getDisplayedMnemonicIndex

```java
public int getDisplayedMnemonicIndex()
```

Returns the character, as an index, that the look and feel should
provide decoration for as representing the mnemonic character.

**Returns:** index representing mnemonic character
**Since:** 1.4
**See Also:** setDisplayedMnemonicIndex(int)

- checkHorizontalKey

```java
protected int checkHorizontalKey​(int key,

String
message)
```

Verify that key is a legal value for the horizontalAlignment properties.

**Parameters:** key

- the property value to check
**Parameters:** message

- the IllegalArgumentException detail message
**Returns:** the key value if

key

is a a legal value for the
horizontalAlignment properties
**Throws:** IllegalArgumentException

- if key isn't LEFT, CENTER, RIGHT,
LEADING or TRAILING.
**See Also:** setHorizontalTextPosition(int)

,

setHorizontalAlignment(int)

- checkVerticalKey

```java
protected int checkVerticalKey​(int key,

String
message)
```

Verify that key is a legal value for the
verticalAlignment or verticalTextPosition properties.

**Parameters:** key

- the property value to check
**Parameters:** message

- the IllegalArgumentException detail message
**Returns:** the key value if

key

is a legal value for the
verticalAlignment or verticalTextPosition properties
**Throws:** IllegalArgumentException

- if key isn't TOP, CENTER, or BOTTOM.
**See Also:** setVerticalAlignment(int)

,

setVerticalTextPosition(int)

- getIconTextGap

```java
public int getIconTextGap()
```

Returns the amount of space between the text and the icon
displayed in this label.

**Returns:** an int equal to the number of pixels between the text
and the icon.
**See Also:** setIconTextGap(int)

- setIconTextGap

```java
@BeanProperty
(
visualUpdate
=true,

description
="If both the icon and text properties are set, this property defines the space between them.")
public void setIconTextGap​(int iconTextGap)
```

If both the icon and text properties are set, this property
defines the space between them.

The default value of this property is 4 pixels.

This is a JavaBeans bound property.

**Parameters:** iconTextGap

- the space between the icon and text properties
**See Also:** getIconTextGap()

- getVerticalAlignment

```java
public int getVerticalAlignment()
```

Returns the alignment of the label's contents along the Y axis.

**Returns:** The value of the verticalAlignment property, one of the
following constants defined in

SwingConstants

:

TOP

,

CENTER

, or

BOTTOM

.
**See Also:** SwingConstants

,

setVerticalAlignment(int)

- setVerticalAlignment

```java
@BeanProperty
(
visualUpdate
=true,

enumerationValues
={"SwingConstants.TOP","SwingConstants.CENTER","SwingConstants.BOTTOM"},

description
="The alignment of the label\'s contents along the Y axis.")
public void setVerticalAlignment​(int alignment)
```

Sets the alignment of the label's contents along the Y axis.

The default value of this property is CENTER.

**Parameters:** alignment

- One of the following constants
defined in

SwingConstants

:

TOP

,

CENTER

(the default), or

BOTTOM

.
**See Also:** SwingConstants

,

getVerticalAlignment()

- getHorizontalAlignment

```java
public int getHorizontalAlignment()
```

Returns the alignment of the label's contents along the X axis.

**Returns:** The value of the horizontalAlignment property, one of the
following constants defined in

SwingConstants

:

LEFT

,

CENTER

,

RIGHT

,

LEADING

or

TRAILING

.
**See Also:** setHorizontalAlignment(int)

,

SwingConstants

- setHorizontalAlignment

```java
@BeanProperty
(
visualUpdate
=true,

enumerationValues
={"SwingConstants.LEFT","SwingConstants.CENTER","SwingConstants.RIGHT","SwingConstants.LEADING","SwingConstants.TRAILING"},

description
="The alignment of the label\'s content along the X axis.")
public void setHorizontalAlignment​(int alignment)
```

Sets the alignment of the label's contents along the X axis.

This is a JavaBeans bound property.

**Parameters:** alignment

- One of the following constants
defined in

SwingConstants

:

LEFT

,

CENTER

(the default for image-only labels),

RIGHT

,

LEADING

(the default for text-only labels) or

TRAILING

.
**See Also:** SwingConstants

,

getHorizontalAlignment()

- getVerticalTextPosition

```java
public int getVerticalTextPosition()
```

Returns the vertical position of the label's text,
relative to its image.

**Returns:** One of the following constants
defined in

SwingConstants

:

TOP

,

CENTER

, or

BOTTOM

.
**See Also:** setVerticalTextPosition(int)

,

SwingConstants

- setVerticalTextPosition

```java
@BeanProperty
(
expert
=true,

visualUpdate
=true,

enumerationValues
={"SwingConstants.TOP","SwingConstants.CENTER","SwingConstants.BOTTOM"},

description
="The vertical position of the text relative to it\'s image.")
public void setVerticalTextPosition​(int textPosition)
```

Sets the vertical position of the label's text,
relative to its image.

The default value of this property is CENTER.

This is a JavaBeans bound property.

**Parameters:** textPosition

- One of the following constants
defined in

SwingConstants

:

TOP

,

CENTER

(the default), or

BOTTOM

.
**See Also:** SwingConstants

,

getVerticalTextPosition()

- getHorizontalTextPosition

```java
public int getHorizontalTextPosition()
```

Returns the horizontal position of the label's text,
relative to its image.

**Returns:** One of the following constants
defined in

SwingConstants

:

LEFT

,

CENTER

,

RIGHT

,

LEADING

or

TRAILING

.
**See Also:** SwingConstants

- setHorizontalTextPosition

```java
@BeanProperty
(
expert
=true,

visualUpdate
=true,

enumerationValues
={"SwingConstants.LEFT","SwingConstants.CENTER","SwingConstants.RIGHT","SwingConstants.LEADING","SwingConstants.TRAILING"},

description
="The horizontal position of the label\'s text, relative to its image.")
public void setHorizontalTextPosition​(int textPosition)
```

Sets the horizontal position of the label's text,
relative to its image.

**Parameters:** textPosition

- One of the following constants
defined in

SwingConstants

:

LEFT

,

CENTER

,

RIGHT

,

LEADING

, or

TRAILING

(the default).
**See Also:** SwingConstants

- imageUpdate

```java
public boolean imageUpdate​(
Image
img,
int infoflags,
int x,
int y,
int w,
int h)
```

This is overridden to return false if the current Icon's Image is
not equal to the passed in Image

img

.

**Specified by:** imageUpdate

in interface

ImageObserver
**Overrides:** imageUpdate

in class

Component
**Parameters:** img

- the image being observed
**Parameters:** infoflags

- see

imageUpdate

for more information
**Parameters:** x

- the

x

coordinate
**Parameters:** y

- the

y

coordinate
**Parameters:** w

- the width
**Parameters:** h

- the height
**Returns:** false

if the infoflags indicate that the
image is completely loaded;

true

otherwise.
**See Also:** ImageObserver

,

Component.imageUpdate(java.awt.Image, int, int, int, int, int)

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this JLabel. This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

JComponent
**Returns:** a string representation of this JLabel.

- getLabelFor

```java
public
Component
getLabelFor()
```

Get the component this is labelling.

**Returns:** the Component this is labelling. Can be null if this
does not label a Component. If the displayedMnemonic
property is set and the labelFor property is also set, the label
will call the requestFocus method of the component specified by the
labelFor property when the mnemonic is activated.
**See Also:** getDisplayedMnemonic()

,

setDisplayedMnemonic(int)

- setLabelFor

```java
@BeanProperty
(
description
="The component this is labelling.")
public void setLabelFor​(
Component
c)
```

Set the component this is labelling. Can be null if this does not
label a Component. If the displayedMnemonic property is set
and the labelFor property is also set, the label will
call the requestFocus method of the component specified by the
labelFor property when the mnemonic is activated.

**Parameters:** c

- the Component this label is for, or null if the label is
not the label for a component
**See Also:** getDisplayedMnemonic()

,

setDisplayedMnemonic(int)

- getAccessibleContext

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="The AccessibleContext associated with this Label.")
public
AccessibleContext
getAccessibleContext()
```

Get the AccessibleContext of this object

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** the AccessibleContext of this object

---

#### Method Detail

getUI

```java
public
LabelUI
getUI()
```

Returns the L&F object that renders this component.

**Overrides:** getUI

in class

JComponent
**Returns:** LabelUI object

---

#### getUI

public

LabelUI

getUI()

Returns the L&F object that renders this component.

setUI

```java
@BeanProperty
(
hidden
=true,

visualUpdate
=true,

description
="The UI object that implements the Component\'s LookAndFeel.")
public void setUI​(
LabelUI
ui)
```

Sets the L&F object that renders this component.

**Parameters:** ui

- the LabelUI L&F object
**See Also:** UIDefaults.getUI(javax.swing.JComponent)

---

#### setUI

@BeanProperty

(

hidden

=true,

visualUpdate

=true,

description

="The UI object that implements the Component\'s LookAndFeel.")
public void setUI​(

LabelUI

ui)

Sets the L&F object that renders this component.

updateUI

```java
public void updateUI()
```

Resets the UI property to a value from the current look and feel.

**Overrides:** updateUI

in class

JComponent
**See Also:** JComponent.updateUI()

---

#### updateUI

public void updateUI()

Resets the UI property to a value from the current look and feel.

getUIClassID

```java
@BeanProperty
(
bound
=false)
public
String
getUIClassID()
```

Returns a string that specifies the name of the l&f class
that renders this component.

**Overrides:** getUIClassID

in class

JComponent
**Returns:** String "LabelUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

---

#### getUIClassID

@BeanProperty

(

bound

=false)
public

String

getUIClassID()

Returns a string that specifies the name of the l&f class
that renders this component.

getText

```java
public
String
getText()
```

Returns the text string that the label displays.

**Returns:** a String
**See Also:** setText(java.lang.String)

---

#### getText

public

String

getText()

Returns the text string that the label displays.

setText

```java
@BeanProperty
(
preferred
=true,

visualUpdate
=true,

description
="Defines the single line of text this component will display.")
public void setText​(
String
text)
```

Defines the single line of text this component will display. If
the value of text is null or empty string, nothing is displayed.

The default value of this property is null.

This is a JavaBeans bound property.

**Parameters:** text

- the single line of text this component will display
**See Also:** setVerticalTextPosition(int)

,

setHorizontalTextPosition(int)

,

setIcon(javax.swing.Icon)

---

#### setText

@BeanProperty

(

preferred

=true,

visualUpdate

=true,

description

="Defines the single line of text this component will display.")
public void setText​(

String

text)

Defines the single line of text this component will display. If
the value of text is null or empty string, nothing is displayed.

The default value of this property is null.

This is a JavaBeans bound property.

The default value of this property is null.

This is a JavaBeans bound property.

This is a JavaBeans bound property.

getIcon

```java
public
Icon
getIcon()
```

Returns the graphic image (glyph, icon) that the label displays.

**Returns:** an Icon
**See Also:** setIcon(javax.swing.Icon)

---

#### getIcon

public

Icon

getIcon()

Returns the graphic image (glyph, icon) that the label displays.

setIcon

```java
@BeanProperty
(
preferred
=true,

visualUpdate
=true,

description
="The icon this component will display.")
public void setIcon​(
Icon
icon)
```

Defines the icon this component will display. If
the value of icon is null, nothing is displayed.

The default value of this property is null.

This is a JavaBeans bound property.

**Parameters:** icon

- the default icon this component will display
**See Also:** setVerticalTextPosition(int)

,

setHorizontalTextPosition(int)

,

getIcon()

---

#### setIcon

@BeanProperty

(

preferred

=true,

visualUpdate

=true,

description

="The icon this component will display.")
public void setIcon​(

Icon

icon)

Defines the icon this component will display. If
the value of icon is null, nothing is displayed.

The default value of this property is null.

This is a JavaBeans bound property.

The default value of this property is null.

This is a JavaBeans bound property.

This is a JavaBeans bound property.

getDisabledIcon

```java
public
Icon
getDisabledIcon()
```

Returns the icon used by the label when it's disabled.
If no disabled icon has been set this will forward the call to
the look and feel to construct an appropriate disabled Icon.

Some look and feels might not render the disabled Icon, in which
case they will ignore this.

**Returns:** the

disabledIcon

property
**See Also:** setDisabledIcon(javax.swing.Icon)

,

LookAndFeel.getDisabledIcon(javax.swing.JComponent, javax.swing.Icon)

,

ImageIcon

---

#### getDisabledIcon

public

Icon

getDisabledIcon()

Returns the icon used by the label when it's disabled.
If no disabled icon has been set this will forward the call to
the look and feel to construct an appropriate disabled Icon.

Some look and feels might not render the disabled Icon, in which
case they will ignore this.

Some look and feels might not render the disabled Icon, in which
case they will ignore this.

setDisabledIcon

```java
@BeanProperty
(
visualUpdate
=true,

description
="The icon to display if the label is disabled.")
public void setDisabledIcon​(
Icon
disabledIcon)
```

Set the icon to be displayed if this JLabel is "disabled"
(JLabel.setEnabled(false)).

The default value of this property is null.

**Parameters:** disabledIcon

- the Icon to display when the component is disabled
**See Also:** getDisabledIcon()

,

JComponent.setEnabled(boolean)

---

#### setDisabledIcon

@BeanProperty

(

visualUpdate

=true,

description

="The icon to display if the label is disabled.")
public void setDisabledIcon​(

Icon

disabledIcon)

Set the icon to be displayed if this JLabel is "disabled"
(JLabel.setEnabled(false)).

The default value of this property is null.

The default value of this property is null.

setDisplayedMnemonic

```java
@BeanProperty
(
visualUpdate
=true,

description
="The mnemonic keycode.")
public void setDisplayedMnemonic​(int key)
```

Specify a keycode that indicates a mnemonic key.
This property is used when the label is part of a larger component.
If the labelFor property of the label is not null, the label will
call the requestFocus method of the component specified by the
labelFor property when the mnemonic is activated.

**Parameters:** key

- a keycode that indicates a mnemonic key
**See Also:** getLabelFor()

,

setLabelFor(java.awt.Component)

---

#### setDisplayedMnemonic

@BeanProperty

(

visualUpdate

=true,

description

="The mnemonic keycode.")
public void setDisplayedMnemonic​(int key)

Specify a keycode that indicates a mnemonic key.
This property is used when the label is part of a larger component.
If the labelFor property of the label is not null, the label will
call the requestFocus method of the component specified by the
labelFor property when the mnemonic is activated.

setDisplayedMnemonic

```java
public void setDisplayedMnemonic​(char aChar)
```

Specifies the displayedMnemonic as a char value.

**Parameters:** aChar

- a char specifying the mnemonic to display
**See Also:** setDisplayedMnemonic(int)

---

#### setDisplayedMnemonic

public void setDisplayedMnemonic​(char aChar)

Specifies the displayedMnemonic as a char value.

getDisplayedMnemonic

```java
public int getDisplayedMnemonic()
```

Return the keycode that indicates a mnemonic key.
This property is used when the label is part of a larger component.
If the labelFor property of the label is not null, the label will
call the requestFocus method of the component specified by the
labelFor property when the mnemonic is activated.

**Returns:** int value for the mnemonic key
**See Also:** getLabelFor()

,

setLabelFor(java.awt.Component)

---

#### getDisplayedMnemonic

public int getDisplayedMnemonic()

Return the keycode that indicates a mnemonic key.
This property is used when the label is part of a larger component.
If the labelFor property of the label is not null, the label will
call the requestFocus method of the component specified by the
labelFor property when the mnemonic is activated.

setDisplayedMnemonicIndex

```java
@BeanProperty
(
visualUpdate
=true,

description
="the index into the String to draw the keyboard character mnemonic at")
public void setDisplayedMnemonicIndex​(int index)
throws
IllegalArgumentException
```

Provides a hint to the look and feel as to which character in the
text should be decorated to represent the mnemonic. Not all look and
feels may support this. A value of -1 indicates either there is no
mnemonic, the mnemonic character is not contained in the string, or
the developer does not wish the mnemonic to be displayed.

The value of this is updated as the properties relating to the
mnemonic change (such as the mnemonic itself, the text...).
You should only ever have to call this if
you do not wish the default character to be underlined. For example, if
the text was 'Save As', with a mnemonic of 'a', and you wanted the 'A'
to be decorated, as 'Save

A

s', you would have to invoke

setDisplayedMnemonicIndex(5)

after invoking

setDisplayedMnemonic(KeyEvent.VK_A)

.

**Parameters:** index

- Index into the String to underline
**Throws:** IllegalArgumentException

- will be thrown if

index

is >= length of the text, or < -1
**Since:** 1.4

---

#### setDisplayedMnemonicIndex

@BeanProperty

(

visualUpdate

=true,

description

="the index into the String to draw the keyboard character mnemonic at")
public void setDisplayedMnemonicIndex​(int index)
throws

IllegalArgumentException

Provides a hint to the look and feel as to which character in the
text should be decorated to represent the mnemonic. Not all look and
feels may support this. A value of -1 indicates either there is no
mnemonic, the mnemonic character is not contained in the string, or
the developer does not wish the mnemonic to be displayed.

The value of this is updated as the properties relating to the
mnemonic change (such as the mnemonic itself, the text...).
You should only ever have to call this if
you do not wish the default character to be underlined. For example, if
the text was 'Save As', with a mnemonic of 'a', and you wanted the 'A'
to be decorated, as 'Save

A

s', you would have to invoke

setDisplayedMnemonicIndex(5)

after invoking

setDisplayedMnemonic(KeyEvent.VK_A)

.

The value of this is updated as the properties relating to the
mnemonic change (such as the mnemonic itself, the text...).
You should only ever have to call this if
you do not wish the default character to be underlined. For example, if
the text was 'Save As', with a mnemonic of 'a', and you wanted the 'A'
to be decorated, as 'Save

A

s', you would have to invoke

setDisplayedMnemonicIndex(5)

after invoking

setDisplayedMnemonic(KeyEvent.VK_A)

.

getDisplayedMnemonicIndex

```java
public int getDisplayedMnemonicIndex()
```

Returns the character, as an index, that the look and feel should
provide decoration for as representing the mnemonic character.

**Returns:** index representing mnemonic character
**Since:** 1.4
**See Also:** setDisplayedMnemonicIndex(int)

---

#### getDisplayedMnemonicIndex

public int getDisplayedMnemonicIndex()

Returns the character, as an index, that the look and feel should
provide decoration for as representing the mnemonic character.

checkHorizontalKey

```java
protected int checkHorizontalKey​(int key,

String
message)
```

Verify that key is a legal value for the horizontalAlignment properties.

**Parameters:** key

- the property value to check
**Parameters:** message

- the IllegalArgumentException detail message
**Returns:** the key value if

key

is a a legal value for the
horizontalAlignment properties
**Throws:** IllegalArgumentException

- if key isn't LEFT, CENTER, RIGHT,
LEADING or TRAILING.
**See Also:** setHorizontalTextPosition(int)

,

setHorizontalAlignment(int)

---

#### checkHorizontalKey

protected int checkHorizontalKey​(int key,

String

message)

Verify that key is a legal value for the horizontalAlignment properties.

checkVerticalKey

```java
protected int checkVerticalKey​(int key,

String
message)
```

Verify that key is a legal value for the
verticalAlignment or verticalTextPosition properties.

**Parameters:** key

- the property value to check
**Parameters:** message

- the IllegalArgumentException detail message
**Returns:** the key value if

key

is a legal value for the
verticalAlignment or verticalTextPosition properties
**Throws:** IllegalArgumentException

- if key isn't TOP, CENTER, or BOTTOM.
**See Also:** setVerticalAlignment(int)

,

setVerticalTextPosition(int)

---

#### checkVerticalKey

protected int checkVerticalKey​(int key,

String

message)

Verify that key is a legal value for the
verticalAlignment or verticalTextPosition properties.

getIconTextGap

```java
public int getIconTextGap()
```

Returns the amount of space between the text and the icon
displayed in this label.

**Returns:** an int equal to the number of pixels between the text
and the icon.
**See Also:** setIconTextGap(int)

---

#### getIconTextGap

public int getIconTextGap()

Returns the amount of space between the text and the icon
displayed in this label.

setIconTextGap

```java
@BeanProperty
(
visualUpdate
=true,

description
="If both the icon and text properties are set, this property defines the space between them.")
public void setIconTextGap​(int iconTextGap)
```

If both the icon and text properties are set, this property
defines the space between them.

The default value of this property is 4 pixels.

This is a JavaBeans bound property.

**Parameters:** iconTextGap

- the space between the icon and text properties
**See Also:** getIconTextGap()

---

#### setIconTextGap

@BeanProperty

(

visualUpdate

=true,

description

="If both the icon and text properties are set, this property defines the space between them.")
public void setIconTextGap​(int iconTextGap)

If both the icon and text properties are set, this property
defines the space between them.

The default value of this property is 4 pixels.

This is a JavaBeans bound property.

The default value of this property is 4 pixels.

This is a JavaBeans bound property.

This is a JavaBeans bound property.

getVerticalAlignment

```java
public int getVerticalAlignment()
```

Returns the alignment of the label's contents along the Y axis.

**Returns:** The value of the verticalAlignment property, one of the
following constants defined in

SwingConstants

:

TOP

,

CENTER

, or

BOTTOM

.
**See Also:** SwingConstants

,

setVerticalAlignment(int)

---

#### getVerticalAlignment

public int getVerticalAlignment()

Returns the alignment of the label's contents along the Y axis.

setVerticalAlignment

```java
@BeanProperty
(
visualUpdate
=true,

enumerationValues
={"SwingConstants.TOP","SwingConstants.CENTER","SwingConstants.BOTTOM"},

description
="The alignment of the label\'s contents along the Y axis.")
public void setVerticalAlignment​(int alignment)
```

Sets the alignment of the label's contents along the Y axis.

The default value of this property is CENTER.

**Parameters:** alignment

- One of the following constants
defined in

SwingConstants

:

TOP

,

CENTER

(the default), or

BOTTOM

.
**See Also:** SwingConstants

,

getVerticalAlignment()

---

#### setVerticalAlignment

@BeanProperty

(

visualUpdate

=true,

enumerationValues

={"SwingConstants.TOP","SwingConstants.CENTER","SwingConstants.BOTTOM"},

description

="The alignment of the label\'s contents along the Y axis.")
public void setVerticalAlignment​(int alignment)

Sets the alignment of the label's contents along the Y axis.

The default value of this property is CENTER.

The default value of this property is CENTER.

getHorizontalAlignment

```java
public int getHorizontalAlignment()
```

Returns the alignment of the label's contents along the X axis.

**Returns:** The value of the horizontalAlignment property, one of the
following constants defined in

SwingConstants

:

LEFT

,

CENTER

,

RIGHT

,

LEADING

or

TRAILING

.
**See Also:** setHorizontalAlignment(int)

,

SwingConstants

---

#### getHorizontalAlignment

public int getHorizontalAlignment()

Returns the alignment of the label's contents along the X axis.

setHorizontalAlignment

```java
@BeanProperty
(
visualUpdate
=true,

enumerationValues
={"SwingConstants.LEFT","SwingConstants.CENTER","SwingConstants.RIGHT","SwingConstants.LEADING","SwingConstants.TRAILING"},

description
="The alignment of the label\'s content along the X axis.")
public void setHorizontalAlignment​(int alignment)
```

Sets the alignment of the label's contents along the X axis.

This is a JavaBeans bound property.

**Parameters:** alignment

- One of the following constants
defined in

SwingConstants

:

LEFT

,

CENTER

(the default for image-only labels),

RIGHT

,

LEADING

(the default for text-only labels) or

TRAILING

.
**See Also:** SwingConstants

,

getHorizontalAlignment()

---

#### setHorizontalAlignment

@BeanProperty

(

visualUpdate

=true,

enumerationValues

={"SwingConstants.LEFT","SwingConstants.CENTER","SwingConstants.RIGHT","SwingConstants.LEADING","SwingConstants.TRAILING"},

description

="The alignment of the label\'s content along the X axis.")
public void setHorizontalAlignment​(int alignment)

Sets the alignment of the label's contents along the X axis.

This is a JavaBeans bound property.

This is a JavaBeans bound property.

getVerticalTextPosition

```java
public int getVerticalTextPosition()
```

Returns the vertical position of the label's text,
relative to its image.

**Returns:** One of the following constants
defined in

SwingConstants

:

TOP

,

CENTER

, or

BOTTOM

.
**See Also:** setVerticalTextPosition(int)

,

SwingConstants

---

#### getVerticalTextPosition

public int getVerticalTextPosition()

Returns the vertical position of the label's text,
relative to its image.

setVerticalTextPosition

```java
@BeanProperty
(
expert
=true,

visualUpdate
=true,

enumerationValues
={"SwingConstants.TOP","SwingConstants.CENTER","SwingConstants.BOTTOM"},

description
="The vertical position of the text relative to it\'s image.")
public void setVerticalTextPosition​(int textPosition)
```

Sets the vertical position of the label's text,
relative to its image.

The default value of this property is CENTER.

This is a JavaBeans bound property.

**Parameters:** textPosition

- One of the following constants
defined in

SwingConstants

:

TOP

,

CENTER

(the default), or

BOTTOM

.
**See Also:** SwingConstants

,

getVerticalTextPosition()

---

#### setVerticalTextPosition

@BeanProperty

(

expert

=true,

visualUpdate

=true,

enumerationValues

={"SwingConstants.TOP","SwingConstants.CENTER","SwingConstants.BOTTOM"},

description

="The vertical position of the text relative to it\'s image.")
public void setVerticalTextPosition​(int textPosition)

Sets the vertical position of the label's text,
relative to its image.

The default value of this property is CENTER.

This is a JavaBeans bound property.

The default value of this property is CENTER.

This is a JavaBeans bound property.

This is a JavaBeans bound property.

getHorizontalTextPosition

```java
public int getHorizontalTextPosition()
```

Returns the horizontal position of the label's text,
relative to its image.

**Returns:** One of the following constants
defined in

SwingConstants

:

LEFT

,

CENTER

,

RIGHT

,

LEADING

or

TRAILING

.
**See Also:** SwingConstants

---

#### getHorizontalTextPosition

public int getHorizontalTextPosition()

Returns the horizontal position of the label's text,
relative to its image.

setHorizontalTextPosition

```java
@BeanProperty
(
expert
=true,

visualUpdate
=true,

enumerationValues
={"SwingConstants.LEFT","SwingConstants.CENTER","SwingConstants.RIGHT","SwingConstants.LEADING","SwingConstants.TRAILING"},

description
="The horizontal position of the label\'s text, relative to its image.")
public void setHorizontalTextPosition​(int textPosition)
```

Sets the horizontal position of the label's text,
relative to its image.

**Parameters:** textPosition

- One of the following constants
defined in

SwingConstants

:

LEFT

,

CENTER

,

RIGHT

,

LEADING

, or

TRAILING

(the default).
**See Also:** SwingConstants

---

#### setHorizontalTextPosition

@BeanProperty

(

expert

=true,

visualUpdate

=true,

enumerationValues

={"SwingConstants.LEFT","SwingConstants.CENTER","SwingConstants.RIGHT","SwingConstants.LEADING","SwingConstants.TRAILING"},

description

="The horizontal position of the label\'s text, relative to its image.")
public void setHorizontalTextPosition​(int textPosition)

Sets the horizontal position of the label's text,
relative to its image.

imageUpdate

```java
public boolean imageUpdate​(
Image
img,
int infoflags,
int x,
int y,
int w,
int h)
```

This is overridden to return false if the current Icon's Image is
not equal to the passed in Image

img

.

**Specified by:** imageUpdate

in interface

ImageObserver
**Overrides:** imageUpdate

in class

Component
**Parameters:** img

- the image being observed
**Parameters:** infoflags

- see

imageUpdate

for more information
**Parameters:** x

- the

x

coordinate
**Parameters:** y

- the

y

coordinate
**Parameters:** w

- the width
**Parameters:** h

- the height
**Returns:** false

if the infoflags indicate that the
image is completely loaded;

true

otherwise.
**See Also:** ImageObserver

,

Component.imageUpdate(java.awt.Image, int, int, int, int, int)

---

#### imageUpdate

public boolean imageUpdate​(

Image

img,
int infoflags,
int x,
int y,
int w,
int h)

This is overridden to return false if the current Icon's Image is
not equal to the passed in Image

img

.

paramString

```java
protected
String
paramString()
```

Returns a string representation of this JLabel. This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

JComponent
**Returns:** a string representation of this JLabel.

---

#### paramString

protected

String

paramString()

Returns a string representation of this JLabel. This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

getLabelFor

```java
public
Component
getLabelFor()
```

Get the component this is labelling.

**Returns:** the Component this is labelling. Can be null if this
does not label a Component. If the displayedMnemonic
property is set and the labelFor property is also set, the label
will call the requestFocus method of the component specified by the
labelFor property when the mnemonic is activated.
**See Also:** getDisplayedMnemonic()

,

setDisplayedMnemonic(int)

---

#### getLabelFor

public

Component

getLabelFor()

Get the component this is labelling.

setLabelFor

```java
@BeanProperty
(
description
="The component this is labelling.")
public void setLabelFor​(
Component
c)
```

Set the component this is labelling. Can be null if this does not
label a Component. If the displayedMnemonic property is set
and the labelFor property is also set, the label will
call the requestFocus method of the component specified by the
labelFor property when the mnemonic is activated.

**Parameters:** c

- the Component this label is for, or null if the label is
not the label for a component
**See Also:** getDisplayedMnemonic()

,

setDisplayedMnemonic(int)

---

#### setLabelFor

@BeanProperty

(

description

="The component this is labelling.")
public void setLabelFor​(

Component

c)

Set the component this is labelling. Can be null if this does not
label a Component. If the displayedMnemonic property is set
and the labelFor property is also set, the label will
call the requestFocus method of the component specified by the
labelFor property when the mnemonic is activated.

getAccessibleContext

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="The AccessibleContext associated with this Label.")
public
AccessibleContext
getAccessibleContext()
```

Get the AccessibleContext of this object

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** the AccessibleContext of this object

---

#### getAccessibleContext

@BeanProperty

(

bound

=false,

expert

=true,

description

="The AccessibleContext associated with this Label.")
public

AccessibleContext

getAccessibleContext()

Get the AccessibleContext of this object

---

