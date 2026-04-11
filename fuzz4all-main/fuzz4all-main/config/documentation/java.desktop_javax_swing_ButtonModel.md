# Interface ButtonModel

**Source:** `java.desktop\javax\swing\ButtonModel.html`

### Class Description

```java
public interface
ButtonModel

extends
ItemSelectable
```

State model for buttons.

This model is used for regular buttons, as well as check boxes
and radio buttons, which are special kinds of buttons. In practice,
a button's UI takes the responsibility of calling methods on its
model to manage the state, as detailed below:

In simple terms, pressing and releasing the mouse over a regular
button triggers the button and causes and

ActionEvent

to be fired. The same behavior can be produced via a keyboard key
defined by the look and feel of the button (typically the SPACE BAR).
Pressing and releasing this key while the button has
focus will give the same results. For check boxes and radio buttons, the
mouse or keyboard equivalent sequence just described causes the button
to become selected.

In details, the state model for buttons works as follows
when used with the mouse:

Pressing the mouse on top of a button makes the model both
armed and pressed. As long as the mouse remains down,
the model remains pressed, even if the mouse moves
outside the button. On the contrary, the model is only
armed while the mouse remains pressed within the bounds of
the button (it can move in or out of the button, but the model
is only armed during the portion of time spent within the button).
A button is triggered, and an

ActionEvent

is fired,
when the mouse is released while the model is armed
- meaning when it is released over top of the button after the mouse
has previously been pressed on that button (and not already released).
Upon mouse release, the model becomes unarmed and unpressed.

In details, the state model for buttons works as follows
when used with the keyboard:

Pressing the look and feel defined keyboard key while the button
has focus makes the model both armed and pressed. As long as this key
remains down, the model remains in this state. Releasing the key sets
the model to unarmed and unpressed, triggers the button, and causes an

ActionEvent

to be fired.

**All Superinterfaces:** ItemSelectable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean isArmed()

Indicates partial commitment towards triggering the
button.

**Returns:**
- true

if the button is armed,
and ready to be triggered

**See Also:**
- setArmed(boolean)

---

#### boolean isSelected()

Indicates if the button has been selected. Only needed for
certain types of buttons - such as radio buttons and check boxes.

**Returns:**
- true

if the button is selected

---

#### boolean isEnabled()

Indicates if the button can be selected or triggered by
an input device, such as a mouse pointer.

**Returns:**
- true

if the button is enabled

---

#### boolean isPressed()

Indicates if the button is pressed.

**Returns:**
- true

if the button is pressed

---

#### boolean isRollover()

Indicates that the mouse is over the button.

**Returns:**
- true

if the mouse is over the button

---

#### void setArmed​(boolean b)

Marks the button as armed or unarmed.

**Parameters:**
- b

- whether or not the button should be armed

---

#### void setSelected​(boolean b)

Selects or deselects the button.

**Parameters:**
- b

-

true

selects the button,

false

deselects the button

---

#### void setEnabled​(boolean b)

Enables or disables the button.

**Parameters:**
- b

- whether or not the button should be enabled

**See Also:**
- isEnabled()

---

#### void setPressed​(boolean b)

Sets the button to pressed or unpressed.

**Parameters:**
- b

- whether or not the button should be pressed

**See Also:**
- isPressed()

---

#### void setRollover​(boolean b)

Sets or clears the button's rollover state

**Parameters:**
- b

- whether or not the button is in the rollover state

**See Also:**
- isRollover()

---

#### void setMnemonic​(int key)

Sets the keyboard mnemonic (shortcut key or
accelerator key) for the button.

**Parameters:**
- key

- an int specifying the accelerator key

---

#### int getMnemonic()

Gets the keyboard mnemonic for the button.

**Returns:**
- an int specifying the accelerator key

**See Also:**
- setMnemonic(int)

---

#### void setActionCommand​(
String
s)

Sets the action command string that gets sent as part of the

ActionEvent

when the button is triggered.

**Parameters:**
- s

- the

String

that identifies the generated event

**See Also:**
- getActionCommand()

,

ActionEvent.getActionCommand()

---

#### String
getActionCommand()

Returns the action command string for the button.

**Returns:**
- the

String

that identifies the generated event

**See Also:**
- setActionCommand(java.lang.String)

