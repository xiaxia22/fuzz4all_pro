# Class AbstractButton

**Source:** `java.desktop\javax\swing\AbstractButton.html`

### Class Description

```java
@JavaBean
(
defaultProperty
="UI")
public abstract class
AbstractButton

extends
JComponent

implements
ItemSelectable
,
SwingConstants
```

Defines common behaviors for buttons and menu items.

Buttons can be configured, and to some degree controlled, by

Action

s. Using an

Action

with a button has many benefits beyond directly
configuring a button. Refer to

Swing Components Supporting

Action

for more
details, and you can find more information in

How
to Use Actions

, a section in

The Java Tutorial

.

For further information see

How to Use Buttons, Check Boxes, and Radio Buttons

,
a section in

The Java Tutorial

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

ItemSelectable

,

MenuContainer

,

Serializable

,

SwingConstants

---

### Field Details

#### public static final
String
MODEL_CHANGED_PROPERTY

Identifies a change in the button model.

**See Also:**
- Constant Field Values

---

#### public static final
String
TEXT_CHANGED_PROPERTY

Identifies a change in the button's text.

**See Also:**
- Constant Field Values

---

#### public static final
String
MNEMONIC_CHANGED_PROPERTY

Identifies a change to the button's mnemonic.

**See Also:**
- Constant Field Values

---

#### public static final
String
MARGIN_CHANGED_PROPERTY

Identifies a change in the button's margins.

**See Also:**
- Constant Field Values

---

#### public static final
String
VERTICAL_ALIGNMENT_CHANGED_PROPERTY

Identifies a change in the button's vertical alignment.

**See Also:**
- Constant Field Values

---

#### public static final
String
HORIZONTAL_ALIGNMENT_CHANGED_PROPERTY

Identifies a change in the button's horizontal alignment.

**See Also:**
- Constant Field Values

---

#### public static final
String
VERTICAL_TEXT_POSITION_CHANGED_PROPERTY

Identifies a change in the button's vertical text position.

**See Also:**
- Constant Field Values

---

#### public static final
String
HORIZONTAL_TEXT_POSITION_CHANGED_PROPERTY

Identifies a change in the button's horizontal text position.

**See Also:**
- Constant Field Values

---

#### public static final
String
BORDER_PAINTED_CHANGED_PROPERTY

Identifies a change to having the border drawn,
or having it not drawn.

**See Also:**
- Constant Field Values

---

#### public static final
String
FOCUS_PAINTED_CHANGED_PROPERTY

Identifies a change to having the border highlighted when focused,
or not.

**See Also:**
- Constant Field Values

---

#### public static final
String
ROLLOVER_ENABLED_CHANGED_PROPERTY

Identifies a change from rollover enabled to disabled or back
to enabled.

**See Also:**
- Constant Field Values

---

#### public static final
String
CONTENT_AREA_FILLED_CHANGED_PROPERTY

Identifies a change to having the button paint the content area.

**See Also:**
- Constant Field Values

---

#### public static final
String
ICON_CHANGED_PROPERTY

Identifies a change to the icon that represents the button.

**See Also:**
- Constant Field Values

---

#### public static final
String
PRESSED_ICON_CHANGED_PROPERTY

Identifies a change to the icon used when the button has been
pressed.

**See Also:**
- Constant Field Values

---

#### public static final
String
SELECTED_ICON_CHANGED_PROPERTY

Identifies a change to the icon used when the button has
been selected.

**See Also:**
- Constant Field Values

---

#### public static final
String
ROLLOVER_ICON_CHANGED_PROPERTY

Identifies a change to the icon used when the cursor is over
the button.

**See Also:**
- Constant Field Values

---

#### public static final
String
ROLLOVER_SELECTED_ICON_CHANGED_PROPERTY

Identifies a change to the icon used when the cursor is
over the button and it has been selected.

**See Also:**
- Constant Field Values

---

#### public static final
String
DISABLED_ICON_CHANGED_PROPERTY

Identifies a change to the icon used when the button has
been disabled.

**See Also:**
- Constant Field Values

---

#### public static final
String
DISABLED_SELECTED_ICON_CHANGED_PROPERTY

Identifies a change to the icon used when the button has been
disabled and selected.

**See Also:**
- Constant Field Values

---

#### protected
ButtonModel
model

The data model that determines the button's state.

---

#### protected
ChangeListener
changeListener

The button model's

changeListener

.

---

#### protected
ActionListener
actionListener

The button model's

ActionListener

.

---

#### protected
ItemListener
itemListener

The button model's

ItemListener

.

---

#### protected transient
ChangeEvent
changeEvent

Only one

ChangeEvent

is needed per button
instance since the
event's only state is the source property. The source of events
generated is always "this".

---

### Constructor Details

#### public AbstractButton()

*No description found.*

---

### Method Details

#### @BeanProperty
(
expert
=true,

description
="Whether the text of the button should come from the <code>Action</code>.")
public void setHideActionText​(boolean hideActionText)

Sets the

hideActionText

property, which determines
whether the button displays text from the

Action

.
This is useful only if an

Action

has been
installed on the button.

**Parameters:**
- hideActionText

-

true

if the button's

text

property should not reflect
that of the

Action

; the default is

false

**See Also:**
- Swing Components Supporting

Action

**Since:**
- 1.6

---

#### public boolean getHideActionText()

Returns the value of the

hideActionText

property, which
determines whether the button displays text from the

Action

. This is useful only if an

Action

has been installed on the button.

**Returns:**
- true

if the button's

text

property should not reflect that of the

Action

; the default is

false

**Since:**
- 1.6

---

#### public
String
getText()

Returns the button's text.

**Returns:**
- the buttons text

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
="The button\'s text.")
public void setText​(
String
text)

Sets the button's text.

**Parameters:**
- text

- the string used to set the text

**See Also:**
- getText()

---

#### public boolean isSelected()

Returns the state of the button. True if the
toggle button is selected, false if it's not.

**Returns:**
- true if the toggle button is selected, otherwise false

---

#### public void setSelected​(boolean b)

Sets the state of the button. Note that this method does not
trigger an

actionEvent

.
Call

doClick

to perform a programmatic action change.

**Parameters:**
- b

- true if the button is selected, otherwise false

---

#### public void doClick()

Programmatically perform a "click". This does the same
thing as if the user had pressed and released the button.

---

#### public void doClick​(int pressTime)

Programmatically perform a "click". This does the same
thing as if the user had pressed and released the button.
The button stays visually "pressed" for

pressTime

milliseconds.

**Parameters:**
- pressTime

- the time to "hold down" the button, in milliseconds

---

#### @BeanProperty
(
visualUpdate
=true,

description
="The space between the button\'s border and the label.")
public void setMargin​(
Insets
m)

Sets space for margin between the button's border and
the label. Setting to

null

will cause the button to
use the default margin. The button's default

Border

object will use this value to create the proper margin.
However, if a non-default border is set on the button,
it is that

Border

object's responsibility to create the
appropriate margin space (else this property will
effectively be ignored).

**Parameters:**
- m

- the space between the border and the label

---

#### public
Insets
getMargin()

Returns the margin between the button's border and
the label.

**Returns:**
- an

Insets

object specifying the margin
between the botton's border and the label

**See Also:**
- setMargin(java.awt.Insets)

---

#### public
Icon
getIcon()

Returns the default icon.

**Returns:**
- the default

Icon

**See Also:**
- setIcon(javax.swing.Icon)

---

#### @BeanProperty
(
visualUpdate
=true,

description
="The button\'s default icon")
public void setIcon​(
Icon
defaultIcon)

Sets the button's default icon. This icon is
also used as the "pressed" and "disabled" icon if
there is no explicitly set pressed icon.

**Parameters:**
- defaultIcon

- the icon used as the default image

**See Also:**
- getIcon()

,

setPressedIcon(javax.swing.Icon)

---

#### public
Icon
getPressedIcon()

Returns the pressed icon for the button.

**Returns:**
- the

pressedIcon

property

**See Also:**
- setPressedIcon(javax.swing.Icon)

---

#### @BeanProperty
(
visualUpdate
=true,

description
="The pressed icon for the button.")
public void setPressedIcon​(
Icon
pressedIcon)

Sets the pressed icon for the button.

**Parameters:**
- pressedIcon

- the icon used as the "pressed" image

**See Also:**
- getPressedIcon()

---

#### public
Icon
getSelectedIcon()

Returns the selected icon for the button.

**Returns:**
- the

selectedIcon

property

**See Also:**
- setSelectedIcon(javax.swing.Icon)

---

#### @BeanProperty
(
visualUpdate
=true,

description
="The selected icon for the button.")
public void setSelectedIcon​(
Icon
selectedIcon)

Sets the selected icon for the button.

**Parameters:**
- selectedIcon

- the icon used as the "selected" image

**See Also:**
- getSelectedIcon()

---

#### public
Icon
getRolloverIcon()

Returns the rollover icon for the button.

**Returns:**
- the

rolloverIcon

property

**See Also:**
- setRolloverIcon(javax.swing.Icon)

---

#### @BeanProperty
(
visualUpdate
=true,

description
="The rollover icon for the button.")
public void setRolloverIcon​(
Icon
rolloverIcon)

Sets the rollover icon for the button.

**Parameters:**
- rolloverIcon

- the icon used as the "rollover" image

**See Also:**
- getRolloverIcon()

---

#### public
Icon
getRolloverSelectedIcon()

Returns the rollover selection icon for the button.

**Returns:**
- the

rolloverSelectedIcon

property

**See Also:**
- setRolloverSelectedIcon(javax.swing.Icon)

---

#### @BeanProperty
(
visualUpdate
=true,

description
="The rollover selected icon for the button.")
public void setRolloverSelectedIcon​(
Icon
rolloverSelectedIcon)

Sets the rollover selected icon for the button.

**Parameters:**
- rolloverSelectedIcon

- the icon used as the
"selected rollover" image

**See Also:**
- getRolloverSelectedIcon()

---

#### public
Icon
getDisabledIcon()

Returns the icon used by the button when it's disabled.
If no disabled icon has been set this will forward the call to
the look and feel to construct an appropriate disabled Icon.

Some look and feels might not render the disabled Icon, in which
case they will ignore this.

**Returns:**
- the

disabledIcon

property

**See Also:**
- getPressedIcon()

,

setDisabledIcon(javax.swing.Icon)

,

LookAndFeel.getDisabledIcon(javax.swing.JComponent, javax.swing.Icon)

---

#### @BeanProperty
(
visualUpdate
=true,

description
="The disabled icon for the button.")
public void setDisabledIcon​(
Icon
disabledIcon)

Sets the disabled icon for the button.

**Parameters:**
- disabledIcon

- the icon used as the disabled image

**See Also:**
- getDisabledIcon()

---

#### public
Icon
getDisabledSelectedIcon()

Returns the icon used by the button when it's disabled and selected.
If no disabled selection icon has been set, this will forward
the call to the LookAndFeel to construct an appropriate disabled
Icon from the selection icon if it has been set and to

getDisabledIcon()

otherwise.

Some look and feels might not render the disabled selected Icon, in
which case they will ignore this.

**Returns:**
- the

disabledSelectedIcon

property

**See Also:**
- getDisabledIcon()

,

setDisabledSelectedIcon(javax.swing.Icon)

,

LookAndFeel.getDisabledSelectedIcon(javax.swing.JComponent, javax.swing.Icon)

---

#### @BeanProperty
(
visualUpdate
=true,

description
="The disabled selection icon for the button.")
public void setDisabledSelectedIcon​(
Icon
disabledSelectedIcon)

Sets the disabled selection icon for the button.

**Parameters:**
- disabledSelectedIcon

- the icon used as the disabled
selection image

**See Also:**
- getDisabledSelectedIcon()

---

#### public int getVerticalAlignment()

Returns the vertical alignment of the text and icon.

**Returns:**
- the

verticalAlignment

property, one of the
following values:

- SwingConstants.CENTER

(the default)

SwingConstants.TOP

SwingConstants.BOTTOM

---

#### @BeanProperty
(
visualUpdate
=true,

enumerationValues
={"SwingConstants.TOP","SwingConstants.CENTER","SwingConstants.BOTTOM"},

description
="The vertical alignment of the icon and text.")
public void setVerticalAlignment​(int alignment)

Sets the vertical alignment of the icon and text.

**Parameters:**
- alignment

- one of the following values:

- SwingConstants.CENTER

(the default)

SwingConstants.TOP

SwingConstants.BOTTOM

**Throws:**
- IllegalArgumentException

- if the alignment is not one of the legal
values listed above

---

#### public int getHorizontalAlignment()

Returns the horizontal alignment of the icon and text.

AbstractButton

's default is

SwingConstants.CENTER

,
but subclasses such as

JCheckBox

may use a different default.

**Returns:**
- the

horizontalAlignment

property,
one of the following values:

- SwingConstants.RIGHT

SwingConstants.LEFT

SwingConstants.CENTER

SwingConstants.LEADING

SwingConstants.TRAILING

---

#### @BeanProperty
(
visualUpdate
=true,

enumerationValues
={"SwingConstants.LEFT","SwingConstants.CENTER","SwingConstants.RIGHT","SwingConstants.LEADING","SwingConstants.TRAILING"},

description
="The horizontal alignment of the icon and text.")
public void setHorizontalAlignment​(int alignment)

Sets the horizontal alignment of the icon and text.

AbstractButton

's default is

SwingConstants.CENTER

,
but subclasses such as

JCheckBox

may use a different default.

**Parameters:**
- alignment

- the alignment value, one of the following values:

- SwingConstants.RIGHT

SwingConstants.LEFT

SwingConstants.CENTER

SwingConstants.LEADING

SwingConstants.TRAILING

**Throws:**
- IllegalArgumentException

- if the alignment is not one of the
valid values

---

#### public int getVerticalTextPosition()

Returns the vertical position of the text relative to the icon.

**Returns:**
- the

verticalTextPosition

property,
one of the following values:

- SwingConstants.CENTER

(the default)

SwingConstants.TOP

SwingConstants.BOTTOM

---

#### @BeanProperty
(
visualUpdate
=true,

enumerationValues
={"SwingConstants.TOP","SwingConstants.CENTER","SwingConstants.BOTTOM"},

description
="The vertical position of the text relative to the icon.")
public void setVerticalTextPosition​(int textPosition)

Sets the vertical position of the text relative to the icon.

**Parameters:**
- textPosition

- one of the following values:

- SwingConstants.CENTER

(the default)

SwingConstants.TOP

SwingConstants.BOTTOM

---

#### public int getHorizontalTextPosition()

Returns the horizontal position of the text relative to the icon.

**Returns:**
- the

horizontalTextPosition

property,
one of the following values:

- SwingConstants.RIGHT

SwingConstants.LEFT

SwingConstants.CENTER

SwingConstants.LEADING

SwingConstants.TRAILING

(the default)

---

#### @BeanProperty
(
visualUpdate
=true,

enumerationValues
={"SwingConstants.LEFT","SwingConstants.CENTER","SwingConstants.RIGHT","SwingConstants.LEADING","SwingConstants.TRAILING"},

description
="The horizontal position of the text relative to the icon.")
public void setHorizontalTextPosition​(int textPosition)

Sets the horizontal position of the text relative to the icon.

**Parameters:**
- textPosition

- one of the following values:

- SwingConstants.RIGHT

SwingConstants.LEFT

SwingConstants.CENTER

SwingConstants.LEADING

SwingConstants.TRAILING

(the default)

**Throws:**
- IllegalArgumentException

- if

textPosition

is not one of the legal values listed above

---

#### public int getIconTextGap()

Returns the amount of space between the text and the icon
displayed in this button.

**Returns:**
- an int equal to the number of pixels between the text
and the icon.

**See Also:**
- setIconTextGap(int)

**Since:**
- 1.4

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

- the space between icon and text if these properties are set.

**See Also:**
- getIconTextGap()

**Since:**
- 1.4

---

#### protected int checkHorizontalKey​(int key,

String
exception)

Verify that the

key

argument is a legal value for the

horizontalAlignment

and

horizontalTextPosition

properties. Valid values are:

- SwingConstants.RIGHT

SwingConstants.LEFT

SwingConstants.CENTER

SwingConstants.LEADING

SwingConstants.TRAILING

**Parameters:**
- key

- the property value to check
- exception

- the message to use in the

IllegalArgumentException

that is thrown for an invalid
value

**Returns:**
- the

key

argument

**Throws:**
- IllegalArgumentException

- if key is not one of the legal
values listed above

**See Also:**
- setHorizontalTextPosition(int)

,

setHorizontalAlignment(int)

---

#### protected int checkVerticalKey​(int key,

String
exception)

Verify that the

key

argument is a legal value for the
vertical properties. Valid values are:

- SwingConstants.CENTER

SwingConstants.TOP

SwingConstants.BOTTOM

**Parameters:**
- key

- the property value to check
- exception

- the message to use in the

IllegalArgumentException

that is thrown for an invalid
value

**Returns:**
- the

key

argument

**Throws:**
- IllegalArgumentException

- if key is not one of the legal
values listed above

---

#### public void removeNotify()

Notifies this component that it no longer has a parent component.
When this method is invoked, any

KeyboardAction

s
set up in the chain of parent components are removed.
This method is called by the toolkit internally and should
not be called directly by programs.

**Overrides:**
- removeNotify

in class

JComponent

**See Also:**
- JComponent.registerKeyboardAction(java.awt.event.ActionListener, java.lang.String, javax.swing.KeyStroke, int)

**Since:**
- 1.6

---

#### public void setActionCommand​(
String
actionCommand)

Sets the action command for this button.

**Parameters:**
- actionCommand

- the action command for this button

---

#### public
String
getActionCommand()

Returns the action command for this button.

**Returns:**
- the action command for this button

---

#### @BeanProperty
(
visualUpdate
=true,

description
="the Action instance connected with this ActionEvent source")
public void setAction​(
Action
a)

Sets the

Action

.
The new

Action

replaces any previously set

Action

but does not affect

ActionListeners

independently added with

addActionListener

.
If the

Action

is already a registered

ActionListener

for the button, it is not re-registered.

Setting the

Action

results in immediately changing
all the properties described in

Swing Components Supporting

Action

.
Subsequently, the button's properties are automatically updated
as the

Action

's properties change.

This method uses three other methods to set
and help track the

Action

's property values.
It uses the

configurePropertiesFromAction

method
to immediately change the button's properties.
To track changes in the

Action

's property values,
this method registers the

PropertyChangeListener

returned by

createActionPropertyChangeListener

. The
default

PropertyChangeListener

invokes the

actionPropertyChanged

method when a property in the

Action

changes.

**Parameters:**
- a

- the

Action

for the

AbstractButton

,
or

null

**See Also:**
- Action

,

getAction()

,

configurePropertiesFromAction(javax.swing.Action)

,

createActionPropertyChangeListener(javax.swing.Action)

,

actionPropertyChanged(javax.swing.Action, java.lang.String)

**Since:**
- 1.3

---

#### public
Action
getAction()

Returns the currently set

Action

for this

ActionEvent

source, or

null

if no

Action

is set.

**Returns:**
- the

Action

for this

ActionEvent

source, or

null

**See Also:**
- Action

,

setAction(javax.swing.Action)

**Since:**
- 1.3

---

#### protected void configurePropertiesFromAction​(
Action
a)

Sets the properties on this button to match those in the specified

Action

. Refer to

Swing Components Supporting

Action

for more
details as to which properties this sets.

**Parameters:**
- a

- the

Action

from which to get the properties,
or

null

**See Also:**
- Action

,

setAction(javax.swing.Action)

**Since:**
- 1.3

---

#### protected void actionPropertyChanged​(
Action
action,

String
propertyName)

Updates the button's state in response to property changes in the
associated action. This method is invoked from the

PropertyChangeListener

returned from

createActionPropertyChangeListener

. Subclasses do not normally
need to invoke this. Subclasses that support additional

Action

properties should override this and

configurePropertiesFromAction

.

Refer to the table at

Swing Components Supporting

Action

for a list of
the properties this method sets.

**Parameters:**
- action

- the

Action

associated with this button
- propertyName

- the name of the property that changed

**See Also:**
- Action

,

configurePropertiesFromAction(javax.swing.Action)

**Since:**
- 1.6

---

#### protected
PropertyChangeListener
createActionPropertyChangeListener​(
Action
a)

Creates and returns a

PropertyChangeListener

that is
responsible for listening for changes from the specified

Action

and updating the appropriate properties.

Warning:

If you subclass this do not create an anonymous
inner class. If you do the lifetime of the button will be tied to
that of the

Action

.

**Parameters:**
- a

- the button's action

**Returns:**
- the

PropertyChangeListener

**See Also:**
- Action

,

setAction(javax.swing.Action)

**Since:**
- 1.3

---

#### public boolean isBorderPainted()

Gets the

borderPainted

property.

**Returns:**
- the value of the

borderPainted

property

**See Also:**
- setBorderPainted(boolean)

---

#### @BeanProperty
(
visualUpdate
=true,

description
="Whether the border should be painted.")
public void setBorderPainted​(boolean b)

Sets the

borderPainted

property.
If

true

and the button has a border,
the border is painted. The default value for the

borderPainted

property is

true

.

Some look and feels might not support
the

borderPainted

property,
in which case they ignore this.

**Parameters:**
- b

- if true and border property is not

null

,
the border is painted

**See Also:**
- isBorderPainted()

---

#### protected void paintBorder​(
Graphics
g)

Paint the button's border if

BorderPainted

property is true and the button has a border.

**Overrides:**
- paintBorder

in class

JComponent

**Parameters:**
- g

- the

Graphics

context in which to paint

**See Also:**
- JComponent.paint(java.awt.Graphics)

,

JComponent.setBorder(javax.swing.border.Border)

---

#### public boolean isFocusPainted()

Gets the

paintFocus

property.

**Returns:**
- the

paintFocus

property

**See Also:**
- setFocusPainted(boolean)

---

#### @BeanProperty
(
visualUpdate
=true,

description
="Whether focus should be painted")
public void setFocusPainted​(boolean b)

Sets the

paintFocus

property, which must
be

true

for the focus state to be painted.
The default value for the

paintFocus

property
is

true

.
Some look and feels might not paint focus state;
they will ignore this property.

**Parameters:**
- b

- if

true

, the focus state should be painted

**See Also:**
- isFocusPainted()

---

#### public boolean isContentAreaFilled()

Gets the

contentAreaFilled

property.

**Returns:**
- the

contentAreaFilled

property

**See Also:**
- setContentAreaFilled(boolean)

---

#### @BeanProperty
(
visualUpdate
=true,

description
="Whether the button should paint the content area or leave it transparent.")
public void setContentAreaFilled​(boolean b)

Sets the

contentAreaFilled

property.
If

true

the button will paint the content
area. If you wish to have a transparent button, such as
an icon only button, for example, then you should set
this to

false

. Do not call

setOpaque(false)

.
The default value for the

contentAreaFilled

property is

true

.

This function may cause the component's opaque property to change.

The exact behavior of calling this function varies on a
component-by-component and L&F-by-L&F basis.

**Parameters:**
- b

- if true, the content should be filled; if false
the content area is not filled

**See Also:**
- isContentAreaFilled()

,

JComponent.setOpaque(boolean)

---

#### public boolean isRolloverEnabled()

Gets the

rolloverEnabled

property.

**Returns:**
- the value of the

rolloverEnabled

property

**See Also:**
- setRolloverEnabled(boolean)

---

#### @BeanProperty
(
visualUpdate
=true,

description
="Whether rollover effects should be enabled.")
public void setRolloverEnabled​(boolean b)

Sets the

rolloverEnabled

property, which
must be

true

for rollover effects to occur.
The default value for the

rolloverEnabled

property is

false

.
Some look and feels might not implement rollover effects;
they will ignore this property.

**Parameters:**
- b

- if

true

, rollover effects should be painted

**See Also:**
- isRolloverEnabled()

---

#### public int getMnemonic()

Returns the keyboard mnemonic from the current model.

**Returns:**
- the keyboard mnemonic from the model

---

#### @BeanProperty
(
visualUpdate
=true,

description
="the keyboard character mnemonic")
public void setMnemonic​(int mnemonic)

Sets the keyboard mnemonic on the current model.
The mnemonic is the key which when combined with the look and feel's
mouseless modifier (usually Alt) will activate this button
if focus is contained somewhere within this button's ancestor
window.

A mnemonic must correspond to a single key on the keyboard
and should be specified using one of the

VK_XXX

keycodes defined in

java.awt.event.KeyEvent

.
These codes and the wider array of codes for international
keyboards may be obtained through

java.awt.event.KeyEvent.getExtendedKeyCodeForChar

.
Mnemonics are case-insensitive, therefore a key event
with the corresponding keycode would cause the button to be
activated whether or not the Shift modifier was pressed.

If the character defined by the mnemonic is found within
the button's label string, the first occurrence of it
will be underlined to indicate the mnemonic to the user.

**Parameters:**
- mnemonic

- the key code which represents the mnemonic

