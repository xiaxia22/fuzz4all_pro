# Class JSpinner

**Source:** `java.desktop\javax\swing\JSpinner.html`

### Class Description

```java
@JavaBean
(
defaultProperty
="UI",

description
="A single line input field that lets the user select a number or an object value from an ordered set.")
public class
JSpinner

extends
JComponent

implements
Accessible
```

A single line input field that lets the user select a
number or an object value from an ordered sequence. Spinners typically
provide a pair of tiny arrow buttons for stepping through the elements
of the sequence. The keyboard up/down arrow keys also cycle through the
elements. The user may also be allowed to type a (legal) value directly
into the spinner. Although combo boxes provide similar functionality,
spinners are sometimes preferred because they don't require a drop down list
that can obscure important data.

A

JSpinner

's sequence value is defined by its

SpinnerModel

.
The

model

can be specified as a constructor argument and
changed with the

model

property.

SpinnerModel

classes for some common types are provided:

SpinnerListModel

,

SpinnerNumberModel

, and

SpinnerDateModel

.

A

JSpinner

has a single child component that's
responsible for displaying
and potentially changing the current element or

value

of
the model, which is called the

editor

. The editor is created
by the

JSpinner

's constructor and can be changed with the

editor

property. The

JSpinner

's editor stays
in sync with the model by listening for

ChangeEvent

s. If the
user has changed the value displayed by the

editor

it is
possible for the

model

's value to differ from that of
the

editor

. To make sure the

model

has the same
value as the editor use the

commitEdit

method, eg:

```java
try {
spinner.commitEdit();
}
catch (ParseException pe) {
// Edited value is invalid, spinner.getValue() will return
// the last valid value, you could revert the spinner to show that:
JComponent editor = spinner.getEditor();
if (editor instanceof DefaultEditor) {
((DefaultEditor)editor).getTextField().setValue(spinner.getValue());
}
// reset the value to some known value:
spinner.setValue(fallbackValue);
// or treat the last valid value as the current, in which
// case you don't need to do anything.
}
return spinner.getValue();
```

For information and examples of using spinner see

How to Use Spinners

,
a section in

The Java Tutorial.

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

---

### Field Details

*No entries found.*

### Constructor Details

#### public JSpinner​(
SpinnerModel
model)

Constructs a spinner for the given model. The spinner has
a set of previous/next buttons, and an editor appropriate
for the model.

**Parameters:**
- model

- a model for the new spinner

**Throws:**
- NullPointerException

- if the model is

null

---

#### public JSpinner()

Constructs a spinner with an

Integer SpinnerNumberModel

with initial value 0 and no minimum or maximum limits.

---

### Method Details

#### public
SpinnerUI
getUI()

Returns the look and feel (L&F) object that renders this component.

**Overrides:**
- getUI

in class

JComponent

**Returns:**
- the

SpinnerUI

object that renders this component

---

#### public void setUI​(
SpinnerUI
ui)

Sets the look and feel (L&F) object that renders this component.

**Parameters:**
- ui

- the

SpinnerUI

L&F object

**See Also:**
- UIDefaults.getUI(javax.swing.JComponent)

---

#### @BeanProperty
(
bound
=false)
public
String
getUIClassID()

Returns the suffix used to construct the name of the look and feel
(L&F) class used to render this component.

**Overrides:**
- getUIClassID

in class

JComponent

**Returns:**
- the string "SpinnerUI"

**See Also:**
- JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

---

#### public void updateUI()

Resets the UI property with the value from the current look and feel.

**Overrides:**
- updateUI

in class

JComponent

**See Also:**
- UIManager.getUI(javax.swing.JComponent)

---

#### protected
JComponent
createEditor​(
SpinnerModel
model)

This method is called by the constructors to create the

JComponent

that displays the current value of the sequence. The editor may
also allow the user to enter an element of the sequence directly.
An editor must listen for

ChangeEvents

on the

model

and keep the value it displays
in sync with the value of the model.

Subclasses may override this method to add support for new

SpinnerModel

classes. Alternatively one can just
replace the editor created here with the

setEditor

method. The default mapping from model type to editor is:

- SpinnerNumberModel => JSpinner.NumberEditor

SpinnerDateModel => JSpinner.DateEditor

SpinnerListModel => JSpinner.ListEditor

all others

=>

JSpinner.DefaultEditor

**Parameters:**
- model

- the value of getModel

**Returns:**
- a component that displays the current value of the sequence

**See Also:**
- getModel()

,

setEditor(javax.swing.JComponent)

---

#### @BeanProperty
(
visualUpdate
=true,

description
="Model that represents the value of this spinner.")
public void setModel​(
SpinnerModel
model)

Changes the model that represents the value of this spinner.
If the editor property has not been explicitly set,
the editor property is (implicitly) set after the

"model"

PropertyChangeEvent

has been fired. The editor
property is set to the value returned by

createEditor

,
as in:

```java
setEditor(createEditor(model));
```

**Parameters:**
- model

- the new

SpinnerModel

**Throws:**
- IllegalArgumentException

- if model is

null

**See Also:**
- getModel()

,

getEditor()

,

setEditor(javax.swing.JComponent)

---

#### public
SpinnerModel
getModel()

Returns the

SpinnerModel

that defines
this spinners sequence of values.

**Returns:**
- the value of the model property

**See Also:**
- setModel(javax.swing.SpinnerModel)

---

#### public
Object
getValue()

Returns the current value of the model, typically
this value is displayed by the

editor

. If the
user has changed the value displayed by the

editor

it is
possible for the

model

's value to differ from that of
the

editor

, refer to the class level javadoc for examples
of how to deal with this.

This method simply delegates to the

model

.
It is equivalent to:

```java
getModel().getValue()
```

**Returns:**
- the current value of the model

**See Also:**
- setValue(java.lang.Object)

,

SpinnerModel.getValue()

---

#### public void setValue​(
Object
value)

Changes current value of the model, typically
this value is displayed by the

editor

.
If the

SpinnerModel

implementation
doesn't support the specified value then an

IllegalArgumentException

is thrown.

This method simply delegates to the

model

.
It is equivalent to:

```java
getModel().setValue(value)
```

**Parameters:**
- value

- new value for the spinner

**Throws:**
- IllegalArgumentException

- if

value

isn't allowed

**See Also:**
- getValue()

,

SpinnerModel.setValue(java.lang.Object)

---

#### @BeanProperty
(
bound
=false)
public
Object
getNextValue()

Returns the object in the sequence that comes after the object returned
by

getValue()

. If the end of the sequence has been reached
then return

null

.
Calling this method does not effect

value

.

This method simply delegates to the

model

.
It is equivalent to:

```java
getModel().getNextValue()
```

**Returns:**
- the next legal value or

null

if one doesn't exist

**See Also:**
- getValue()

,

getPreviousValue()

,

SpinnerModel.getNextValue()

---

#### public void addChangeListener​(
ChangeListener
listener)

Adds a listener to the list that is notified each time a change
to the model occurs. The source of

ChangeEvents