---

#### void setGroup​(
ButtonGroup
group)

Identifies the group the button belongs to --
needed for radio buttons, which are mutually
exclusive within their group.

**Parameters:**
- group

- the

ButtonGroup

the button belongs to

---

#### default
ButtonGroup
getGroup()

Returns the group that the button belongs to.
Normally used with radio buttons, which are mutually
exclusive within their group.

**Returns:**
- the

ButtonGroup

that the button belongs to

**Since:**
- 10

**Implementation Requirements:**
- The default implementation of this method returns

null

.
Subclasses should return the group set by setGroup().

---

#### void addActionListener​(
ActionListener
l)

Adds an

ActionListener

to the model.

**Parameters:**
- l

- the listener to add

---

#### void removeActionListener​(
ActionListener
l)

Removes an

ActionListener

from the model.

**Parameters:**
- l

- the listener to remove

---

#### void addItemListener​(
ItemListener
l)

Adds an

ItemListener

to the model.

**Specified by:**
- addItemListener

in interface

ItemSelectable

**Parameters:**
- l

- the listener to add

**See Also:**
- ItemEvent

---

#### void removeItemListener​(
ItemListener
l)

Removes an

ItemListener

from the model.

**Specified by:**
- removeItemListener

in interface

ItemSelectable

**Parameters:**
- l

- the listener to remove

**See Also:**
- ItemEvent

---

#### void addChangeListener​(
ChangeListener
l)

Adds a

ChangeListener

to the model.

**Parameters:**
- l

- the listener to add

---

#### void removeChangeListener​(
ChangeListener
l)

Removes a

ChangeListener

from the model.

**Parameters:**
- l

- the listener to remove

---

### Additional Sections

#### Interface ButtonModel

**All Superinterfaces:** ItemSelectable

**All Known Implementing Classes:** DefaultButtonModel

,

JToggleButton.ToggleButtonModel

```java
public interface
ButtonModel

extends
ItemSelectable
```

State model for buttons.

This model is used for regular buttons, as well as check boxes
and radio buttons, which are special kinds of buttons. In practice,
a button's UI takes the responsibility of calling methods on its
model to manage the state, as detailed below:

In simple terms, pressing and releasing the mouse over a regular
button triggers the button and causes and

ActionEvent

to be fired. The same behavior can be produced via a keyboard key
defined by the look and feel of the button (typically the SPACE BAR).
Pressing and releasing this key while the button has
focus will give the same results. For check boxes and radio buttons, the
mouse or keyboard equivalent sequence just described causes the button
to become selected.

In details, the state model for buttons works as follows
when used with the mouse:

Pressing the mouse on top of a button makes the model both
armed and pressed. As long as the mouse remains down,
the model remains pressed, even if the mouse moves
outside the button. On the contrary, the model is only
armed while the mouse remains pressed within the bounds of
the button (it can move in or out of the button, but the model
is only armed during the portion of time spent within the button).
A button is triggered, and an

ActionEvent

is fired,
when the mouse is released while the model is armed
- meaning when it is released over top of the button after the mouse
has previously been pressed on that button (and not already released).
Upon mouse release, the model becomes unarmed and unpressed.

In details, the state model for buttons works as follows
when used with the keyboard:

Pressing the look and feel defined keyboard key while the button
has focus makes the model both armed and pressed. As long as this key
remains down, the model remains in this state. Releasing the key sets
the model to unarmed and unpressed, triggers the button, and causes an

ActionEvent

to be fired.

**Since:** 1.2

public interface

ButtonModel

extends

ItemSelectable

State model for buttons.

This model is used for regular buttons, as well as check boxes
and radio buttons, which are special kinds of buttons. In practice,
a button's UI takes the responsibility of calling methods on its
model to manage the state, as detailed below:

In simple terms, pressing and releasing the mouse over a regular
button triggers the button and causes and

ActionEvent

to be fired. The same behavior can be produced via a keyboard key
defined by the look and feel of the button (typically the SPACE BAR).
Pressing and releasing this key while the button has
focus will give the same results. For check boxes and radio buttons, the
mouse or keyboard equivalent sequence just described causes the button
to become selected.

In details, the state model for buttons works as follows
when used with the mouse:

Pressing the mouse on top of a button makes the model both
armed and pressed. As long as the mouse remains down,
the model remains pressed, even if the mouse moves
outside the button. On the contrary, the model is only
armed while the mouse remains pressed within the bounds of
the button (it can move in or out of the button, but the model
is only armed during the portion of time spent within the button).
A button is triggered, and an

ActionEvent

is fired,
when the mouse is released while the model is armed
- meaning when it is released over top of the button after the mouse
has previously been pressed on that button (and not already released).
Upon mouse release, the model becomes unarmed and unpressed.

In details, the state model for buttons works as follows
when used with the keyboard:

Pressing the look and feel defined keyboard key while the button
has focus makes the model both armed and pressed. As long as this key
remains down, the model remains in this state. Releasing the key sets
the model to unarmed and unpressed, triggers the button, and causes an

ActionEvent

to be fired.

This model is used for regular buttons, as well as check boxes
and radio buttons, which are special kinds of buttons. In practice,
a button's UI takes the responsibility of calling methods on its
model to manage the state, as detailed below:

In simple terms, pressing and releasing the mouse over a regular
button triggers the button and causes and

ActionEvent

to be fired. The same behavior can be produced via a keyboard key
defined by the look and feel of the button (typically the SPACE BAR).
Pressing and releasing this key while the button has
focus will give the same results. For check boxes and radio buttons, the
mouse or keyboard equivalent sequence just described causes the button
to become selected.

In details, the state model for buttons works as follows
when used with the mouse:

Pressing the mouse on top of a button makes the model both
armed and pressed. As long as the mouse remains down,
the model remains pressed, even if the mouse moves
outside the button. On the contrary, the model is only
armed while the mouse remains pressed within the bounds of
the button (it can move in or out of the button, but the model
is only armed during the portion of time spent within the button).
A button is triggered, and an

ActionEvent

is fired,
when the mouse is released while the model is armed
- meaning when it is released over top of the button after the mouse
has previously been pressed on that button (and not already released).
Upon mouse release, the model becomes unarmed and unpressed.

In details, the state model for buttons works as follows
when used with the keyboard:

Pressing the look and feel defined keyboard key while the button
has focus makes the model both armed and pressed. As long as this key
remains down, the model remains in this state. Releasing the key sets
the model to unarmed and unpressed, triggers the button, and causes an

ActionEvent

to be fired.

In simple terms, pressing and releasing the mouse over a regular
button triggers the button and causes and

ActionEvent

to be fired. The same behavior can be produced via a keyboard key
defined by the look and feel of the button (typically the SPACE BAR).
Pressing and releasing this key while the button has
focus will give the same results. For check boxes and radio buttons, the
mouse or keyboard equivalent sequence just described causes the button
to become selected.

In details, the state model for buttons works as follows
when used with the mouse:

Pressing the mouse on top of a button makes the model both
armed and pressed. As long as the mouse remains down,
the model remains pressed, even if the mouse moves
outside the button. On the contrary, the model is only
armed while the mouse remains pressed within the bounds of
the button (it can move in or out of the button, but the model
is only armed during the portion of time spent within the button).
A button is triggered, and an

ActionEvent

is fired,
when the mouse is released while the model is armed
- meaning when it is released over top of the button after the mouse
has previously been pressed on that button (and not already released).
Upon mouse release, the model becomes unarmed and unpressed.

In details, the state model for buttons works as follows
when used with the keyboard:

Pressing the look and feel defined keyboard key while the button
has focus makes the model both armed and pressed. As long as this key
remains down, the model remains in this state. Releasing the key sets
the model to unarmed and unpressed, triggers the button, and causes an

ActionEvent

to be fired.

In details, the state model for buttons works as follows
when used with the mouse:

Pressing the mouse on top of a button makes the model both
armed and pressed. As long as the mouse remains down,
the model remains pressed, even if the mouse moves
outside the button. On the contrary, the model is only
armed while the mouse remains pressed within the bounds of
the button (it can move in or out of the button, but the model
is only armed during the portion of time spent within the button).
A button is triggered, and an

ActionEvent

is fired,
when the mouse is released while the model is armed
- meaning when it is released over top of the button after the mouse
has previously been pressed on that button (and not already released).
Upon mouse release, the model becomes unarmed and unpressed.