**See Also:**
- KeyEvent

,

setDisplayedMnemonicIndex(int)

---

#### @BeanProperty
(
visualUpdate
=true,

description
="the keyboard character mnemonic")
public void setMnemonic​(char mnemonic)

This method is now obsolete, please use

setMnemonic(int)

to set the mnemonic for a button. This method is only designed
to handle character values which fall between 'a' and 'z' or
'A' and 'Z'.

**Parameters:**
- mnemonic

- a char specifying the mnemonic value

**See Also:**
- setMnemonic(int)

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

setMnemonic(KeyEvent.VK_A)

.

**Parameters:**
- index

- Index into the String to underline

**Throws:**
- IllegalArgumentException

- will be thrown if

index

is >= length of the text, or < -1

**See Also:**
- getDisplayedMnemonicIndex()

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

#### public void setMultiClickThreshhold​(long threshhold)

Sets the amount of time (in milliseconds) required between
mouse press events for the button to generate the corresponding
action events. After the initial mouse press occurs (and action
event generated) any subsequent mouse press events which occur
on intervals less than the threshhold will be ignored and no
corresponding action event generated. By default the threshhold is 0,
which means that for each mouse press, an action event will be
fired, no matter how quickly the mouse clicks occur. In buttons
where this behavior is not desirable (for example, the "OK" button
in a dialog), this threshhold should be set to an appropriate
positive value.

**Parameters:**
- threshhold

- the amount of time required between mouse
press events to generate corresponding action events

**Throws:**
- IllegalArgumentException

- if threshhold < 0

**See Also:**
- getMultiClickThreshhold()

**Since:**
- 1.4

---

#### public long getMultiClickThreshhold()

Gets the amount of time (in milliseconds) required between
mouse press events for the button to generate the corresponding
action events.

**Returns:**
- the amount of time required between mouse press events
to generate corresponding action events

**See Also:**
- setMultiClickThreshhold(long)

**Since:**
- 1.4

---

#### public
ButtonModel
getModel()

Returns the model that this button represents.

**Returns:**
- the

model

property

**See Also:**
- setModel(javax.swing.ButtonModel)

---

#### @BeanProperty
(
description
="Model that the Button uses.")
public void setModel​(
ButtonModel
newModel)

Sets the model that this button represents.

**Parameters:**
- newModel

- the new

ButtonModel

**See Also:**
- getModel()

---

#### public
ButtonUI
getUI()

Returns the L&F object that renders this component.

**Overrides:**
- getUI

in class

JComponent

**Returns:**
- the ButtonUI object

**See Also:**
- setUI(javax.swing.plaf.ButtonUI)

---

#### @BeanProperty
(
hidden
=true,

visualUpdate
=true,

description
="The UI object that implements the LookAndFeel.")
public void setUI​(
ButtonUI
ui)

Sets the L&F object that renders this component.

**Parameters:**
- ui

- the

ButtonUI

L&F object

**See Also:**
- getUI()

---

#### public void updateUI()

Resets the UI property to a value from the current look
and feel. Subtypes of

AbstractButton

should override this to update the UI. For
example,

JButton

might do the following:

```java
setUI((ButtonUI)UIManager.getUI(
"ButtonUI", "javax.swing.plaf.basic.BasicButtonUI", this));
```

**Overrides:**
- updateUI

in class

JComponent

**See Also:**
- JComponent.setUI(javax.swing.plaf.ComponentUI)

,

UIManager.getLookAndFeel()

,

UIManager.getUI(javax.swing.JComponent)

---

#### protected void addImpl​(
Component
comp,

Object
constraints,
int index)

Adds the specified component to this container at the specified
index, refer to

Container.addImpl(Component, Object, int)

for a complete description of this method.

**Overrides:**
- addImpl

in class

Container

**Parameters:**
- comp

- the component to be added
- constraints

- an object expressing layout constraints
for this component
- index

- the position in the container's list at which to
insert the component, where

-1

means append to the end

**Throws:**
- IllegalArgumentException

- if

index

is invalid
- IllegalArgumentException

- if adding the container's parent
to itself
- IllegalArgumentException

- if adding a window to a container

**See Also:**
- Container.add(Component)

,

Container.add(Component, int)

,

Container.add(Component, java.lang.Object)

,

Container.invalidate()

,

LayoutManager

,

LayoutManager2

**Since:**
- 1.5

---

#### public void setLayout​(
LayoutManager
mgr)

Sets the layout manager for this container, refer to

Container.setLayout(LayoutManager)

for a complete description of this method.

**Overrides:**
- setLayout

in class

Container

**Parameters:**
- mgr

- the specified layout manager

**See Also:**
- Container.doLayout()

,

Container.getLayout()

,

Container.invalidate()

**Since:**
- 1.5

---

#### public void addChangeListener​(
ChangeListener
l)

Adds a

ChangeListener

to the button.

**Parameters:**
- l

- the listener to be added

---

#### public void removeChangeListener​(
ChangeListener
l)

Removes a ChangeListener from the button.

**Parameters:**
- l

- the listener to be removed

---

#### @BeanProperty
(
bound
=false)
public
ChangeListener
[] getChangeListeners()

Returns an array of all the

ChangeListener

s added
to this AbstractButton with addChangeListener().

**Returns:**
- all of the

ChangeListener

s added or an empty
array if no listeners have been added

**Since:**
- 1.4

---

#### protected void fireStateChanged()

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created.

**See Also:**
- EventListenerList

---

#### public void addActionListener​(
ActionListener
l)

Adds an

ActionListener

to the button.

**Parameters:**
- l

- the

ActionListener

to be added

---

#### public void removeActionListener​(
ActionListener
l)

Removes an

ActionListener

from the button.
If the listener is the currently set

Action

for the button, then the

Action

is set to

null

.

**Parameters:**
- l

- the listener to be removed

---

#### @BeanProperty
(
bound
=false)
public
ActionListener
[] getActionListeners()

Returns an array of all the

ActionListener

s added
to this AbstractButton with addActionListener().

**Returns:**
- all of the

ActionListener

s added or an empty
array if no listeners have been added

**Since:**
- 1.4

---

#### protected
ChangeListener
createChangeListener()

Subclasses that want to handle

ChangeEvents

differently
can override this to return another

ChangeListener

implementation.

**Returns:**
- the new

ChangeListener

---

#### protected void fireActionPerformed​(
ActionEvent
event)

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the

event

parameter.

**Parameters:**
- event

- the

ActionEvent

object

**See Also:**
- EventListenerList

---

#### protected void fireItemStateChanged​(
ItemEvent
event)

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the

event

parameter.

**Parameters:**
- event

- the

ItemEvent

object

**See Also:**
- EventListenerList

---

#### protected
ActionListener
createActionListener()

Returns

ActionListener

that is added to model.

**Returns:**
- the

ActionListener

---

#### protected
ItemListener
createItemListener()

Returns

ItemListener

that is added to model.

**Returns:**
- the

ItemListener

---

#### public void setEnabled​(boolean b)

Enables (or disables) the button.

**Overrides:**
- setEnabled

in class

JComponent

**Parameters:**
- b

- true to enable the button, otherwise false

**See Also:**
- Component.isEnabled()

,

Component.isLightweight()

---

#### @Deprecated

public
String
getLabel()

Returns the label text.

**Returns:**
- a

String

containing the label

---

#### @Deprecated

@BeanProperty
(
description
="Replace by setText(text)")
public void setLabel​(
String
label)

Sets the label text.

**Parameters:**
- label

- a

String

containing the text

---

#### public void addItemListener​(
ItemListener
l)

Adds an

ItemListener

to the

checkbox

.

**Specified by:**
- addItemListener

in interface

ItemSelectable

**Parameters:**
- l

- the

ItemListener

to be added

**See Also:**
- ItemEvent

---

#### public void removeItemListener​(
ItemListener
l)

Removes an

ItemListener

from the button.

**Specified by:**
- removeItemListener

in interface

ItemSelectable

**Parameters:**
- l

- the

ItemListener

to be removed

**See Also:**
- ItemEvent

---

#### @BeanProperty
(
bound
=false)
public
ItemListener
[] getItemListeners()

Returns an array of all the

ItemListener

s added
to this AbstractButton with addItemListener().

**Returns:**
- all of the

ItemListener

s added or an empty
array if no listeners have been added

**Since:**
- 1.4

---

#### @BeanProperty
(
bound
=false)
public
Object
[] getSelectedObjects()

Returns an array (length 1) containing the label or

null

if the button is not selected.

**Specified by:**
- getSelectedObjects

in interface

ItemSelectable

**Returns:**
- an array containing 1 Object: the text of the button,
if the item is selected; otherwise

null

---

#### protected void init​(
String
text,

Icon
icon)

Initialization of the

AbstractButton

.

**Parameters:**
- text

- the text of the button
- icon

- the Icon image to display on the button

---

#### public boolean imageUpdate​(
Image
img,
int infoflags,
int x,
int y,
int w,
int h)

This is overridden to return false if the current

Icon

's

Image

is not equal to the
passed in

Image

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

- the

Image

to be compared
- infoflags

- flags used to repaint the button when the image
is updated and which determine how much is to be painted
- x

- the x coordinate
- y

- the y coordinate
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

Returns a string representation of this

AbstractButton

.
This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

Overriding

paramString

to provide information about the
specific new aspects of the JFC components.

**Overrides:**
- paramString

in class

JComponent

**Returns:**
- a string representation of this

AbstractButton

---

### Additional Sections

#### Class AbstractButton

java.lang.Object

- java.awt.Component
- - java.awt.Container
- - javax.swing.JComponent
- - javax.swing.AbstractButton

java.awt.Component

- java.awt.Container
- - javax.swing.JComponent
- - javax.swing.AbstractButton

java.awt.Container

- javax.swing.JComponent
- - javax.swing.AbstractButton

javax.swing.JComponent

- javax.swing.AbstractButton

javax.swing.AbstractButton

**All Implemented Interfaces:** ImageObserver

,

ItemSelectable

,

MenuContainer

,

Serializable

,

SwingConstants

**Direct Known Subclasses:** JButton

,

JMenuItem

,

JToggleButton

```java
@JavaBean
(
defaultProperty
="UI")
public abstract class
AbstractButton

extends
JComponent

implements
ItemSelectable
,
SwingConstants
```

Defines common behaviors for buttons and menu items.

Buttons can be configured, and to some degree controlled, by

Action

s. Using an

Action

with a button has many benefits beyond directly
configuring a button. Refer to

Swing Components Supporting

Action

for more
details, and you can find more information in

How
to Use Actions

, a section in

The Java Tutorial

.

For further information see

How to Use Buttons, Check Boxes, and Radio Buttons

,
a section in

The Java Tutorial

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

="UI")
public abstract class

AbstractButton

extends

JComponent

implements

ItemSelectable

,

SwingConstants

Defines common behaviors for buttons and menu items.

Buttons can be configured, and to some degree controlled, by

Action

s. Using an

Action

with a button has many benefits beyond directly
configuring a button. Refer to

Swing Components Supporting

Action

for more
details, and you can find more information in

How
to Use Actions

, a section in

The Java Tutorial

.

For further information see

How to Use Buttons, Check Boxes, and Radio Buttons

,
a section in

The Java Tutorial

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

Buttons can be configured, and to some degree controlled, by

Action

s. Using an

Action

with a button has many benefits beyond directly
configuring a button. Refer to

Swing Components Supporting

Action

for more
details, and you can find more information in

How
to Use Actions

, a section in

The Java Tutorial

.

For further information see

How to Use Buttons, Check Boxes, and Radio Buttons

,
a section in

The Java Tutorial

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

For further information see

How to Use Buttons, Check Boxes, and Radio Buttons

,
a section in

The Java Tutorial

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

AbstractButton.AccessibleAbstractButton

This class implements accessibility support for the

AbstractButton

class.

protected class

AbstractButton.ButtonChangeListener

Extends

ChangeListener

to be serializable.

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

ActionListener

actionListener

The button model's

ActionListener

.

static

String

BORDER_PAINTED_CHANGED_PROPERTY

Identifies a change to having the border drawn,
or having it not drawn.

protected

ChangeEvent

changeEvent

Only one

ChangeEvent

is needed per button
instance since the
event's only state is the source property.

protected

ChangeListener

changeListener

The button model's

changeListener

.

static

String

CONTENT_AREA_FILLED_CHANGED_PROPERTY

Identifies a change to having the button paint the content area.

static

String

DISABLED_ICON_CHANGED_PROPERTY

Identifies a change to the icon used when the button has
been disabled.

static

String

DISABLED_SELECTED_ICON_CHANGED_PROPERTY

Identifies a change to the icon used when the button has been
disabled and selected.

static

String

FOCUS_PAINTED_CHANGED_PROPERTY

Identifies a change to having the border highlighted when focused,
or not.

static

String

HORIZONTAL_ALIGNMENT_CHANGED_PROPERTY

Identifies a change in the button's horizontal alignment.

static

String

HORIZONTAL_TEXT_POSITION_CHANGED_PROPERTY

Identifies a change in the button's horizontal text position.

static

String

ICON_CHANGED_PROPERTY

Identifies a change to the icon that represents the button.

protected

ItemListener

itemListener

The button model's

ItemListener

.

static

String

MARGIN_CHANGED_PROPERTY

Identifies a change in the button's margins.

static

String

MNEMONIC_CHANGED_PROPERTY

Identifies a change to the button's mnemonic.

protected

ButtonModel

model

The data model that determines the button's state.

static

String

MODEL_CHANGED_PROPERTY

Identifies a change in the button model.

static

String

PRESSED_ICON_CHANGED_PROPERTY

Identifies a change to the icon used when the button has been
pressed.

static

String

ROLLOVER_ENABLED_CHANGED_PROPERTY

Identifies a change from rollover enabled to disabled or back
to enabled.

static

String

ROLLOVER_ICON_CHANGED_PROPERTY

Identifies a change to the icon used when the cursor is over
the button.

static

String

ROLLOVER_SELECTED_ICON_CHANGED_PROPERTY

Identifies a change to the icon used when the cursor is
over the button and it has been selected.

static

String

SELECTED_ICON_CHANGED_PROPERTY

Identifies a change to the icon used when the button has
been selected.

static

String

TEXT_CHANGED_PROPERTY

Identifies a change in the button's text.

static

String

VERTICAL_ALIGNMENT_CHANGED_PROPERTY

Identifies a change in the button's vertical alignment.

static

String

VERTICAL_TEXT_POSITION_CHANGED_PROPERTY

Identifies a change in the button's vertical text position.

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

AbstractButton

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

protected void

actionPropertyChanged

​(

Action

action,

String

propertyName)

Updates the button's state in response to property changes in the
associated action.

void

addActionListener

​(

ActionListener

l)

Adds an

ActionListener

to the button.

void

addChangeListener

​(

ChangeListener

l)

Adds a

ChangeListener

to the button.

protected void

addImpl

​(

Component

comp,

Object

constraints,
int index)

Adds the specified component to this container at the specified
index, refer to

Container.addImpl(Component, Object, int)

for a complete description of this method.

void

addItemListener

​(

ItemListener

l)

Adds an

ItemListener

to the

checkbox

.

protected int

checkHorizontalKey

​(int key,

String

exception)

Verify that the

key

argument is a legal value for the

horizontalAlignment

and

horizontalTextPosition

properties.

protected int

checkVerticalKey

​(int key,

String

exception)

Verify that the

key

argument is a legal value for the
vertical properties.

protected void

configurePropertiesFromAction

​(

Action

a)

Sets the properties on this button to match those in the specified

Action

.

protected

ActionListener

createActionListener

()

Returns

ActionListener

that is added to model.

protected

PropertyChangeListener

createActionPropertyChangeListener

​(

Action

a)

Creates and returns a

PropertyChangeListener

that is
responsible for listening for changes from the specified

Action

and updating the appropriate properties.

protected

ChangeListener

createChangeListener

()

Subclasses that want to handle

ChangeEvents

differently
can override this to return another

ChangeListener

implementation.

protected

ItemListener

createItemListener

()

Returns

ItemListener

that is added to model.

void

doClick

()

Programmatically perform a "click".

void

doClick

​(int pressTime)

Programmatically perform a "click".

protected void

fireActionPerformed

​(

ActionEvent

event)

Notifies all listeners that have registered interest for
notification on this event type.

protected void

fireItemStateChanged

​(

ItemEvent

event)

Notifies all listeners that have registered interest for
notification on this event type.

protected void

fireStateChanged

()

Notifies all listeners that have registered interest for
notification on this event type.

Action

getAction

()

Returns the currently set

Action

for this

ActionEvent

source, or

null

if no

Action

is set.

String

getActionCommand

()

Returns the action command for this button.

ActionListener

[]

getActionListeners

()

Returns an array of all the

ActionListener

s added
to this AbstractButton with addActionListener().

ChangeListener

[]

getChangeListeners

()

Returns an array of all the

ChangeListener

s added
to this AbstractButton with addChangeListener().

Icon

getDisabledIcon

()

Returns the icon used by the button when it's disabled.

Icon

getDisabledSelectedIcon

()

Returns the icon used by the button when it's disabled and selected.

int

getDisplayedMnemonicIndex

()

Returns the character, as an index, that the look and feel should
provide decoration for as representing the mnemonic character.

boolean

getHideActionText

()

Returns the value of the

hideActionText

property, which
determines whether the button displays text from the

Action

.

int

getHorizontalAlignment

()

Returns the horizontal alignment of the icon and text.

int

getHorizontalTextPosition

()

Returns the horizontal position of the text relative to the icon.

Icon

getIcon

()

Returns the default icon.

int

getIconTextGap

()

Returns the amount of space between the text and the icon
displayed in this button.

ItemListener

[]

getItemListeners

()

Returns an array of all the

ItemListener

s added
to this AbstractButton with addItemListener().

String

getLabel

()

Deprecated.

- Replaced by

getText

Insets

getMargin

()

Returns the margin between the button's border and
the label.

int

getMnemonic

()

Returns the keyboard mnemonic from the current model.

ButtonModel

getModel

()

Returns the model that this button represents.

long

getMultiClickThreshhold

()

Gets the amount of time (in milliseconds) required between
mouse press events for the button to generate the corresponding
action events.

Icon

getPressedIcon

()

Returns the pressed icon for the button.

Icon

getRolloverIcon

()

Returns the rollover icon for the button.

Icon

getRolloverSelectedIcon

()

Returns the rollover selection icon for the button.

Icon

getSelectedIcon

()

Returns the selected icon for the button.

Object

[]

getSelectedObjects

()

Returns an array (length 1) containing the label or

null

if the button is not selected.

String

getText

()

Returns the button's text.

ButtonUI

getUI

()

Returns the L&F object that renders this component.

int

getVerticalAlignment

()

Returns the vertical alignment of the text and icon.

int

getVerticalTextPosition

()

Returns the vertical position of the text relative to the icon.

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

This is overridden to return false if the current

Icon

's

Image

is not equal to the
passed in

Image

img

.

protected void

init

​(

String

text,

Icon

icon)

Initialization of the

AbstractButton

.

boolean

isBorderPainted

()

Gets the

borderPainted

property.

boolean

isContentAreaFilled

()

Gets the

contentAreaFilled

property.

boolean

isFocusPainted

()

Gets the

paintFocus

property.

boolean

isRolloverEnabled

()

Gets the

rolloverEnabled

property.

boolean

isSelected

()

Returns the state of the button.

protected void

paintBorder

​(

Graphics

g)

Paint the button's border if

BorderPainted

property is true and the button has a border.

protected

String

paramString

()

Returns a string representation of this

AbstractButton

.

void

removeActionListener

​(

ActionListener

l)

Removes an

ActionListener

from the button.

void

removeChangeListener

​(

ChangeListener

l)

Removes a ChangeListener from the button.

void

removeItemListener

​(

ItemListener

l)

Removes an

ItemListener

from the button.

void

removeNotify

()

Notifies this component that it no longer has a parent component.

void

setAction

​(

Action

a)

Sets the

Action

.

void

setActionCommand

​(

String

actionCommand)

Sets the action command for this button.

void

setBorderPainted

​(boolean b)

Sets the

borderPainted

property.

void

setContentAreaFilled

​(boolean b)

Sets the

contentAreaFilled

property.

void

setDisabledIcon

​(

Icon

disabledIcon)

Sets the disabled icon for the button.

void

setDisabledSelectedIcon

​(

Icon

disabledSelectedIcon)

Sets the disabled selection icon for the button.

void

setDisplayedMnemonicIndex

​(int index)

Provides a hint to the look and feel as to which character in the
text should be decorated to represent the mnemonic.

void

setEnabled

​(boolean b)

Enables (or disables) the button.

void

setFocusPainted

​(boolean b)

Sets the

paintFocus

property, which must
be

true

for the focus state to be painted.

void

setHideActionText

​(boolean hideActionText)

Sets the

hideActionText

property, which determines
whether the button displays text from the

Action

.

void

setHorizontalAlignment

​(int alignment)

Sets the horizontal alignment of the icon and text.

void

setHorizontalTextPosition

​(int textPosition)

Sets the horizontal position of the text relative to the icon.

void

setIcon

​(

Icon

defaultIcon)

Sets the button's default icon.

void

setIconTextGap

​(int iconTextGap)

If both the icon and text properties are set, this property
defines the space between them.

void

setLabel

​(

String

label)

Deprecated.

- Replaced by

setText(text)

void

setLayout

​(

LayoutManager

mgr)

Sets the layout manager for this container, refer to

Container.setLayout(LayoutManager)

for a complete description of this method.

void

setMargin

​(

Insets

m)

Sets space for margin between the button's border and
the label.

void

setMnemonic

​(char mnemonic)

This method is now obsolete, please use

setMnemonic(int)

to set the mnemonic for a button.

void

setMnemonic

​(int mnemonic)

Sets the keyboard mnemonic on the current model.

void

setModel

​(

ButtonModel

newModel)

Sets the model that this button represents.

void

setMultiClickThreshhold

​(long threshhold)

Sets the amount of time (in milliseconds) required between
mouse press events for the button to generate the corresponding
action events.

void

setPressedIcon

​(

Icon

pressedIcon)

Sets the pressed icon for the button.

void

setRolloverEnabled

​(boolean b)

Sets the

rolloverEnabled

property, which
must be

true

for rollover effects to occur.

void

setRolloverIcon

​(

Icon

rolloverIcon)

Sets the rollover icon for the button.

void

setRolloverSelectedIcon

​(

Icon

rolloverSelectedIcon)

Sets the rollover selected icon for the button.

void

setSelected

​(boolean b)

Sets the state of the button.

void

setSelectedIcon

​(

Icon

selectedIcon)

Sets the selected icon for the button.

void

setText

​(

String

text)

Sets the button's text.

void

setUI

​(

ButtonUI

ui)

Sets the L&F object that renders this component.

void

setVerticalAlignment

​(int alignment)

Sets the vertical alignment of the icon and text.

void

setVerticalTextPosition

​(int textPosition)

Sets the vertical position of the text relative to the icon.

void

updateUI

()

Resets the UI property to a value from the current look
and feel.

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

getUIClassID

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

getAccessibleContext

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

AbstractButton.AccessibleAbstractButton

This class implements accessibility support for the

AbstractButton

class.

protected class

AbstractButton.ButtonChangeListener

Extends

ChangeListener

to be serializable.

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

This class implements accessibility support for the

AbstractButton

class.

Extends

ChangeListener

to be serializable.

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

ActionListener

actionListener

The button model's

ActionListener

.

static

String

BORDER_PAINTED_CHANGED_PROPERTY

Identifies a change to having the border drawn,
or having it not drawn.

protected

ChangeEvent

changeEvent

Only one

ChangeEvent

is needed per button
instance since the
event's only state is the source property.

protected

ChangeListener

changeListener

The button model's

changeListener

.

static

String

CONTENT_AREA_FILLED_CHANGED_PROPERTY

Identifies a change to having the button paint the content area.

static

String

DISABLED_ICON_CHANGED_PROPERTY

Identifies a change to the icon used when the button has
been disabled.

static

String

DISABLED_SELECTED_ICON_CHANGED_PROPERTY

Identifies a change to the icon used when the button has been
disabled and selected.

static

String

FOCUS_PAINTED_CHANGED_PROPERTY

Identifies a change to having the border highlighted when focused,
or not.

static

String

HORIZONTAL_ALIGNMENT_CHANGED_PROPERTY

Identifies a change in the button's horizontal alignment.

static

String

HORIZONTAL_TEXT_POSITION_CHANGED_PROPERTY

Identifies a change in the button's horizontal text position.

static

String

ICON_CHANGED_PROPERTY

Identifies a change to the icon that represents the button.

protected

ItemListener

itemListener

The button model's

ItemListener

.

static

String

MARGIN_CHANGED_PROPERTY

Identifies a change in the button's margins.

static

String

MNEMONIC_CHANGED_PROPERTY

Identifies a change to the button's mnemonic.

protected

ButtonModel

model

The data model that determines the button's state.