delivered to

ChangeListeners

will be this

JSpinner

. Note also that replacing the model
will not affect listeners added directly to JSpinner.
Applications can add listeners to the model directly. In that
case is that the source of the event would be the

SpinnerModel

.

**Parameters:**
- listener

- the

ChangeListener

to add

**See Also:**
- removeChangeListener(javax.swing.event.ChangeListener)

,

getModel()

---

#### public void removeChangeListener​(
ChangeListener
listener)

Removes a

ChangeListener

from this spinner.

**Parameters:**
- listener

- the

ChangeListener

to remove

**See Also:**
- fireStateChanged()

,

addChangeListener(javax.swing.event.ChangeListener)

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
to this JSpinner with addChangeListener().

**Returns:**
- all of the

ChangeListener

s added or an empty
array if no listeners have been added

**Since:**
- 1.4

---

#### protected void fireStateChanged()

Sends a

ChangeEvent

, whose source is this

JSpinner

, to each

ChangeListener

.
When a

ChangeListener

has been added
to the spinner, this method is called each time
a

ChangeEvent

is received from the model.

**See Also:**
- addChangeListener(javax.swing.event.ChangeListener)

,

removeChangeListener(javax.swing.event.ChangeListener)

,

EventListenerList

---

#### @BeanProperty
(
bound
=false)
public
Object
getPreviousValue()

Returns the object in the sequence that comes
before the object returned by

getValue()

.
If the end of the sequence has been reached then
return

null

. Calling this method does
not effect

value

.

This method simply delegates to the

model

.
It is equivalent to:

```java
getModel().getPreviousValue()
```

**Returns:**
- the previous legal value or

null

if one doesn't exist

**See Also:**
- getValue()

,

getNextValue()

,

SpinnerModel.getPreviousValue()

---

#### @BeanProperty
(
visualUpdate
=true,

description
="JComponent that displays the current value of the model")
public void setEditor​(
JComponent
editor)

Changes the

JComponent

that displays the current value
of the

SpinnerModel

. It is the responsibility of this
method to

disconnect

the old editor from the model and to
connect the new editor. This may mean removing the
old editors

ChangeListener

from the model or the
spinner itself and adding one for the new editor.

**Parameters:**
- editor

- the new editor

**Throws:**
- IllegalArgumentException

- if editor is

null

**See Also:**
- getEditor()

,

createEditor(javax.swing.SpinnerModel)

,

getModel()

---

#### public
JComponent
getEditor()

Returns the component that displays and potentially
changes the model's value.

**Returns:**
- the component that displays and potentially
changes the model's value

**See Also:**
- setEditor(javax.swing.JComponent)

,

createEditor(javax.swing.SpinnerModel)

---

#### public void commitEdit()
throws
ParseException

Commits the currently edited value to the

SpinnerModel

.

If the editor is an instance of

DefaultEditor

, the
call if forwarded to the editor, otherwise this does nothing.

**Throws:**
- ParseException

- if the currently edited value couldn't
be committed.

---

#### @BeanProperty
(
bound
=false)
public
AccessibleContext
getAccessibleContext()

Gets the

AccessibleContext

for the

JSpinner

**Specified by:**
- getAccessibleContext

in interface

Accessible

**Overrides:**
- getAccessibleContext

in class

Component

**Returns:**
- the

AccessibleContext

for the

JSpinner

**Since:**
- 1.5

---

### Additional Sections

#### Class JSpinner

java.lang.Object

- java.awt.Component
- - java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JSpinner

java.awt.Component

- java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JSpinner

java.awt.Container

- javax.swing.JComponent
- - javax.swing.JSpinner

javax.swing.JComponent

- javax.swing.JSpinner

javax.swing.JSpinner

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

```java
@JavaBean
(
defaultProperty
="UI",

description
="A single line input field that lets the user select a number or an object value from an ordered set.")
public class
JSpinner

extends
JComponent

implements
Accessible
```

A single line input field that lets the user select a
number or an object value from an ordered sequence. Spinners typically
provide a pair of tiny arrow buttons for stepping through the elements
of the sequence. The keyboard up/down arrow keys also cycle through the
elements. The user may also be allowed to type a (legal) value directly
into the spinner. Although combo boxes provide similar functionality,
spinners are sometimes preferred because they don't require a drop down list
that can obscure important data.

A

JSpinner

's sequence value is defined by its

SpinnerModel

.
The

model

can be specified as a constructor argument and
changed with the

model

property.

SpinnerModel

classes for some common types are provided:

SpinnerListModel

,

SpinnerNumberModel

, and

SpinnerDateModel

.

A

JSpinner

has a single child component that's
responsible for displaying
and potentially changing the current element or

value

of
the model, which is called the

editor

. The editor is created
by the

JSpinner

's constructor and can be changed with the

editor

property. The

JSpinner

's editor stays
in sync with the model by listening for

ChangeEvent

s. If the
user has changed the value displayed by the

editor

it is
possible for the

model

's value to differ from that of
the

editor

. To make sure the

model

has the same
value as the editor use the

commitEdit

method, eg:

```java
try {
spinner.commitEdit();
}
catch (ParseException pe) {
// Edited value is invalid, spinner.getValue() will return
// the last valid value, you could revert the spinner to show that:
JComponent editor = spinner.getEditor();
if (editor instanceof DefaultEditor) {
((DefaultEditor)editor).getTextField().setValue(spinner.getValue());
}
// reset the value to some known value:
spinner.setValue(fallbackValue);
// or treat the last valid value as the current, in which
// case you don't need to do anything.
}
return spinner.getValue();
```

For information and examples of using spinner see

How to Use Spinners

,
a section in

The Java Tutorial.

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

**Since:** 1.4
**See Also:** SpinnerModel

,

AbstractSpinnerModel

,

SpinnerListModel

,

SpinnerNumberModel

,

SpinnerDateModel

,

JFormattedTextField

,

Serialized Form

@JavaBean

(

defaultProperty

="UI",

description

="A single line input field that lets the user select a number or an object value from an ordered set.")
public class

JSpinner

extends

JComponent

implements

Accessible

A single line input field that lets the user select a
number or an object value from an ordered sequence. Spinners typically
provide a pair of tiny arrow buttons for stepping through the elements
of the sequence. The keyboard up/down arrow keys also cycle through the
elements. The user may also be allowed to type a (legal) value directly
into the spinner. Although combo boxes provide similar functionality,
spinners are sometimes preferred because they don't require a drop down list
that can obscure important data.

A

JSpinner

's sequence value is defined by its

SpinnerModel

.
The

model

can be specified as a constructor argument and
changed with the

model

property.

SpinnerModel

classes for some common types are provided:

SpinnerListModel

,

SpinnerNumberModel

, and

SpinnerDateModel

.

A

JSpinner

has a single child component that's
responsible for displaying
and potentially changing the current element or

value

of
the model, which is called the

editor

. The editor is created
by the

JSpinner

's constructor and can be changed with the

editor

property. The

JSpinner

's editor stays
in sync with the model by listening for