In details, the state model for buttons works as follows
when used with the keyboard:

Pressing the look and feel defined keyboard key while the button
has focus makes the model both armed and pressed. As long as this key
remains down, the model remains in this state. Releasing the key sets
the model to unarmed and unpressed, triggers the button, and causes an

ActionEvent

to be fired.

In details, the state model for buttons works as follows
when used with the keyboard:

Pressing the look and feel defined keyboard key while the button
has focus makes the model both armed and pressed. As long as this key
remains down, the model remains in this state. Releasing the key sets
the model to unarmed and unpressed, triggers the button, and causes an

ActionEvent

to be fired.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

void

addActionListener

​(

ActionListener

l)

Adds an

ActionListener

to the model.

void

addChangeListener

​(

ChangeListener

l)

Adds a

ChangeListener

to the model.

void

addItemListener

​(

ItemListener

l)

Adds an

ItemListener

to the model.

String

getActionCommand

()

Returns the action command string for the button.

default

ButtonGroup

getGroup

()

Returns the group that the button belongs to.

int

getMnemonic

()

Gets the keyboard mnemonic for the button.

boolean

isArmed

()

Indicates partial commitment towards triggering the
button.

boolean

isEnabled

()

Indicates if the button can be selected or triggered by
an input device, such as a mouse pointer.

boolean

isPressed

()

Indicates if the button is pressed.

boolean

isRollover

()

Indicates that the mouse is over the button.

boolean

isSelected

()

Indicates if the button has been selected.

void

removeActionListener

​(

ActionListener

l)

Removes an

ActionListener

from the model.

void

removeChangeListener

​(

ChangeListener

l)

Removes a

ChangeListener

from the model.

void

removeItemListener

​(

ItemListener

l)

Removes an

ItemListener

from the model.

void

setActionCommand

​(

String

s)

Sets the action command string that gets sent as part of the

ActionEvent

when the button is triggered.

void

setArmed

​(boolean b)

Marks the button as armed or unarmed.

void

setEnabled

​(boolean b)

Enables or disables the button.

void

setGroup

​(

ButtonGroup

group)

Identifies the group the button belongs to --
needed for radio buttons, which are mutually
exclusive within their group.

void

setMnemonic

​(int key)

Sets the keyboard mnemonic (shortcut key or
accelerator key) for the button.

void

setPressed

​(boolean b)

Sets the button to pressed or unpressed.

void

setRollover

​(boolean b)

Sets or clears the button's rollover state

void

setSelected

​(boolean b)

Selects or deselects the button.

- Methods declared in interface java.awt.

ItemSelectable

getSelectedObjects

Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

void

addActionListener

​(

ActionListener

l)

Adds an

ActionListener

to the model.

void

addChangeListener

​(

ChangeListener

l)

Adds a

ChangeListener

to the model.

void

addItemListener

​(

ItemListener

l)

Adds an

ItemListener

to the model.

String

getActionCommand

()

Returns the action command string for the button.

default

ButtonGroup

getGroup

()

Returns the group that the button belongs to.

int

getMnemonic

()

Gets the keyboard mnemonic for the button.

boolean

isArmed

()

Indicates partial commitment towards triggering the
button.

boolean

isEnabled

()

Indicates if the button can be selected or triggered by
an input device, such as a mouse pointer.

boolean

isPressed

()

Indicates if the button is pressed.

boolean

isRollover

()

Indicates that the mouse is over the button.

boolean

isSelected

()

Indicates if the button has been selected.

void

removeActionListener

​(

ActionListener

l)

Removes an

ActionListener

from the model.

void

removeChangeListener

​(

ChangeListener

l)

Removes a

ChangeListener

from the model.

void

removeItemListener

​(

ItemListener

l)

Removes an

ItemListener

from the model.

void

setActionCommand

​(

String

s)

Sets the action command string that gets sent as part of the

ActionEvent

when the button is triggered.

void

setArmed

​(boolean b)

Marks the button as armed or unarmed.

void

setEnabled

​(boolean b)

Enables or disables the button.

void

setGroup

​(

ButtonGroup

group)

Identifies the group the button belongs to --
needed for radio buttons, which are mutually
exclusive within their group.

void

setMnemonic

​(int key)