static

String

MODEL_CHANGED_PROPERTY

Identifies a change in the button model.

static

String

PRESSED_ICON_CHANGED_PROPERTY

Identifies a change to the icon used when the button has been
pressed.

static

String

ROLLOVER_ENABLED_CHANGED_PROPERTY

Identifies a change from rollover enabled to disabled or back
to enabled.

static

String

ROLLOVER_ICON_CHANGED_PROPERTY

Identifies a change to the icon used when the cursor is over
the button.

static

String

ROLLOVER_SELECTED_ICON_CHANGED_PROPERTY

Identifies a change to the icon used when the cursor is
over the button and it has been selected.

static

String

SELECTED_ICON_CHANGED_PROPERTY

Identifies a change to the icon used when the button has
been selected.

static

String

TEXT_CHANGED_PROPERTY

Identifies a change in the button's text.

static

String

VERTICAL_ALIGNMENT_CHANGED_PROPERTY

Identifies a change in the button's vertical alignment.

static

String

VERTICAL_TEXT_POSITION_CHANGED_PROPERTY

Identifies a change in the button's vertical text position.

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

The button model's

ActionListener

.

Identifies a change to having the border drawn,
or having it not drawn.

Only one

ChangeEvent

is needed per button
instance since the
event's only state is the source property.

The button model's

changeListener

.

Identifies a change to having the button paint the content area.

Identifies a change to the icon used when the button has
been disabled.

Identifies a change to the icon used when the button has been
disabled and selected.

Identifies a change to having the border highlighted when focused,
or not.

Identifies a change in the button's horizontal alignment.

Identifies a change in the button's horizontal text position.

Identifies a change to the icon that represents the button.

The button model's

ItemListener

.

Identifies a change in the button's margins.

Identifies a change to the button's mnemonic.

The data model that determines the button's state.

Identifies a change in the button model.

Identifies a change to the icon used when the button has been
pressed.

Identifies a change from rollover enabled to disabled or back
to enabled.

Identifies a change to the icon used when the cursor is over
the button.

Identifies a change to the icon used when the cursor is
over the button and it has been selected.

Identifies a change to the icon used when the button has
been selected.

Identifies a change in the button's text.

Identifies a change in the button's vertical alignment.

Identifies a change in the button's vertical text position.

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

AbstractButton

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

protected void

actionPropertyChanged

​(

Action

action,

String

propertyName)

Updates the button's state in response to property changes in the
associated action.

void

addActionListener

​(

ActionListener

l)

Adds an

ActionListener

to the button.

void

addChangeListener

​(

ChangeListener

l)

Adds a

ChangeListener

to the button.

protected void

addImpl

​(

Component

comp,

Object

constraints,
int index)

Adds the specified component to this container at the specified
index, refer to

Container.addImpl(Component, Object, int)

for a complete description of this method.

void

addItemListener

​(

ItemListener

l)

Adds an

ItemListener

to the

checkbox

.

protected int

checkHorizontalKey

​(int key,

String

exception)

Verify that the

key

argument is a legal value for the

horizontalAlignment

and

horizontalTextPosition

properties.

protected int

checkVerticalKey

​(int key,

String

exception)

Verify that the

key

argument is a legal value for the
vertical properties.

protected void

configurePropertiesFromAction

​(

Action

a)

Sets the properties on this button to match those in the specified

Action

.

protected

ActionListener

createActionListener

()

Returns

ActionListener

that is added to model.

protected

PropertyChangeListener

createActionPropertyChangeListener

​(

Action

a)

Creates and returns a

PropertyChangeListener

that is
responsible for listening for changes from the specified

Action

and updating the appropriate properties.

protected

ChangeListener

createChangeListener

()

Subclasses that want to handle

ChangeEvents

differently
can override this to return another

ChangeListener

implementation.

protected

ItemListener

createItemListener

()

Returns

ItemListener

that is added to model.

void

doClick

()

Programmatically perform a "click".

void

doClick

​(int pressTime)

Programmatically perform a "click".

protected void

fireActionPerformed

​(

ActionEvent

event)

Notifies all listeners that have registered interest for
notification on this event type.

protected void

fireItemStateChanged

​(

ItemEvent

event)

Notifies all listeners that have registered interest for
notification on this event type.

protected void

fireStateChanged

()

Notifies all listeners that have registered interest for
notification on this event type.

Action

getAction

()

Returns the currently set

Action

for this

ActionEvent

source, or

null

if no

Action

is set.

String

getActionCommand

()

Returns the action command for this button.

ActionListener

[]

getActionListeners

()

Returns an array of all the

ActionListener

s added
to this AbstractButton with addActionListener().

ChangeListener

[]

getChangeListeners

()

Returns an array of all the

ChangeListener

s added
to this AbstractButton with addChangeListener().

Icon

getDisabledIcon

()

Returns the icon used by the button when it's disabled.

Icon

getDisabledSelectedIcon

()

Returns the icon used by the button when it's disabled and selected.

int

getDisplayedMnemonicIndex

()

Returns the character, as an index, that the look and feel should
provide decoration for as representing the mnemonic character.

boolean

getHideActionText

()

Returns the value of the

hideActionText

property, which
determines whether the button displays text from the

Action

.

int

getHorizontalAlignment

()

Returns the horizontal alignment of the icon and text.

int

getHorizontalTextPosition

()

Returns the horizontal position of the text relative to the icon.

Icon

getIcon

()

Returns the default icon.

int

getIconTextGap

()

Returns the amount of space between the text and the icon
displayed in this button.

ItemListener

[]

getItemListeners

()

Returns an array of all the

ItemListener

s added
to this AbstractButton with addItemListener().

String

getLabel

()

Deprecated.

- Replaced by

getText

Insets

getMargin

()

Returns the margin between the button's border and
the label.

int

getMnemonic

()

Returns the keyboard mnemonic from the current model.

ButtonModel

getModel

()

Returns the model that this button represents.

long

getMultiClickThreshhold

()

Gets the amount of time (in milliseconds) required between
mouse press events for the button to generate the corresponding
action events.

Icon

getPressedIcon

()

Returns the pressed icon for the button.

Icon

getRolloverIcon

()

Returns the rollover icon for the button.

Icon

getRolloverSelectedIcon

()

Returns the rollover selection icon for the button.

Icon

getSelectedIcon

()

Returns the selected icon for the button.

Object

[]

getSelectedObjects

()

Returns an array (length 1) containing the label or

null

if the button is not selected.

String

getText

()

Returns the button's text.

ButtonUI

getUI

()

Returns the L&F object that renders this component.

int

getVerticalAlignment

()

Returns the vertical alignment of the text and icon.

int

getVerticalTextPosition

()

Returns the vertical position of the text relative to the icon.

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

This is overridden to return false if the current

Icon

's

Image

is not equal to the
passed in

Image

img

.

protected void

init

​(

String

text,

Icon

icon)

Initialization of the

AbstractButton

.

boolean

isBorderPainted

()

Gets the

borderPainted

property.

boolean

isContentAreaFilled

()

Gets the

contentAreaFilled

property.

boolean

isFocusPainted

()

Gets the

paintFocus

property.

boolean

isRolloverEnabled

()

Gets the

rolloverEnabled

property.

boolean

isSelected

()

Returns the state of the button.

protected void

paintBorder

​(

Graphics

g)

Paint the button's border if

BorderPainted

property is true and the button has a border.

protected

String

paramString

()

Returns a string representation of this

AbstractButton

.

void

removeActionListener

​(

ActionListener

l)

Removes an

ActionListener

from the button.

void

removeChangeListener

​(

ChangeListener

l)

Removes a ChangeListener from the button.

void

removeItemListener

​(

ItemListener

l)

Removes an

ItemListener

from the button.

void

removeNotify

()

Notifies this component that it no longer has a parent component.

void

setAction

​(

Action

a)

Sets the

Action

.

void

setActionCommand

​(

String

actionCommand)

Sets the action command for this button.

void

setBorderPainted

​(boolean b)

Sets the

borderPainted

property.

void

setContentAreaFilled

​(boolean b)

Sets the

contentAreaFilled

property.

void

setDisabledIcon

​(

Icon

disabledIcon)

Sets the disabled icon for the button.

void

setDisabledSelectedIcon

​(

Icon

disabledSelectedIcon)

Sets the disabled selection icon for the button.

void

setDisplayedMnemonicIndex

​(int index)

Provides a hint to the look and feel as to which character in the
text should be decorated to represent the mnemonic.

void

setEnabled

​(boolean b)

Enables (or disables) the button.

void

setFocusPainted

​(boolean b)

Sets the

paintFocus

property, which must
be

true

for the focus state to be painted.

void

setHideActionText

​(boolean hideActionText)

Sets the

hideActionText

property, which determines
whether the button displays text from the

Action

.

void

setHorizontalAlignment

​(int alignment)

Sets the horizontal alignment of the icon and text.

void

setHorizontalTextPosition

​(int textPosition)

Sets the horizontal position of the text relative to the icon.

void

setIcon

​(

Icon

defaultIcon)

Sets the button's default icon.

void

setIconTextGap

​(int iconTextGap)

If both the icon and text properties are set, this property
defines the space between them.

void

setLabel

​(

String

label)

Deprecated.

- Replaced by

setText(text)

void

setLayout

​(

LayoutManager

mgr)

Sets the layout manager for this container, refer to

Container.setLayout(LayoutManager)

for a complete description of this method.

void

setMargin

​(

Insets

m)

Sets space for margin between the button's border and
the label.

void

setMnemonic

​(char mnemonic)

This method is now obsolete, please use

setMnemonic(int)

to set the mnemonic for a button.

void

setMnemonic

​(int mnemonic)

Sets the keyboard mnemonic on the current model.

void

setModel

​(

ButtonModel

newModel)

Sets the model that this button represents.

void

setMultiClickThreshhold

​(long threshhold)

Sets the amount of time (in milliseconds) required between
mouse press events for the button to generate the corresponding
action events.

void

setPressedIcon

​(

Icon

pressedIcon)

Sets the pressed icon for the button.

void

setRolloverEnabled

​(boolean b)

Sets the

rolloverEnabled

property, which
must be

true

for rollover effects to occur.

void

setRolloverIcon

​(

Icon

rolloverIcon)

Sets the rollover icon for the button.

void

setRolloverSelectedIcon

​(

Icon

rolloverSelectedIcon)

Sets the rollover selected icon for the button.

void

setSelected

​(boolean b)

Sets the state of the button.

void

setSelectedIcon

​(

Icon

selectedIcon)

Sets the selected icon for the button.

void

setText

​(

String

text)

Sets the button's text.

void

setUI

​(

ButtonUI

ui)

Sets the L&F object that renders this component.

void

setVerticalAlignment

​(int alignment)

Sets the vertical alignment of the icon and text.

void

setVerticalTextPosition

​(int textPosition)

Sets the vertical position of the text relative to the icon.

void

updateUI

()

Resets the UI property to a value from the current look
and feel.

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

getUIClassID

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

getAccessibleContext

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

Updates the button's state in response to property changes in the
associated action.

Adds an

ActionListener

to the button.

Adds a

ChangeListener

to the button.

Adds the specified component to this container at the specified
index, refer to

Container.addImpl(Component, Object, int)

for a complete description of this method.

Adds an

ItemListener

to the

checkbox

.

Verify that the

key

argument is a legal value for the

horizontalAlignment

and

horizontalTextPosition

properties.

Verify that the

key

argument is a legal value for the
vertical properties.

Sets the properties on this button to match those in the specified

Action

.

Returns

ActionListener

that is added to model.

Creates and returns a

PropertyChangeListener

that is
responsible for listening for changes from the specified

Action

and updating the appropriate properties.

Subclasses that want to handle

ChangeEvents

differently
can override this to return another

ChangeListener

implementation.

Returns

ItemListener

that is added to model.

Programmatically perform a "click".

Notifies all listeners that have registered interest for
notification on this event type.

Returns the currently set

Action

for this

ActionEvent

source, or

null

if no

Action

is set.

Returns the action command for this button.

Returns an array of all the

ActionListener

s added
to this AbstractButton with addActionListener().

Returns an array of all the

ChangeListener

s added
to this AbstractButton with addChangeListener().

Returns the icon used by the button when it's disabled.

Returns the icon used by the button when it's disabled and selected.

Returns the character, as an index, that the look and feel should
provide decoration for as representing the mnemonic character.

Returns the value of the

hideActionText

property, which
determines whether the button displays text from the

Action

.

Returns the horizontal alignment of the icon and text.

Returns the horizontal position of the text relative to the icon.

Returns the default icon.

Returns the amount of space between the text and the icon
displayed in this button.

Returns an array of all the

ItemListener

s added
to this AbstractButton with addItemListener().

Deprecated.

- Replaced by

getText

Returns the margin between the button's border and
the label.

Returns the keyboard mnemonic from the current model.

Returns the model that this button represents.

Gets the amount of time (in milliseconds) required between
mouse press events for the button to generate the corresponding
action events.

Returns the pressed icon for the button.

Returns the rollover icon for the button.

Returns the rollover selection icon for the button.

Returns the selected icon for the button.

Returns an array (length 1) containing the label or

null

if the button is not selected.

Returns the button's text.

Returns the L&F object that renders this component.

Returns the vertical alignment of the text and icon.

Returns the vertical position of the text relative to the icon.

This is overridden to return false if the current

Icon

's

Image

is not equal to the
passed in

Image

img

.

Initialization of the

AbstractButton

.

Gets the

borderPainted

property.

Gets the

contentAreaFilled

property.

Gets the

paintFocus

property.

Gets the

rolloverEnabled

property.

Returns the state of the button.

Paint the button's border if

BorderPainted

property is true and the button has a border.

Returns a string representation of this

AbstractButton

.

Removes an

ActionListener

from the button.

Removes a ChangeListener from the button.

Removes an

ItemListener

from the button.

Notifies this component that it no longer has a parent component.

Sets the

Action

.

Sets the action command for this button.

Sets the

borderPainted

property.

Sets the

contentAreaFilled

property.

Sets the disabled icon for the button.

Sets the disabled selection icon for the button.

Provides a hint to the look and feel as to which character in the
text should be decorated to represent the mnemonic.

Enables (or disables) the button.

Sets the

paintFocus

property, which must
be

true

for the focus state to be painted.

Sets the

hideActionText

property, which determines
whether the button displays text from the

Action

.

Sets the horizontal alignment of the icon and text.

Sets the horizontal position of the text relative to the icon.

Sets the button's default icon.

If both the icon and text properties are set, this property
defines the space between them.

Deprecated.

- Replaced by

setText(text)

Sets the layout manager for this container, refer to

Container.setLayout(LayoutManager)

for a complete description of this method.

Sets space for margin between the button's border and
the label.

This method is now obsolete, please use

setMnemonic(int)

to set the mnemonic for a button.

Sets the keyboard mnemonic on the current model.

Sets the model that this button represents.

Sets the amount of time (in milliseconds) required between
mouse press events for the button to generate the corresponding
action events.

Sets the pressed icon for the button.

Sets the

rolloverEnabled

property, which
must be

true

for rollover effects to occur.

Sets the rollover icon for the button.

Sets the rollover selected icon for the button.

Sets the state of the button.

Sets the selected icon for the button.

Sets the button's text.

Sets the L&F object that renders this component.

Sets the vertical alignment of the icon and text.

Sets the vertical position of the text relative to the icon.

Resets the UI property to a value from the current look
and feel.

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

getUIClassID

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

getAccessibleContext

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

- MODEL_CHANGED_PROPERTY

```java
public static final
String
MODEL_CHANGED_PROPERTY
```

Identifies a change in the button model.

**See Also:** Constant Field Values

- TEXT_CHANGED_PROPERTY

```java
public static final
String
TEXT_CHANGED_PROPERTY
```

Identifies a change in the button's text.

**See Also:** Constant Field Values

- MNEMONIC_CHANGED_PROPERTY

```java
public static final
String
MNEMONIC_CHANGED_PROPERTY
```

Identifies a change to the button's mnemonic.

**See Also:** Constant Field Values

- MARGIN_CHANGED_PROPERTY

```java
public static final
String
MARGIN_CHANGED_PROPERTY
```

Identifies a change in the button's margins.

**See Also:** Constant Field Values

- VERTICAL_ALIGNMENT_CHANGED_PROPERTY

```java
public static final
String
VERTICAL_ALIGNMENT_CHANGED_PROPERTY
```

Identifies a change in the button's vertical alignment.

**See Also:** Constant Field Values

- HORIZONTAL_ALIGNMENT_CHANGED_PROPERTY

```java
public static final
String
HORIZONTAL_ALIGNMENT_CHANGED_PROPERTY
```

Identifies a change in the button's horizontal alignment.

**See Also:** Constant Field Values

- VERTICAL_TEXT_POSITION_CHANGED_PROPERTY

```java
public static final
String
VERTICAL_TEXT_POSITION_CHANGED_PROPERTY
```

Identifies a change in the button's vertical text position.

**See Also:** Constant Field Values

- HORIZONTAL_TEXT_POSITION_CHANGED_PROPERTY

```java
public static final
String
HORIZONTAL_TEXT_POSITION_CHANGED_PROPERTY
```

Identifies a change in the button's horizontal text position.

**See Also:** Constant Field Values

- BORDER_PAINTED_CHANGED_PROPERTY

```java
public static final
String
BORDER_PAINTED_CHANGED_PROPERTY
```

Identifies a change to having the border drawn,
or having it not drawn.

**See Also:** Constant Field Values

- FOCUS_PAINTED_CHANGED_PROPERTY

```java
public static final
String
FOCUS_PAINTED_CHANGED_PROPERTY
```

Identifies a change to having the border highlighted when focused,
or not.

**See Also:** Constant Field Values

- ROLLOVER_ENABLED_CHANGED_PROPERTY

```java
public static final
String
ROLLOVER_ENABLED_CHANGED_PROPERTY
```

Identifies a change from rollover enabled to disabled or back
to enabled.

**See Also:** Constant Field Values

- CONTENT_AREA_FILLED_CHANGED_PROPERTY

```java
public static final
String
CONTENT_AREA_FILLED_CHANGED_PROPERTY
```

Identifies a change to having the button paint the content area.

**See Also:** Constant Field Values

- ICON_CHANGED_PROPERTY

```java
public static final
String
ICON_CHANGED_PROPERTY
```

Identifies a change to the icon that represents the button.

**See Also:** Constant Field Values

- PRESSED_ICON_CHANGED_PROPERTY

```java
public static final
String
PRESSED_ICON_CHANGED_PROPERTY
```

Identifies a change to the icon used when the button has been
pressed.

**See Also:** Constant Field Values

- SELECTED_ICON_CHANGED_PROPERTY

```java
public static final
String
SELECTED_ICON_CHANGED_PROPERTY
```

Identifies a change to the icon used when the button has
been selected.

**See Also:** Constant Field Values

- ROLLOVER_ICON_CHANGED_PROPERTY

```java
public static final
String
ROLLOVER_ICON_CHANGED_PROPERTY
```

Identifies a change to the icon used when the cursor is over
the button.

**See Also:** Constant Field Values

- ROLLOVER_SELECTED_ICON_CHANGED_PROPERTY

```java
public static final
String
ROLLOVER_SELECTED_ICON_CHANGED_PROPERTY
```

Identifies a change to the icon used when the cursor is
over the button and it has been selected.

**See Also:** Constant Field Values

- DISABLED_ICON_CHANGED_PROPERTY

```java
public static final
String
DISABLED_ICON_CHANGED_PROPERTY
```

Identifies a change to the icon used when the button has
been disabled.

**See Also:** Constant Field Values

- DISABLED_SELECTED_ICON_CHANGED_PROPERTY

```java
public static final
String
DISABLED_SELECTED_ICON_CHANGED_PROPERTY
```

Identifies a change to the icon used when the button has been
disabled and selected.

**See Also:** Constant Field Values

- model

```java
protected
ButtonModel
model
```

The data model that determines the button's state.

- changeListener

```java
protected
ChangeListener
changeListener
```

The button model's

changeListener

.

- actionListener

```java
protected
ActionListener
actionListener
```

The button model's

ActionListener

.

- itemListener

```java
protected
ItemListener
itemListener
```

The button model's

ItemListener

.

- changeEvent

```java
protected transient
ChangeEvent
changeEvent
```

Only one

ChangeEvent

is needed per button
instance since the
event's only state is the source property. The source of events
generated is always "this".

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AbstractButton

```java
public AbstractButton()
```

============ METHOD DETAIL ==========

- Method Detail

- setHideActionText

```java
@BeanProperty
(
expert
=true,

description
="Whether the text of the button should come from the <code>Action</code>.")
public void setHideActionText​(boolean hideActionText)
```

Sets the

hideActionText

property, which determines
whether the button displays text from the

Action

.
This is useful only if an

Action

has been
installed on the button.

**Parameters:** hideActionText

-

true

if the button's

text

property should not reflect
that of the

Action

; the default is

false
**Since:** 1.6
**See Also:** Swing Components Supporting

Action

- getHideActionText

```java
public boolean getHideActionText()
```

Returns the value of the

hideActionText

property, which
determines whether the button displays text from the

Action

. This is useful only if an

Action

has been installed on the button.

**Returns:** true

if the button's

text

property should not reflect that of the

Action

; the default is

false
**Since:** 1.6

- getText

```java
public
String
getText()
```

Returns the button's text.