ChangeEvent

s. If the
user has changed the value displayed by the

editor

it is
possible for the

model

's value to differ from that of
the

editor

. To make sure the

model

has the same
value as the editor use the

commitEdit

method, eg:

```java
try {
spinner.commitEdit();
}
catch (ParseException pe) {
// Edited value is invalid, spinner.getValue() will return
// the last valid value, you could revert the spinner to show that:
JComponent editor = spinner.getEditor();
if (editor instanceof DefaultEditor) {
((DefaultEditor)editor).getTextField().setValue(spinner.getValue());
}
// reset the value to some known value:
spinner.setValue(fallbackValue);
// or treat the last valid value as the current, in which
// case you don't need to do anything.
}
return spinner.getValue();
```

For information and examples of using spinner see

How to Use Spinners

,
a section in

The Java Tutorial.

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

JSpinner

's sequence value is defined by its

SpinnerModel

.
The

model

can be specified as a constructor argument and
changed with the

model

property.

SpinnerModel

classes for some common types are provided:

SpinnerListModel

,

SpinnerNumberModel

, and

SpinnerDateModel

.

A

JSpinner

has a single child component that's
responsible for displaying
and potentially changing the current element or

value

of
the model, which is called the

editor

. The editor is created
by the

JSpinner

's constructor and can be changed with the

editor

property. The

JSpinner

's editor stays
in sync with the model by listening for

ChangeEvent

s. If the
user has changed the value displayed by the

editor

it is
possible for the

model

's value to differ from that of
the

editor

. To make sure the

model

has the same
value as the editor use the

commitEdit

method, eg:

```java
try {
spinner.commitEdit();
}
catch (ParseException pe) {
// Edited value is invalid, spinner.getValue() will return
// the last valid value, you could revert the spinner to show that:
JComponent editor = spinner.getEditor();
if (editor instanceof DefaultEditor) {
((DefaultEditor)editor).getTextField().setValue(spinner.getValue());
}
// reset the value to some known value:
spinner.setValue(fallbackValue);
// or treat the last valid value as the current, in which
// case you don't need to do anything.
}
return spinner.getValue();
```

For information and examples of using spinner see

How to Use Spinners

,
a section in

The Java Tutorial.

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

JSpinner

has a single child component that's
responsible for displaying
and potentially changing the current element or

value

of
the model, which is called the

editor

. The editor is created
by the

JSpinner

's constructor and can be changed with the

editor

property. The

JSpinner

's editor stays
in sync with the model by listening for

ChangeEvent

s. If the
user has changed the value displayed by the

editor

it is
possible for the

model

's value to differ from that of
the

editor

. To make sure the

model

has the same
value as the editor use the

commitEdit

method, eg:

```java
try {
spinner.commitEdit();
}
catch (ParseException pe) {
// Edited value is invalid, spinner.getValue() will return
// the last valid value, you could revert the spinner to show that:
JComponent editor = spinner.getEditor();
if (editor instanceof DefaultEditor) {
((DefaultEditor)editor).getTextField().setValue(spinner.getValue());
}
// reset the value to some known value:
spinner.setValue(fallbackValue);
// or treat the last valid value as the current, in which
// case you don't need to do anything.
}
return spinner.getValue();
```

For information and examples of using spinner see

How to Use Spinners

,
a section in

The Java Tutorial.

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

try {
spinner.commitEdit();
}
catch (ParseException pe) {
// Edited value is invalid, spinner.getValue() will return
// the last valid value, you could revert the spinner to show that:
JComponent editor = spinner.getEditor();
if (editor instanceof DefaultEditor) {
((DefaultEditor)editor).getTextField().setValue(spinner.getValue());
}
// reset the value to some known value:
spinner.setValue(fallbackValue);
// or treat the last valid value as the current, in which
// case you don't need to do anything.
}
return spinner.getValue();

For information and examples of using spinner see

How to Use Spinners

,
a section in

The Java Tutorial.

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

JSpinner.AccessibleJSpinner

AccessibleJSpinner

implements accessibility
support for the

JSpinner

class.

static class

JSpinner.DateEditor

An editor for a

JSpinner

whose model is a

SpinnerDateModel

.

static class

JSpinner.DefaultEditor

A simple base class for more specialized editors
that displays a read-only view of the model's current
value with a

JFormattedTextField

.

static class

JSpinner.ListEditor

An editor for a

JSpinner

whose model is a

SpinnerListModel

.

static class

JSpinner.NumberEditor

An editor for a

JSpinner

whose model is a

SpinnerNumberModel

.

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

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

JSpinner

()

Constructs a spinner with an

Integer SpinnerNumberModel

with initial value 0 and no minimum or maximum limits.

JSpinner

​(

SpinnerModel

model)

Constructs a spinner for the given model.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addChangeListener

​(

ChangeListener

listener)

Adds a listener to the list that is notified each time a change
to the model occurs.

void

commitEdit

()

Commits the currently edited value to the

SpinnerModel

.

protected

JComponent

createEditor

​(

SpinnerModel

model)

This method is called by the constructors to create the

JComponent

that displays the current value of the sequence.

protected void

fireStateChanged

()

Sends a

ChangeEvent

, whose source is this

JSpinner

, to each

ChangeListener

.

AccessibleContext

getAccessibleContext

()

Gets the

AccessibleContext

for the

JSpinner

ChangeListener

[]

getChangeListeners

()

Returns an array of all the

ChangeListener

s added
to this JSpinner with addChangeListener().

JComponent

getEditor

()

Returns the component that displays and potentially
changes the model's value.

SpinnerModel

getModel

()

Returns the

SpinnerModel

that defines
this spinners sequence of values.

Object

getNextValue

()

Returns the object in the sequence that comes after the object returned
by

getValue()

.

Object

getPreviousValue

()

Returns the object in the sequence that comes
before the object returned by

getValue()

.

SpinnerUI

getUI

()

Returns the look and feel (L&F) object that renders this component.

String

getUIClassID

()

Returns the suffix used to construct the name of the look and feel
(L&F) class used to render this component.

Object

getValue

()

Returns the current value of the model, typically
this value is displayed by the

editor

.

void

removeChangeListener

​(

ChangeListener

listener)

Removes a

ChangeListener

from this spinner.

void

setEditor

​(

JComponent

editor)

Changes the

JComponent

that displays the current value
of the

SpinnerModel

.

void

setModel

​(

SpinnerModel

model)

Changes the model that represents the value of this spinner.

void

setUI

​(

SpinnerUI

ui)

Sets the look and feel (L&F) object that renders this component.

void

setValue

​(

Object

value)

Changes current value of the model, typically
this value is displayed by the

editor

.

void

updateUI

()

Resets the UI property with the value from the current look and feel.

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

paramString

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

imageUpdate

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

JSpinner.AccessibleJSpinner

AccessibleJSpinner

implements accessibility
support for the

JSpinner

class.

static class

JSpinner.DateEditor

An editor for a

JSpinner

whose model is a

SpinnerDateModel

.

static class