Sets the keyboard mnemonic (shortcut key or
accelerator key) for the button.

void

setPressed

​(boolean b)

Sets the button to pressed or unpressed.

void

setRollover

​(boolean b)

Sets or clears the button's rollover state

void

setSelected

​(boolean b)

Selects or deselects the button.

- Methods declared in interface java.awt.

ItemSelectable

getSelectedObjects

---

#### Method Summary

Adds an

ActionListener

to the model.

Adds a

ChangeListener

to the model.

Adds an

ItemListener

to the model.

Returns the action command string for the button.

Returns the group that the button belongs to.

Gets the keyboard mnemonic for the button.

Indicates partial commitment towards triggering the
button.

Indicates if the button can be selected or triggered by
an input device, such as a mouse pointer.

Indicates if the button is pressed.

Indicates that the mouse is over the button.

Indicates if the button has been selected.

Removes an

ActionListener

from the model.

Removes a

ChangeListener

from the model.

Removes an

ItemListener

from the model.

Sets the action command string that gets sent as part of the

ActionEvent

when the button is triggered.

Marks the button as armed or unarmed.

Enables or disables the button.

Identifies the group the button belongs to --
needed for radio buttons, which are mutually
exclusive within their group.

Sets the keyboard mnemonic (shortcut key or
accelerator key) for the button.

Sets the button to pressed or unpressed.

Sets or clears the button's rollover state

Selects or deselects the button.

Methods declared in interface java.awt.

ItemSelectable

getSelectedObjects

---

#### Methods declared in interface java.awt. ItemSelectable

============ METHOD DETAIL ==========

- Method Detail

- isArmed

```java
boolean isArmed()
```

Indicates partial commitment towards triggering the
button.

**Returns:** true

if the button is armed,
and ready to be triggered
**See Also:** setArmed(boolean)

- isSelected

```java
boolean isSelected()
```

Indicates if the button has been selected. Only needed for
certain types of buttons - such as radio buttons and check boxes.

**Returns:** true

if the button is selected

- isEnabled

```java
boolean isEnabled()
```

Indicates if the button can be selected or triggered by
an input device, such as a mouse pointer.

**Returns:** true

if the button is enabled

- isPressed

```java
boolean isPressed()
```

Indicates if the button is pressed.

**Returns:** true

if the button is pressed

- isRollover

```java
boolean isRollover()
```

Indicates that the mouse is over the button.

**Returns:** true

if the mouse is over the button

- setArmed

```java
void setArmed​(boolean b)
```

Marks the button as armed or unarmed.

**Parameters:** b

- whether or not the button should be armed

- setSelected

```java
void setSelected​(boolean b)
```

Selects or deselects the button.

**Parameters:** b

-

true

selects the button,

false

deselects the button

- setEnabled

```java
void setEnabled​(boolean b)
```

Enables or disables the button.

**Parameters:** b

- whether or not the button should be enabled
**See Also:** isEnabled()

- setPressed

```java
void setPressed​(boolean b)
```

Sets the button to pressed or unpressed.

**Parameters:** b

- whether or not the button should be pressed
**See Also:** isPressed()

- setRollover

```java
void setRollover​(boolean b)
```

Sets or clears the button's rollover state

**Parameters:** b

- whether or not the button is in the rollover state
**See Also:** isRollover()

- setMnemonic

```java
void setMnemonic​(int key)
```

Sets the keyboard mnemonic (shortcut key or
accelerator key) for the button.

**Parameters:** key

- an int specifying the accelerator key

- getMnemonic

```java
int getMnemonic()
```

Gets the keyboard mnemonic for the button.

**Returns:** an int specifying the accelerator key
**See Also:** setMnemonic(int)

- setActionCommand

```java
void setActionCommand​(
String
s)
```

Sets the action command string that gets sent as part of the

ActionEvent

when the button is triggered.

**Parameters:** s

- the

String

that identifies the generated event
**See Also:** getActionCommand()

,

ActionEvent.getActionCommand()

- getActionCommand

```java
String
getActionCommand()
```

Returns the action command string for the button.

**Returns:** the

String

that identifies the generated event
**See Also:** setActionCommand(java.lang.String)

- setGroup

```java
void setGroup​(
ButtonGroup
group)
```

Identifies the group the button belongs to --
needed for radio buttons, which are mutually
exclusive within their group.