**Returns:** the buttons text
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
="The button\'s text.")
public void setText​(
String
text)
```

Sets the button's text.

**Parameters:** text

- the string used to set the text
**See Also:** getText()

- isSelected

```java
public boolean isSelected()
```

Returns the state of the button. True if the
toggle button is selected, false if it's not.

**Returns:** true if the toggle button is selected, otherwise false

- setSelected

```java
public void setSelected​(boolean b)
```

Sets the state of the button. Note that this method does not
trigger an

actionEvent

.
Call

doClick

to perform a programmatic action change.

**Parameters:** b

- true if the button is selected, otherwise false

- doClick

```java
public void doClick()
```

Programmatically perform a "click". This does the same
thing as if the user had pressed and released the button.

- doClick

```java
public void doClick​(int pressTime)
```

Programmatically perform a "click". This does the same
thing as if the user had pressed and released the button.
The button stays visually "pressed" for

pressTime

milliseconds.

**Parameters:** pressTime

- the time to "hold down" the button, in milliseconds

- setMargin

```java
@BeanProperty
(
visualUpdate
=true,

description
="The space between the button\'s border and the label.")
public void setMargin​(
Insets
m)
```

Sets space for margin between the button's border and
the label. Setting to

null

will cause the button to
use the default margin. The button's default

Border

object will use this value to create the proper margin.
However, if a non-default border is set on the button,
it is that

Border

object's responsibility to create the
appropriate margin space (else this property will
effectively be ignored).

**Parameters:** m

- the space between the border and the label

- getMargin

```java
public
Insets
getMargin()
```

Returns the margin between the button's border and
the label.

**Returns:** an

Insets

object specifying the margin
between the botton's border and the label
**See Also:** setMargin(java.awt.Insets)

- getIcon

```java
public
Icon
getIcon()
```

Returns the default icon.

**Returns:** the default

Icon
**See Also:** setIcon(javax.swing.Icon)

- setIcon

```java
@BeanProperty
(
visualUpdate
=true,

description
="The button\'s default icon")
public void setIcon​(
Icon
defaultIcon)
```

Sets the button's default icon. This icon is
also used as the "pressed" and "disabled" icon if
there is no explicitly set pressed icon.

**Parameters:** defaultIcon

- the icon used as the default image
**See Also:** getIcon()

,

setPressedIcon(javax.swing.Icon)

- getPressedIcon

```java
public
Icon
getPressedIcon()
```

Returns the pressed icon for the button.

**Returns:** the

pressedIcon

property
**See Also:** setPressedIcon(javax.swing.Icon)

- setPressedIcon

```java
@BeanProperty
(
visualUpdate
=true,

description
="The pressed icon for the button.")
public void setPressedIcon​(
Icon
pressedIcon)
```

Sets the pressed icon for the button.

**Parameters:** pressedIcon

- the icon used as the "pressed" image
**See Also:** getPressedIcon()

- getSelectedIcon

```java
public
Icon
getSelectedIcon()
```

Returns the selected icon for the button.

**Returns:** the

selectedIcon

property
**See Also:** setSelectedIcon(javax.swing.Icon)

- setSelectedIcon

```java
@BeanProperty
(
visualUpdate
=true,

description
="The selected icon for the button.")
public void setSelectedIcon​(
Icon
selectedIcon)
```

Sets the selected icon for the button.

**Parameters:** selectedIcon

- the icon used as the "selected" image
**See Also:** getSelectedIcon()

- getRolloverIcon

```java
public
Icon
getRolloverIcon()
```

Returns the rollover icon for the button.

**Returns:** the

rolloverIcon

property
**See Also:** setRolloverIcon(javax.swing.Icon)

- setRolloverIcon

```java
@BeanProperty
(
visualUpdate
=true,

description
="The rollover icon for the button.")
public void setRolloverIcon​(
Icon
rolloverIcon)
```

Sets the rollover icon for the button.

**Parameters:** rolloverIcon

- the icon used as the "rollover" image
**See Also:** getRolloverIcon()

- getRolloverSelectedIcon

```java
public
Icon
getRolloverSelectedIcon()
```

Returns the rollover selection icon for the button.

**Returns:** the

rolloverSelectedIcon

property
**See Also:** setRolloverSelectedIcon(javax.swing.Icon)

- setRolloverSelectedIcon

```java
@BeanProperty
(
visualUpdate
=true,

description
="The rollover selected icon for the button.")
public void setRolloverSelectedIcon​(
Icon
rolloverSelectedIcon)
```

Sets the rollover selected icon for the button.

**Parameters:** rolloverSelectedIcon

- the icon used as the
"selected rollover" image
**See Also:** getRolloverSelectedIcon()

- getDisabledIcon

```java
public
Icon
getDisabledIcon()
```

Returns the icon used by the button when it's disabled.
If no disabled icon has been set this will forward the call to
the look and feel to construct an appropriate disabled Icon.

Some look and feels might not render the disabled Icon, in which
case they will ignore this.

**Returns:** the

disabledIcon

property
**See Also:** getPressedIcon()

,

setDisabledIcon(javax.swing.Icon)

,

LookAndFeel.getDisabledIcon(javax.swing.JComponent, javax.swing.Icon)

- setDisabledIcon

```java
@BeanProperty
(
visualUpdate
=true,

description
="The disabled icon for the button.")
public void setDisabledIcon​(
Icon
disabledIcon)
```

Sets the disabled icon for the button.

**Parameters:** disabledIcon

- the icon used as the disabled image
**See Also:** getDisabledIcon()

- getDisabledSelectedIcon

```java
public
Icon
getDisabledSelectedIcon()
```

Returns the icon used by the button when it's disabled and selected.
If no disabled selection icon has been set, this will forward
the call to the LookAndFeel to construct an appropriate disabled
Icon from the selection icon if it has been set and to

getDisabledIcon()

otherwise.

Some look and feels might not render the disabled selected Icon, in
which case they will ignore this.

**Returns:** the

disabledSelectedIcon

property
**See Also:** getDisabledIcon()

,

setDisabledSelectedIcon(javax.swing.Icon)

,

LookAndFeel.getDisabledSelectedIcon(javax.swing.JComponent, javax.swing.Icon)

- setDisabledSelectedIcon

```java
@BeanProperty
(
visualUpdate
=true,

description
="The disabled selection icon for the button.")
public void setDisabledSelectedIcon​(
Icon
disabledSelectedIcon)
```

Sets the disabled selection icon for the button.

**Parameters:** disabledSelectedIcon

- the icon used as the disabled
selection image
**See Also:** getDisabledSelectedIcon()

- getVerticalAlignment

```java
public int getVerticalAlignment()
```

Returns the vertical alignment of the text and icon.

**Returns:** the

verticalAlignment

property, one of the
following values:

- SwingConstants.CENTER

(the default)

SwingConstants.TOP

SwingConstants.BOTTOM

- setVerticalAlignment

```java
@BeanProperty
(
visualUpdate
=true,

enumerationValues
={"SwingConstants.TOP","SwingConstants.CENTER","SwingConstants.BOTTOM"},

description
="The vertical alignment of the icon and text.")
public void setVerticalAlignment​(int alignment)
```

Sets the vertical alignment of the icon and text.

**Parameters:** alignment

- one of the following values:

- SwingConstants.CENTER

(the default)

SwingConstants.TOP

SwingConstants.BOTTOM
**Throws:** IllegalArgumentException

- if the alignment is not one of the legal
values listed above

- getHorizontalAlignment

```java
public int getHorizontalAlignment()
```

Returns the horizontal alignment of the icon and text.

AbstractButton

's default is

SwingConstants.CENTER

,
but subclasses such as

JCheckBox

may use a different default.

**Returns:** the

horizontalAlignment

property,
one of the following values:

- SwingConstants.RIGHT

SwingConstants.LEFT

SwingConstants.CENTER

SwingConstants.LEADING

SwingConstants.TRAILING

- setHorizontalAlignment

```java
@BeanProperty
(
visualUpdate
=true,

enumerationValues
={"SwingConstants.LEFT","SwingConstants.CENTER","SwingConstants.RIGHT","SwingConstants.LEADING","SwingConstants.TRAILING"},

description
="The horizontal alignment of the icon and text.")
public void setHorizontalAlignment​(int alignment)
```

Sets the horizontal alignment of the icon and text.

AbstractButton

's default is

SwingConstants.CENTER

,
but subclasses such as

JCheckBox

may use a different default.

**Parameters:** alignment

- the alignment value, one of the following values:

- SwingConstants.RIGHT

SwingConstants.LEFT

SwingConstants.CENTER

SwingConstants.LEADING

SwingConstants.TRAILING
**Throws:** IllegalArgumentException

- if the alignment is not one of the
valid values

- getVerticalTextPosition

```java
public int getVerticalTextPosition()
```

Returns the vertical position of the text relative to the icon.

**Returns:** the

verticalTextPosition

property,
one of the following values:

- SwingConstants.CENTER

(the default)

SwingConstants.TOP

SwingConstants.BOTTOM

- setVerticalTextPosition

```java
@BeanProperty
(
visualUpdate
=true,

enumerationValues
={"SwingConstants.TOP","SwingConstants.CENTER","SwingConstants.BOTTOM"},

description
="The vertical position of the text relative to the icon.")
public void setVerticalTextPosition​(int textPosition)
```

Sets the vertical position of the text relative to the icon.

**Parameters:** textPosition

- one of the following values:

- SwingConstants.CENTER

(the default)

SwingConstants.TOP

SwingConstants.BOTTOM

- getHorizontalTextPosition

```java
public int getHorizontalTextPosition()
```

Returns the horizontal position of the text relative to the icon.

**Returns:** the

horizontalTextPosition

property,
one of the following values:

- SwingConstants.RIGHT

SwingConstants.LEFT

SwingConstants.CENTER

SwingConstants.LEADING

SwingConstants.TRAILING

(the default)

- setHorizontalTextPosition

```java
@BeanProperty
(
visualUpdate
=true,

enumerationValues
={"SwingConstants.LEFT","SwingConstants.CENTER","SwingConstants.RIGHT","SwingConstants.LEADING","SwingConstants.TRAILING"},

description
="The horizontal position of the text relative to the icon.")
public void setHorizontalTextPosition​(int textPosition)
```

Sets the horizontal position of the text relative to the icon.

**Parameters:** textPosition

- one of the following values:

- SwingConstants.RIGHT

SwingConstants.LEFT

SwingConstants.CENTER

SwingConstants.LEADING

SwingConstants.TRAILING

(the default)
**Throws:** IllegalArgumentException

- if

textPosition

is not one of the legal values listed above

- getIconTextGap

```java
public int getIconTextGap()
```

Returns the amount of space between the text and the icon
displayed in this button.

**Returns:** an int equal to the number of pixels between the text
and the icon.
**Since:** 1.4
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

- the space between icon and text if these properties are set.
**Since:** 1.4
**See Also:** getIconTextGap()

- checkHorizontalKey

```java
protected int checkHorizontalKey​(int key,

String
exception)
```

Verify that the

key

argument is a legal value for the

horizontalAlignment

and

horizontalTextPosition

properties. Valid values are:

- SwingConstants.RIGHT

SwingConstants.LEFT

SwingConstants.CENTER

SwingConstants.LEADING

SwingConstants.TRAILING

**Parameters:** key

- the property value to check
**Parameters:** exception

- the message to use in the

IllegalArgumentException

that is thrown for an invalid
value
**Returns:** the

key

argument
**Throws:** IllegalArgumentException

- if key is not one of the legal
values listed above
**See Also:** setHorizontalTextPosition(int)

,

setHorizontalAlignment(int)

- checkVerticalKey

```java
protected int checkVerticalKey​(int key,

String
exception)
```

Verify that the

key

argument is a legal value for the
vertical properties. Valid values are:

- SwingConstants.CENTER

SwingConstants.TOP

SwingConstants.BOTTOM

**Parameters:** key

- the property value to check
**Parameters:** exception

- the message to use in the

IllegalArgumentException

that is thrown for an invalid
value
**Returns:** the

key

argument
**Throws:** IllegalArgumentException

- if key is not one of the legal
values listed above

- removeNotify

```java
public void removeNotify()
```

Notifies this component that it no longer has a parent component.
When this method is invoked, any

KeyboardAction

s
set up in the chain of parent components are removed.
This method is called by the toolkit internally and should
not be called directly by programs.

**Overrides:** removeNotify

in class

JComponent
**Since:** 1.6
**See Also:** JComponent.registerKeyboardAction(java.awt.event.ActionListener, java.lang.String, javax.swing.KeyStroke, int)

- setActionCommand

```java
public void setActionCommand​(
String
actionCommand)
```

Sets the action command for this button.

**Parameters:** actionCommand

- the action command for this button

- getActionCommand

```java
public
String
getActionCommand()
```

Returns the action command for this button.

**Returns:** the action command for this button

- setAction

```java
@BeanProperty
(
visualUpdate
=true,

description
="the Action instance connected with this ActionEvent source")
public void setAction​(
Action
a)
```

Sets the

Action

.
The new

Action

replaces any previously set

Action

but does not affect

ActionListeners

independently added with

addActionListener

.
If the

Action

is already a registered

ActionListener

for the button, it is not re-registered.

Setting the

Action

results in immediately changing
all the properties described in

Swing Components Supporting

Action

.
Subsequently, the button's properties are automatically updated
as the

Action

's properties change.

This method uses three other methods to set
and help track the

Action

's property values.
It uses the

configurePropertiesFromAction

method
to immediately change the button's properties.
To track changes in the

Action

's property values,
this method registers the

PropertyChangeListener

returned by

createActionPropertyChangeListener

. The
default

PropertyChangeListener

invokes the

actionPropertyChanged

method when a property in the

Action

changes.

**Parameters:** a

- the

Action

for the

AbstractButton

,
or

null
**Since:** 1.3
**See Also:** Action

,

getAction()

,

configurePropertiesFromAction(javax.swing.Action)

,

createActionPropertyChangeListener(javax.swing.Action)

,

actionPropertyChanged(javax.swing.Action, java.lang.String)

- getAction

```java
public
Action
getAction()
```

Returns the currently set

Action

for this

ActionEvent

source, or

null

if no

Action

is set.

**Returns:** the

Action

for this

ActionEvent

source, or

null
**Since:** 1.3
**See Also:** Action

,

setAction(javax.swing.Action)

- configurePropertiesFromAction

```java
protected void configurePropertiesFromAction​(
Action
a)
```

Sets the properties on this button to match those in the specified

Action

. Refer to

Swing Components Supporting

Action

for more
details as to which properties this sets.

**Parameters:** a

- the

Action

from which to get the properties,
or

null
**Since:** 1.3
**See Also:** Action

,

setAction(javax.swing.Action)

- actionPropertyChanged

```java
protected void actionPropertyChanged​(
Action
action,

String
propertyName)
```

Updates the button's state in response to property changes in the
associated action. This method is invoked from the

PropertyChangeListener

returned from

createActionPropertyChangeListener

. Subclasses do not normally
need to invoke this. Subclasses that support additional

Action

properties should override this and

configurePropertiesFromAction

.

Refer to the table at

Swing Components Supporting

Action

for a list of
the properties this method sets.

**Parameters:** action

- the

Action

associated with this button
**Parameters:** propertyName

- the name of the property that changed
**Since:** 1.6
**See Also:** Action

,

configurePropertiesFromAction(javax.swing.Action)

- createActionPropertyChangeListener

```java
protected
PropertyChangeListener
createActionPropertyChangeListener​(
Action
a)
```

Creates and returns a

PropertyChangeListener

that is
responsible for listening for changes from the specified

Action

and updating the appropriate properties.

Warning:

If you subclass this do not create an anonymous
inner class. If you do the lifetime of the button will be tied to
that of the

Action

.

**Parameters:** a

- the button's action
**Returns:** the

PropertyChangeListener
**Since:** 1.3
**See Also:** Action

,

setAction(javax.swing.Action)

- isBorderPainted

```java
public boolean isBorderPainted()
```

Gets the

borderPainted

property.

**Returns:** the value of the

borderPainted

property
**See Also:** setBorderPainted(boolean)

- setBorderPainted

```java
@BeanProperty
(
visualUpdate
=true,

description
="Whether the border should be painted.")
public void setBorderPainted​(boolean b)
```

Sets the

borderPainted

property.
If

true

and the button has a border,
the border is painted. The default value for the

borderPainted

property is

true

.

Some look and feels might not support
the

borderPainted

property,
in which case they ignore this.

**Parameters:** b

- if true and border property is not

null

,
the border is painted
**See Also:** isBorderPainted()

- paintBorder

```java
protected void paintBorder​(
Graphics
g)
```

Paint the button's border if

BorderPainted

property is true and the button has a border.

**Overrides:** paintBorder

in class

JComponent
**Parameters:** g

- the

Graphics

context in which to paint
**See Also:** JComponent.paint(java.awt.Graphics)

,

JComponent.setBorder(javax.swing.border.Border)

- isFocusPainted

```java
public boolean isFocusPainted()
```

Gets the

paintFocus

property.

**Returns:** the

paintFocus

property
**See Also:** setFocusPainted(boolean)

- setFocusPainted

```java
@BeanProperty
(
visualUpdate
=true,

description
="Whether focus should be painted")
public void setFocusPainted​(boolean b)
```

Sets the

paintFocus

property, which must
be

true

for the focus state to be painted.
The default value for the

paintFocus

property
is

true

.
Some look and feels might not paint focus state;
they will ignore this property.

**Parameters:** b

- if

true

, the focus state should be painted
**See Also:** isFocusPainted()

- isContentAreaFilled

```java
public boolean isContentAreaFilled()
```

Gets the

contentAreaFilled

property.

**Returns:** the

contentAreaFilled

property
**See Also:** setContentAreaFilled(boolean)

- setContentAreaFilled

```java
@BeanProperty
(
visualUpdate
=true,

description
="Whether the button should paint the content area or leave it transparent.")
public void setContentAreaFilled​(boolean b)
```

Sets the

contentAreaFilled

property.
If

true

the button will paint the content
area. If you wish to have a transparent button, such as
an icon only button, for example, then you should set
this to

false

. Do not call

setOpaque(false)

.
The default value for the

contentAreaFilled

property is

true

.

This function may cause the component's opaque property to change.

The exact behavior of calling this function varies on a
component-by-component and L&F-by-L&F basis.

**Parameters:** b

- if true, the content should be filled; if false
the content area is not filled
**See Also:** isContentAreaFilled()

,

JComponent.setOpaque(boolean)

- isRolloverEnabled

```java
public boolean isRolloverEnabled()
```

Gets the

rolloverEnabled

property.

**Returns:** the value of the

rolloverEnabled

property
**See Also:** setRolloverEnabled(boolean)

- setRolloverEnabled

```java
@BeanProperty
(
visualUpdate
=true,

description
="Whether rollover effects should be enabled.")
public void setRolloverEnabled​(boolean b)
```

Sets the

rolloverEnabled

property, which
must be

true

for rollover effects to occur.
The default value for the

rolloverEnabled

property is

false

.
Some look and feels might not implement rollover effects;
they will ignore this property.

**Parameters:** b

- if

true

, rollover effects should be painted
**See Also:** isRolloverEnabled()

- getMnemonic

```java
public int getMnemonic()
```

Returns the keyboard mnemonic from the current model.

**Returns:** the keyboard mnemonic from the model

- setMnemonic

```java
@BeanProperty
(
visualUpdate
=true,

description
="the keyboard character mnemonic")
public void setMnemonic​(int mnemonic)
```

Sets the keyboard mnemonic on the current model.
The mnemonic is the key which when combined with the look and feel's
mouseless modifier (usually Alt) will activate this button
if focus is contained somewhere within this button's ancestor
window.

A mnemonic must correspond to a single key on the keyboard
and should be specified using one of the

VK_XXX

keycodes defined in

java.awt.event.KeyEvent

.
These codes and the wider array of codes for international
keyboards may be obtained through

java.awt.event.KeyEvent.getExtendedKeyCodeForChar

.
Mnemonics are case-insensitive, therefore a key event
with the corresponding keycode would cause the button to be
activated whether or not the Shift modifier was pressed.

If the character defined by the mnemonic is found within
the button's label string, the first occurrence of it
will be underlined to indicate the mnemonic to the user.

**Parameters:** mnemonic

- the key code which represents the mnemonic
**See Also:** KeyEvent

,

setDisplayedMnemonicIndex(int)

- setMnemonic

```java
@BeanProperty
(
visualUpdate
=true,

description
="the keyboard character mnemonic")
public void setMnemonic​(char mnemonic)
```

This method is now obsolete, please use

setMnemonic(int)

to set the mnemonic for a button. This method is only designed
to handle character values which fall between 'a' and 'z' or
'A' and 'Z'.

**Parameters:** mnemonic

- a char specifying the mnemonic value
**See Also:** setMnemonic(int)

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

setMnemonic(KeyEvent.VK_A)

.

**Parameters:** index

- Index into the String to underline
**Throws:** IllegalArgumentException

- will be thrown if

index

is >= length of the text, or < -1
**Since:** 1.4
**See Also:** getDisplayedMnemonicIndex()

- getDisplayedMnemonicIndex

```java
public int getDisplayedMnemonicIndex()
```

Returns the character, as an index, that the look and feel should
provide decoration for as representing the mnemonic character.

**Returns:** index representing mnemonic character
**Since:** 1.4
**See Also:** setDisplayedMnemonicIndex(int)

- setMultiClickThreshhold

```java
public void setMultiClickThreshhold​(long threshhold)
```

Sets the amount of time (in milliseconds) required between
mouse press events for the button to generate the corresponding
action events. After the initial mouse press occurs (and action
event generated) any subsequent mouse press events which occur
on intervals less than the threshhold will be ignored and no
corresponding action event generated. By default the threshhold is 0,
which means that for each mouse press, an action event will be
fired, no matter how quickly the mouse clicks occur. In buttons
where this behavior is not desirable (for example, the "OK" button
in a dialog), this threshhold should be set to an appropriate
positive value.

**Parameters:** threshhold

- the amount of time required between mouse
press events to generate corresponding action events
**Throws:** IllegalArgumentException

- if threshhold < 0
**Since:** 1.4
**See Also:** getMultiClickThreshhold()

- getMultiClickThreshhold

```java
public long getMultiClickThreshhold()
```

Gets the amount of time (in milliseconds) required between
mouse press events for the button to generate the corresponding
action events.

**Returns:** the amount of time required between mouse press events
to generate corresponding action events
**Since:** 1.4
**See Also:** setMultiClickThreshhold(long)

- getModel

```java
public
ButtonModel
getModel()
```

Returns the model that this button represents.

**Returns:** the

model

property
**See Also:** setModel(javax.swing.ButtonModel)

- setModel

```java
@BeanProperty
(
description
="Model that the Button uses.")
public void setModel​(
ButtonModel
newModel)
```

Sets the model that this button represents.

**Parameters:** newModel

- the new

ButtonModel
**See Also:** getModel()

- getUI

```java
public
ButtonUI
getUI()
```

Returns the L&F object that renders this component.

**Overrides:** getUI

in class

JComponent
**Returns:** the ButtonUI object
**See Also:** setUI(javax.swing.plaf.ButtonUI)

- setUI

```java
@BeanProperty
(
hidden
=true,

visualUpdate
=true,

description
="The UI object that implements the LookAndFeel.")
public void setUI​(
ButtonUI
ui)
```

Sets the L&F object that renders this component.

**Parameters:** ui

- the

ButtonUI

L&F object
**See Also:** getUI()

- updateUI

```java
public void updateUI()
```

Resets the UI property to a value from the current look
and feel. Subtypes of

AbstractButton

should override this to update the UI. For
example,

JButton

might do the following:

```java
setUI((ButtonUI)UIManager.getUI(
"ButtonUI", "javax.swing.plaf.basic.BasicButtonUI", this));
```

**Overrides:** updateUI

in class

JComponent
**See Also:** JComponent.setUI(javax.swing.plaf.ComponentUI)

,

UIManager.getLookAndFeel()

,

UIManager.getUI(javax.swing.JComponent)

- addImpl

```java
protected void addImpl​(
Component
comp,

Object
constraints,
int index)
```

Adds the specified component to this container at the specified
index, refer to

Container.addImpl(Component, Object, int)

for a complete description of this method.

**Overrides:** addImpl

in class

Container
**Parameters:** comp

- the component to be added
**Parameters:** constraints

- an object expressing layout constraints
for this component
**Parameters:** index

- the position in the container's list at which to
insert the component, where

-1

means append to the end
**Throws:** IllegalArgumentException

- if

index

is invalid
**Throws:** IllegalArgumentException

- if adding the container's parent
to itself
**Throws:** IllegalArgumentException

- if adding a window to a container
**Since:** 1.5
**See Also:** Container.add(Component)

,

Container.add(Component, int)

,

Container.add(Component, java.lang.Object)

,

Container.invalidate()

,

LayoutManager

,

LayoutManager2

- setLayout

```java
public void setLayout​(
LayoutManager
mgr)
```

Sets the layout manager for this container, refer to

Container.setLayout(LayoutManager)

for a complete description of this method.

**Overrides:** setLayout

in class

Container
**Parameters:** mgr

- the specified layout manager
**Since:** 1.5
**See Also:** Container.doLayout()

,

Container.getLayout()

,

Container.invalidate()

- addChangeListener

```java
public void addChangeListener​(
ChangeListener
l)
```

Adds a

ChangeListener

to the button.

**Parameters:** l

- the listener to be added

- removeChangeListener

```java
public void removeChangeListener​(
ChangeListener
l)
```

Removes a ChangeListener from the button.

**Parameters:** l

- the listener to be removed

- getChangeListeners

```java
@BeanProperty
(
bound
=false)
public
ChangeListener
[] getChangeListeners()
```

Returns an array of all the

ChangeListener

s added
to this AbstractButton with addChangeListener().

**Returns:** all of the

ChangeListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

- fireStateChanged

```java
protected void fireStateChanged()
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created.

**See Also:** EventListenerList

- addActionListener

```java
public void addActionListener​(
ActionListener
l)
```

Adds an

ActionListener

to the button.

**Parameters:** l

- the

ActionListener

to be added

- removeActionListener

```java
public void removeActionListener​(
ActionListener
l)
```

Removes an

ActionListener

from the button.
If the listener is the currently set

Action

for the button, then the

Action

is set to

null

.

**Parameters:** l

- the listener to be removed

- getActionListeners

```java
@BeanProperty
(
bound
=false)
public
ActionListener
[] getActionListeners()
```

Returns an array of all the

ActionListener

s added
to this AbstractButton with addActionListener().

**Returns:** all of the

ActionListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

- createChangeListener

```java
protected
ChangeListener
createChangeListener()
```

Subclasses that want to handle

ChangeEvents

differently
can override this to return another

ChangeListener

implementation.

**Returns:** the new

ChangeListener

- fireActionPerformed

```java
protected void fireActionPerformed​(
ActionEvent
event)
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the

event

parameter.

**Parameters:** event

- the

ActionEvent

object
**See Also:** EventListenerList

- fireItemStateChanged

```java
protected void fireItemStateChanged​(
ItemEvent
event)
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the

event

parameter.

**Parameters:** event

- the

ItemEvent

object
**See Also:** EventListenerList

- createActionListener

```java
protected
ActionListener
createActionListener()
```

Returns

ActionListener

that is added to model.

**Returns:** the

ActionListener

- createItemListener

```java
protected
ItemListener
createItemListener()
```

Returns

ItemListener

that is added to model.

**Returns:** the

ItemListener

- setEnabled

```java
public void setEnabled​(boolean b)
```

Enables (or disables) the button.

**Overrides:** setEnabled

in class

JComponent
**Parameters:** b

- true to enable the button, otherwise false
**See Also:** Component.isEnabled()

,

Component.isLightweight()

- getLabel

```java
@Deprecated

public
String
getLabel()
```

Deprecated.

- Replaced by

getText

Returns the label text.

**Returns:** a

String

containing the label

- setLabel

```java
@Deprecated

@BeanProperty
(
description
="Replace by setText(text)")
public void setLabel​(
String
label)
```

Deprecated.

- Replaced by

setText(text)

Sets the label text.

**Parameters:** label

- a

String

containing the text

- addItemListener

```java
public void addItemListener​(
ItemListener
l)
```

Adds an

ItemListener

to the

checkbox

.

**Specified by:** addItemListener

in interface

ItemSelectable
**Parameters:** l

- the

ItemListener

to be added
**See Also:** ItemEvent

- removeItemListener

```java
public void removeItemListener​(
ItemListener
l)
```