JSpinner.DefaultEditor

A simple base class for more specialized editors
that displays a read-only view of the model's current
value with a

JFormattedTextField

.

static class

JSpinner.ListEditor

An editor for a

JSpinner

whose model is a

SpinnerListModel

.

static class

JSpinner.NumberEditor

An editor for a

JSpinner

whose model is a

SpinnerNumberModel

.

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

AccessibleJSpinner

implements accessibility
support for the

JSpinner

class.

An editor for a

JSpinner

whose model is a

SpinnerDateModel

.

A simple base class for more specialized editors
that displays a read-only view of the model's current
value with a

JFormattedTextField

.

An editor for a

JSpinner

whose model is a

SpinnerListModel

.

An editor for a

JSpinner

whose model is a

SpinnerNumberModel

.

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

---

#### Field Summary

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

Constructor Summary

Constructors

Constructor

Description

JSpinner

()

Constructs a spinner with an

Integer SpinnerNumberModel

with initial value 0 and no minimum or maximum limits.

JSpinner

​(

SpinnerModel

model)

Constructs a spinner for the given model.

---

#### Constructor Summary

Constructs a spinner with an

Integer SpinnerNumberModel

with initial value 0 and no minimum or maximum limits.

Constructs a spinner for the given model.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addChangeListener

​(

ChangeListener

listener)

Adds a listener to the list that is notified each time a change
to the model occurs.

void

commitEdit

()

Commits the currently edited value to the

SpinnerModel

.

protected

JComponent

createEditor

​(

SpinnerModel

model)

This method is called by the constructors to create the

JComponent

that displays the current value of the sequence.

protected void

fireStateChanged

()

Sends a

ChangeEvent

, whose source is this

JSpinner

, to each

ChangeListener

.

AccessibleContext

getAccessibleContext

()

Gets the

AccessibleContext

for the

JSpinner

ChangeListener

[]

getChangeListeners

()

Returns an array of all the

ChangeListener

s added
to this JSpinner with addChangeListener().

JComponent

getEditor

()

Returns the component that displays and potentially
changes the model's value.

SpinnerModel

getModel

()

Returns the

SpinnerModel

that defines
this spinners sequence of values.

Object

getNextValue

()

Returns the object in the sequence that comes after the object returned
by

getValue()

.

Object

getPreviousValue

()

Returns the object in the sequence that comes
before the object returned by

getValue()

.

SpinnerUI

getUI

()

Returns the look and feel (L&F) object that renders this component.

String

getUIClassID

()

Returns the suffix used to construct the name of the look and feel
(L&F) class used to render this component.

Object

getValue

()

Returns the current value of the model, typically
this value is displayed by the

editor

.

void

removeChangeListener

​(

ChangeListener

listener)

Removes a

ChangeListener

from this spinner.

void

setEditor

​(

JComponent

editor)

Changes the

JComponent

that displays the current value
of the

SpinnerModel

.

void

setModel

​(

SpinnerModel

model)

Changes the model that represents the value of this spinner.

void

setUI

​(

SpinnerUI

ui)

Sets the look and feel (L&F) object that renders this component.

void

setValue

​(

Object

value)

Changes current value of the model, typically
this value is displayed by the

editor

.

void

updateUI

()

Resets the UI property with the value from the current look and feel.

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

paramString

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

imageUpdate

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

Adds a listener to the list that is notified each time a change
to the model occurs.

Commits the currently edited value to the

SpinnerModel

.

This method is called by the constructors to create the

JComponent

that displays the current value of the sequence.

Sends a

ChangeEvent

, whose source is this

JSpinner

, to each

ChangeListener

.

Gets the

AccessibleContext

for the

JSpinner

Returns an array of all the

ChangeListener

s added
to this JSpinner with addChangeListener().

Returns the component that displays and potentially
changes the model's value.

Returns the

SpinnerModel

that defines
this spinners sequence of values.

Returns the object in the sequence that comes after the object returned
by

getValue()

.

Returns the object in the sequence that comes
before the object returned by

getValue()

.

Returns the look and feel (L&F) object that renders this component.

Returns the suffix used to construct the name of the look and feel
(L&F) class used to render this component.

Returns the current value of the model, typically
this value is displayed by the

editor

.

Removes a

ChangeListener

from this spinner.

Changes the

JComponent

that displays the current value
of the

SpinnerModel

.

Changes the model that represents the value of this spinner.

Sets the look and feel (L&F) object that renders this component.

Changes current value of the model, typically
this value is displayed by the

editor

.

Resets the UI property with the value from the current look and feel.

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

paramString

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

imageUpdate

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- JSpinner

```java
public JSpinner​(
SpinnerModel
model)
```

Constructs a spinner for the given model. The spinner has
a set of previous/next buttons, and an editor appropriate
for the model.

**Parameters:** model

- a model for the new spinner
**Throws:** NullPointerException

- if the model is

null

- JSpinner

```java
public JSpinner()
```

Constructs a spinner with an

Integer SpinnerNumberModel

with initial value 0 and no minimum or maximum limits.

============ METHOD DETAIL ==========

- Method Detail

- getUI

```java
public
SpinnerUI
getUI()
```

Returns the look and feel (L&F) object that renders this component.

**Overrides:** getUI

in class

JComponent
**Returns:** the

SpinnerUI

object that renders this component

- setUI

```java
public void setUI​(
SpinnerUI
ui)
```

Sets the look and feel (L&F) object that renders this component.

**Parameters:** ui

- the

SpinnerUI

L&F object
**See Also:** UIDefaults.getUI(javax.swing.JComponent)

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

Returns the suffix used to construct the name of the look and feel
(L&F) class used to render this component.

**Overrides:** getUIClassID

in class

JComponent
**Returns:** the string "SpinnerUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

- updateUI

```java
public void updateUI()
```

Resets the UI property with the value from the current look and feel.

**Overrides:** updateUI

in class

JComponent
**See Also:** UIManager.getUI(javax.swing.JComponent)

- createEditor

```java
protected
JComponent
createEditor​(
SpinnerModel
model)
```

This method is called by the constructors to create the

JComponent

that displays the current value of the sequence. The editor may
also allow the user to enter an element of the sequence directly.
An editor must listen for

ChangeEvents

on the

model

and keep the value it displays
in sync with the value of the model.

Subclasses may override this method to add support for new

SpinnerModel

classes. Alternatively one can just
replace the editor created here with the

setEditor

method. The default mapping from model type to editor is:

- SpinnerNumberModel => JSpinner.NumberEditor

SpinnerDateModel => JSpinner.DateEditor

SpinnerListModel => JSpinner.ListEditor

all others

=>

JSpinner.DefaultEditor

**Parameters:** model

- the value of getModel
**Returns:** a component that displays the current value of the sequence
**See Also:** getModel()

,

setEditor(javax.swing.JComponent)

- setModel

```java
@BeanProperty
(
visualUpdate
=true,

description
="Model that represents the value of this spinner.")
public void setModel​(
SpinnerModel
model)
```