**Parameters:** group

- the

ButtonGroup

the button belongs to

- getGroup

```java
default
ButtonGroup
getGroup()
```

Returns the group that the button belongs to.
Normally used with radio buttons, which are mutually
exclusive within their group.

**Implementation Requirements:** The default implementation of this method returns

null

.
Subclasses should return the group set by setGroup().
**Returns:** the

ButtonGroup

that the button belongs to
**Since:** 10

- addActionListener

```java
void addActionListener​(
ActionListener
l)
```

Adds an

ActionListener

to the model.

**Parameters:** l

- the listener to add

- removeActionListener

```java
void removeActionListener​(
ActionListener
l)
```

Removes an

ActionListener

from the model.

**Parameters:** l

- the listener to remove

- addItemListener

```java
void addItemListener​(
ItemListener
l)
```

Adds an

ItemListener

to the model.

**Specified by:** addItemListener

in interface

ItemSelectable
**Parameters:** l

- the listener to add
**See Also:** ItemEvent

- removeItemListener

```java
void removeItemListener​(
ItemListener
l)
```

Removes an

ItemListener

from the model.

**Specified by:** removeItemListener

in interface

ItemSelectable
**Parameters:** l

- the listener to remove
**See Also:** ItemEvent

- addChangeListener

```java
void addChangeListener​(
ChangeListener
l)
```

Adds a

ChangeListener

to the model.

**Parameters:** l

- the listener to add

- removeChangeListener

```java
void removeChangeListener​(
ChangeListener
l)
```

Removes a

ChangeListener

from the model.

**Parameters:** l

- the listener to remove

Method Detail

- isArmed

```java
boolean isArmed()
```

Indicates partial commitment towards triggering the
button.

**Returns:** true

if the button is armed,
and ready to be triggered
**See Also:** setArmed(boolean)

- isSelected

```java
boolean isSelected()
```

Indicates if the button has been selected. Only needed for
certain types of buttons - such as radio buttons and check boxes.

**Returns:** true

if the button is selected

- isEnabled

```java
boolean isEnabled()
```

Indicates if the button can be selected or triggered by
an input device, such as a mouse pointer.

**Returns:** true

if the button is enabled

- isPressed

```java
boolean isPressed()
```

Indicates if the button is pressed.

**Returns:** true

if the button is pressed

- isRollover

```java
boolean isRollover()
```

Indicates that the mouse is over the button.

**Returns:** true

if the mouse is over the button

- setArmed

```java
void setArmed​(boolean b)
```

Marks the button as armed or unarmed.

**Parameters:** b

- whether or not the button should be armed

- setSelected

```java
void setSelected​(boolean b)
```

Selects or deselects the button.

**Parameters:** b

-

true

selects the button,

false

deselects the button

- setEnabled

```java
void setEnabled​(boolean b)
```

Enables or disables the button.

**Parameters:** b

- whether or not the button should be enabled
**See Also:** isEnabled()

- setPressed

```java
void setPressed​(boolean b)
```

Sets the button to pressed or unpressed.

**Parameters:** b

- whether or not the button should be pressed
**See Also:** isPressed()

- setRollover

```java
void setRollover​(boolean b)
```

Sets or clears the button's rollover state

**Parameters:** b

- whether or not the button is in the rollover state
**See Also:** isRollover()

- setMnemonic

```java
void setMnemonic​(int key)
```

Sets the keyboard mnemonic (shortcut key or
accelerator key) for the button.

**Parameters:** key

- an int specifying the accelerator key

- getMnemonic

```java
int getMnemonic()
```

Gets the keyboard mnemonic for the button.

**Returns:** an int specifying the accelerator key
**See Also:** setMnemonic(int)

- setActionCommand

```java
void setActionCommand​(
String
s)
```

Sets the action command string that gets sent as part of the

ActionEvent

when the button is triggered.

**Parameters:** s

- the

String

that identifies the generated event
**See Also:** getActionCommand()

,

ActionEvent.getActionCommand()

- getActionCommand

```java
String
getActionCommand()
```

Returns the action command string for the button.

**Returns:** the

String

that identifies the generated event
**See Also:** setActionCommand(java.lang.String)

- setGroup