Removes an

ItemListener

from the button.

**Specified by:** removeItemListener

in interface

ItemSelectable
**Parameters:** l

- the

ItemListener

to be removed
**See Also:** ItemEvent

- getItemListeners

```java
@BeanProperty
(
bound
=false)
public
ItemListener
[] getItemListeners()
```

Returns an array of all the

ItemListener

s added
to this AbstractButton with addItemListener().

**Returns:** all of the

ItemListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

- getSelectedObjects

```java
@BeanProperty
(
bound
=false)
public
Object
[] getSelectedObjects()
```

Returns an array (length 1) containing the label or

null

if the button is not selected.

**Specified by:** getSelectedObjects

in interface

ItemSelectable
**Returns:** an array containing 1 Object: the text of the button,
if the item is selected; otherwise

null

- init

```java
protected void init​(
String
text,

Icon
icon)
```

Initialization of the

AbstractButton

.

**Parameters:** text

- the text of the button
**Parameters:** icon

- the Icon image to display on the button

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

This is overridden to return false if the current

Icon

's

Image

is not equal to the
passed in

Image

img

.

**Specified by:** imageUpdate

in interface

ImageObserver
**Overrides:** imageUpdate

in class

Component
**Parameters:** img

- the

Image

to be compared
**Parameters:** infoflags

- flags used to repaint the button when the image
is updated and which determine how much is to be painted
**Parameters:** x

- the x coordinate
**Parameters:** y

- the y coordinate
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

Returns a string representation of this

AbstractButton

.
This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

Overriding

paramString

to provide information about the
specific new aspects of the JFC components.

**Overrides:** paramString

in class

JComponent
**Returns:** a string representation of this

AbstractButton

Field Detail

- MODEL_CHANGED_PROPERTY

```java
public static final
String
MODEL_CHANGED_PROPERTY
```

Identifies a change in the button model.

**See Also:** Constant Field Values

- TEXT_CHANGED_PROPERTY

```java
public static final
String
TEXT_CHANGED_PROPERTY
```

Identifies a change in the button's text.

**See Also:** Constant Field Values

- MNEMONIC_CHANGED_PROPERTY

```java
public static final
String
MNEMONIC_CHANGED_PROPERTY
```

Identifies a change to the button's mnemonic.

**See Also:** Constant Field Values

- MARGIN_CHANGED_PROPERTY

```java
public static final
String
MARGIN_CHANGED_PROPERTY
```

Identifies a change in the button's margins.

**See Also:** Constant Field Values

- VERTICAL_ALIGNMENT_CHANGED_PROPERTY

```java
public static final
String
VERTICAL_ALIGNMENT_CHANGED_PROPERTY
```

Identifies a change in the button's vertical alignment.

**See Also:** Constant Field Values

- HORIZONTAL_ALIGNMENT_CHANGED_PROPERTY

```java
public static final
String
HORIZONTAL_ALIGNMENT_CHANGED_PROPERTY
```

Identifies a change in the button's horizontal alignment.

**See Also:** Constant Field Values

- VERTICAL_TEXT_POSITION_CHANGED_PROPERTY

```java
public static final
String
VERTICAL_TEXT_POSITION_CHANGED_PROPERTY
```

Identifies a change in the button's vertical text position.

**See Also:** Constant Field Values

- HORIZONTAL_TEXT_POSITION_CHANGED_PROPERTY

```java
public static final
String
HORIZONTAL_TEXT_POSITION_CHANGED_PROPERTY
```

Identifies a change in the button's horizontal text position.

**See Also:** Constant Field Values

- BORDER_PAINTED_CHANGED_PROPERTY

```java
public static final
String
BORDER_PAINTED_CHANGED_PROPERTY
```

Identifies a change to having the border drawn,
or having it not drawn.

**See Also:** Constant Field Values

- FOCUS_PAINTED_CHANGED_PROPERTY

```java
public static final
String
FOCUS_PAINTED_CHANGED_PROPERTY
```

Identifies a change to having the border highlighted when focused,
or not.

**See Also:** Constant Field Values

- ROLLOVER_ENABLED_CHANGED_PROPERTY

```java
public static final
String
ROLLOVER_ENABLED_CHANGED_PROPERTY
```

Identifies a change from rollover enabled to disabled or back
to enabled.

**See Also:** Constant Field Values

- CONTENT_AREA_FILLED_CHANGED_PROPERTY

```java
public static final
String
CONTENT_AREA_FILLED_CHANGED_PROPERTY
```

Identifies a change to having the button paint the content area.

**See Also:** Constant Field Values

- ICON_CHANGED_PROPERTY

```java
public static final
String
ICON_CHANGED_PROPERTY
```

Identifies a change to the icon that represents the button.

**See Also:** Constant Field Values

- PRESSED_ICON_CHANGED_PROPERTY

```java
public static final
String
PRESSED_ICON_CHANGED_PROPERTY
```

Identifies a change to the icon used when the button has been
pressed.

**See Also:** Constant Field Values

- SELECTED_ICON_CHANGED_PROPERTY

```java
public static final
String
SELECTED_ICON_CHANGED_PROPERTY
```

Identifies a change to the icon used when the button has
been selected.

**See Also:** Constant Field Values

- ROLLOVER_ICON_CHANGED_PROPERTY

```java
public static final
String
ROLLOVER_ICON_CHANGED_PROPERTY
```

Identifies a change to the icon used when the cursor is over
the button.

**See Also:** Constant Field Values

- ROLLOVER_SELECTED_ICON_CHANGED_PROPERTY

```java
public static final
String
ROLLOVER_SELECTED_ICON_CHANGED_PROPERTY
```

Identifies a change to the icon used when the cursor is
over the button and it has been selected.

**See Also:** Constant Field Values

- DISABLED_ICON_CHANGED_PROPERTY

```java
public static final
String
DISABLED_ICON_CHANGED_PROPERTY
```

Identifies a change to the icon used when the button has
been disabled.

**See Also:** Constant Field Values

- DISABLED_SELECTED_ICON_CHANGED_PROPERTY

```java
public static final
String
DISABLED_SELECTED_ICON_CHANGED_PROPERTY
```

Identifies a change to the icon used when the button has been
disabled and selected.

**See Also:** Constant Field Values

- model

```java
protected
ButtonModel
model
```

The data model that determines the button's state.

- changeListener

```java
protected
ChangeListener
changeListener
```

The button model's

changeListener

.

- actionListener

```java
protected
ActionListener
actionListener
```

The button model's

ActionListener

.

- itemListener

```java
protected
ItemListener
itemListener
```

The button model's

ItemListener

.

- changeEvent

```java
protected transient
ChangeEvent
changeEvent
```

Only one

ChangeEvent

is needed per button
instance since the
event's only state is the source property. The source of events
generated is always "this".

---

#### Field Detail

MODEL_CHANGED_PROPERTY

```java
public static final
String
MODEL_CHANGED_PROPERTY
```

Identifies a change in the button model.

**See Also:** Constant Field Values

---

#### MODEL_CHANGED_PROPERTY

public static final

String

MODEL_CHANGED_PROPERTY

Identifies a change in the button model.

TEXT_CHANGED_PROPERTY

```java
public static final
String
TEXT_CHANGED_PROPERTY
```

Identifies a change in the button's text.

**See Also:** Constant Field Values

---

#### TEXT_CHANGED_PROPERTY

public static final

String

TEXT_CHANGED_PROPERTY

Identifies a change in the button's text.

MNEMONIC_CHANGED_PROPERTY

```java
public static final
String
MNEMONIC_CHANGED_PROPERTY
```

Identifies a change to the button's mnemonic.

**See Also:** Constant Field Values

---

#### MNEMONIC_CHANGED_PROPERTY

public static final

String

MNEMONIC_CHANGED_PROPERTY

Identifies a change to the button's mnemonic.

MARGIN_CHANGED_PROPERTY

```java
public static final
String
MARGIN_CHANGED_PROPERTY
```

Identifies a change in the button's margins.

**See Also:** Constant Field Values

---

#### MARGIN_CHANGED_PROPERTY

public static final

String

MARGIN_CHANGED_PROPERTY

Identifies a change in the button's margins.

VERTICAL_ALIGNMENT_CHANGED_PROPERTY

```java
public static final
String
VERTICAL_ALIGNMENT_CHANGED_PROPERTY
```

Identifies a change in the button's vertical alignment.

**See Also:** Constant Field Values

---

#### VERTICAL_ALIGNMENT_CHANGED_PROPERTY

public static final

String

VERTICAL_ALIGNMENT_CHANGED_PROPERTY

Identifies a change in the button's vertical alignment.

HORIZONTAL_ALIGNMENT_CHANGED_PROPERTY

```java
public static final
String
HORIZONTAL_ALIGNMENT_CHANGED_PROPERTY
```

Identifies a change in the button's horizontal alignment.

**See Also:** Constant Field Values

---

#### HORIZONTAL_ALIGNMENT_CHANGED_PROPERTY

public static final

String

HORIZONTAL_ALIGNMENT_CHANGED_PROPERTY

Identifies a change in the button's horizontal alignment.

VERTICAL_TEXT_POSITION_CHANGED_PROPERTY

```java
public static final
String
VERTICAL_TEXT_POSITION_CHANGED_PROPERTY
```

Identifies a change in the button's vertical text position.

**See Also:** Constant Field Values

---

#### VERTICAL_TEXT_POSITION_CHANGED_PROPERTY

public static final

String

VERTICAL_TEXT_POSITION_CHANGED_PROPERTY

Identifies a change in the button's vertical text position.

HORIZONTAL_TEXT_POSITION_CHANGED_PROPERTY

```java
public static final
String
HORIZONTAL_TEXT_POSITION_CHANGED_PROPERTY
```

Identifies a change in the button's horizontal text position.

**See Also:** Constant Field Values

---

#### HORIZONTAL_TEXT_POSITION_CHANGED_PROPERTY

public static final

String

HORIZONTAL_TEXT_POSITION_CHANGED_PROPERTY

Identifies a change in the button's horizontal text position.

BORDER_PAINTED_CHANGED_PROPERTY

```java
public static final
String
BORDER_PAINTED_CHANGED_PROPERTY
```

Identifies a change to having the border drawn,
or having it not drawn.

**See Also:** Constant Field Values

---

#### BORDER_PAINTED_CHANGED_PROPERTY

public static final

String

BORDER_PAINTED_CHANGED_PROPERTY

Identifies a change to having the border drawn,
or having it not drawn.

FOCUS_PAINTED_CHANGED_PROPERTY

```java
public static final
String
FOCUS_PAINTED_CHANGED_PROPERTY
```

Identifies a change to having the border highlighted when focused,
or not.

**See Also:** Constant Field Values

---

#### FOCUS_PAINTED_CHANGED_PROPERTY

public static final

String

FOCUS_PAINTED_CHANGED_PROPERTY

Identifies a change to having the border highlighted when focused,
or not.

ROLLOVER_ENABLED_CHANGED_PROPERTY

```java
public static final
String
ROLLOVER_ENABLED_CHANGED_PROPERTY
```

Identifies a change from rollover enabled to disabled or back
to enabled.

**See Also:** Constant Field Values

---

#### ROLLOVER_ENABLED_CHANGED_PROPERTY

public static final

String

ROLLOVER_ENABLED_CHANGED_PROPERTY

Identifies a change from rollover enabled to disabled or back
to enabled.

CONTENT_AREA_FILLED_CHANGED_PROPERTY

```java
public static final
String
CONTENT_AREA_FILLED_CHANGED_PROPERTY
```

Identifies a change to having the button paint the content area.

**See Also:** Constant Field Values

---

#### CONTENT_AREA_FILLED_CHANGED_PROPERTY

public static final

String

CONTENT_AREA_FILLED_CHANGED_PROPERTY

Identifies a change to having the button paint the content area.

ICON_CHANGED_PROPERTY

```java
public static final
String
ICON_CHANGED_PROPERTY
```

Identifies a change to the icon that represents the button.

**See Also:** Constant Field Values

---

#### ICON_CHANGED_PROPERTY

public static final

String

ICON_CHANGED_PROPERTY

Identifies a change to the icon that represents the button.

PRESSED_ICON_CHANGED_PROPERTY

```java
public static final
String
PRESSED_ICON_CHANGED_PROPERTY
```

Identifies a change to the icon used when the button has been
pressed.

**See Also:** Constant Field Values

---

#### PRESSED_ICON_CHANGED_PROPERTY

public static final

String

PRESSED_ICON_CHANGED_PROPERTY

Identifies a change to the icon used when the button has been
pressed.

SELECTED_ICON_CHANGED_PROPERTY

```java
public static final
String
SELECTED_ICON_CHANGED_PROPERTY
```

Identifies a change to the icon used when the button has
been selected.

**See Also:** Constant Field Values

---

#### SELECTED_ICON_CHANGED_PROPERTY

public static final

String

SELECTED_ICON_CHANGED_PROPERTY

Identifies a change to the icon used when the button has
been selected.

ROLLOVER_ICON_CHANGED_PROPERTY

```java
public static final
String
ROLLOVER_ICON_CHANGED_PROPERTY
```

Identifies a change to the icon used when the cursor is over
the button.

**See Also:** Constant Field Values

---

#### ROLLOVER_ICON_CHANGED_PROPERTY

public static final

String

ROLLOVER_ICON_CHANGED_PROPERTY

Identifies a change to the icon used when the cursor is over
the button.

ROLLOVER_SELECTED_ICON_CHANGED_PROPERTY

```java
public static final
String
ROLLOVER_SELECTED_ICON_CHANGED_PROPERTY
```

Identifies a change to the icon used when the cursor is
over the button and it has been selected.

**See Also:** Constant Field Values

---

#### ROLLOVER_SELECTED_ICON_CHANGED_PROPERTY

public static final

String

ROLLOVER_SELECTED_ICON_CHANGED_PROPERTY

Identifies a change to the icon used when the cursor is
over the button and it has been selected.

DISABLED_ICON_CHANGED_PROPERTY

```java
public static final
String
DISABLED_ICON_CHANGED_PROPERTY
```

Identifies a change to the icon used when the button has
been disabled.

**See Also:** Constant Field Values

---

#### DISABLED_ICON_CHANGED_PROPERTY

public static final

String

DISABLED_ICON_CHANGED_PROPERTY

Identifies a change to the icon used when the button has
been disabled.

DISABLED_SELECTED_ICON_CHANGED_PROPERTY

```java
public static final
String
DISABLED_SELECTED_ICON_CHANGED_PROPERTY
```

Identifies a change to the icon used when the button has been
disabled and selected.

**See Also:** Constant Field Values

---

#### DISABLED_SELECTED_ICON_CHANGED_PROPERTY

public static final

String

DISABLED_SELECTED_ICON_CHANGED_PROPERTY

Identifies a change to the icon used when the button has been
disabled and selected.

model

```java
protected
ButtonModel
model
```

The data model that determines the button's state.

---

#### model

protected

ButtonModel

model

The data model that determines the button's state.

changeListener

```java
protected
ChangeListener
changeListener
```

The button model's

changeListener

.

---

#### changeListener

protected

ChangeListener

changeListener

The button model's

changeListener

.

actionListener

```java
protected
ActionListener
actionListener
```

The button model's

ActionListener

.

---

#### actionListener

protected

ActionListener

actionListener

The button model's

ActionListener

.

itemListener

```java
protected
ItemListener
itemListener
```

The button model's

ItemListener

.

---

#### itemListener

protected

ItemListener

itemListener

The button model's

ItemListener

.

changeEvent

```java
protected transient
ChangeEvent
changeEvent
```

Only one

ChangeEvent

is needed per button
instance since the
event's only state is the source property. The source of events
generated is always "this".

---

#### changeEvent

protected transient

ChangeEvent

changeEvent

Only one

ChangeEvent

is needed per button
instance since the
event's only state is the source property. The source of events
generated is always "this".

Constructor Detail

- AbstractButton

```java
public AbstractButton()
```

---

#### Constructor Detail

AbstractButton

```java
public AbstractButton()
```

---

#### AbstractButton

public AbstractButton()

Method Detail

- setHideActionText

```java
@BeanProperty
(
expert
=true,

description
="Whether the text of the button should come from the <code>Action</code>.")
public void setHideActionText​(boolean hideActionText)
```

Sets the

hideActionText

property, which determines
whether the button displays text from the

Action

.
This is useful only if an

Action

has been
installed on the button.

**Parameters:** hideActionText

-

true

if the button's

text

property should not reflect
that of the

Action

; the default is

false
**Since:** 1.6
**See Also:** Swing Components Supporting

Action

- getHideActionText

```java
public boolean getHideActionText()
```

Returns the value of the

hideActionText

property, which
determines whether the button displays text from the

Action

. This is useful only if an

Action

has been installed on the button.

**Returns:** true

if the button's

text

property should not reflect that of the

Action

; the default is

false
**Since:** 1.6

- getText

```java
public
String
getText()
```

Returns the button's text.