Changes the model that represents the value of this spinner.
If the editor property has not been explicitly set,
the editor property is (implicitly) set after the

"model"

PropertyChangeEvent

has been fired. The editor
property is set to the value returned by

createEditor

,
as in:

```java
setEditor(createEditor(model));
```

**Parameters:** model

- the new

SpinnerModel
**Throws:** IllegalArgumentException

- if model is

null
**See Also:** getModel()

,

getEditor()

,

setEditor(javax.swing.JComponent)

- getModel

```java
public
SpinnerModel
getModel()
```

Returns the

SpinnerModel

that defines
this spinners sequence of values.

**Returns:** the value of the model property
**See Also:** setModel(javax.swing.SpinnerModel)

- getValue

```java
public
Object
getValue()
```

Returns the current value of the model, typically
this value is displayed by the

editor

. If the
user has changed the value displayed by the

editor

it is
possible for the

model

's value to differ from that of
the

editor

, refer to the class level javadoc for examples
of how to deal with this.

This method simply delegates to the

model

.
It is equivalent to:

```java
getModel().getValue()
```

**Returns:** the current value of the model
**See Also:** setValue(java.lang.Object)

,

SpinnerModel.getValue()

- setValue

```java
public void setValue​(
Object
value)
```

Changes current value of the model, typically
this value is displayed by the

editor

.
If the

SpinnerModel

implementation
doesn't support the specified value then an

IllegalArgumentException

is thrown.

This method simply delegates to the

model

.
It is equivalent to:

```java
getModel().setValue(value)
```

**Parameters:** value

- new value for the spinner
**Throws:** IllegalArgumentException

- if

value

isn't allowed
**See Also:** getValue()

,

SpinnerModel.setValue(java.lang.Object)

- getNextValue

```java
@BeanProperty
(
bound
=false)
public
Object
getNextValue()
```

Returns the object in the sequence that comes after the object returned
by

getValue()

. If the end of the sequence has been reached
then return

null

.
Calling this method does not effect

value

.

This method simply delegates to the

model

.
It is equivalent to:

```java
getModel().getNextValue()
```

**Returns:** the next legal value or

null

if one doesn't exist
**See Also:** getValue()

,

getPreviousValue()

,

SpinnerModel.getNextValue()

- addChangeListener

```java
public void addChangeListener​(
ChangeListener
listener)
```

Adds a listener to the list that is notified each time a change
to the model occurs. The source of

ChangeEvents

delivered to

ChangeListeners

will be this

JSpinner

. Note also that replacing the model
will not affect listeners added directly to JSpinner.
Applications can add listeners to the model directly. In that
case is that the source of the event would be the

SpinnerModel

.

**Parameters:** listener

- the

ChangeListener

to add
**See Also:** removeChangeListener(javax.swing.event.ChangeListener)

,

getModel()

- removeChangeListener

```java
public void removeChangeListener​(
ChangeListener
listener)
```

Removes a

ChangeListener

from this spinner.

**Parameters:** listener

- the

ChangeListener

to remove
**See Also:** fireStateChanged()

,

addChangeListener(javax.swing.event.ChangeListener)

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
to this JSpinner with addChangeListener().

**Returns:** all of the

ChangeListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

- fireStateChanged

```java
protected void fireStateChanged()
```

Sends a

ChangeEvent

, whose source is this

JSpinner

, to each

ChangeListener

.
When a

ChangeListener

has been added
to the spinner, this method is called each time
a

ChangeEvent

is received from the model.

**See Also:** addChangeListener(javax.swing.event.ChangeListener)

,

removeChangeListener(javax.swing.event.ChangeListener)

,

EventListenerList

- getPreviousValue

```java
@BeanProperty
(
bound
=false)
public
Object
getPreviousValue()
```

Returns the object in the sequence that comes
before the object returned by

getValue()

.
If the end of the sequence has been reached then
return

null

. Calling this method does
not effect

value

.

This method simply delegates to the

model

.
It is equivalent to:

```java
getModel().getPreviousValue()
```

**Returns:** the previous legal value or

null

if one doesn't exist
**See Also:** getValue()

,

getNextValue()

,

SpinnerModel.getPreviousValue()

- setEditor

```java
@BeanProperty
(
visualUpdate
=true,

description
="JComponent that displays the current value of the model")
public void setEditor​(
JComponent
editor)
```

Changes the

JComponent

that displays the current value
of the

SpinnerModel

. It is the responsibility of this
method to

disconnect

the old editor from the model and to
connect the new editor. This may mean removing the
old editors

ChangeListener

from the model or the
spinner itself and adding one for the new editor.

**Parameters:** editor

- the new editor
**Throws:** IllegalArgumentException

- if editor is

null
**See Also:** getEditor()

,

createEditor(javax.swing.SpinnerModel)

,

getModel()

- getEditor

```java
public
JComponent
getEditor()
```

Returns the component that displays and potentially
changes the model's value.

**Returns:** the component that displays and potentially
changes the model's value
**See Also:** setEditor(javax.swing.JComponent)

,

createEditor(javax.swing.SpinnerModel)

- commitEdit

```java
public void commitEdit()
throws
ParseException
```

Commits the currently edited value to the

SpinnerModel

.

If the editor is an instance of

DefaultEditor

, the
call if forwarded to the editor, otherwise this does nothing.

**Throws:** ParseException

- if the currently edited value couldn't
be committed.

- getAccessibleContext

```java
@BeanProperty
(
bound
=false)
public
AccessibleContext
getAccessibleContext()
```

Gets the

AccessibleContext

for the

JSpinner

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** the

AccessibleContext

for the

JSpinner
**Since:** 1.5

Constructor Detail

- JSpinner

```java
public JSpinner​(
SpinnerModel
model)
```

Constructs a spinner for the given model. The spinner has
a set of previous/next buttons, and an editor appropriate
for the model.

**Parameters:** model

- a model for the new spinner
**Throws:** NullPointerException

- if the model is

null

- JSpinner

```java
public JSpinner()
```

Constructs a spinner with an

Integer SpinnerNumberModel

with initial value 0 and no minimum or maximum limits.

---

#### Constructor Detail

JSpinner

```java
public JSpinner​(
SpinnerModel
model)
```

Constructs a spinner for the given model. The spinner has
a set of previous/next buttons, and an editor appropriate
for the model.

**Parameters:** model

- a model for the new spinner
**Throws:** NullPointerException

- if the model is

null

---

#### JSpinner

public JSpinner​(

SpinnerModel

model)

Constructs a spinner for the given model. The spinner has
a set of previous/next buttons, and an editor appropriate
for the model.

JSpinner

```java
public JSpinner()
```

Constructs a spinner with an

Integer SpinnerNumberModel

with initial value 0 and no minimum or maximum limits.

---

#### JSpinner

public JSpinner()

Constructs a spinner with an

Integer SpinnerNumberModel

with initial value 0 and no minimum or maximum limits.

Method Detail

- getUI

```java
public
SpinnerUI
getUI()
```

Returns the look and feel (L&F) object that renders this component.