```java
void setGroup​(
ButtonGroup
group)
```

Identifies the group the button belongs to --
needed for radio buttons, which are mutually
exclusive within their group.

**Parameters:** group

- the

ButtonGroup

the button belongs to

- getGroup

```java
default
ButtonGroup
getGroup()
```

Returns the group that the button belongs to.
Normally used with radio buttons, which are mutually
exclusive within their group.

**Implementation Requirements:** The default implementation of this method returns

null

.
Subclasses should return the group set by setGroup().
**Returns:** the

ButtonGroup

that the button belongs to
**Since:** 10

- addActionListener

```java
void addActionListener​(
ActionListener
l)
```

Adds an

ActionListener

to the model.

**Parameters:** l

- the listener to add

- removeActionListener

```java
void removeActionListener​(
ActionListener
l)
```

Removes an

ActionListener

from the model.

**Parameters:** l

- the listener to remove

- addItemListener

```java
void addItemListener​(
ItemListener
l)
```

Adds an

ItemListener

to the model.

**Specified by:** addItemListener

in interface

ItemSelectable
**Parameters:** l

- the listener to add
**See Also:** ItemEvent

- removeItemListener

```java
void removeItemListener​(
ItemListener
l)
```

Removes an

ItemListener

from the model.

**Specified by:** removeItemListener

in interface

ItemSelectable
**Parameters:** l

- the listener to remove
**See Also:** ItemEvent

- addChangeListener

```java
void addChangeListener​(
ChangeListener
l)
```

Adds a

ChangeListener

to the model.

**Parameters:** l

- the listener to add

- removeChangeListener

```java
void removeChangeListener​(
ChangeListener
l)
```

Removes a

ChangeListener

from the model.

**Parameters:** l

- the listener to remove

---

#### Method Detail

isArmed

```java
boolean isArmed()
```

Indicates partial commitment towards triggering the
button.

**Returns:** true

if the button is armed,
and ready to be triggered
**See Also:** setArmed(boolean)

---

#### isArmed

boolean isArmed()

Indicates partial commitment towards triggering the
button.

isSelected

```java
boolean isSelected()
```

Indicates if the button has been selected. Only needed for
certain types of buttons - such as radio buttons and check boxes.

**Returns:** true

if the button is selected

---

#### isSelected

boolean isSelected()

Indicates if the button has been selected. Only needed for
certain types of buttons - such as radio buttons and check boxes.

isEnabled

```java
boolean isEnabled()
```

Indicates if the button can be selected or triggered by
an input device, such as a mouse pointer.

**Returns:** true

if the button is enabled

---

#### isEnabled

boolean isEnabled()

Indicates if the button can be selected or triggered by
an input device, such as a mouse pointer.

isPressed

```java
boolean isPressed()
```

Indicates if the button is pressed.

**Returns:** true

if the button is pressed

---

#### isPressed

boolean isPressed()

Indicates if the button is pressed.

isRollover

```java
boolean isRollover()
```

Indicates that the mouse is over the button.

**Returns:** true

if the mouse is over the button

---

#### isRollover

boolean isRollover()

Indicates that the mouse is over the button.

setArmed

```java
void setArmed​(boolean b)
```

Marks the button as armed or unarmed.

**Parameters:** b

- whether or not the button should be armed

---

#### setArmed

void setArmed​(boolean b)

Marks the button as armed or unarmed.

setSelected

```java
void setSelected​(boolean b)
```

Selects or deselects the button.

**Parameters:** b

-

true

selects the button,

false

deselects the button

---

#### setSelected

void setSelected​(boolean b)

Selects or deselects the button.

setEnabled

```java
void setEnabled​(boolean b)
```

Enables or disables the button.

**Parameters:** b

- whether or not the button should be enabled
**See Also:** isEnabled()

---

#### setEnabled

void setEnabled​(boolean b)

Enables or disables the button.

setPressed

```java
void setPressed​(boolean b)
```

Sets the button to pressed or unpressed.

**Parameters:** b

- whether or not the button should be pressed
**See Also:** isPressed()

---

#### setPressed

void setPressed​(boolean b)

Sets the button to pressed or unpressed.

setRollover

```java
void setRollover​(boolean b)
```

Sets or clears the button's rollover state

**Parameters:** b