**Returns:** the buttons text
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
="The button\'s text.")
public void setText​(
String
text)
```

Sets the button's text.

**Parameters:** text

- the string used to set the text
**See Also:** getText()

- isSelected

```java
public boolean isSelected()
```

Returns the state of the button. True if the
toggle button is selected, false if it's not.

**Returns:** true if the toggle button is selected, otherwise false

- setSelected

```java
public void setSelected​(boolean b)
```

Sets the state of the button. Note that this method does not
trigger an

actionEvent

.
Call

doClick

to perform a programmatic action change.

**Parameters:** b

- true if the button is selected, otherwise false

- doClick

```java
public void doClick()
```

Programmatically perform a "click". This does the same
thing as if the user had pressed and released the button.

- doClick

```java
public void doClick​(int pressTime)
```

Programmatically perform a "click". This does the same
thing as if the user had pressed and released the button.
The button stays visually "pressed" for

pressTime

milliseconds.

**Parameters:** pressTime

- the time to "hold down" the button, in milliseconds

- setMargin

```java
@BeanProperty
(
visualUpdate
=true,

description
="The space between the button\'s border and the label.")
public void setMargin​(
Insets
m)
```

Sets space for margin between the button's border and
the label. Setting to

null

will cause the button to
use the default margin. The button's default

Border

object will use this value to create the proper margin.
However, if a non-default border is set on the button,
it is that

Border

object's responsibility to create the
appropriate margin space (else this property will
effectively be ignored).

**Parameters:** m

- the space between the border and the label

- getMargin

```java
public
Insets
getMargin()
```

Returns the margin between the button's border and
the label.

**Returns:** an

Insets

object specifying the margin
between the botton's border and the label
**See Also:** setMargin(java.awt.Insets)

- getIcon

```java
public
Icon
getIcon()
```

Returns the default icon.

**Returns:** the default

Icon
**See Also:** setIcon(javax.swing.Icon)

- setIcon

```java
@BeanProperty
(
visualUpdate
=true,

description
="The button\'s default icon")
public void setIcon​(
Icon
defaultIcon)
```

Sets the button's default icon. This icon is
also used as the "pressed" and "disabled" icon if
there is no explicitly set pressed icon.

**Parameters:** defaultIcon

- the icon used as the default image
**See Also:** getIcon()

,

setPressedIcon(javax.swing.Icon)

- getPressedIcon

```java
public
Icon
getPressedIcon()
```

Returns the pressed icon for the button.

**Returns:** the

pressedIcon

property
**See Also:** setPressedIcon(javax.swing.Icon)

- setPressedIcon

```java
@BeanProperty
(
visualUpdate
=true,

description
="The pressed icon for the button.")
public void setPressedIcon​(
Icon
pressedIcon)
```

Sets the pressed icon for the button.

**Parameters:** pressedIcon

- the icon used as the "pressed" image
**See Also:** getPressedIcon()

- getSelectedIcon

```java
public
Icon
getSelectedIcon()
```

Returns the selected icon for the button.

**Returns:** the

selectedIcon

property
**See Also:** setSelectedIcon(javax.swing.Icon)

- setSelectedIcon

```java
@BeanProperty
(
visualUpdate
=true,

description
="The selected icon for the button.")
public void setSelectedIcon​(
Icon
selectedIcon)
```

Sets the selected icon for the button.

**Parameters:** selectedIcon

- the icon used as the "selected" image
**See Also:** getSelectedIcon()

- getRolloverIcon

```java
public
Icon
getRolloverIcon()
```

Returns the rollover icon for the button.

**Returns:** the

rolloverIcon

property
**See Also:** setRolloverIcon(javax.swing.Icon)

- setRolloverIcon

```java
@BeanProperty
(
visualUpdate
=true,

description
="The rollover icon for the button.")
public void setRolloverIcon​(
Icon
rolloverIcon)
```

Sets the rollover icon for the button.

**Parameters:** rolloverIcon

- the icon used as the "rollover" image
**See Also:** getRolloverIcon()

- getRolloverSelectedIcon

```java
public
Icon
getRolloverSelectedIcon()
```

Returns the rollover selection icon for the button.

**Returns:** the

rolloverSelectedIcon

property
**See Also:** setRolloverSelectedIcon(javax.swing.Icon)

- setRolloverSelectedIcon

```java
@BeanProperty
(
visualUpdate
=true,

description
="The rollover selected icon for the button.")
public void setRolloverSelectedIcon​(
Icon
rolloverSelectedIcon)
```

Sets the rollover selected icon for the button.

**Parameters:** rolloverSelectedIcon

- the icon used as the
"selected rollover" image
**See Also:** getRolloverSelectedIcon()

- getDisabledIcon

```java
public
Icon
getDisabledIcon()
```

Returns the icon used by the button when it's disabled.
If no disabled icon has been set this will forward the call to
the look and feel to construct an appropriate disabled Icon.

Some look and feels might not render the disabled Icon, in which
case they will ignore this.

**Returns:** the

disabledIcon

property
**See Also:** getPressedIcon()

,

setDisabledIcon(javax.swing.Icon)

,

LookAndFeel.getDisabledIcon(javax.swing.JComponent, javax.swing.Icon)

- setDisabledIcon

```java
@BeanProperty
(
visualUpdate
=true,

description
="The disabled icon for the button.")
public void setDisabledIcon​(
Icon
disabledIcon)
```

Sets the disabled icon for the button.

**Parameters:** disabledIcon

- the icon used as the disabled image
**See Also:** getDisabledIcon()

- getDisabledSelectedIcon

```java
public
Icon
getDisabledSelectedIcon()
```

Returns the icon used by the button when it's disabled and selected.
If no disabled selection icon has been set, this will forward
the call to the LookAndFeel to construct an appropriate disabled
Icon from the selection icon if it has been set and to

getDisabledIcon()

otherwise.

Some look and feels might not render the disabled selected Icon, in
which case they will ignore this.

**Returns:** the

disabledSelectedIcon

property
**See Also:** getDisabledIcon()

,

setDisabledSelectedIcon(javax.swing.Icon)

,

LookAndFeel.getDisabledSelectedIcon(javax.swing.JComponent, javax.swing.Icon)

- setDisabledSelectedIcon

```java
@BeanProperty
(
visualUpdate
=true,

description
="The disabled selection icon for the button.")
public void setDisabledSelectedIcon​(
Icon
disabledSelectedIcon)
```

Sets the disabled selection icon for the button.

**Parameters:** disabledSelectedIcon

- the icon used as the disabled
selection image
**See Also:** getDisabledSelectedIcon()

- getVerticalAlignment

```java
public int getVerticalAlignment()
```

Returns the vertical alignment of the text and icon.

**Returns:** the

verticalAlignment

property, one of the
following values:

- SwingConstants.CENTER

(the default)

SwingConstants.TOP

SwingConstants.BOTTOM

- setVerticalAlignment

```java
@BeanProperty
(
visualUpdate
=true,

enumerationValues
={"SwingConstants.TOP","SwingConstants.CENTER","SwingConstants.BOTTOM"},

description
="The vertical alignment of the icon and text.")
public void setVerticalAlignment​(int alignment)
```

Sets the vertical alignment of the icon and text.

**Parameters:** alignment

- one of the following values:

- SwingConstants.CENTER

(the default)

SwingConstants.TOP

SwingConstants.BOTTOM
**Throws:** IllegalArgumentException

- if the alignment is not one of the legal
values listed above

- getHorizontalAlignment

```java
public int getHorizontalAlignment()
```

Returns the horizontal alignment of the icon and text.

AbstractButton

's default is

SwingConstants.CENTER

,
but subclasses such as

JCheckBox

may use a different default.

**Returns:** the

horizontalAlignment

property,
one of the following values:

- SwingConstants.RIGHT

SwingConstants.LEFT

SwingConstants.CENTER

SwingConstants.LEADING

SwingConstants.TRAILING

- setHorizontalAlignment

```java
@BeanProperty
(
visualUpdate
=true,

enumerationValues
={"SwingConstants.LEFT","SwingConstants.CENTER","SwingConstants.RIGHT","SwingConstants.LEADING","SwingConstants.TRAILING"},

description
="The horizontal alignment of the icon and text.")
public void setHorizontalAlignment​(int alignment)
```

Sets the horizontal alignment of the icon and text.

AbstractButton

's default is

SwingConstants.CENTER

,
but subclasses such as

JCheckBox

may use a different default.

**Parameters:** alignment

- the alignment value, one of the following values:

- SwingConstants.RIGHT

SwingConstants.LEFT

SwingConstants.CENTER

SwingConstants.LEADING

SwingConstants.TRAILING
**Throws:** IllegalArgumentException

- if the alignment is not one of the
valid values

- getVerticalTextPosition

```java
public int getVerticalTextPosition()
```

Returns the vertical position of the text relative to the icon.

**Returns:** the

verticalTextPosition

property,
one of the following values:

- SwingConstants.CENTER

(the default)

SwingConstants.TOP

SwingConstants.BOTTOM

- setVerticalTextPosition

```java
@BeanProperty
(
visualUpdate
=true,

enumerationValues
={"SwingConstants.TOP","SwingConstants.CENTER","SwingConstants.BOTTOM"},

description
="The vertical position of the text relative to the icon.")
public void setVerticalTextPosition​(int textPosition)
```

Sets the vertical position of the text relative to the icon.

**Parameters:** textPosition

- one of the following values:

- SwingConstants.CENTER

(the default)

SwingConstants.TOP

SwingConstants.BOTTOM

- getHorizontalTextPosition

```java
public int getHorizontalTextPosition()
```

Returns the horizontal position of the text relative to the icon.

**Returns:** the

horizontalTextPosition

property,
one of the following values:

- SwingConstants.RIGHT

SwingConstants.LEFT

SwingConstants.CENTER

SwingConstants.LEADING

SwingConstants.TRAILING

(the default)

- setHorizontalTextPosition

```java
@BeanProperty
(
visualUpdate
=true,

enumerationValues
={"SwingConstants.LEFT","SwingConstants.CENTER","SwingConstants.RIGHT","SwingConstants.LEADING","SwingConstants.TRAILING"},

description
="The horizontal position of the text relative to the icon.")
public void setHorizontalTextPosition​(int textPosition)
```

Sets the horizontal position of the text relative to the icon.

**Parameters:** textPosition

- one of the following values:

- SwingConstants.RIGHT

SwingConstants.LEFT

SwingConstants.CENTER

SwingConstants.LEADING

SwingConstants.TRAILING

(the default)
**Throws:** IllegalArgumentException

- if

textPosition

is not one of the legal values listed above

- getIconTextGap

```java
public int getIconTextGap()
```

Returns the amount of space between the text and the icon
displayed in this button.

**Returns:** an int equal to the number of pixels between the text
and the icon.
**Since:** 1.4
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

- the space between icon and text if these properties are set.
**Since:** 1.4
**See Also:** getIconTextGap()

- checkHorizontalKey

```java
protected int checkHorizontalKey​(int key,

String
exception)
```

Verify that the

key

argument is a legal value for the

horizontalAlignment

and

horizontalTextPosition

properties. Valid values are:

- SwingConstants.RIGHT

SwingConstants.LEFT

SwingConstants.CENTER

SwingConstants.LEADING

SwingConstants.TRAILING

**Parameters:** key

- the property value to check
**Parameters:** exception

- the message to use in the

IllegalArgumentException

that is thrown for an invalid
value
**Returns:** the

key

argument
**Throws:** IllegalArgumentException

- if key is not one of the legal
values listed above
**See Also:** setHorizontalTextPosition(int)

,

setHorizontalAlignment(int)

- checkVerticalKey

```java
protected int checkVerticalKey​(int key,

String
exception)
```

Verify that the

key

argument is a legal value for the
vertical properties. Valid values are:

- SwingConstants.CENTER

SwingConstants.TOP

SwingConstants.BOTTOM

**Parameters:** key

- the property value to check
**Parameters:** exception

- the message to use in the

IllegalArgumentException

that is thrown for an invalid
value
**Returns:** the

key

argument
**Throws:** IllegalArgumentException

- if key is not one of the legal
values listed above

- removeNotify

```java
public void removeNotify()
```

Notifies this component that it no longer has a parent component.
When this method is invoked, any

KeyboardAction

s
set up in the chain of parent components are removed.
This method is called by the toolkit internally and should
not be called directly by programs.

**Overrides:** removeNotify

in class

JComponent
**Since:** 1.6
**See Also:** JComponent.registerKeyboardAction(java.awt.event.ActionListener, java.lang.String, javax.swing.KeyStroke, int)

- setActionCommand

```java
public void setActionCommand​(
String
actionCommand)
```

Sets the action command for this button.

**Parameters:** actionCommand

- the action command for this button

- getActionCommand

```java
public
String
getActionCommand()
```

Returns the action command for this button.

**Returns:** the action command for this button

- setAction

```java
@BeanProperty
(
visualUpdate
=true,

description
="the Action instance connected with this ActionEvent source")
public void setAction​(
Action
a)
```

Sets the

Action

.
The new

Action

replaces any previously set

Action

but does not affect

ActionListeners

independently added with

addActionListener

.
If the

Action

is already a registered

ActionListener

for the button, it is not re-registered.

Setting the

Action

results in immediately changing
all the properties described in

Swing Components Supporting

Action

.
Subsequently, the button's properties are automatically updated
as the

Action

's properties change.

This method uses three other methods to set
and help track the

Action

's property values.
It uses the

configurePropertiesFromAction

method
to immediately change the button's properties.
To track changes in the

Action

's property values,
this method registers the

PropertyChangeListener

returned by

createActionPropertyChangeListener

. The
default

PropertyChangeListener

invokes the

actionPropertyChanged

method when a property in the

Action

changes.

**Parameters:** a

- the

Action

for the

AbstractButton

,
or

null
**Since:** 1.3
**See Also:** Action

,

getAction()

,

configurePropertiesFromAction(javax.swing.Action)

,

createActionPropertyChangeListener(javax.swing.Action)

,

actionPropertyChanged(javax.swing.Action, java.lang.String)

- getAction

```java
public
Action
getAction()
```

Returns the currently set

Action

for this

ActionEvent

source, or

null

if no

Action

is set.

**Returns:** the

Action

for this

ActionEvent

source, or

null
**Since:** 1.3
**See Also:** Action

,

setAction(javax.swing.Action)

- configurePropertiesFromAction

```java
protected void configurePropertiesFromAction​(
Action
a)
```

Sets the properties on this button to match those in the specified

Action

. Refer to

Swing Components Supporting

Action

for more
details as to which properties this sets.

**Parameters:** a

- the

Action

from which to get the properties,
or

null
**Since:** 1.3
**See Also:** Action

,

setAction(javax.swing.Action)

- actionPropertyChanged

```java
protected void actionPropertyChanged​(
Action
action,

String
propertyName)
```

Updates the button's state in response to property changes in the
associated action. This method is invoked from the

PropertyChangeListener

returned from

createActionPropertyChangeListener

. Subclasses do not normally
need to invoke this. Subclasses that support additional

Action

properties should override this and

configurePropertiesFromAction

.

Refer to the table at

Swing Components Supporting

Action

for a list of
the properties this method sets.

**Parameters:** action

- the

Action

associated with this button
**Parameters:** propertyName

- the name of the property that changed
**Since:** 1.6
**See Also:** Action

,

configurePropertiesFromAction(javax.swing.Action)

- createActionPropertyChangeListener

```java
protected
PropertyChangeListener
createActionPropertyChangeListener​(
Action
a)
```

Creates and returns a

PropertyChangeListener

that is
responsible for listening for changes from the specified

Action

and updating the appropriate properties.

Warning:

If you subclass this do not create an anonymous
inner class. If you do the lifetime of the button will be tied to
that of the

Action

.

**Parameters:** a

- the button's action
**Returns:** the

PropertyChangeListener
**Since:** 1.3
**See Also:** Action

,

setAction(javax.swing.Action)

- isBorderPainted

```java
public boolean isBorderPainted()
```

Gets the

borderPainted

property.

**Returns:** the value of the

borderPainted

property
**See Also:** setBorderPainted(boolean)

- setBorderPainted

```java
@BeanProperty
(
visualUpdate
=true,

description
="Whether the border should be painted.")
public void setBorderPainted​(boolean b)
```

Sets the

borderPainted

property.
If

true

and the button has a border,
the border is painted. The default value for the

borderPainted

property is

true

.

Some look and feels might not support
the

borderPainted

property,
in which case they ignore this.

**Parameters:** b

- if true and border property is not

null

,
the border is painted
**See Also:** isBorderPainted()

- paintBorder

```java
protected void paintBorder​(
Graphics
g)
```

Paint the button's border if

BorderPainted

property is true and the button has a border.

**Overrides:** paintBorder

in class

JComponent
**Parameters:** g

- the

Graphics

context in which to paint
**See Also:** JComponent.paint(java.awt.Graphics)

,

JComponent.setBorder(javax.swing.border.Border)

- isFocusPainted

```java
public boolean isFocusPainted()
```

Gets the

paintFocus

property.

**Returns:** the

paintFocus

property
**See Also:** setFocusPainted(boolean)

- setFocusPainted

```java
@BeanProperty
(
visualUpdate
=true,

description
="Whether focus should be painted")
public void setFocusPainted​(boolean b)
```

Sets the

paintFocus

property, which must
be

true

for the focus state to be painted.
The default value for the

paintFocus

property
is

true

.
Some look and feels might not paint focus state;
they will ignore this property.

**Parameters:** b

- if

true

, the focus state should be painted
**See Also:** isFocusPainted()

- isContentAreaFilled

```java
public boolean isContentAreaFilled()
```

Gets the

contentAreaFilled

property.

**Returns:** the

contentAreaFilled

property
**See Also:** setContentAreaFilled(boolean)

- setContentAreaFilled

```java
@BeanProperty
(
visualUpdate
=true,

description
="Whether the button should paint the content area or leave it transparent.")
public void setContentAreaFilled​(boolean b)
```

Sets the

contentAreaFilled

property.
If

true

the button will paint the content
area. If you wish to have a transparent button, such as
an icon only button, for example, then you should set
this to

false

. Do not call

setOpaque(false)

.
The default value for the

contentAreaFilled

property is

true

.

This function may cause the component's opaque property to change.

The exact behavior of calling this function varies on a
component-by-component and L&F-by-L&F basis.

**Parameters:** b

- if true, the content should be filled; if false
the content area is not filled
**See Also:** isContentAreaFilled()

,

JComponent.setOpaque(boolean)

- isRolloverEnabled

```java
public boolean isRolloverEnabled()
```

Gets the

rolloverEnabled

property.

**Returns:** the value of the

rolloverEnabled

property
**See Also:** setRolloverEnabled(boolean)

- setRolloverEnabled

```java
@BeanProperty
(
visualUpdate
=true,

description
="Whether rollover effects should be enabled.")
public void setRolloverEnabled​(boolean b)
```

Sets the

rolloverEnabled

property, which
must be

true

for rollover effects to occur.
The default value for the

rolloverEnabled

property is

false

.
Some look and feels might not implement rollover effects;
they will ignore this property.

**Parameters:** b

- if

true

, rollover effects should be painted
**See Also:** isRolloverEnabled()

- getMnemonic

```java
public int getMnemonic()
```

Returns the keyboard mnemonic from the current model.

**Returns:** the keyboard mnemonic from the model

- setMnemonic

```java
@BeanProperty
(
visualUpdate
=true,

description
="the keyboard character mnemonic")
public void setMnemonic​(int mnemonic)
```

Sets the keyboard mnemonic on the current model.
The mnemonic is the key which when combined with the look and feel's
mouseless modifier (usually Alt) will activate this button
if focus is contained somewhere within this button's ancestor
window.

A mnemonic must correspond to a single key on the keyboard
and should be specified using one of the

VK_XXX

keycodes defined in

java.awt.event.KeyEvent

.
These codes and the wider array of codes for international
keyboards may be obtained through

java.awt.event.KeyEvent.getExtendedKeyCodeForChar

.
Mnemonics are case-insensitive, therefore a key event
with the corresponding keycode would cause the button to be
activated whether or not the Shift modifier was pressed.

If the character defined by the mnemonic is found within
the button's label string, the first occurrence of it
will be underlined to indicate the mnemonic to the user.

**Parameters:** mnemonic

- the key code which represents the mnemonic
**See Also:** KeyEvent

,

setDisplayedMnemonicIndex(int)

- setMnemonic

```java
@BeanProperty
(
visualUpdate
=true,

description
="the keyboard character mnemonic")
public void setMnemonic​(char mnemonic)
```

This method is now obsolete, please use

setMnemonic(int)

to set the mnemonic for a button. This method is only designed
to handle character values which fall between 'a' and 'z' or
'A' and 'Z'.

**Parameters:** mnemonic

- a char specifying the mnemonic value
**See Also:** setMnemonic(int)

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

setMnemonic(KeyEvent.VK_A)

.

**Parameters:** index

- Index into the String to underline
**Throws:** IllegalArgumentException

- will be thrown if

index

is >= length of the text, or < -1
**Since:** 1.4
**See Also:** getDisplayedMnemonicIndex()

- getDisplayedMnemonicIndex

```java
public int getDisplayedMnemonicIndex()
```

Returns the character, as an index, that the look and feel should
provide decoration for as representing the mnemonic character.

**Returns:** index representing mnemonic character
**Since:** 1.4
**See Also:** setDisplayedMnemonicIndex(int)

- setMultiClickThreshhold

```java
public void setMultiClickThreshhold​(long threshhold)
```

Sets the amount of time (in milliseconds) required between
mouse press events for the button to generate the corresponding
action events. After the initial mouse press occurs (and action
event generated) any subsequent mouse press events which occur
on intervals less than the threshhold will be ignored and no
corresponding action event generated. By default the threshhold is 0,
which means that for each mouse press, an action event will be
fired, no matter how quickly the mouse clicks occur. In buttons
where this behavior is not desirable (for example, the "OK" button
in a dialog), this threshhold should be set to an appropriate
positive value.

**Parameters:** threshhold

- the amount of time required between mouse
press events to generate corresponding action events
**Throws:** IllegalArgumentException

- if threshhold < 0
**Since:** 1.4
**See Also:** getMultiClickThreshhold()

- getMultiClickThreshhold

```java
public long getMultiClickThreshhold()
```

Gets the amount of time (in milliseconds) required between
mouse press events for the button to generate the corresponding
action events.

**Returns:** the amount of time required between mouse press events
to generate corresponding action events
**Since:** 1.4
**See Also:** setMultiClickThreshhold(long)

- getModel

```java
public
ButtonModel
getModel()
```

Returns the model that this button represents.

**Returns:** the

model

property
**See Also:** setModel(javax.swing.ButtonModel)

- setModel

```java
@BeanProperty
(
description
="Model that the Button uses.")
public void setModel​(
ButtonModel
newModel)
```

Sets the model that this button represents.

**Parameters:** newModel

- the new

ButtonModel
**See Also:** getModel()

- getUI

```java
public
ButtonUI
getUI()
```

Returns the L&F object that renders this component.

**Overrides:** getUI

in class

JComponent
**Returns:** the ButtonUI object
**See Also:** setUI(javax.swing.plaf.ButtonUI)

- setUI

```java
@BeanProperty
(
hidden
=true,

visualUpdate
=true,

description
="The UI object that implements the LookAndFeel.")
public void setUI​(
ButtonUI
ui)
```

Sets the L&F object that renders this component.

**Parameters:** ui

- the

ButtonUI

L&F object
**See Also:** getUI()

- updateUI

```java
public void updateUI()
```

Resets the UI property to a value from the current look
and feel. Subtypes of

AbstractButton

should override this to update the UI. For
example,

JButton

might do the following:

```java
setUI((ButtonUI)UIManager.getUI(
"ButtonUI", "javax.swing.plaf.basic.BasicButtonUI", this));
```

**Overrides:** updateUI

in class

JComponent
**See Also:** JComponent.setUI(javax.swing.plaf.ComponentUI)

,

UIManager.getLookAndFeel()

,

UIManager.getUI(javax.swing.JComponent)

- addImpl

```java
protected void addImpl​(
Component
comp,

Object
constraints,
int index)
```

Adds the specified component to this container at the specified
index, refer to

Container.addImpl(Component, Object, int)

for a complete description of this method.

**Overrides:** addImpl

in class

Container
**Parameters:** comp

- the component to be added
**Parameters:** constraints

- an object expressing layout constraints
for this component
**Parameters:** index

- the position in the container's list at which to
insert the component, where

-1

means append to the end
**Throws:** IllegalArgumentException

- if

index

is invalid
**Throws:** IllegalArgumentException

- if adding the container's parent
to itself
**Throws:** IllegalArgumentException

- if adding a window to a container
**Since:** 1.5
**See Also:** Container.add(Component)

,

Container.add(Component, int)

,

Container.add(Component, java.lang.Object)

,

Container.invalidate()

,

LayoutManager

,

LayoutManager2

- setLayout

```java
public void setLayout​(
LayoutManager
mgr)
```

Sets the layout manager for this container, refer to

Container.setLayout(LayoutManager)

for a complete description of this method.

**Overrides:** setLayout

in class

Container
**Parameters:** mgr

- the specified layout manager
**Since:** 1.5
**See Also:** Container.doLayout()

,

Container.getLayout()

,

Container.invalidate()

- addChangeListener

```java
public void addChangeListener​(
ChangeListener
l)
```

Adds a

ChangeListener

to the button.

**Parameters:** l

- the listener to be added

- removeChangeListener

```java
public void removeChangeListener​(
ChangeListener
l)
```

Removes a ChangeListener from the button.

**Parameters:** l

- the listener to be removed

- getChangeListeners

```java
@BeanProperty
(
bound
=false)
public
ChangeListener
[] getChangeListeners()
```

Returns an array of all the

ChangeListener

s added
to this AbstractButton with addChangeListener().

**Returns:** all of the

ChangeListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

- fireStateChanged

```java
protected void fireStateChanged()
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created.

**See Also:** EventListenerList

- addActionListener

```java
public void addActionListener​(
ActionListener
l)
```

Adds an

ActionListener

to the button.

**Parameters:** l

- the

ActionListener

to be added

- removeActionListener

```java
public void removeActionListener​(
ActionListener
l)
```

Removes an

ActionListener

from the button.
If the listener is the currently set

Action

for the button, then the

Action

is set to

null

.

**Parameters:** l

- the listener to be removed

- getActionListeners

```java
@BeanProperty
(
bound
=false)
public
ActionListener
[] getActionListeners()
```

Returns an array of all the

ActionListener

s added
to this AbstractButton with addActionListener().

**Returns:** all of the

ActionListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

- createChangeListener

```java
protected
ChangeListener
createChangeListener()
```

Subclasses that want to handle

ChangeEvents

differently
can override this to return another

ChangeListener

implementation.

**Returns:** the new

ChangeListener

- fireActionPerformed

```java
protected void fireActionPerformed​(
ActionEvent
event)
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the

event

parameter.

**Parameters:** event

- the

ActionEvent

object
**See Also:** EventListenerList

- fireItemStateChanged

```java
protected void fireItemStateChanged​(
ItemEvent
event)
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the

event

parameter.

**Parameters:** event

- the

ItemEvent

object
**See Also:** EventListenerList

- createActionListener

```java
protected
ActionListener
createActionListener()
```

Returns

ActionListener

that is added to model.

**Returns:** the

ActionListener

- createItemListener

```java
protected
ItemListener
createItemListener()
```

Returns

ItemListener

that is added to model.

**Returns:** the

ItemListener

- setEnabled

```java
public void setEnabled​(boolean b)
```

Enables (or disables) the button.

**Overrides:** setEnabled

in class

JComponent
**Parameters:** b

- true to enable the button, otherwise false
**See Also:** Component.isEnabled()

,

Component.isLightweight()

- getLabel

```java
@Deprecated

public
String
getLabel()
```

Deprecated.

- Replaced by

getText

Returns the label text.

**Returns:** a

String

containing the label

- setLabel

```java
@Deprecated

@BeanProperty
(
description
="Replace by setText(text)")
public void setLabel​(
String
label)
```

Deprecated.

- Replaced by

setText(text)

Sets the label text.

**Parameters:** label

- a

String

containing the text

- addItemListener

```java
public void addItemListener​(
ItemListener
l)
```

Adds an

ItemListener

to the

checkbox

.

**Specified by:** addItemListener

in interface

ItemSelectable
**Parameters:** l

- the

ItemListener

to be added
**See Also:** ItemEvent

- removeItemListener

```java
public void removeItemListener​(
ItemListener
l)
```

Removes an

ItemListener

from the button.

**Specified by:** removeItemListener

in interface

ItemSelectable
**Parameters:** l

- the

ItemListener

to be removed
**See Also:** ItemEvent

- getItemListeners

```java
@BeanProperty
(
bound
=false)
public
ItemListener
[] getItemListeners()
```

Returns an array of all the

ItemListener

s added
to this AbstractButton with addItemListener().

**Returns:** all of the

ItemListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

- getSelectedObjects

```java
@BeanProperty
(
bound
=false)
public
Object
[] getSelectedObjects()
```

Returns an array (length 1) containing the label or

null

if the button is not selected.

**Specified by:** getSelectedObjects

in interface

ItemSelectable
**Returns:** an array containing 1 Object: the text of the button,
if the item is selected; otherwise

null

- init

```java
protected void init​(
String
text,

Icon
icon)
```

Initialization of the

AbstractButton

.

**Parameters:** text

- the text of the button
**Parameters:** icon

- the Icon image to display on the button

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

This is overridden to return false if the current

Icon

's

Image

is not equal to the
passed in

Image

img

.

**Specified by:** imageUpdate

in interface

ImageObserver
**Overrides:** imageUpdate

in class

Component
**Parameters:** img

- the

Image

to be compared
**Parameters:** infoflags

- flags used to repaint the button when the image
is updated and which determine how much is to be painted
**Parameters:** x

- the x coordinate
**Parameters:** y

- the y coordinate
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

Returns a string representation of this

AbstractButton

.
This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

Overriding

paramString

to provide information about the
specific new aspects of the JFC components.

**Overrides:** paramString

in class

JComponent
**Returns:** a string representation of this

AbstractButton

---

#### Method Detail

setHideActionText

```java
@BeanProperty
(
expert
=true,

description
="Whether the text of the button should come from the <code>Action</code>.")
public void setHideActionText​(boolean hideActionText)
```

Sets the

hideActionText

property, which determines
whether the button displays text from the

Action

.
This is useful only if an

Action

has been
installed on the button.

**Parameters:** hideActionText

-

true

if the button's

text

property should not reflect
that of the

Action

; the default is

false
**Since:** 1.6
**See Also:** Swing Components Supporting

Action

---

#### setHideActionText

@BeanProperty

(

expert

=true,

description

="Whether the text of the button should come from the <code>Action</code>.")
public void setHideActionText​(boolean hideActionText)

Sets the

hideActionText

property, which determines
whether the button displays text from the

Action

.
This is useful only if an

Action

has been
installed on the button.

getHideActionText

```java
public boolean getHideActionText()
```

Returns the value of the

hideActionText

property, which
determines whether the button displays text from the

Action

. This is useful only if an

Action

has been installed on the button.

**Returns:** true

if the button's

text

property should not reflect that of the

Action

; the default is

false
**Since:** 1.6

---

#### getHideActionText

public boolean getHideActionText()

Returns the value of the

hideActionText

property, which
determines whether the button displays text from the

Action

. This is useful only if an

Action

has been installed on the button.

getText

```java
public
String
getText()
```

Returns the button's text.

**Returns:** the buttons text
**See Also:** setText(java.lang.String)

---

#### getText

public

String

getText()

Returns the button's text.

setText

```java
@BeanProperty
(
preferred
=true,

visualUpdate
=true,

description
="The button\'s text.")
public void setText​(
String
text)
```

Sets the button's text.

**Parameters:** text

- the string used to set the text
**See Also:** getText()

---

#### setText

@BeanProperty

(

preferred

=true,

visualUpdate

=true,

description

="The button\'s text.")
public void setText​(

String

text)

Sets the button's text.

isSelected

```java
public boolean isSelected()
```

Returns the state of the button. True if the
toggle button is selected, false if it's not.

**Returns:** true if the toggle button is selected, otherwise false

---

#### isSelected

public boolean isSelected()

Returns the state of the button. True if the
toggle button is selected, false if it's not.

setSelected

```java
public void setSelected​(boolean b)
```

Sets the state of the button. Note that this method does not
trigger an

actionEvent

.
Call

doClick

to perform a programmatic action change.

**Parameters:** b

- true if the button is selected, otherwise false

---

#### setSelected

public void setSelected​(boolean b)

Sets the state of the button. Note that this method does not
trigger an

actionEvent

.
Call

doClick

to perform a programmatic action change.

doClick

```java
public void doClick()
```

Programmatically perform a "click". This does the same
thing as if the user had pressed and released the button.

---

#### doClick

public void doClick()

Programmatically perform a "click". This does the same
thing as if the user had pressed and released the button.