**Overrides:** getUI

in class

JComponent
**Returns:** the

SpinnerUI

object that renders this component

- setUI

```java
public void setUI​(
SpinnerUI
ui)
```

Sets the look and feel (L&F) object that renders this component.

**Parameters:** ui

- the

SpinnerUI

L&F object
**See Also:** UIDefaults.getUI(javax.swing.JComponent)

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

Returns the suffix used to construct the name of the look and feel
(L&F) class used to render this component.

**Overrides:** getUIClassID

in class

JComponent
**Returns:** the string "SpinnerUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

- updateUI

```java
public void updateUI()
```

Resets the UI property with the value from the current look and feel.

**Overrides:** updateUI

in class

JComponent
**See Also:** UIManager.getUI(javax.swing.JComponent)

- createEditor

```java
protected
JComponent
createEditor​(
SpinnerModel
model)
```

This method is called by the constructors to create the

JComponent

that displays the current value of the sequence. The editor may
also allow the user to enter an element of the sequence directly.
An editor must listen for

ChangeEvents

on the

model

and keep the value it displays
in sync with the value of the model.

Subclasses may override this method to add support for new

SpinnerModel

classes. Alternatively one can just
replace the editor created here with the

setEditor

method. The default mapping from model type to editor is:

- SpinnerNumberModel => JSpinner.NumberEditor

SpinnerDateModel => JSpinner.DateEditor

SpinnerListModel => JSpinner.ListEditor

all others

=>

JSpinner.DefaultEditor

**Parameters:** model

- the value of getModel
**Returns:** a component that displays the current value of the sequence
**See Also:** getModel()

,

setEditor(javax.swing.JComponent)

- setModel

```java
@BeanProperty
(
visualUpdate
=true,

description
="Model that represents the value of this spinner.")
public void setModel​(
SpinnerModel
model)
```

Changes the model that represents the value of this spinner.
If the editor property has not been explicitly set,
the editor property is (implicitly) set after the

"model"

PropertyChangeEvent

has been fired. The editor
property is set to the value returned by

createEditor

,
as in:

```java
setEditor(createEditor(model));
```

**Parameters:** model

- the new

SpinnerModel
**Throws:** IllegalArgumentException

- if model is

null
**See Also:** getModel()

,

getEditor()

,

setEditor(javax.swing.JComponent)

- getModel

```java
public
SpinnerModel
getModel()
```

Returns the

SpinnerModel

that defines
this spinners sequence of values.

**Returns:** the value of the model property
**See Also:** setModel(javax.swing.SpinnerModel)

- getValue

```java
public
Object
getValue()
```

Returns the current value of the model, typically
this value is displayed by the

editor

. If the
user has changed the value displayed by the

editor

it is
possible for the

model

's value to differ from that of
the

editor

, refer to the class level javadoc for examples
of how to deal with this.

This method simply delegates to the

model

.
It is equivalent to:

```java
getModel().getValue()
```

**Returns:** the current value of the model
**See Also:** setValue(java.lang.Object)

,

SpinnerModel.getValue()

- setValue

```java
public void setValue​(
Object
value)
```

Changes current value of the model, typically
this value is displayed by the

editor

.
If the

SpinnerModel

implementation
doesn't support the specified value then an

IllegalArgumentException

is thrown.

This method simply delegates to the

model

.
It is equivalent to:

```java
getModel().setValue(value)
```

**Parameters:** value

- new value for the spinner
**Throws:** IllegalArgumentException

- if

value

isn't allowed
**See Also:** getValue()

,

SpinnerModel.setValue(java.lang.Object)

- getNextValue

```java
@BeanProperty
(
bound
=false)
public
Object
getNextValue()
```

Returns the object in the sequence that comes after the object returned
by

getValue()

. If the end of the sequence has been reached
then return

null

.
Calling this method does not effect

value

.

This method simply delegates to the

model

.
It is equivalent to:

```java
getModel().getNextValue()
```

**Returns:** the next legal value or

null

if one doesn't exist
**See Also:** getValue()

,

getPreviousValue()

,

SpinnerModel.getNextValue()

- addChangeListener

```java
public void addChangeListener​(
ChangeListener
listener)
```

Adds a listener to the list that is notified each time a change
to the model occurs. The source of

ChangeEvents

delivered to

ChangeListeners

will be this

JSpinner

. Note also that replacing the model
will not affect listeners added directly to JSpinner.
Applications can add listeners to the model directly. In that
case is that the source of the event would be the

SpinnerModel

.

**Parameters:** listener

- the

ChangeListener

to add
**See Also:** removeChangeListener(javax.swing.event.ChangeListener)

,

getModel()

- removeChangeListener

```java
public void removeChangeListener​(
ChangeListener
listener)
```

Removes a

ChangeListener

from this spinner.

**Parameters:** listener

- the

ChangeListener

to remove
**See Also:** fireStateChanged()

,

addChangeListener(javax.swing.event.ChangeListener)

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
to this JSpinner with addChangeListener().

**Returns:** all of the

ChangeListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

- fireStateChanged

```java
protected void fireStateChanged()
```

Sends a

ChangeEvent

, whose source is this

JSpinner

, to each

ChangeListener

.
When a

ChangeListener

has been added
to the spinner, this method is called each time
a

ChangeEvent

is received from the model.

**See Also:** addChangeListener(javax.swing.event.ChangeListener)

,

removeChangeListener(javax.swing.event.ChangeListener)

,

EventListenerList

- getPreviousValue

```java
@BeanProperty
(
bound
=false)
public
Object
getPreviousValue()
```

Returns the object in the sequence that comes
before the object returned by

getValue()

.
If the end of the sequence has been reached then
return

null

. Calling this method does
not effect

value

.

This method simply delegates to the

model

.
It is equivalent to:

```java
getModel().getPreviousValue()
```

**Returns:** the previous legal value or

null

if one doesn't exist
**See Also:** getValue()

,

getNextValue()

,

SpinnerModel.getPreviousValue()

- setEditor

```java
@BeanProperty
(
visualUpdate
=true,

description
="JComponent that displays the current value of the model")
public void setEditor​(
JComponent
editor)
```

Changes the

JComponent

that displays the current value
of the

SpinnerModel

. It is the responsibility of this
method to

disconnect

the old editor from the model and to
connect the new editor. This may mean removing the
old editors

ChangeListener

from the model or the
spinner itself and adding one for the new editor.

**Parameters:** editor

- the new editor
**Throws:** IllegalArgumentException

- if editor is

null
**See Also:** getEditor()

,

createEditor(javax.swing.SpinnerModel)

,

getModel()

- getEditor

```java
public
JComponent
getEditor()
```

Returns the component that displays and potentially
changes the model's value.

**Returns:** the component that displays and potentially
changes the model's value
**See Also:** setEditor(javax.swing.JComponent)

,

createEditor(javax.swing.SpinnerModel)

- commitEdit

```java
public void commitEdit()
throws
ParseException
```

Commits the currently edited value to the

SpinnerModel

.

If the editor is an instance of