- whether or not the button is in the rollover state
**See Also:** isRollover()

---

#### setRollover

void setRollover​(boolean b)

Sets or clears the button's rollover state

setMnemonic

```java
void setMnemonic​(int key)
```

Sets the keyboard mnemonic (shortcut key or
accelerator key) for the button.

**Parameters:** key

- an int specifying the accelerator key

---

#### setMnemonic

void setMnemonic​(int key)

Sets the keyboard mnemonic (shortcut key or
accelerator key) for the button.

getMnemonic

```java
int getMnemonic()
```

Gets the keyboard mnemonic for the button.

**Returns:** an int specifying the accelerator key
**See Also:** setMnemonic(int)

---

#### getMnemonic

int getMnemonic()

Gets the keyboard mnemonic for the button.

setActionCommand

```java
void setActionCommand​(
String
s)
```

Sets the action command string that gets sent as part of the

ActionEvent

when the button is triggered.

**Parameters:** s

- the

String

that identifies the generated event
**See Also:** getActionCommand()

,

ActionEvent.getActionCommand()

---

#### setActionCommand

void setActionCommand​(

String

s)

Sets the action command string that gets sent as part of the

ActionEvent

when the button is triggered.

getActionCommand

```java
String
getActionCommand()
```

Returns the action command string for the button.

**Returns:** the

String

that identifies the generated event
**See Also:** setActionCommand(java.lang.String)

---

#### getActionCommand

String

getActionCommand()

Returns the action command string for the button.

setGroup

```java
void setGroup​(
ButtonGroup
group)
```

Identifies the group the button belongs to --
needed for radio buttons, which are mutually
exclusive within their group.

**Parameters:** group

- the

ButtonGroup

the button belongs to

---

#### setGroup

void setGroup​(

ButtonGroup

group)

Identifies the group the button belongs to --
needed for radio buttons, which are mutually
exclusive within their group.

getGroup

```java
default
ButtonGroup
getGroup()
```

Returns the group that the button belongs to.
Normally used with radio buttons, which are mutually
exclusive within their group.

**Implementation Requirements:** The default implementation of this method returns

null

.
Subclasses should return the group set by setGroup().
**Returns:** the

ButtonGroup

that the button belongs to
**Since:** 10

---

#### getGroup

default

ButtonGroup

getGroup()

Returns the group that the button belongs to.
Normally used with radio buttons, which are mutually
exclusive within their group.

addActionListener

```java
void addActionListener​(
ActionListener
l)
```

Adds an

ActionListener

to the model.

**Parameters:** l

- the listener to add

---

#### addActionListener

void addActionListener​(

ActionListener

l)

Adds an

ActionListener

to the model.

removeActionListener

```java
void removeActionListener​(
ActionListener
l)
```

Removes an

ActionListener

from the model.

**Parameters:** l

- the listener to remove

---

#### removeActionListener

void removeActionListener​(

ActionListener

l)

Removes an

ActionListener

from the model.

addItemListener

```java
void addItemListener​(
ItemListener
l)
```

Adds an

ItemListener

to the model.

**Specified by:** addItemListener

in interface

ItemSelectable
**Parameters:** l

- the listener to add
**See Also:** ItemEvent

---

#### addItemListener

void addItemListener​(

ItemListener

l)

Adds an

ItemListener

to the model.

removeItemListener

```java
void removeItemListener​(
ItemListener
l)
```

Removes an

ItemListener

from the model.

**Specified by:** removeItemListener

in interface

ItemSelectable
**Parameters:** l

- the listener to remove
**See Also:** ItemEvent

---

#### removeItemListener

void removeItemListener​(

ItemListener

l)

Removes an

ItemListener

from the model.

addChangeListener

```java
void addChangeListener​(
ChangeListener
l)
```

Adds a

ChangeListener

to the model.

**Parameters:** l

- the listener to add

---

#### addChangeListener

void addChangeListener​(

ChangeListener

l)

Adds a

ChangeListener

to the model.

removeChangeListener

```java
void removeChangeListener​(
ChangeListener
l)
```

Removes a

ChangeListener

from the model.

**Parameters:** l

- the listener to remove

---

#### removeChangeListener

void removeChangeListener​(

ChangeListener

l)

Removes a

ChangeListener

from the model.

---