doClick

```java
public void doClick​(int pressTime)
```

Programmatically perform a "click". This does the same
thing as if the user had pressed and released the button.
The button stays visually "pressed" for

pressTime

milliseconds.

**Parameters:** pressTime

- the time to "hold down" the button, in milliseconds

---

#### doClick

public void doClick​(int pressTime)

Programmatically perform a "click". This does the same
thing as if the user had pressed and released the button.
The button stays visually "pressed" for

pressTime

milliseconds.

setMargin

```java
@BeanProperty
(
visualUpdate
=true,

description
="The space between the button\'s border and the label.")
public void setMargin​(
Insets
m)
```

Sets space for margin between the button's border and
the label. Setting to

null

will cause the button to
use the default margin. The button's default

Border

object will use this value to create the proper margin.
However, if a non-default border is set on the button,
it is that

Border

object's responsibility to create the
appropriate margin space (else this property will
effectively be ignored).

**Parameters:** m

- the space between the border and the label

---

#### setMargin

@BeanProperty

(

visualUpdate

=true,

description

="The space between the button\'s border and the label.")
public void setMargin​(

Insets

m)

Sets space for margin between the button's border and
the label. Setting to

null

will cause the button to
use the default margin. The button's default

Border

object will use this value to create the proper margin.
However, if a non-default border is set on the button,
it is that

Border

object's responsibility to create the
appropriate margin space (else this property will
effectively be ignored).

getMargin

```java
public
Insets
getMargin()
```

Returns the margin between the button's border and
the label.

**Returns:** an

Insets

object specifying the margin
between the botton's border and the label
**See Also:** setMargin(java.awt.Insets)

---

#### getMargin

public

Insets

getMargin()

Returns the margin between the button's border and
the label.

getIcon

```java
public
Icon
getIcon()
```

Returns the default icon.

**Returns:** the default

Icon
**See Also:** setIcon(javax.swing.Icon)

---

#### getIcon

public

Icon

getIcon()

Returns the default icon.

setIcon

```java
@BeanProperty
(
visualUpdate
=true,

description
="The button\'s default icon")
public void setIcon​(
Icon
defaultIcon)
```

Sets the button's default icon. This icon is
also used as the "pressed" and "disabled" icon if
there is no explicitly set pressed icon.

**Parameters:** defaultIcon

- the icon used as the default image
**See Also:** getIcon()

,

setPressedIcon(javax.swing.Icon)

---

#### setIcon

@BeanProperty

(

visualUpdate

=true,

description

="The button\'s default icon")
public void setIcon​(

Icon

defaultIcon)

Sets the button's default icon. This icon is
also used as the "pressed" and "disabled" icon if
there is no explicitly set pressed icon.

getPressedIcon

```java
public
Icon
getPressedIcon()
```

Returns the pressed icon for the button.

**Returns:** the

pressedIcon

property
**See Also:** setPressedIcon(javax.swing.Icon)

---

#### getPressedIcon

public

Icon

getPressedIcon()

Returns the pressed icon for the button.

setPressedIcon

```java
@BeanProperty
(
visualUpdate
=true,

description
="The pressed icon for the button.")
public void setPressedIcon​(
Icon
pressedIcon)
```

Sets the pressed icon for the button.

**Parameters:** pressedIcon

- the icon used as the "pressed" image
**See Also:** getPressedIcon()

---

#### setPressedIcon

@BeanProperty

(

visualUpdate

=true,

description

="The pressed icon for the button.")
public void setPressedIcon​(

Icon

pressedIcon)

Sets the pressed icon for the button.

getSelectedIcon

```java
public
Icon
getSelectedIcon()
```

Returns the selected icon for the button.

**Returns:** the

selectedIcon

property
**See Also:** setSelectedIcon(javax.swing.Icon)

---

#### getSelectedIcon

public

Icon

getSelectedIcon()

Returns the selected icon for the button.

setSelectedIcon

```java
@BeanProperty
(
visualUpdate
=true,

description
="The selected icon for the button.")
public void setSelectedIcon​(
Icon
selectedIcon)
```

Sets the selected icon for the button.

**Parameters:** selectedIcon

- the icon used as the "selected" image
**See Also:** getSelectedIcon()

---

#### setSelectedIcon

@BeanProperty

(

visualUpdate

=true,

description

="The selected icon for the button.")
public void setSelectedIcon​(

Icon

selectedIcon)

Sets the selected icon for the button.

getRolloverIcon

```java
public
Icon
getRolloverIcon()
```

Returns the rollover icon for the button.

**Returns:** the

rolloverIcon

property
**See Also:** setRolloverIcon(javax.swing.Icon)

---

#### getRolloverIcon

public

Icon

getRolloverIcon()

Returns the rollover icon for the button.

setRolloverIcon

```java
@BeanProperty
(
visualUpdate
=true,

description
="The rollover icon for the button.")
public void setRolloverIcon​(
Icon
rolloverIcon)
```

Sets the rollover icon for the button.

**Parameters:** rolloverIcon

- the icon used as the "rollover" image
**See Also:** getRolloverIcon()

---

#### setRolloverIcon

@BeanProperty

(

visualUpdate

=true,

description

="The rollover icon for the button.")
public void setRolloverIcon​(

Icon

rolloverIcon)

Sets the rollover icon for the button.

getRolloverSelectedIcon

```java
public
Icon
getRolloverSelectedIcon()
```

Returns the rollover selection icon for the button.

**Returns:** the

rolloverSelectedIcon

property
**See Also:** setRolloverSelectedIcon(javax.swing.Icon)

---

#### getRolloverSelectedIcon

public

Icon

getRolloverSelectedIcon()

Returns the rollover selection icon for the button.

setRolloverSelectedIcon

```java
@BeanProperty
(
visualUpdate
=true,

description
="The rollover selected icon for the button.")
public void setRolloverSelectedIcon​(
Icon
rolloverSelectedIcon)
```

Sets the rollover selected icon for the button.

**Parameters:** rolloverSelectedIcon

- the icon used as the
"selected rollover" image
**See Also:** getRolloverSelectedIcon()

---

#### setRolloverSelectedIcon

@BeanProperty

(

visualUpdate

=true,

description

="The rollover selected icon for the button.")
public void setRolloverSelectedIcon​(

Icon

rolloverSelectedIcon)

Sets the rollover selected icon for the button.

getDisabledIcon

```java
public
Icon
getDisabledIcon()
```

Returns the icon used by the button when it's disabled.
If no disabled icon has been set this will forward the call to
the look and feel to construct an appropriate disabled Icon.

Some look and feels might not render the disabled Icon, in which
case they will ignore this.

**Returns:** the

disabledIcon

property
**See Also:** getPressedIcon()

,

setDisabledIcon(javax.swing.Icon)

,

LookAndFeel.getDisabledIcon(javax.swing.JComponent, javax.swing.Icon)

---

#### getDisabledIcon

public

Icon

getDisabledIcon()

Returns the icon used by the button when it's disabled.
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
="The disabled icon for the button.")
public void setDisabledIcon​(
Icon
disabledIcon)
```

Sets the disabled icon for the button.

**Parameters:** disabledIcon

- the icon used as the disabled image
**See Also:** getDisabledIcon()

---

#### setDisabledIcon

@BeanProperty

(

visualUpdate

=true,

description

="The disabled icon for the button.")
public void setDisabledIcon​(

Icon

disabledIcon)

Sets the disabled icon for the button.

getDisabledSelectedIcon

```java
public
Icon
getDisabledSelectedIcon()
```

Returns the icon used by the button when it's disabled and selected.
If no disabled selection icon has been set, this will forward
the call to the LookAndFeel to construct an appropriate disabled
Icon from the selection icon if it has been set and to

getDisabledIcon()

otherwise.

Some look and feels might not render the disabled selected Icon, in
which case they will ignore this.

**Returns:** the

disabledSelectedIcon

property
**See Also:** getDisabledIcon()

,

setDisabledSelectedIcon(javax.swing.Icon)

,

LookAndFeel.getDisabledSelectedIcon(javax.swing.JComponent, javax.swing.Icon)

---

#### getDisabledSelectedIcon

public

Icon

getDisabledSelectedIcon()

Returns the icon used by the button when it's disabled and selected.
If no disabled selection icon has been set, this will forward
the call to the LookAndFeel to construct an appropriate disabled
Icon from the selection icon if it has been set and to

getDisabledIcon()

otherwise.

Some look and feels might not render the disabled selected Icon, in
which case they will ignore this.

Some look and feels might not render the disabled selected Icon, in
which case they will ignore this.

setDisabledSelectedIcon

```java
@BeanProperty
(
visualUpdate
=true,

description
="The disabled selection icon for the button.")
public void setDisabledSelectedIcon​(
Icon
disabledSelectedIcon)
```

Sets the disabled selection icon for the button.

**Parameters:** disabledSelectedIcon

- the icon used as the disabled
selection image
**See Also:** getDisabledSelectedIcon()

---

#### setDisabledSelectedIcon

@BeanProperty

(

visualUpdate

=true,

description

="The disabled selection icon for the button.")
public void setDisabledSelectedIcon​(

Icon

disabledSelectedIcon)

Sets the disabled selection icon for the button.

getVerticalAlignment

```java
public int getVerticalAlignment()
```

Returns the vertical alignment of the text and icon.

**Returns:** the

verticalAlignment

property, one of the
following values:

- SwingConstants.CENTER

(the default)

SwingConstants.TOP

SwingConstants.BOTTOM

---

#### getVerticalAlignment

public int getVerticalAlignment()

Returns the vertical alignment of the text and icon.

SwingConstants.CENTER

(the default)

SwingConstants.TOP

SwingConstants.BOTTOM

setVerticalAlignment

```java
@BeanProperty
(
visualUpdate
=true,

enumerationValues
={"SwingConstants.TOP","SwingConstants.CENTER","SwingConstants.BOTTOM"},

description
="The vertical alignment of the icon and text.")
public void setVerticalAlignment​(int alignment)
```

Sets the vertical alignment of the icon and text.

**Parameters:** alignment

- one of the following values:

- SwingConstants.CENTER

(the default)

SwingConstants.TOP

SwingConstants.BOTTOM
**Throws:** IllegalArgumentException

- if the alignment is not one of the legal
values listed above

---

#### setVerticalAlignment

@BeanProperty

(

visualUpdate

=true,

enumerationValues

={"SwingConstants.TOP","SwingConstants.CENTER","SwingConstants.BOTTOM"},

description

="The vertical alignment of the icon and text.")
public void setVerticalAlignment​(int alignment)

Sets the vertical alignment of the icon and text.

SwingConstants.CENTER

(the default)

SwingConstants.TOP

SwingConstants.BOTTOM

getHorizontalAlignment

```java
public int getHorizontalAlignment()
```

Returns the horizontal alignment of the icon and text.

AbstractButton

's default is

SwingConstants.CENTER

,
but subclasses such as

JCheckBox

may use a different default.

**Returns:** the

horizontalAlignment

property,
one of the following values:

- SwingConstants.RIGHT

SwingConstants.LEFT

SwingConstants.CENTER

SwingConstants.LEADING

SwingConstants.TRAILING

---

#### getHorizontalAlignment

public int getHorizontalAlignment()

Returns the horizontal alignment of the icon and text.

AbstractButton

's default is

SwingConstants.CENTER

,
but subclasses such as

JCheckBox

may use a different default.

SwingConstants.RIGHT

SwingConstants.LEFT

SwingConstants.CENTER

SwingConstants.LEADING

SwingConstants.TRAILING

setHorizontalAlignment

```java
@BeanProperty
(
visualUpdate
=true,

enumerationValues
={"SwingConstants.LEFT","SwingConstants.CENTER","SwingConstants.RIGHT","SwingConstants.LEADING","SwingConstants.TRAILING"},

description
="The horizontal alignment of the icon and text.")
public void setHorizontalAlignment​(int alignment)
```

Sets the horizontal alignment of the icon and text.

AbstractButton

's default is

SwingConstants.CENTER

,
but subclasses such as

JCheckBox

may use a different default.

**Parameters:** alignment

- the alignment value, one of the following values:

- SwingConstants.RIGHT

SwingConstants.LEFT

SwingConstants.CENTER

SwingConstants.LEADING

SwingConstants.TRAILING
**Throws:** IllegalArgumentException

- if the alignment is not one of the
valid values

---

#### setHorizontalAlignment

@BeanProperty

(

visualUpdate

=true,

enumerationValues

={"SwingConstants.LEFT","SwingConstants.CENTER","SwingConstants.RIGHT","SwingConstants.LEADING","SwingConstants.TRAILING"},

description

="The horizontal alignment of the icon and text.")
public void setHorizontalAlignment​(int alignment)

Sets the horizontal alignment of the icon and text.

AbstractButton

's default is

SwingConstants.CENTER

,
but subclasses such as

JCheckBox

may use a different default.

SwingConstants.RIGHT

SwingConstants.LEFT

SwingConstants.CENTER

SwingConstants.LEADING

SwingConstants.TRAILING

getVerticalTextPosition

```java
public int getVerticalTextPosition()
```

Returns the vertical position of the text relative to the icon.

**Returns:** the

verticalTextPosition

property,
one of the following values:

- SwingConstants.CENTER

(the default)

SwingConstants.TOP

SwingConstants.BOTTOM

---

#### getVerticalTextPosition

public int getVerticalTextPosition()

Returns the vertical position of the text relative to the icon.

SwingConstants.CENTER

(the default)

SwingConstants.TOP

SwingConstants.BOTTOM

setVerticalTextPosition

```java
@BeanProperty
(
visualUpdate
=true,

enumerationValues
={"SwingConstants.TOP","SwingConstants.CENTER","SwingConstants.BOTTOM"},

description
="The vertical position of the text relative to the icon.")
public void setVerticalTextPosition​(int textPosition)
```

Sets the vertical position of the text relative to the icon.

**Parameters:** textPosition

- one of the following values:

- SwingConstants.CENTER

(the default)

SwingConstants.TOP

SwingConstants.BOTTOM

---

#### setVerticalTextPosition

@BeanProperty

(

visualUpdate

=true,

enumerationValues

={"SwingConstants.TOP","SwingConstants.CENTER","SwingConstants.BOTTOM"},

description

="The vertical position of the text relative to the icon.")
public void setVerticalTextPosition​(int textPosition)

Sets the vertical position of the text relative to the icon.

SwingConstants.CENTER

(the default)

SwingConstants.TOP

SwingConstants.BOTTOM

getHorizontalTextPosition

```java
public int getHorizontalTextPosition()
```

Returns the horizontal position of the text relative to the icon.

**Returns:** the

horizontalTextPosition

property,
one of the following values:

- SwingConstants.RIGHT

SwingConstants.LEFT

SwingConstants.CENTER

SwingConstants.LEADING

SwingConstants.TRAILING

(the default)

---

#### getHorizontalTextPosition

public int getHorizontalTextPosition()

Returns the horizontal position of the text relative to the icon.

SwingConstants.RIGHT

SwingConstants.LEFT

SwingConstants.CENTER

SwingConstants.LEADING

SwingConstants.TRAILING

(the default)

setHorizontalTextPosition

```java
@BeanProperty
(
visualUpdate
=true,

enumerationValues
={"SwingConstants.LEFT","SwingConstants.CENTER","SwingConstants.RIGHT","SwingConstants.LEADING","SwingConstants.TRAILING"},

description
="The horizontal position of the text relative to the icon.")
public void setHorizontalTextPosition​(int textPosition)
```

Sets the horizontal position of the text relative to the icon.

**Parameters:** textPosition

- one of the following values:

- SwingConstants.RIGHT

SwingConstants.LEFT

SwingConstants.CENTER

SwingConstants.LEADING

SwingConstants.TRAILING

(the default)
**Throws:** IllegalArgumentException

- if

textPosition

is not one of the legal values listed above

---

#### setHorizontalTextPosition

@BeanProperty

(

visualUpdate

=true,

enumerationValues

={"SwingConstants.LEFT","SwingConstants.CENTER","SwingConstants.RIGHT","SwingConstants.LEADING","SwingConstants.TRAILING"},

description

="The horizontal position of the text relative to the icon.")
public void setHorizontalTextPosition​(int textPosition)

Sets the horizontal position of the text relative to the icon.

SwingConstants.RIGHT

SwingConstants.LEFT

SwingConstants.CENTER

SwingConstants.LEADING

SwingConstants.TRAILING

(the default)

getIconTextGap

```java
public int getIconTextGap()
```

Returns the amount of space between the text and the icon
displayed in this button.

**Returns:** an int equal to the number of pixels between the text
and the icon.
**Since:** 1.4
**See Also:** setIconTextGap(int)

---

#### getIconTextGap

public int getIconTextGap()

Returns the amount of space between the text and the icon
displayed in this button.

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

- the space between icon and text if these properties are set.
**Since:** 1.4
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

checkHorizontalKey

```java
protected int checkHorizontalKey​(int key,

String
exception)
```

Verify that the

key

argument is a legal value for the

horizontalAlignment

and

horizontalTextPosition

properties. Valid values are:

- SwingConstants.RIGHT

SwingConstants.LEFT

SwingConstants.CENTER

SwingConstants.LEADING

SwingConstants.TRAILING

**Parameters:** key

- the property value to check
**Parameters:** exception

- the message to use in the

IllegalArgumentException

that is thrown for an invalid
value
**Returns:** the

key

argument
**Throws:** IllegalArgumentException

- if key is not one of the legal
values listed above
**See Also:** setHorizontalTextPosition(int)

,

setHorizontalAlignment(int)

---

#### checkHorizontalKey

protected int checkHorizontalKey​(int key,

String

exception)

Verify that the

key

argument is a legal value for the

horizontalAlignment

and

horizontalTextPosition

properties. Valid values are:

- SwingConstants.RIGHT

SwingConstants.LEFT

SwingConstants.CENTER

SwingConstants.LEADING

SwingConstants.TRAILING

SwingConstants.RIGHT

SwingConstants.LEFT

SwingConstants.CENTER

SwingConstants.LEADING

SwingConstants.TRAILING

checkVerticalKey

```java
protected int checkVerticalKey​(int key,

String
exception)
```

Verify that the

key

argument is a legal value for the
vertical properties. Valid values are:

- SwingConstants.CENTER

SwingConstants.TOP

SwingConstants.BOTTOM

**Parameters:** key

- the property value to check
**Parameters:** exception

- the message to use in the

IllegalArgumentException

that is thrown for an invalid
value
**Returns:** the

key

argument
**Throws:** IllegalArgumentException

- if key is not one of the legal
values listed above

---

#### checkVerticalKey

protected int checkVerticalKey​(int key,

String

exception)

Verify that the

key

argument is a legal value for the
vertical properties. Valid values are:

- SwingConstants.CENTER

SwingConstants.TOP

SwingConstants.BOTTOM

SwingConstants.CENTER

SwingConstants.TOP

SwingConstants.BOTTOM

removeNotify

```java
public void removeNotify()
```

Notifies this component that it no longer has a parent component.
When this method is invoked, any

KeyboardAction

s
set up in the chain of parent components are removed.
This method is called by the toolkit internally and should
not be called directly by programs.

**Overrides:** removeNotify

in class

JComponent
**Since:** 1.6
**See Also:** JComponent.registerKeyboardAction(java.awt.event.ActionListener, java.lang.String, javax.swing.KeyStroke, int)

---

#### removeNotify

public void removeNotify()

Notifies this component that it no longer has a parent component.
When this method is invoked, any

KeyboardAction

s
set up in the chain of parent components are removed.
This method is called by the toolkit internally and should
not be called directly by programs.

setActionCommand

```java
public void setActionCommand​(
String
actionCommand)
```

Sets the action command for this button.

**Parameters:** actionCommand

- the action command for this button

---

#### setActionCommand

public void setActionCommand​(

String

actionCommand)

Sets the action command for this button.

getActionCommand

```java
public
String
getActionCommand()
```

Returns the action command for this button.

**Returns:** the action command for this button

---

#### getActionCommand

public

String

getActionCommand()

Returns the action command for this button.

setAction

```java
@BeanProperty
(
visualUpdate
=true,

description
="the Action instance connected with this ActionEvent source")
public void setAction​(
Action
a)
```

Sets the

Action

.
The new

Action

replaces any previously set

Action

but does not affect

ActionListeners

independently added with

addActionListener

.
If the

Action

is already a registered

ActionListener

for the button, it is not re-registered.

Setting the

Action

results in immediately changing
all the properties described in

Swing Components Supporting

Action

.
Subsequently, the button's properties are automatically updated
as the

Action

's properties change.

This method uses three other methods to set
and help track the

Action

's property values.
It uses the

configurePropertiesFromAction

method
to immediately change the button's properties.
To track changes in the

Action

's property values,
this method registers the

PropertyChangeListener

returned by

createActionPropertyChangeListener

. The
default

PropertyChangeListener

invokes the

actionPropertyChanged

method when a property in the

Action

changes.

**Parameters:** a

- the

Action

for the

AbstractButton

,
or

null
**Since:** 1.3
**See Also:** Action

,

getAction()

,

configurePropertiesFromAction(javax.swing.Action)

,

createActionPropertyChangeListener(javax.swing.Action)

,

actionPropertyChanged(javax.swing.Action, java.lang.String)

---

#### setAction

@BeanProperty

(

visualUpdate

=true,

description

="the Action instance connected with this ActionEvent source")
public void setAction​(

Action

a)

Sets the

Action

.
The new

Action

replaces any previously set

Action

but does not affect

ActionListeners

independently added with

addActionListener

.
If the

Action

is already a registered

ActionListener

for the button, it is not re-registered.

Setting the

Action

results in immediately changing
all the properties described in

Swing Components Supporting

Action

.
Subsequently, the button's properties are automatically updated
as the

Action

's properties change.

This method uses three other methods to set
and help track the

Action

's property values.
It uses the

configurePropertiesFromAction

method
to immediately change the button's properties.
To track changes in the

Action

's property values,
this method registers the

PropertyChangeListener

returned by

createActionPropertyChangeListener

. The
default

PropertyChangeListener

invokes the

actionPropertyChanged

method when a property in the

Action

changes.

Setting the

Action

results in immediately changing
all the properties described in

Swing Components Supporting

Action

.
Subsequently, the button's properties are automatically updated
as the

Action

's properties change.

This method uses three other methods to set
and help track the

Action

's property values.
It uses the

configurePropertiesFromAction

method
to immediately change the button's properties.
To track changes in the

Action

's property values,
this method registers the

PropertyChangeListener

returned by

createActionPropertyChangeListener

. The
default

PropertyChangeListener

invokes the

actionPropertyChanged

method when a property in the

Action

changes.

This method uses three other methods to set
and help track the

Action

's property values.
It uses the

configurePropertiesFromAction

method
to immediately change the button's properties.
To track changes in the

Action

's property values,
this method registers the

PropertyChangeListener

returned by

createActionPropertyChangeListener

. The
default

PropertyChangeListener

invokes the

actionPropertyChanged

method when a property in the

Action

changes.

getAction

```java
public
Action
getAction()
```

Returns the currently set

Action

for this

ActionEvent

source, or

null

if no

Action

is set.

**Returns:** the

Action

for this

ActionEvent

source, or

null
**Since:** 1.3
**See Also:** Action

,

setAction(javax.swing.Action)

---

#### getAction

public

Action

getAction()

Returns the currently set

Action

for this

ActionEvent

source, or

null

if no

Action

is set.

configurePropertiesFromAction

```java
protected void configurePropertiesFromAction​(
Action
a)
```

Sets the properties on this button to match those in the specified

Action

. Refer to

Swing Components Supporting

Action

for more
details as to which properties this sets.

**Parameters:** a

- the

Action

from which to get the properties,
or

null
**Since:** 1.3
**See Also:** Action

,

setAction(javax.swing.Action)

---

#### configurePropertiesFromAction

protected void configurePropertiesFromAction​(

Action

a)

Sets the properties on this button to match those in the specified

Action

. Refer to

Swing Components Supporting

Action

for more
details as to which properties this sets.

actionPropertyChanged

```java
protected void actionPropertyChanged​(
Action
action,

String
propertyName)
```

Updates the button's state in response to property changes in the
associated action. This method is invoked from the

PropertyChangeListener

returned from

createActionPropertyChangeListener

. Subclasses do not normally
need to invoke this. Subclasses that support additional

Action

properties should override this and

configurePropertiesFromAction

.

Refer to the table at

Swing Components Supporting

Action

for a list of
the properties this method sets.

**Parameters:** action

- the

Action

associated with this button
**Parameters:** propertyName

- the name of the property that changed
**Since:** 1.6
**See Also:** Action

,

configurePropertiesFromAction(javax.swing.Action)

---

#### actionPropertyChanged

protected void actionPropertyChanged​(

Action

action,

String

propertyName)

Updates the button's state in response to property changes in the
associated action. This method is invoked from the

PropertyChangeListener

returned from

createActionPropertyChangeListener

. Subclasses do not normally
need to invoke this. Subclasses that support additional

Action

properties should override this and

configurePropertiesFromAction

.

Refer to the table at

Swing Components Supporting

Action

for a list of
the properties this method sets.

Refer to the table at

Swing Components Supporting

Action

for a list of
the properties this method sets.

createActionPropertyChangeListener

```java
protected
PropertyChangeListener
createActionPropertyChangeListener​(
Action
a)
```

Creates and returns a

PropertyChangeListener

that is
responsible for listening for changes from the specified

Action

and updating the appropriate properties.

Warning:

If you subclass this do not create an anonymous
inner class. If you do the lifetime of the button will be tied to
that of the

Action

.

**Parameters:** a

- the button's action
**Returns:** the

PropertyChangeListener
**Since:** 1.3
**See Also:** Action

,

setAction(javax.swing.Action)

---

#### createActionPropertyChangeListener

protected

PropertyChangeListener

createActionPropertyChangeListener​(

Action

a)

Creates and returns a

PropertyChangeListener

that is
responsible for listening for changes from the specified

Action

and updating the appropriate properties.

Warning:

If you subclass this do not create an anonymous
inner class. If you do the lifetime of the button will be tied to
that of the

Action

.

Warning:

If you subclass this do not create an anonymous
inner class. If you do the lifetime of the button will be tied to
that of the

Action

.

isBorderPainted

```java
public boolean isBorderPainted()
```

Gets the

borderPainted

property.

**Returns:** the value of the

borderPainted

property
**See Also:** setBorderPainted(boolean)

---

#### isBorderPainted

public boolean isBorderPainted()

Gets the

borderPainted

property.

setBorderPainted

```java
@BeanProperty
(
visualUpdate
=true,

description
="Whether the border should be painted.")
public void setBorderPainted​(boolean b)
```

Sets the

borderPainted

property.
If

true

and the button has a border,
the border is painted. The default value for the

borderPainted

property is

true

.

Some look and feels might not support
the

borderPainted

property,
in which case they ignore this.

**Parameters:** b

- if true and border property is not

null

,
the border is painted
**See Also:** isBorderPainted()

---

#### setBorderPainted

@BeanProperty

(

visualUpdate

=true,

description

="Whether the border should be painted.")
public void setBorderPainted​(boolean b)

Sets the

borderPainted

property.
If

true

and the button has a border,
the border is painted. The default value for the

borderPainted

property is

true

.

Some look and feels might not support
the

borderPainted

property,
in which case they ignore this.

Some look and feels might not support
the

borderPainted

property,
in which case they ignore this.

paintBorder

```java
protected void paintBorder​(
Graphics
g)
```

Paint the button's border if

BorderPainted

property is true and the button has a border.

**Overrides:** paintBorder

in class

JComponent
**Parameters:** g

- the

Graphics

context in which to paint
**See Also:** JComponent.paint(java.awt.Graphics)

,

JComponent.setBorder(javax.swing.border.Border)

---

#### paintBorder

protected void paintBorder​(

Graphics

g)

Paint the button's border if

BorderPainted

property is true and the button has a border.

isFocusPainted

```java
public boolean isFocusPainted()
```

Gets the

paintFocus

property.

**Returns:** the

paintFocus

property
**See Also:** setFocusPainted(boolean)

---

#### isFocusPainted

public boolean isFocusPainted()

Gets the

paintFocus

property.

setFocusPainted

```java
@BeanProperty
(
visualUpdate
=true,

description
="Whether focus should be painted")
public void setFocusPainted​(boolean b)
```

Sets the

paintFocus

property, which must
be

true

for the focus state to be painted.
The default value for the

paintFocus

property
is

true

.
Some look and feels might not paint focus state;
they will ignore this property.

**Parameters:** b

- if

true

, the focus state should be painted
**See Also:** isFocusPainted()

---

#### setFocusPainted

@BeanProperty

(

visualUpdate

=true,

description

="Whether focus should be painted")
public void setFocusPainted​(boolean b)

Sets the

paintFocus

property, which must
be

true

for the focus state to be painted.
The default value for the

paintFocus

property
is

true

.
Some look and feels might not paint focus state;
they will ignore this property.

isContentAreaFilled

```java
public boolean isContentAreaFilled()
```

Gets the

contentAreaFilled

property.

**Returns:** the

contentAreaFilled

property
**See Also:** setContentAreaFilled(boolean)

---

#### isContentAreaFilled

public boolean isContentAreaFilled()

Gets the

contentAreaFilled

property.

setContentAreaFilled

```java
@BeanProperty
(
visualUpdate
=true,

description
="Whether the button should paint the content area or leave it transparent.")
public void setContentAreaFilled​(boolean b)
```

Sets the

contentAreaFilled

property.
If

true

the button will paint the content
area. If you wish to have a transparent button, such as
an icon only button, for example, then you should set
this to

false

. Do not call

setOpaque(false)

.
The default value for the

contentAreaFilled

property is

true

.

This function may cause the component's opaque property to change.

The exact behavior of calling this function varies on a
component-by-component and L&F-by-L&F basis.

**Parameters:** b

- if true, the content should be filled; if false
the content area is not filled
**See Also:** isContentAreaFilled()

,

JComponent.setOpaque(boolean)

---

#### setContentAreaFilled

@BeanProperty

(

visualUpdate

=true,

description

="Whether the button should paint the content area or leave it transparent.")
public void setContentAreaFilled​(boolean b)

Sets the

contentAreaFilled

property.
If

true

the button will paint the content
area. If you wish to have a transparent button, such as
an icon only button, for example, then you should set
this to

false

. Do not call

setOpaque(false)

.
The default value for the

contentAreaFilled

property is

true

.

This function may cause the component's opaque property to change.

The exact behavior of calling this function varies on a
component-by-component and L&F-by-L&F basis.

This function may cause the component's opaque property to change.

The exact behavior of calling this function varies on a
component-by-component and L&F-by-L&F basis.

The exact behavior of calling this function varies on a
component-by-component and L&F-by-L&F basis.

isRolloverEnabled

```java
public boolean isRolloverEnabled()
```

Gets the

rolloverEnabled

property.

**Returns:** the value of the

rolloverEnabled

property
**See Also:** setRolloverEnabled(boolean)

---

#### isRolloverEnabled

public boolean isRolloverEnabled()

Gets the

rolloverEnabled

property.

setRolloverEnabled

```java
@BeanProperty
(
visualUpdate
=true,

description
="Whether rollover effects should be enabled.")
public void setRolloverEnabled​(boolean b)
```

Sets the

rolloverEnabled

property, which
must be

true

for rollover effects to occur.
The default value for the

rolloverEnabled

property is

false

.
Some look and feels might not implement rollover effects;
they will ignore this property.

**Parameters:** b

- if

true

, rollover effects should be painted
**See Also:** isRolloverEnabled()

---

#### setRolloverEnabled

@BeanProperty

(

visualUpdate

=true,

description

="Whether rollover effects should be enabled.")
public void setRolloverEnabled​(boolean b)

Sets the

rolloverEnabled

property, which
must be

true

for rollover effects to occur.
The default value for the

rolloverEnabled

property is

false

.
Some look and feels might not implement rollover effects;
they will ignore this property.

getMnemonic

```java
public int getMnemonic()
```

Returns the keyboard mnemonic from the current model.

**Returns:** the keyboard mnemonic from the model

---

#### getMnemonic

public int getMnemonic()

Returns the keyboard mnemonic from the current model.

setMnemonic

```java
@BeanProperty
(
visualUpdate
=true,

description
="the keyboard character mnemonic")
public void setMnemonic​(int mnemonic)
```

Sets the keyboard mnemonic on the current model.
The mnemonic is the key which when combined with the look and feel's
mouseless modifier (usually Alt) will activate this button
if focus is contained somewhere within this button's ancestor
window.

A mnemonic must correspond to a single key on the keyboard
and should be specified using one of the

VK_XXX

keycodes defined in

java.awt.event.KeyEvent

.
These codes and the wider array of codes for international
keyboards may be obtained through

java.awt.event.KeyEvent.getExtendedKeyCodeForChar

.
Mnemonics are case-insensitive, therefore a key event
with the corresponding keycode would cause the button to be
activated whether or not the Shift modifier was pressed.

If the character defined by the mnemonic is found within
the button's label string, the first occurrence of it
will be underlined to indicate the mnemonic to the user.

**Parameters:** mnemonic

- the key code which represents the mnemonic
**See Also:** KeyEvent

,

setDisplayedMnemonicIndex(int)

---

#### setMnemonic

@BeanProperty

(

visualUpdate

=true,

description

="the keyboard character mnemonic")
public void setMnemonic​(int mnemonic)

Sets the keyboard mnemonic on the current model.
The mnemonic is the key which when combined with the look and feel's
mouseless modifier (usually Alt) will activate this button
if focus is contained somewhere within this button's ancestor
window.

A mnemonic must correspond to a single key on the keyboard
and should be specified using one of the

VK_XXX

keycodes defined in

java.awt.event.KeyEvent

.
These codes and the wider array of codes for international
keyboards may be obtained through

java.awt.event.KeyEvent.getExtendedKeyCodeForChar

.
Mnemonics are case-insensitive, therefore a key event
with the corresponding keycode would cause the button to be
activated whether or not the Shift modifier was pressed.

If the character defined by the mnemonic is found within
the button's label string, the first occurrence of it
will be underlined to indicate the mnemonic to the user.

A mnemonic must correspond to a single key on the keyboard
and should be specified using one of the

VK_XXX

keycodes defined in

java.awt.event.KeyEvent

.
These codes and the wider array of codes for international
keyboards may be obtained through

java.awt.event.KeyEvent.getExtendedKeyCodeForChar

.
Mnemonics are case-insensitive, therefore a key event
with the corresponding keycode would cause the button to be
activated whether or not the Shift modifier was pressed.

If the character defined by the mnemonic is found within
the button's label string, the first occurrence of it
will be underlined to indicate the mnemonic to the user.

If the character defined by the mnemonic is found within
the button's label string, the first occurrence of it
will be underlined to indicate the mnemonic to the user.

setMnemonic

```java
@BeanProperty
(
visualUpdate
=true,

description
="the keyboard character mnemonic")
public void setMnemonic​(char mnemonic)
```

This method is now obsolete, please use

setMnemonic(int)

to set the mnemonic for a button. This method is only designed
to handle character values which fall between 'a' and 'z' or
'A' and 'Z'.

**Parameters:** mnemonic

- a char specifying the mnemonic value
**See Also:** setMnemonic(int)

---

#### setMnemonic

@BeanProperty

(

visualUpdate

=true,

description

="the keyboard character mnemonic")
public void setMnemonic​(char mnemonic)

This method is now obsolete, please use

setMnemonic(int)

to set the mnemonic for a button. This method is only designed
to handle character values which fall between 'a' and 'z' or
'A' and 'Z'.

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

setMnemonic(KeyEvent.VK_A)

.

**Parameters:** index

- Index into the String to underline
**Throws:** IllegalArgumentException

- will be thrown if

index

is >= length of the text, or < -1
**Since:** 1.4
**See Also:** getDisplayedMnemonicIndex()

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

setMnemonic(KeyEvent.VK_A)

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

setMnemonic(KeyEvent.VK_A)

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

setMultiClickThreshhold

```java
public void setMultiClickThreshhold​(long threshhold)
```

Sets the amount of time (in milliseconds) required between
mouse press events for the button to generate the corresponding
action events. After the initial mouse press occurs (and action
event generated) any subsequent mouse press events which occur
on intervals less than the threshhold will be ignored and no
corresponding action event generated. By default the threshhold is 0,
which means that for each mouse press, an action event will be
fired, no matter how quickly the mouse clicks occur. In buttons
where this behavior is not desirable (for example, the "OK" button
in a dialog), this threshhold should be set to an appropriate
positive value.

**Parameters:** threshhold

- the amount of time required between mouse
press events to generate corresponding action events
**Throws:** IllegalArgumentException

- if threshhold < 0
**Since:** 1.4
**See Also:** getMultiClickThreshhold()

---

#### setMultiClickThreshhold

public void setMultiClickThreshhold​(long threshhold)

Sets the amount of time (in milliseconds) required between
mouse press events for the button to generate the corresponding
action events. After the initial mouse press occurs (and action
event generated) any subsequent mouse press events which occur
on intervals less than the threshhold will be ignored and no
corresponding action event generated. By default the threshhold is 0,
which means that for each mouse press, an action event will be
fired, no matter how quickly the mouse clicks occur. In buttons
where this behavior is not desirable (for example, the "OK" button
in a dialog), this threshhold should be set to an appropriate
positive value.

getMultiClickThreshhold

```java
public long getMultiClickThreshhold()
```

Gets the amount of time (in milliseconds) required between
mouse press events for the button to generate the corresponding
action events.

**Returns:** the amount of time required between mouse press events
to generate corresponding action events
**Since:** 1.4
**See Also:** setMultiClickThreshhold(long)

---

#### getMultiClickThreshhold

public long getMultiClickThreshhold()

Gets the amount of time (in milliseconds) required between
mouse press events for the button to generate the corresponding
action events.

getModel

```java
public
ButtonModel
getModel()
```

Returns the model that this button represents.

**Returns:** the

model

property
**See Also:** setModel(javax.swing.ButtonModel)

---

#### getModel

public

ButtonModel

getModel()

Returns the model that this button represents.

setModel

```java
@BeanProperty
(
description
="Model that the Button uses.")
public void setModel​(
ButtonModel
newModel)
```

Sets the model that this button represents.

**Parameters:** newModel

- the new

ButtonModel
**See Also:** getModel()

---

#### setModel

@BeanProperty

(

description

="Model that the Button uses.")
public void setModel​(

ButtonModel

newModel)

Sets the model that this button represents.

getUI

```java
public
ButtonUI
getUI()
```

Returns the L&F object that renders this component.

**Overrides:** getUI

in class

JComponent
**Returns:** the ButtonUI object
**See Also:** setUI(javax.swing.plaf.ButtonUI)

---

#### getUI

public

ButtonUI

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
="The UI object that implements the LookAndFeel.")
public void setUI​(
ButtonUI
ui)
```