DefaultEditor

, the
call if forwarded to the editor, otherwise this does nothing.

**Throws:** ParseException

- if the currently edited value couldn't
be committed.

- getAccessibleContext

```java
@BeanProperty
(
bound
=false)
public
AccessibleContext
getAccessibleContext()
```

Gets the

AccessibleContext

for the

JSpinner

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** the

AccessibleContext

for the

JSpinner
**Since:** 1.5

---

#### Method Detail

getUI

```java
public
SpinnerUI
getUI()
```

Returns the look and feel (L&F) object that renders this component.

**Overrides:** getUI

in class

JComponent
**Returns:** the

SpinnerUI

object that renders this component

---

#### getUI

public

SpinnerUI

getUI()

Returns the look and feel (L&F) object that renders this component.

setUI

```java
public void setUI​(
SpinnerUI
ui)
```

Sets the look and feel (L&F) object that renders this component.

**Parameters:** ui

- the

SpinnerUI

L&F object
**See Also:** UIDefaults.getUI(javax.swing.JComponent)

---

#### setUI

public void setUI​(

SpinnerUI

ui)

Sets the look and feel (L&F) object that renders this component.

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

Returns the suffix used to construct the name of the look and feel
(L&F) class used to render this component.

**Overrides:** getUIClassID

in class

JComponent
**Returns:** the string "SpinnerUI"
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

Returns the suffix used to construct the name of the look and feel
(L&F) class used to render this component.

updateUI

```java
public void updateUI()
```

Resets the UI property with the value from the current look and feel.

**Overrides:** updateUI

in class

JComponent
**See Also:** UIManager.getUI(javax.swing.JComponent)

---

#### updateUI

public void updateUI()

Resets the UI property with the value from the current look and feel.

createEditor

```java
protected
JComponent
createEditor​(
SpinnerModel
model)
```

This method is called by the constructors to create the

JComponent

that displays the current value of the sequence. The editor may
also allow the user to enter an element of the sequence directly.
An editor must listen for

ChangeEvents

on the

model

and keep the value it displays
in sync with the value of the model.

Subclasses may override this method to add support for new

SpinnerModel

classes. Alternatively one can just
replace the editor created here with the

setEditor

method. The default mapping from model type to editor is:

- SpinnerNumberModel => JSpinner.NumberEditor

SpinnerDateModel => JSpinner.DateEditor

SpinnerListModel => JSpinner.ListEditor

all others

=>

JSpinner.DefaultEditor

**Parameters:** model

- the value of getModel
**Returns:** a component that displays the current value of the sequence
**See Also:** getModel()

,

setEditor(javax.swing.JComponent)

---

#### createEditor

protected

JComponent

createEditor​(

SpinnerModel

model)

This method is called by the constructors to create the

JComponent

that displays the current value of the sequence. The editor may
also allow the user to enter an element of the sequence directly.
An editor must listen for

ChangeEvents

on the

model

and keep the value it displays
in sync with the value of the model.

Subclasses may override this method to add support for new

SpinnerModel

classes. Alternatively one can just
replace the editor created here with the

setEditor

method. The default mapping from model type to editor is:

- SpinnerNumberModel => JSpinner.NumberEditor

SpinnerDateModel => JSpinner.DateEditor

SpinnerListModel => JSpinner.ListEditor

all others

=>

JSpinner.DefaultEditor

Subclasses may override this method to add support for new

SpinnerModel

classes. Alternatively one can just
replace the editor created here with the

setEditor

method. The default mapping from model type to editor is:

- SpinnerNumberModel => JSpinner.NumberEditor

SpinnerDateModel => JSpinner.DateEditor

SpinnerListModel => JSpinner.ListEditor

all others

=>

JSpinner.DefaultEditor

SpinnerNumberModel => JSpinner.NumberEditor

SpinnerDateModel => JSpinner.DateEditor

SpinnerListModel => JSpinner.ListEditor

all others

=>

JSpinner.DefaultEditor

setModel

```java
@BeanProperty
(
visualUpdate
=true,

description
="Model that represents the value of this spinner.")
public void setModel​(
SpinnerModel
model)
```

Changes the model that represents the value of this spinner.
If the editor property has not been explicitly set,
the editor property is (implicitly) set after the

"model"

PropertyChangeEvent

has been fired. The editor
property is set to the value returned by

createEditor

,
as in:

```java
setEditor(createEditor(model));
```

**Parameters:** model

- the new

SpinnerModel
**Throws:** IllegalArgumentException

- if model is

null
**See Also:** getModel()

,

getEditor()

,

setEditor(javax.swing.JComponent)

---

#### setModel

@BeanProperty

(

visualUpdate

=true,

description

="Model that represents the value of this spinner.")
public void setModel​(

SpinnerModel

model)

Changes the model that represents the value of this spinner.
If the editor property has not been explicitly set,
the editor property is (implicitly) set after the

"model"

PropertyChangeEvent

has been fired. The editor
property is set to the value returned by

createEditor

,
as in:

```java
setEditor(createEditor(model));
```

setEditor(createEditor(model));

getModel

```java
public
SpinnerModel
getModel()
```

Returns the

SpinnerModel

that defines
this spinners sequence of values.

**Returns:** the value of the model property
**See Also:** setModel(javax.swing.SpinnerModel)

---

#### getModel

public

SpinnerModel

getModel()

Returns the

SpinnerModel

that defines
this spinners sequence of values.

getValue

```java
public
Object
getValue()
```

Returns the current value of the model, typically
this value is displayed by the

editor

. If the
user has changed the value displayed by the

editor

it is
possible for the

model

's value to differ from that of
the

editor

, refer to the class level javadoc for examples
of how to deal with this.

This method simply delegates to the

model

.
It is equivalent to:

```java
getModel().getValue()
```

**Returns:** the current value of the model
**See Also:** setValue(java.lang.Object)

,

SpinnerModel.getValue()

---

#### getValue

public

Object

getValue()

Returns the current value of the model, typically
this value is displayed by the

editor

. If the
user has changed the value displayed by the

editor

it is
possible for the

model

's value to differ from that of
the

editor

, refer to the class level javadoc for examples
of how to deal with this.

This method simply delegates to the

model

.
It is equivalent to:

```java
getModel().getValue()
```

This method simply delegates to the

model

.
It is equivalent to:

```java
getModel().getValue()
```

getModel().getValue()

setValue

```java
public void setValue​(
Object
value)
```

Changes current value of the model, typically
this value is displayed by the

editor

.
If the

SpinnerModel

implementation
doesn't support the specified value then an

IllegalArgumentException

is thrown.

This method simply delegates to the

model

.
It is equivalent to:

```java
getModel().setValue(value)
```

**Parameters:** value

- new value for the spinner
**Throws:** IllegalArgumentException

- if

value

isn't allowed
**See Also:** getValue()

,

SpinnerModel.setValue(java.lang.Object)

---

#### setValue

public void setValue​(

Object

value)

Changes current value of the model, typically
this value is displayed by the

editor

.
If the

SpinnerModel

implementation
doesn't support the specified value then an

IllegalArgumentException

is thrown.

This method simply delegates to the

model

.
It is equivalent to:

```java
getModel().setValue(value)
```

This method simply delegates to the

model

.
It is equivalent to:

```java
getModel().setValue(value)
```

getModel().setValue(value)

getNextValue

```java
@BeanProperty
(
bound
=false)
public
Object
getNextValue()
```

Returns the object in the sequence that comes after the object returned
by

getValue()

. If the end of the sequence has been reached
then return

null

.
Calling this method does not effect

value

.

This method simply delegates to the

model

.
It is equivalent to:

```java
getModel().getNextValue()
```

**Returns:** the next legal value or

null

if one doesn't exist
**See Also:** getValue()

,

getPreviousValue()

,

SpinnerModel.getNextValue()

---

#### getNextValue

@BeanProperty

(

bound

=false)
public

Object

getNextValue()

Returns the object in the sequence that comes after the object returned
by

getValue()

. If the end of the sequence has been reached
then return

null

.
Calling this method does not effect

value

.

This method simply delegates to the

model

.
It is equivalent to:

```java
getModel().getNextValue()
```

This method simply delegates to the

model

.
It is equivalent to:

```java
getModel().getNextValue()
```

getModel().getNextValue()

addChangeListener

```java
public void addChangeListener​(
ChangeListener
listener)
```

Adds a listener to the list that is notified each time a change
to the model occurs. The source of

ChangeEvents

delivered to

ChangeListeners

will be this

JSpinner

. Note also that replacing the model
will not affect listeners added directly to JSpinner.
Applications can add listeners to the model directly. In that
case is that the source of the event would be the

SpinnerModel

.

**Parameters:** listener

- the

ChangeListener

to add
**See Also:** removeChangeListener(javax.swing.event.ChangeListener)

,

getModel()

---

#### addChangeListener

public void addChangeListener​(

ChangeListener

listener)

Adds a listener to the list that is notified each time a change
to the model occurs. The source of

ChangeEvents

delivered to

ChangeListeners

will be this

JSpinner

. Note also that replacing the model
will not affect listeners added directly to JSpinner.
Applications can add listeners to the model directly. In that
case is that the source of the event would be the

SpinnerModel

.

removeChangeListener

```java
public void removeChangeListener​(
ChangeListener
listener)
```

Removes a

ChangeListener

from this spinner.

**Parameters:** listener

- the

ChangeListener

to remove
**See Also:** fireStateChanged()

,

addChangeListener(javax.swing.event.ChangeListener)

---

#### removeChangeListener

public void removeChangeListener​(

ChangeListener

listener)

Removes a

ChangeListener

from this spinner.

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
to this JSpinner with addChangeListener().

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
to this JSpinner with addChangeListener().

fireStateChanged

```java
protected void fireStateChanged()
```

Sends a

ChangeEvent

, whose source is this

JSpinner

, to each

ChangeListener

.
When a

ChangeListener

has been added
to the spinner, this method is called each time
a

ChangeEvent

is received from the model.

**See Also:** addChangeListener(javax.swing.event.ChangeListener)

,

removeChangeListener(javax.swing.event.ChangeListener)

,

EventListenerList

---

#### fireStateChanged

protected void fireStateChanged()

Sends a

ChangeEvent

, whose source is this

JSpinner

, to each

ChangeListener

.
When a

ChangeListener

has been added
to the spinner, this method is called each time
a

ChangeEvent

is received from the model.

getPreviousValue

```java
@BeanProperty
(
bound
=false)
public
Object
getPreviousValue()
```

Returns the object in the sequence that comes
before the object returned by

getValue()

.
If the end of the sequence has been reached then
return

null

. Calling this method does
not effect

value

.

This method simply delegates to the

model

.
It is equivalent to:

```java
getModel().getPreviousValue()
```

**Returns:** the previous legal value or

null

if one doesn't exist
**See Also:** getValue()

,

getNextValue()

,

SpinnerModel.getPreviousValue()

---

#### getPreviousValue

@BeanProperty

(

bound

=false)
public

Object

getPreviousValue()

Returns the object in the sequence that comes
before the object returned by

getValue()

.
If the end of the sequence has been reached then
return

null

. Calling this method does
not effect

value

.

This method simply delegates to the

model

.
It is equivalent to:

```java
getModel().getPreviousValue()
```

This method simply delegates to the

model

.
It is equivalent to:

```java
getModel().getPreviousValue()
```

getModel().getPreviousValue()

setEditor

```java
@BeanProperty
(
visualUpdate
=true,

description
="JComponent that displays the current value of the model")
public void setEditor​(
JComponent
editor)
```

Changes the

JComponent

that displays the current value
of the

SpinnerModel

. It is the responsibility of this
method to

disconnect

the old editor from the model and to
connect the new editor. This may mean removing the
old editors

ChangeListener

from the model or the
spinner itself and adding one for the new editor.

**Parameters:** editor

- the new editor
**Throws:** IllegalArgumentException

- if editor is

null
**See Also:** getEditor()

,

createEditor(javax.swing.SpinnerModel)

,

getModel()

---

#### setEditor

@BeanProperty

(

visualUpdate

=true,

description

="JComponent that displays the current value of the model")
public void setEditor​(

JComponent

editor)

Changes the

JComponent

that displays the current value
of the

SpinnerModel

. It is the responsibility of this
method to

disconnect

the old editor from the model and to
connect the new editor. This may mean removing the
old editors

ChangeListener

from the model or the
spinner itself and adding one for the new editor.

getEditor

```java
public
JComponent
getEditor()
```

Returns the component that displays and potentially
changes the model's value.

**Returns:** the component that displays and potentially
changes the model's value
**See Also:** setEditor(javax.swing.JComponent)

,

createEditor(javax.swing.SpinnerModel)

---

#### getEditor

public

JComponent

getEditor()

Returns the component that displays and potentially
changes the model's value.

commitEdit

```java
public void commitEdit()
throws
ParseException
```

Commits the currently edited value to the

SpinnerModel

.

If the editor is an instance of

DefaultEditor

, the
call if forwarded to the editor, otherwise this does nothing.

**Throws:** ParseException

- if the currently edited value couldn't
be committed.

---

#### commitEdit

public void commitEdit()
throws

ParseException

Commits the currently edited value to the

SpinnerModel

.

If the editor is an instance of

DefaultEditor

, the
call if forwarded to the editor, otherwise this does nothing.

If the editor is an instance of

DefaultEditor

, the
call if forwarded to the editor, otherwise this does nothing.

getAccessibleContext

```java
@BeanProperty
(
bound
=false)
public
AccessibleContext
getAccessibleContext()
```

Gets the

AccessibleContext

for the

JSpinner

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** the

AccessibleContext

for the

JSpinner
**Since:** 1.5

---

#### getAccessibleContext

@BeanProperty

(

bound

=false)
public

AccessibleContext

getAccessibleContext()

Gets the

AccessibleContext

for the

JSpinner

---