Sets the L&F object that renders this component.

**Parameters:** ui

- the

ButtonUI

L&F object
**See Also:** getUI()

---

#### setUI

@BeanProperty

(

hidden

=true,

visualUpdate

=true,

description

="The UI object that implements the LookAndFeel.")
public void setUI​(

ButtonUI

ui)

Sets the L&F object that renders this component.

updateUI

```java
public void updateUI()
```

Resets the UI property to a value from the current look
and feel. Subtypes of

AbstractButton

should override this to update the UI. For
example,

JButton

might do the following:

```java
setUI((ButtonUI)UIManager.getUI(
"ButtonUI", "javax.swing.plaf.basic.BasicButtonUI", this));
```

**Overrides:** updateUI

in class

JComponent
**See Also:** JComponent.setUI(javax.swing.plaf.ComponentUI)

,

UIManager.getLookAndFeel()

,

UIManager.getUI(javax.swing.JComponent)

---

#### updateUI

public void updateUI()

Resets the UI property to a value from the current look
and feel. Subtypes of

AbstractButton

should override this to update the UI. For
example,

JButton

might do the following:

```java
setUI((ButtonUI)UIManager.getUI(
"ButtonUI", "javax.swing.plaf.basic.BasicButtonUI", this));
```

setUI((ButtonUI)UIManager.getUI(
"ButtonUI", "javax.swing.plaf.basic.BasicButtonUI", this));

addImpl

```java
protected void addImpl​(
Component
comp,

Object
constraints,
int index)
```

Adds the specified component to this container at the specified
index, refer to

Container.addImpl(Component, Object, int)

for a complete description of this method.

**Overrides:** addImpl

in class

Container
**Parameters:** comp

- the component to be added
**Parameters:** constraints

- an object expressing layout constraints
for this component
**Parameters:** index

- the position in the container's list at which to
insert the component, where

-1

means append to the end
**Throws:** IllegalArgumentException

- if

index

is invalid
**Throws:** IllegalArgumentException

- if adding the container's parent
to itself
**Throws:** IllegalArgumentException

- if adding a window to a container
**Since:** 1.5
**See Also:** Container.add(Component)

,

Container.add(Component, int)

,

Container.add(Component, java.lang.Object)

,

Container.invalidate()

,

LayoutManager

,

LayoutManager2

---

#### addImpl

protected void addImpl​(

Component

comp,

Object

constraints,
int index)

Adds the specified component to this container at the specified
index, refer to

Container.addImpl(Component, Object, int)

for a complete description of this method.

setLayout

```java
public void setLayout​(
LayoutManager
mgr)
```

Sets the layout manager for this container, refer to

Container.setLayout(LayoutManager)

for a complete description of this method.

**Overrides:** setLayout

in class

Container
**Parameters:** mgr

- the specified layout manager
**Since:** 1.5
**See Also:** Container.doLayout()

,

Container.getLayout()

,

Container.invalidate()

---

#### setLayout

public void setLayout​(

LayoutManager

mgr)

Sets the layout manager for this container, refer to

Container.setLayout(LayoutManager)

for a complete description of this method.

addChangeListener

```java
public void addChangeListener​(
ChangeListener
l)
```

Adds a

ChangeListener

to the button.

**Parameters:** l

- the listener to be added

---

#### addChangeListener

public void addChangeListener​(

ChangeListener

l)

Adds a

ChangeListener

to the button.

removeChangeListener

```java
public void removeChangeListener​(
ChangeListener
l)
```

Removes a ChangeListener from the button.

**Parameters:** l

- the listener to be removed

---

#### removeChangeListener

public void removeChangeListener​(

ChangeListener

l)

Removes a ChangeListener from the button.

getChangeListeners

```java
@BeanProperty
(
bound
=false)
public
ChangeListener
[] getChangeListeners()
```

Returns an array of all the

ChangeListener

s added
to this AbstractButton with addChangeListener().

**Returns:** all of the

ChangeListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

---

#### getChangeListeners

@BeanProperty

(

bound

=false)
public

ChangeListener

[] getChangeListeners()

Returns an array of all the

ChangeListener

s added
to this AbstractButton with addChangeListener().

fireStateChanged

```java
protected void fireStateChanged()
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created.

**See Also:** EventListenerList

---

#### fireStateChanged

protected void fireStateChanged()

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created.

addActionListener

```java
public void addActionListener​(
ActionListener
l)
```

Adds an

ActionListener

to the button.

**Parameters:** l

- the

ActionListener

to be added

---

#### addActionListener

public void addActionListener​(

ActionListener

l)

Adds an

ActionListener

to the button.

removeActionListener

```java
public void removeActionListener​(
ActionListener
l)
```

Removes an

ActionListener

from the button.
If the listener is the currently set

Action

for the button, then the

Action

is set to

null

.

**Parameters:** l

- the listener to be removed

---

#### removeActionListener

public void removeActionListener​(

ActionListener

l)

Removes an

ActionListener

from the button.
If the listener is the currently set

Action

for the button, then the

Action

is set to

null

.

getActionListeners

```java
@BeanProperty
(
bound
=false)
public
ActionListener
[] getActionListeners()
```

Returns an array of all the

ActionListener

s added
to this AbstractButton with addActionListener().

**Returns:** all of the

ActionListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

---

#### getActionListeners

@BeanProperty

(

bound

=false)
public

ActionListener

[] getActionListeners()

Returns an array of all the

ActionListener

s added
to this AbstractButton with addActionListener().

createChangeListener

```java
protected
ChangeListener
createChangeListener()
```

Subclasses that want to handle

ChangeEvents

differently
can override this to return another

ChangeListener

implementation.

**Returns:** the new

ChangeListener

---

#### createChangeListener

protected

ChangeListener

createChangeListener()

Subclasses that want to handle

ChangeEvents

differently
can override this to return another

ChangeListener

implementation.

fireActionPerformed

```java
protected void fireActionPerformed​(
ActionEvent
event)
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the

event

parameter.

**Parameters:** event

- the

ActionEvent

object
**See Also:** EventListenerList

---

#### fireActionPerformed

protected void fireActionPerformed​(

ActionEvent

event)

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the

event

parameter.

fireItemStateChanged

```java
protected void fireItemStateChanged​(
ItemEvent
event)
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the

event

parameter.

**Parameters:** event

- the

ItemEvent

object
**See Also:** EventListenerList

---

#### fireItemStateChanged

protected void fireItemStateChanged​(

ItemEvent

event)

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the

event

parameter.

createActionListener

```java
protected
ActionListener
createActionListener()
```

Returns

ActionListener

that is added to model.

**Returns:** the

ActionListener

---

#### createActionListener

protected

ActionListener

createActionListener()

Returns

ActionListener

that is added to model.

createItemListener

```java
protected
ItemListener
createItemListener()
```

Returns

ItemListener

that is added to model.

**Returns:** the

ItemListener

---

#### createItemListener

protected

ItemListener

createItemListener()

Returns

ItemListener

that is added to model.

setEnabled

```java
public void setEnabled​(boolean b)
```

Enables (or disables) the button.

**Overrides:** setEnabled

in class

JComponent
**Parameters:** b

- true to enable the button, otherwise false
**See Also:** Component.isEnabled()

,

Component.isLightweight()

---

#### setEnabled

public void setEnabled​(boolean b)

Enables (or disables) the button.

getLabel

```java
@Deprecated

public
String
getLabel()
```

Deprecated.

- Replaced by

getText

Returns the label text.

**Returns:** a

String

containing the label

---

#### getLabel

@Deprecated

public

String

getLabel()

Returns the label text.

setLabel

```java
@Deprecated

@BeanProperty
(
description
="Replace by setText(text)")
public void setLabel​(
String
label)
```

Deprecated.

- Replaced by

setText(text)

Sets the label text.

**Parameters:** label

- a

String

containing the text

---

#### setLabel

@Deprecated

@BeanProperty

(

description

="Replace by setText(text)")
public void setLabel​(

String

label)

Sets the label text.

addItemListener

```java
public void addItemListener​(
ItemListener
l)
```

Adds an

ItemListener

to the

checkbox

.

**Specified by:** addItemListener

in interface

ItemSelectable
**Parameters:** l

- the

ItemListener

to be added
**See Also:** ItemEvent

---

#### addItemListener

public void addItemListener​(

ItemListener

l)

Adds an

ItemListener

to the

checkbox

.

removeItemListener

```java
public void removeItemListener​(
ItemListener
l)
```

Removes an

ItemListener

from the button.

**Specified by:** removeItemListener

in interface

ItemSelectable
**Parameters:** l

- the

ItemListener

to be removed
**See Also:** ItemEvent

---

#### removeItemListener

public void removeItemListener​(

ItemListener

l)

Removes an

ItemListener

from the button.

getItemListeners

```java
@BeanProperty
(
bound
=false)
public
ItemListener
[] getItemListeners()
```

Returns an array of all the

ItemListener

s added
to this AbstractButton with addItemListener().

**Returns:** all of the

ItemListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

---

#### getItemListeners

@BeanProperty

(

bound

=false)
public

ItemListener

[] getItemListeners()

Returns an array of all the

ItemListener

s added
to this AbstractButton with addItemListener().

getSelectedObjects

```java
@BeanProperty
(
bound
=false)
public
Object
[] getSelectedObjects()
```

Returns an array (length 1) containing the label or

null

if the button is not selected.

**Specified by:** getSelectedObjects

in interface

ItemSelectable
**Returns:** an array containing 1 Object: the text of the button,
if the item is selected; otherwise

null

---

#### getSelectedObjects

@BeanProperty

(

bound

=false)
public

Object

[] getSelectedObjects()

Returns an array (length 1) containing the label or

null

if the button is not selected.

init

```java
protected void init​(
String
text,

Icon
icon)
```

Initialization of the

AbstractButton

.

**Parameters:** text

- the text of the button
**Parameters:** icon

- the Icon image to display on the button

---

#### init

protected void init​(

String

text,

Icon

icon)

Initialization of the

AbstractButton

.

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

This is overridden to return false if the current

Icon

's

Image

is not equal to the
passed in

Image

img

.

**Specified by:** imageUpdate

in interface

ImageObserver
**Overrides:** imageUpdate

in class

Component
**Parameters:** img

- the

Image

to be compared
**Parameters:** infoflags

- flags used to repaint the button when the image
is updated and which determine how much is to be painted
**Parameters:** x

- the x coordinate
**Parameters:** y

- the y coordinate
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

This is overridden to return false if the current

Icon

's

Image

is not equal to the
passed in

Image

img

.

paramString

```java
protected
String
paramString()
```

Returns a string representation of this

AbstractButton

.
This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

Overriding

paramString

to provide information about the
specific new aspects of the JFC components.

**Overrides:** paramString

in class

JComponent
**Returns:** a string representation of this

AbstractButton

---

#### paramString

protected

String

paramString()

Returns a string representation of this

AbstractButton

.
This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

Overriding

paramString

to provide information about the
specific new aspects of the JFC components.

Overriding

paramString

to provide information about the
specific new aspects of the JFC components.

---

