# Class AccessibleContext

**Source:** `java.desktop\javax\accessibility\AccessibleContext.html`

### Class Description

```java
@JavaBean
(
description
="Minimal information that all accessible objects return")
public abstract class
AccessibleContext

extends
Object
```

AccessibleContext

represents the minimum information all accessible
objects return. This information includes the accessible name, description,
role, and state of the object, as well as information about its parent and
children.

AccessibleContext

also contains methods for obtaining more
specific accessibility information about a component. If the component
supports them, these methods will return an object that implements one or
more of the following interfaces:

- AccessibleAction

- the object can perform one or more actions.
This interface provides the standard mechanism for an assistive technology
to determine what those actions are and tell the object to perform them.
Any object that can be manipulated should support this interface.

AccessibleComponent

- the object has a graphical
representation. This interface provides the standard mechanism for an
assistive technology to determine and set the graphical representation of
the object. Any object that is rendered on the screen should support this
interface.

AccessibleSelection

- the object allows its children to be
selected. This interface provides the standard mechanism for an assistive
technology to determine the currently selected children of the object as
well as modify its selection set. Any object that has children that can be
selected should support this interface.

AccessibleText

- the object presents editable textual
information on the display. This interface provides the standard mechanism
for an assistive technology to access that text via its content,
attributes, and spatial location. Any object that contains editable text
should support this interface.

AccessibleValue

- the object supports a numerical value. This
interface provides the standard mechanism for an assistive technology to
determine and set the current value of the object, as well as obtain its
minimum and maximum values. Any object that supports a numerical value
should support this interface.

**Direct Known Subclasses:** Component.AccessibleAWTComponent

,

ImageIcon.AccessibleImageIcon

,

JList.AccessibleJList.AccessibleJListChild

,

JTable.AccessibleJTable.AccessibleJTableCell

,

JTableHeader.AccessibleJTableHeader.AccessibleJTableHeaderEntry

,

JTree.AccessibleJTree.AccessibleJTreeNode

,

MenuComponent.AccessibleAWTMenuComponent

,

ProgressMonitor.AccessibleProgressMonitor

,

Translator

---

### Field Details

#### public static final
String
ACCESSIBLE_NAME_PROPERTY

Constant used to determine when the

accessibleName

property has
changed. The old value in the

PropertyChangeEvent

will be the old

accessibleName

and the new value will be the new

accessibleName

.

**See Also:**
- getAccessibleName()

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Constant Field Values

---

#### public static final
String
ACCESSIBLE_DESCRIPTION_PROPERTY

Constant used to determine when the

accessibleDescription

property has changed. The old value in the

PropertyChangeEvent

will be the old

accessibleDescription

and the new value will be
the new

accessibleDescription

.

**See Also:**
- getAccessibleDescription()

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Constant Field Values

---

#### public static final
String
ACCESSIBLE_STATE_PROPERTY

Constant used to determine when the

accessibleStateSet

property
has changed. The old value will be the old

AccessibleState

and
the new value will be the new

AccessibleState

in the

accessibleStateSet

. For example, if a component that supports the
vertical and horizontal states changes its orientation from vertical to
horizontal, the old value will be

AccessibleState.VERTICAL

and
the new value will be

AccessibleState.HORIZONTAL

. Please note
that either value can also be

null

. For example, when a component
changes from being enabled to disabled, the old value will be

AccessibleState.ENABLED

and the new value will be

null

.

**See Also:**
- getAccessibleStateSet()

,

AccessibleState

,

AccessibleStateSet

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Constant Field Values

---

#### public static final
String
ACCESSIBLE_VALUE_PROPERTY

Constant used to determine when the

accessibleValue

property has
changed. The old value in the

PropertyChangeEvent

will be a

Number

representing the old value and the new value will be a

Number

representing the new value.

**See Also:**
- getAccessibleValue()

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Constant Field Values

---

#### public static final
String
ACCESSIBLE_SELECTION_PROPERTY

Constant used to determine when the

accessibleSelection

has
changed. The old and new values in the

PropertyChangeEvent

are
currently reserved for future use.

**See Also:**
- getAccessibleSelection()

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Constant Field Values

---

#### public static final
String
ACCESSIBLE_CARET_PROPERTY

Constant used to determine when the

accessibleText

caret has
changed. The old value in the

PropertyChangeEvent

will be an
integer representing the old caret position, and the new value will be an
integer representing the new/current caret position.

**See Also:**
- addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Constant Field Values

---

#### public static final
String
ACCESSIBLE_VISIBLE_DATA_PROPERTY

Constant used to determine when the visual appearance of the object has
changed. The old and new values in the

PropertyChangeEvent

are
currently reserved for future use.

**See Also:**
- addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Constant Field Values

---

#### public static final
String
ACCESSIBLE_CHILD_PROPERTY

Constant used to determine when

Accessible

children are
added/removed from the object. If an

Accessible

child is being
added, the old value will be

null

and the new value will be the

Accessible

child. If an

Accessible

child is being
removed, the old value will be the

Accessible

child, and the new
value will be

null

.

**See Also:**
- addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Constant Field Values

---

#### public static final
String
ACCESSIBLE_ACTIVE_DESCENDANT_PROPERTY

Constant used to determine when the active descendant of a component has
changed. The active descendant is used for objects such as list, tree,
and table, which may have transient children. When the active descendant
has changed, the old value of the property change event will be the

Accessible

representing the previous active child, and the new
value will be the

Accessible

representing the current active
child.

**See Also:**
- addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Constant Field Values

---

#### public static final
String
ACCESSIBLE_TABLE_CAPTION_CHANGED

Constant used to indicate that the table caption has changed. The old
value in the

PropertyChangeEvent

will be an

Accessible

representing the previous table caption and the new value will be an

Accessible

representing the new table caption.

**See Also:**
- Accessible

,

AccessibleTable

,

Constant Field Values

---

#### public static final
String
ACCESSIBLE_TABLE_SUMMARY_CHANGED

Constant used to indicate that the table summary has changed. The old
value in the

PropertyChangeEvent

will be an

Accessible

representing the previous table summary and the new value will be an

Accessible

representing the new table summary.

**See Also:**
- Accessible

,

AccessibleTable

,

Constant Field Values

---

#### public static final
String
ACCESSIBLE_TABLE_MODEL_CHANGED

Constant used to indicate that table data has changed. The old value in
the

PropertyChangeEvent

will be

null

and the new value
will be an

AccessibleTableModelChange

representing the table
change.

**See Also:**
- AccessibleTable

,

AccessibleTableModelChange

,

Constant Field Values

---

#### public static final
String
ACCESSIBLE_TABLE_ROW_HEADER_CHANGED

Constant used to indicate that the row header has changed. The old value
in the

PropertyChangeEvent

will be

null

and the new value
will be an

AccessibleTableModelChange

representing the header
change.

**See Also:**
- AccessibleTable

,

AccessibleTableModelChange

,

Constant Field Values

---

#### public static final
String
ACCESSIBLE_TABLE_ROW_DESCRIPTION_CHANGED

Constant used to indicate that the row description has changed. The old
value in the

PropertyChangeEvent

will be

null

and the new
value will be an

Integer

representing the row index.

**See Also:**
- AccessibleTable

,

Constant Field Values

---

#### public static final
String
ACCESSIBLE_TABLE_COLUMN_HEADER_CHANGED

Constant used to indicate that the column header has changed. The old
value in the

PropertyChangeEvent

will be

null

and the new
value will be an

AccessibleTableModelChange

representing the
header change.

**See Also:**
- AccessibleTable

,

AccessibleTableModelChange

,

Constant Field Values

---

#### public static final
String
ACCESSIBLE_TABLE_COLUMN_DESCRIPTION_CHANGED

Constant used to indicate that the column description has changed. The
old value in the

PropertyChangeEvent

will be

null

and the
new value will be an

Integer

representing the column index.

**See Also:**
- AccessibleTable

,

Constant Field Values

---

#### public static final
String
ACCESSIBLE_ACTION_PROPERTY

Constant used to indicate that the supported set of actions has changed.
The old value in the

PropertyChangeEvent

will be an

Integer

representing the old number of actions supported and the
new value will be an

Integer

representing the new number of
actions supported.

**See Also:**
- AccessibleAction

,

Constant Field Values

---

#### public static final
String
ACCESSIBLE_HYPERTEXT_OFFSET

Constant used to indicate that a hypertext element has received focus.
The old value in the

PropertyChangeEvent

will be an

Integer

representing the start index in the document of the
previous element that had focus and the new value will be an

Integer

representing the start index in the document of the
current element that has focus. A value of -1 indicates that an element
does not or did not have focus.

**See Also:**
- AccessibleHyperlink

,

Constant Field Values

---

#### public static final
String
ACCESSIBLE_TEXT_PROPERTY

PropertyChangeEvent

which indicates that text has changed.

For text insertion, the

oldValue

is

null

and the

newValue

is an

AccessibleTextSequence

specifying the text
that was inserted.

For text deletion, the

oldValue

is an

AccessibleTextSequence

specifying the text that was deleted and
the

newValue

is

null

.

For text replacement, the

oldValue

is an

AccessibleTextSequence

specifying the old text and the

newValue

is an

AccessibleTextSequence

specifying the new
text.

**See Also:**
- getAccessibleText()

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

,

AccessibleTextSequence

,

Constant Field Values

---

#### public static final
String
ACCESSIBLE_INVALIDATE_CHILDREN

PropertyChangeEvent

which indicates that a significant change has
occurred to the children of a component like a tree or text. This change
notifies the event listener that it needs to reacquire the state of the
subcomponents. The

oldValue

is

null

and the

newValue

is the component whose children have become invalid.

**See Also:**
- getAccessibleText()

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

,

AccessibleTextSequence

,

Constant Field Values

**Since:**
- 1.5

---

#### public static final
String
ACCESSIBLE_TEXT_ATTRIBUTES_CHANGED

PropertyChangeEvent

which indicates that text attributes have
changed.

For attribute insertion, the

oldValue

is

null

and the

newValue

is an

AccessibleAttributeSequence

specifying the
attributes that were inserted.

For attribute deletion, the

oldValue

is an

AccessibleAttributeSequence

specifying the attributes that were
deleted and the

newValue

is

null

.

For attribute replacement, the

oldValue

is an

AccessibleAttributeSequence

specifying the old attributes and the

newValue

is an

AccessibleAttributeSequence

specifying the
new attributes.

**See Also:**
- getAccessibleText()

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

,

AccessibleAttributeSequence

,

Constant Field Values

**Since:**
- 1.5

---

#### public static final
String
ACCESSIBLE_COMPONENT_BOUNDS_CHANGED

PropertyChangeEvent

which indicates that a change has occurred in
a component's bounds. The

oldValue

is the old component bounds
and the

newValue

is the new component bounds.

**See Also:**
- addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Constant Field Values

**Since:**
- 1.5

---

#### protected
Accessible
accessibleParent

The accessible parent of this object.

**See Also:**
- getAccessibleParent()

,

setAccessibleParent(javax.accessibility.Accessible)

---

#### protected
String
accessibleName

A localized String containing the name of the object.

**See Also:**
- getAccessibleName()

,

setAccessibleName(java.lang.String)

---

#### protected
String
accessibleDescription

A localized String containing the description of the object.

**See Also:**
- getAccessibleDescription()

,

setAccessibleDescription(java.lang.String)

---

### Constructor Details

#### public AccessibleContext()

*No description found.*

---

### Method Details

#### public
String
getAccessibleName()

Gets the

accessibleName

property of this object. The

accessibleName

property of an object is a localized

String

that designates the purpose of the object. For example,
the

accessibleName

property of a label or button might be the
text of the label or button itself. In the case of an object that doesn't
display its name, the

accessibleName

should still be set. For
example, in the case of a text field used to enter the name of a city,
the

accessibleName

for the

en_US

locale could be 'city.'

**Returns:**
- the localized name of the object;

null

if this object
does not have a name

**See Also:**
- setAccessibleName(java.lang.String)

---

#### @BeanProperty
(
preferred
=true,

description
="Sets the accessible name for the component.")
public void setAccessibleName​(
String
s)

Sets the localized accessible name of this object. Changing the name will
cause a

PropertyChangeEvent

to be fired for the

ACCESSIBLE_NAME_PROPERTY

property.

**Parameters:**
- s

- the new localized name of the object

**See Also:**
- getAccessibleName()

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

---

#### public
String
getAccessibleDescription()

Gets the

accessibleDescription

property of this object. The

accessibleDescription

property of this object is a short
localized phrase describing the purpose of the object. For example, in
the case of a 'Cancel' button, the

accessibleDescription

could be
'Ignore changes and close dialog box.'

**Returns:**
- the localized description of the object;

null

if this
object does not have a description

**See Also:**
- setAccessibleDescription(java.lang.String)

---

#### @BeanProperty
(
preferred
=true,

description
="Sets the accessible description for the component.")
public void setAccessibleDescription​(
String
s)

Sets the accessible description of this object. Changing the name will
cause a

PropertyChangeEvent

to be fired for the

ACCESSIBLE_DESCRIPTION_PROPERTY

property.

**Parameters:**
- s

- the new localized description of the object

**See Also:**
- setAccessibleName(java.lang.String)

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

---

#### public abstract
AccessibleRole
getAccessibleRole()

Gets the role of this object. The role of the object is the generic
purpose or use of the class of this object. For example, the role of a
push button is

AccessibleRole.PUSH_BUTTON

. The roles in

AccessibleRole

are provided so component developers can pick from
a set of predefined roles. This enables assistive technologies to provide
a consistent interface to various tweaked subclasses of components (e.g.,
use

AccessibleRole.PUSH_BUTTON

for all components that act like a
push button) as well as distinguish between subclasses that behave
differently (e.g.,

AccessibleRole.CHECK_BOX

for check boxes and

AccessibleRole.RADIO_BUTTON

for radio buttons).

Note that the

AccessibleRole

class is also extensible, so custom
component developers can define their own

AccessibleRole

's if the
set of predefined roles is inadequate.

**Returns:**
- an instance of

AccessibleRole

describing the role of the
object

**See Also:**
- AccessibleRole

---

#### public abstract
AccessibleStateSet
getAccessibleStateSet()

Gets the state set of this object. The

AccessibleStateSet

of an
object is composed of a set of unique

AccessibleStates

. A change
in the

AccessibleStateSet

of an object will cause a

PropertyChangeEvent

to be fired for the

ACCESSIBLE_STATE_PROPERTY

property.

**Returns:**
- an instance of

AccessibleStateSet

containing the current
state set of the object

**See Also:**
- AccessibleStateSet

,

AccessibleState

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

---

#### public
Accessible
getAccessibleParent()

Gets the

Accessible

parent of this object.

**Returns:**
- the

Accessible

parent of this object;

null

if
this object does not have an

Accessible

parent

---

#### public void setAccessibleParent​(
Accessible
a)

Sets the

Accessible

parent of this object. This is meant to be
used only in the situations where the actual component's parent should
not be treated as the component's accessible parent and is a method that
should only be called by the parent of the accessible child.

**Parameters:**
- a

- -

Accessible

to be set as the parent

---

#### public abstract int getAccessibleIndexInParent()

Gets the 0-based index of this object in its accessible parent.

**Returns:**
- the 0-based index of this object in its parent; -1 if this object
does not have an accessible parent.

**See Also:**
- getAccessibleParent()

,

getAccessibleChildrenCount()

,

getAccessibleChild(int)

---

#### public abstract int getAccessibleChildrenCount()

Returns the number of accessible children of the object.

**Returns:**
- the number of accessible children of the object.

---

#### public abstract
Accessible
getAccessibleChild​(int i)

Returns the specified

Accessible

child of the object. The

Accessible

children of an

Accessible

object are
zero-based, so the first child of an

Accessible

child is at index
0, the second child is at index 1, and so on.

**Parameters:**
- i

- zero-based index of child

**Returns:**
- the

Accessible

child of the object

**See Also:**
- getAccessibleChildrenCount()

---

#### public abstract
Locale
getLocale()
throws
IllegalComponentStateException

Gets the locale of the component. If the component does not have a
locale, then the locale of its parent is returned.

**Returns:**
- this component's locale. If this component does not have a
locale, the locale of its parent is returned.

**Throws:**
- IllegalComponentStateException

- If the component does not have its
own locale and has not yet been added to a containment hierarchy
such that the locale can be determined from the containing
parent

---

#### public void addPropertyChangeListener​(
PropertyChangeListener
listener)

Adds a

PropertyChangeListener

to the listener list. The listener
is registered for all

Accessible

properties and will be called
when those properties change.

**Parameters:**
- listener

- The PropertyChangeListener to be added

**See Also:**
- ACCESSIBLE_NAME_PROPERTY

,

ACCESSIBLE_DESCRIPTION_PROPERTY

,

ACCESSIBLE_STATE_PROPERTY

,

ACCESSIBLE_VALUE_PROPERTY

,

ACCESSIBLE_SELECTION_PROPERTY

,

ACCESSIBLE_TEXT_PROPERTY

,

ACCESSIBLE_VISIBLE_DATA_PROPERTY

---

#### public void removePropertyChangeListener​(
PropertyChangeListener
listener)

Removes a

PropertyChangeListener

from the listener list. This
removes a

PropertyChangeListener

that was registered for all
properties.

**Parameters:**
- listener

- The PropertyChangeListener to be removed

---

#### public
AccessibleAction
getAccessibleAction()

Gets the

AccessibleAction

associated with this object that
supports one or more actions.

**Returns:**
- AccessibleAction

if supported by object; else return

null

**See Also:**
- AccessibleAction

---

#### public
AccessibleComponent
getAccessibleComponent()

Gets the

AccessibleComponent

associated with this object that has
a graphical representation.

**Returns:**
- AccessibleComponent

if supported by object; else return

null

**See Also:**
- AccessibleComponent

---

#### public
AccessibleSelection
getAccessibleSelection()

Gets the

AccessibleSelection

associated with this object which
allows its

Accessible

children to be selected.

**Returns:**
- AccessibleSelection

if supported by object; else return

null

**See Also:**
- AccessibleSelection

---

#### public
AccessibleText
getAccessibleText()

Gets the

AccessibleText

associated with this object presenting
text on the display.

**Returns:**
- AccessibleText

if supported by object; else return

null

**See Also:**
- AccessibleText

---

#### public
AccessibleEditableText
getAccessibleEditableText()

Gets the

AccessibleEditableText

associated with this object
presenting editable text on the display.

**Returns:**
- AccessibleEditableText

if supported by object; else
return

null

**See Also:**
- AccessibleEditableText

**Since:**
- 1.4

---

#### public
AccessibleValue
getAccessibleValue()

Gets the

AccessibleValue

associated with this object that
supports a

Numerical

value.

**Returns:**
- AccessibleValue

if supported by object; else return

null

**See Also:**
- AccessibleValue

---

#### public
AccessibleIcon
[] getAccessibleIcon()

Gets the

AccessibleIcons

associated with an object that has one
or more associated icons.

**Returns:**
- an array of

AccessibleIcon

if supported by object;
otherwise return

null

**See Also:**
- AccessibleIcon

**Since:**
- 1.3

---

#### public
AccessibleRelationSet
getAccessibleRelationSet()

Gets the

AccessibleRelationSet

associated with an object.

**Returns:**
- an

AccessibleRelationSet

if supported by object;
otherwise return

null

**See Also:**
- AccessibleRelationSet

**Since:**
- 1.3

---

#### public
AccessibleTable
getAccessibleTable()

Gets the

AccessibleTable

associated with an object.

**Returns:**
- an

AccessibleTable

if supported by object; otherwise return

null

**See Also:**
- AccessibleTable

**Since:**
- 1.3

---

#### public void firePropertyChange​(
String
propertyName,

Object
oldValue,

Object
newValue)

Support for reporting bound property changes. If

oldValue

and

newValue

are not equal and the

PropertyChangeEvent

listener list is not empty, then fire a

PropertyChange

event to
each listener. In general, this is for use by the

Accessible

objects themselves and should not be called by an application program.

**Parameters:**
- propertyName

- The programmatic name of the property that was
changed
- oldValue

- The old value of the property
- newValue

- The new value of the property

**See Also:**
- PropertyChangeSupport

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

,

removePropertyChangeListener(java.beans.PropertyChangeListener)

,

ACCESSIBLE_NAME_PROPERTY

,

ACCESSIBLE_DESCRIPTION_PROPERTY

,

ACCESSIBLE_STATE_PROPERTY

,

ACCESSIBLE_VALUE_PROPERTY

,

ACCESSIBLE_SELECTION_PROPERTY

,

ACCESSIBLE_TEXT_PROPERTY

,

ACCESSIBLE_VISIBLE_DATA_PROPERTY

---

### Additional Sections

#### Class AccessibleContext

java.lang.Object

- javax.accessibility.AccessibleContext

javax.accessibility.AccessibleContext

**Direct Known Subclasses:** Component.AccessibleAWTComponent

,

ImageIcon.AccessibleImageIcon

,

JList.AccessibleJList.AccessibleJListChild

,

JTable.AccessibleJTable.AccessibleJTableCell

,

JTableHeader.AccessibleJTableHeader.AccessibleJTableHeaderEntry

,

JTree.AccessibleJTree.AccessibleJTreeNode

,

MenuComponent.AccessibleAWTMenuComponent

,

ProgressMonitor.AccessibleProgressMonitor

,

Translator

```java
@JavaBean
(
description
="Minimal information that all accessible objects return")
public abstract class
AccessibleContext

extends
Object
```

AccessibleContext

represents the minimum information all accessible
objects return. This information includes the accessible name, description,
role, and state of the object, as well as information about its parent and
children.

AccessibleContext

also contains methods for obtaining more
specific accessibility information about a component. If the component
supports them, these methods will return an object that implements one or
more of the following interfaces:

- AccessibleAction

- the object can perform one or more actions.
This interface provides the standard mechanism for an assistive technology
to determine what those actions are and tell the object to perform them.
Any object that can be manipulated should support this interface.

AccessibleComponent

- the object has a graphical
representation. This interface provides the standard mechanism for an
assistive technology to determine and set the graphical representation of
the object. Any object that is rendered on the screen should support this
interface.

AccessibleSelection

- the object allows its children to be
selected. This interface provides the standard mechanism for an assistive
technology to determine the currently selected children of the object as
well as modify its selection set. Any object that has children that can be
selected should support this interface.

AccessibleText

- the object presents editable textual
information on the display. This interface provides the standard mechanism
for an assistive technology to access that text via its content,
attributes, and spatial location. Any object that contains editable text
should support this interface.

AccessibleValue

- the object supports a numerical value. This
interface provides the standard mechanism for an assistive technology to
determine and set the current value of the object, as well as obtain its
minimum and maximum values. Any object that supports a numerical value
should support this interface.

@JavaBean

(

description

="Minimal information that all accessible objects return")
public abstract class

AccessibleContext

extends

Object

AccessibleContext

represents the minimum information all accessible
objects return. This information includes the accessible name, description,
role, and state of the object, as well as information about its parent and
children.

AccessibleContext

also contains methods for obtaining more
specific accessibility information about a component. If the component
supports them, these methods will return an object that implements one or
more of the following interfaces:

- AccessibleAction

- the object can perform one or more actions.
This interface provides the standard mechanism for an assistive technology
to determine what those actions are and tell the object to perform them.
Any object that can be manipulated should support this interface.

AccessibleComponent

- the object has a graphical
representation. This interface provides the standard mechanism for an
assistive technology to determine and set the graphical representation of
the object. Any object that is rendered on the screen should support this
interface.

AccessibleSelection

- the object allows its children to be
selected. This interface provides the standard mechanism for an assistive
technology to determine the currently selected children of the object as
well as modify its selection set. Any object that has children that can be
selected should support this interface.

AccessibleText

- the object presents editable textual
information on the display. This interface provides the standard mechanism
for an assistive technology to access that text via its content,
attributes, and spatial location. Any object that contains editable text
should support this interface.

AccessibleValue

- the object supports a numerical value. This
interface provides the standard mechanism for an assistive technology to
determine and set the current value of the object, as well as obtain its
minimum and maximum values. Any object that supports a numerical value
should support this interface.

AccessibleAction

- the object can perform one or more actions.
This interface provides the standard mechanism for an assistive technology
to determine what those actions are and tell the object to perform them.
Any object that can be manipulated should support this interface.

AccessibleComponent

- the object has a graphical
representation. This interface provides the standard mechanism for an
assistive technology to determine and set the graphical representation of
the object. Any object that is rendered on the screen should support this
interface.

AccessibleSelection

- the object allows its children to be
selected. This interface provides the standard mechanism for an assistive
technology to determine the currently selected children of the object as
well as modify its selection set. Any object that has children that can be
selected should support this interface.

AccessibleText

- the object presents editable textual
information on the display. This interface provides the standard mechanism
for an assistive technology to access that text via its content,
attributes, and spatial location. Any object that contains editable text
should support this interface.

AccessibleValue

- the object supports a numerical value. This
interface provides the standard mechanism for an assistive technology to
determine and set the current value of the object, as well as obtain its
minimum and maximum values. Any object that supports a numerical value
should support this interface.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

ACCESSIBLE_ACTION_PROPERTY

Constant used to indicate that the supported set of actions has changed.

static

String

ACCESSIBLE_ACTIVE_DESCENDANT_PROPERTY

Constant used to determine when the active descendant of a component has
changed.

static

String

ACCESSIBLE_CARET_PROPERTY

Constant used to determine when the

accessibleText

caret has
changed.

static

String

ACCESSIBLE_CHILD_PROPERTY

Constant used to determine when

Accessible

children are
added/removed from the object.

static

String

ACCESSIBLE_COMPONENT_BOUNDS_CHANGED

PropertyChangeEvent

which indicates that a change has occurred in
a component's bounds.

static

String

ACCESSIBLE_DESCRIPTION_PROPERTY

Constant used to determine when the

accessibleDescription

property has changed.

static

String

ACCESSIBLE_HYPERTEXT_OFFSET

Constant used to indicate that a hypertext element has received focus.

static

String

ACCESSIBLE_INVALIDATE_CHILDREN

PropertyChangeEvent

which indicates that a significant change has
occurred to the children of a component like a tree or text.

static

String

ACCESSIBLE_NAME_PROPERTY

Constant used to determine when the

accessibleName

property has
changed.

static

String

ACCESSIBLE_SELECTION_PROPERTY

Constant used to determine when the

accessibleSelection

has
changed.

static

String

ACCESSIBLE_STATE_PROPERTY

Constant used to determine when the

accessibleStateSet

property
has changed.

static

String

ACCESSIBLE_TABLE_CAPTION_CHANGED

Constant used to indicate that the table caption has changed.

static

String

ACCESSIBLE_TABLE_COLUMN_DESCRIPTION_CHANGED

Constant used to indicate that the column description has changed.

static

String

ACCESSIBLE_TABLE_COLUMN_HEADER_CHANGED

Constant used to indicate that the column header has changed.

static

String

ACCESSIBLE_TABLE_MODEL_CHANGED

Constant used to indicate that table data has changed.

static

String

ACCESSIBLE_TABLE_ROW_DESCRIPTION_CHANGED

Constant used to indicate that the row description has changed.

static

String

ACCESSIBLE_TABLE_ROW_HEADER_CHANGED

Constant used to indicate that the row header has changed.

static

String

ACCESSIBLE_TABLE_SUMMARY_CHANGED

Constant used to indicate that the table summary has changed.

static

String

ACCESSIBLE_TEXT_ATTRIBUTES_CHANGED

PropertyChangeEvent

which indicates that text attributes have
changed.

static

String

ACCESSIBLE_TEXT_PROPERTY

PropertyChangeEvent

which indicates that text has changed.

static

String

ACCESSIBLE_VALUE_PROPERTY

Constant used to determine when the

accessibleValue

property has
changed.

static

String

ACCESSIBLE_VISIBLE_DATA_PROPERTY

Constant used to determine when the visual appearance of the object has
changed.

protected

String

accessibleDescription

A localized String containing the description of the object.

protected

String

accessibleName

A localized String containing the name of the object.

protected

Accessible

accessibleParent

The accessible parent of this object.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AccessibleContext

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

void

addPropertyChangeListener

​(

PropertyChangeListener

listener)

Adds a

PropertyChangeListener

to the listener list.

void

firePropertyChange

​(

String

propertyName,

Object

oldValue,

Object

newValue)

Support for reporting bound property changes.

AccessibleAction

getAccessibleAction

()

Gets the

AccessibleAction

associated with this object that
supports one or more actions.

abstract

Accessible

getAccessibleChild

​(int i)

Returns the specified

Accessible

child of the object.

abstract int

getAccessibleChildrenCount

()

Returns the number of accessible children of the object.

AccessibleComponent

getAccessibleComponent

()

Gets the

AccessibleComponent

associated with this object that has
a graphical representation.

String

getAccessibleDescription

()

Gets the

accessibleDescription

property of this object.

AccessibleEditableText

getAccessibleEditableText

()

Gets the

AccessibleEditableText

associated with this object
presenting editable text on the display.

AccessibleIcon

[]

getAccessibleIcon

()

Gets the

AccessibleIcons

associated with an object that has one
or more associated icons.

abstract int

getAccessibleIndexInParent

()

Gets the 0-based index of this object in its accessible parent.

String

getAccessibleName

()

Gets the

accessibleName

property of this object.

Accessible

getAccessibleParent

()

Gets the

Accessible

parent of this object.

AccessibleRelationSet

getAccessibleRelationSet

()

Gets the

AccessibleRelationSet

associated with an object.

abstract

AccessibleRole

getAccessibleRole

()

Gets the role of this object.

AccessibleSelection

getAccessibleSelection

()

Gets the

AccessibleSelection

associated with this object which
allows its

Accessible

children to be selected.

abstract

AccessibleStateSet

getAccessibleStateSet

()

Gets the state set of this object.

AccessibleTable

getAccessibleTable

()

Gets the

AccessibleTable

associated with an object.

AccessibleText

getAccessibleText

()

Gets the

AccessibleText

associated with this object presenting
text on the display.

AccessibleValue

getAccessibleValue

()

Gets the

AccessibleValue

associated with this object that
supports a

Numerical

value.

abstract

Locale

getLocale

()

Gets the locale of the component.

void

removePropertyChangeListener

​(

PropertyChangeListener

listener)

Removes a

PropertyChangeListener

from the listener list.

void

setAccessibleDescription

​(

String

s)

Sets the accessible description of this object.

void

setAccessibleName

​(

String

s)

Sets the localized accessible name of this object.

void

setAccessibleParent

​(

Accessible

a)

Sets the

Accessible

parent of this object.

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

static

String

ACCESSIBLE_ACTION_PROPERTY

Constant used to indicate that the supported set of actions has changed.

static

String

ACCESSIBLE_ACTIVE_DESCENDANT_PROPERTY

Constant used to determine when the active descendant of a component has
changed.

static

String

ACCESSIBLE_CARET_PROPERTY

Constant used to determine when the

accessibleText

caret has
changed.

static

String

ACCESSIBLE_CHILD_PROPERTY

Constant used to determine when

Accessible

children are
added/removed from the object.

static

String

ACCESSIBLE_COMPONENT_BOUNDS_CHANGED

PropertyChangeEvent

which indicates that a change has occurred in
a component's bounds.

static

String

ACCESSIBLE_DESCRIPTION_PROPERTY

Constant used to determine when the

accessibleDescription

property has changed.

static

String

ACCESSIBLE_HYPERTEXT_OFFSET

Constant used to indicate that a hypertext element has received focus.

static

String

ACCESSIBLE_INVALIDATE_CHILDREN

PropertyChangeEvent

which indicates that a significant change has
occurred to the children of a component like a tree or text.

static

String

ACCESSIBLE_NAME_PROPERTY

Constant used to determine when the

accessibleName

property has
changed.

static

String

ACCESSIBLE_SELECTION_PROPERTY

Constant used to determine when the

accessibleSelection

has
changed.

static

String

ACCESSIBLE_STATE_PROPERTY

Constant used to determine when the

accessibleStateSet

property
has changed.

static

String

ACCESSIBLE_TABLE_CAPTION_CHANGED

Constant used to indicate that the table caption has changed.

static

String

ACCESSIBLE_TABLE_COLUMN_DESCRIPTION_CHANGED

Constant used to indicate that the column description has changed.

static

String

ACCESSIBLE_TABLE_COLUMN_HEADER_CHANGED

Constant used to indicate that the column header has changed.

static

String

ACCESSIBLE_TABLE_MODEL_CHANGED

Constant used to indicate that table data has changed.

static

String

ACCESSIBLE_TABLE_ROW_DESCRIPTION_CHANGED

Constant used to indicate that the row description has changed.

static

String

ACCESSIBLE_TABLE_ROW_HEADER_CHANGED

Constant used to indicate that the row header has changed.

static

String

ACCESSIBLE_TABLE_SUMMARY_CHANGED

Constant used to indicate that the table summary has changed.

static

String

ACCESSIBLE_TEXT_ATTRIBUTES_CHANGED

PropertyChangeEvent

which indicates that text attributes have
changed.

static

String

ACCESSIBLE_TEXT_PROPERTY

PropertyChangeEvent

which indicates that text has changed.

static

String

ACCESSIBLE_VALUE_PROPERTY

Constant used to determine when the

accessibleValue

property has
changed.

static

String

ACCESSIBLE_VISIBLE_DATA_PROPERTY

Constant used to determine when the visual appearance of the object has
changed.

protected

String

accessibleDescription

A localized String containing the description of the object.

protected

String

accessibleName

A localized String containing the name of the object.

protected

Accessible

accessibleParent

The accessible parent of this object.

---

#### Field Summary

Constant used to indicate that the supported set of actions has changed.

Constant used to determine when the active descendant of a component has
changed.

Constant used to determine when the

accessibleText

caret has
changed.

Constant used to determine when

Accessible

children are
added/removed from the object.

PropertyChangeEvent

which indicates that a change has occurred in
a component's bounds.

Constant used to determine when the

accessibleDescription

property has changed.

Constant used to indicate that a hypertext element has received focus.

PropertyChangeEvent

which indicates that a significant change has
occurred to the children of a component like a tree or text.

Constant used to determine when the

accessibleName

property has
changed.

Constant used to determine when the

accessibleSelection

has
changed.

Constant used to determine when the

accessibleStateSet

property
has changed.

Constant used to indicate that the table caption has changed.

Constant used to indicate that the column description has changed.

Constant used to indicate that the column header has changed.

Constant used to indicate that table data has changed.

Constant used to indicate that the row description has changed.

Constant used to indicate that the row header has changed.

Constant used to indicate that the table summary has changed.

PropertyChangeEvent

which indicates that text attributes have
changed.

PropertyChangeEvent

which indicates that text has changed.

Constant used to determine when the

accessibleValue

property has
changed.

Constant used to determine when the visual appearance of the object has
changed.

A localized String containing the description of the object.

A localized String containing the name of the object.

The accessible parent of this object.

Constructor Summary

Constructors

Constructor

Description

AccessibleContext

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

void

addPropertyChangeListener

​(

PropertyChangeListener

listener)

Adds a

PropertyChangeListener

to the listener list.

void

firePropertyChange

​(

String

propertyName,

Object

oldValue,

Object

newValue)

Support for reporting bound property changes.

AccessibleAction

getAccessibleAction

()

Gets the

AccessibleAction

associated with this object that
supports one or more actions.

abstract

Accessible

getAccessibleChild

​(int i)

Returns the specified

Accessible

child of the object.

abstract int

getAccessibleChildrenCount

()

Returns the number of accessible children of the object.

AccessibleComponent

getAccessibleComponent

()

Gets the

AccessibleComponent

associated with this object that has
a graphical representation.

String

getAccessibleDescription

()

Gets the

accessibleDescription

property of this object.

AccessibleEditableText

getAccessibleEditableText

()

Gets the

AccessibleEditableText

associated with this object
presenting editable text on the display.

AccessibleIcon

[]

getAccessibleIcon

()

Gets the

AccessibleIcons

associated with an object that has one
or more associated icons.

abstract int

getAccessibleIndexInParent

()

Gets the 0-based index of this object in its accessible parent.

String

getAccessibleName

()

Gets the

accessibleName

property of this object.

Accessible

getAccessibleParent

()

Gets the

Accessible

parent of this object.

AccessibleRelationSet

getAccessibleRelationSet

()

Gets the

AccessibleRelationSet

associated with an object.

abstract

AccessibleRole

getAccessibleRole

()

Gets the role of this object.

AccessibleSelection

getAccessibleSelection

()

Gets the

AccessibleSelection

associated with this object which
allows its

Accessible

children to be selected.

abstract

AccessibleStateSet

getAccessibleStateSet

()

Gets the state set of this object.

AccessibleTable

getAccessibleTable

()

Gets the

AccessibleTable

associated with an object.

AccessibleText

getAccessibleText

()

Gets the

AccessibleText

associated with this object presenting
text on the display.

AccessibleValue

getAccessibleValue

()

Gets the

AccessibleValue

associated with this object that
supports a

Numerical

value.

abstract

Locale

getLocale

()

Gets the locale of the component.

void

removePropertyChangeListener

​(

PropertyChangeListener

listener)

Removes a

PropertyChangeListener

from the listener list.

void

setAccessibleDescription

​(

String

s)

Sets the accessible description of this object.

void

setAccessibleName

​(

String

s)

Sets the localized accessible name of this object.

void

setAccessibleParent

​(

Accessible

a)

Sets the

Accessible

parent of this object.

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

Adds a

PropertyChangeListener

to the listener list.

Support for reporting bound property changes.

Gets the

AccessibleAction

associated with this object that
supports one or more actions.

Returns the specified

Accessible

child of the object.

Returns the number of accessible children of the object.

Gets the

AccessibleComponent

associated with this object that has
a graphical representation.

Gets the

accessibleDescription

property of this object.

Gets the

AccessibleEditableText

associated with this object
presenting editable text on the display.

Gets the

AccessibleIcons

associated with an object that has one
or more associated icons.

Gets the 0-based index of this object in its accessible parent.

Gets the

accessibleName

property of this object.

Gets the

Accessible

parent of this object.

Gets the

AccessibleRelationSet

associated with an object.

Gets the role of this object.

Gets the

AccessibleSelection

associated with this object which
allows its

Accessible

children to be selected.

Gets the state set of this object.

Gets the

AccessibleTable

associated with an object.

Gets the

AccessibleText

associated with this object presenting
text on the display.

Gets the

AccessibleValue

associated with this object that
supports a

Numerical

value.

Gets the locale of the component.

Removes a

PropertyChangeListener

from the listener list.

Sets the accessible description of this object.

Sets the localized accessible name of this object.

Sets the

Accessible

parent of this object.

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

- ACCESSIBLE_NAME_PROPERTY

```java
public static final
String
ACCESSIBLE_NAME_PROPERTY
```

Constant used to determine when the

accessibleName

property has
changed. The old value in the

PropertyChangeEvent

will be the old

accessibleName

and the new value will be the new

accessibleName

.

**See Also:** getAccessibleName()

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Constant Field Values

- ACCESSIBLE_DESCRIPTION_PROPERTY

```java
public static final
String
ACCESSIBLE_DESCRIPTION_PROPERTY
```

Constant used to determine when the

accessibleDescription

property has changed. The old value in the

PropertyChangeEvent

will be the old

accessibleDescription

and the new value will be
the new

accessibleDescription

.

**See Also:** getAccessibleDescription()

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Constant Field Values

- ACCESSIBLE_STATE_PROPERTY

```java
public static final
String
ACCESSIBLE_STATE_PROPERTY
```

Constant used to determine when the

accessibleStateSet

property
has changed. The old value will be the old

AccessibleState

and
the new value will be the new

AccessibleState

in the

accessibleStateSet

. For example, if a component that supports the
vertical and horizontal states changes its orientation from vertical to
horizontal, the old value will be

AccessibleState.VERTICAL

and
the new value will be

AccessibleState.HORIZONTAL

. Please note
that either value can also be

null

. For example, when a component
changes from being enabled to disabled, the old value will be

AccessibleState.ENABLED

and the new value will be

null

.

**See Also:** getAccessibleStateSet()

,

AccessibleState

,

AccessibleStateSet

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Constant Field Values

- ACCESSIBLE_VALUE_PROPERTY

```java
public static final
String
ACCESSIBLE_VALUE_PROPERTY
```

Constant used to determine when the

accessibleValue

property has
changed. The old value in the

PropertyChangeEvent

will be a

Number

representing the old value and the new value will be a

Number

representing the new value.

**See Also:** getAccessibleValue()

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Constant Field Values

- ACCESSIBLE_SELECTION_PROPERTY

```java
public static final
String
ACCESSIBLE_SELECTION_PROPERTY
```

Constant used to determine when the

accessibleSelection

has
changed. The old and new values in the

PropertyChangeEvent

are
currently reserved for future use.

**See Also:** getAccessibleSelection()

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Constant Field Values

- ACCESSIBLE_CARET_PROPERTY

```java
public static final
String
ACCESSIBLE_CARET_PROPERTY
```

Constant used to determine when the

accessibleText

caret has
changed. The old value in the

PropertyChangeEvent

will be an
integer representing the old caret position, and the new value will be an
integer representing the new/current caret position.

**See Also:** addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Constant Field Values

- ACCESSIBLE_VISIBLE_DATA_PROPERTY

```java
public static final
String
ACCESSIBLE_VISIBLE_DATA_PROPERTY
```

Constant used to determine when the visual appearance of the object has
changed. The old and new values in the

PropertyChangeEvent

are
currently reserved for future use.

**See Also:** addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Constant Field Values

- ACCESSIBLE_CHILD_PROPERTY

```java
public static final
String
ACCESSIBLE_CHILD_PROPERTY
```

Constant used to determine when

Accessible

children are
added/removed from the object. If an

Accessible

child is being
added, the old value will be

null

and the new value will be the

Accessible

child. If an

Accessible

child is being
removed, the old value will be the

Accessible

child, and the new
value will be

null

.

**See Also:** addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Constant Field Values

- ACCESSIBLE_ACTIVE_DESCENDANT_PROPERTY

```java
public static final
String
ACCESSIBLE_ACTIVE_DESCENDANT_PROPERTY
```

Constant used to determine when the active descendant of a component has
changed. The active descendant is used for objects such as list, tree,
and table, which may have transient children. When the active descendant
has changed, the old value of the property change event will be the

Accessible

representing the previous active child, and the new
value will be the

Accessible

representing the current active
child.

**See Also:** addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Constant Field Values

- ACCESSIBLE_TABLE_CAPTION_CHANGED

```java
public static final
String
ACCESSIBLE_TABLE_CAPTION_CHANGED
```

Constant used to indicate that the table caption has changed. The old
value in the

PropertyChangeEvent

will be an

Accessible

representing the previous table caption and the new value will be an

Accessible

representing the new table caption.

**See Also:** Accessible

,

AccessibleTable

,

Constant Field Values

- ACCESSIBLE_TABLE_SUMMARY_CHANGED

```java
public static final
String
ACCESSIBLE_TABLE_SUMMARY_CHANGED
```

Constant used to indicate that the table summary has changed. The old
value in the

PropertyChangeEvent

will be an

Accessible

representing the previous table summary and the new value will be an

Accessible

representing the new table summary.

**See Also:** Accessible

,

AccessibleTable

,

Constant Field Values

- ACCESSIBLE_TABLE_MODEL_CHANGED

```java
public static final
String
ACCESSIBLE_TABLE_MODEL_CHANGED
```

Constant used to indicate that table data has changed. The old value in
the

PropertyChangeEvent

will be

null

and the new value
will be an

AccessibleTableModelChange

representing the table
change.

**See Also:** AccessibleTable

,

AccessibleTableModelChange

,

Constant Field Values

- ACCESSIBLE_TABLE_ROW_HEADER_CHANGED

```java
public static final
String
ACCESSIBLE_TABLE_ROW_HEADER_CHANGED
```

Constant used to indicate that the row header has changed. The old value
in the

PropertyChangeEvent

will be

null

and the new value
will be an

AccessibleTableModelChange

representing the header
change.

**See Also:** AccessibleTable

,

AccessibleTableModelChange

,

Constant Field Values

- ACCESSIBLE_TABLE_ROW_DESCRIPTION_CHANGED

```java
public static final
String
ACCESSIBLE_TABLE_ROW_DESCRIPTION_CHANGED
```

Constant used to indicate that the row description has changed. The old
value in the

PropertyChangeEvent

will be

null

and the new
value will be an

Integer

representing the row index.

**See Also:** AccessibleTable

,

Constant Field Values

- ACCESSIBLE_TABLE_COLUMN_HEADER_CHANGED

```java
public static final
String
ACCESSIBLE_TABLE_COLUMN_HEADER_CHANGED
```

Constant used to indicate that the column header has changed. The old
value in the

PropertyChangeEvent

will be

null

and the new
value will be an

AccessibleTableModelChange

representing the
header change.

**See Also:** AccessibleTable

,

AccessibleTableModelChange

,

Constant Field Values

- ACCESSIBLE_TABLE_COLUMN_DESCRIPTION_CHANGED

```java
public static final
String
ACCESSIBLE_TABLE_COLUMN_DESCRIPTION_CHANGED
```

Constant used to indicate that the column description has changed. The
old value in the

PropertyChangeEvent

will be

null

and the
new value will be an

Integer

representing the column index.

**See Also:** AccessibleTable

,

Constant Field Values

- ACCESSIBLE_ACTION_PROPERTY

```java
public static final
String
ACCESSIBLE_ACTION_PROPERTY
```

Constant used to indicate that the supported set of actions has changed.
The old value in the

PropertyChangeEvent

will be an

Integer

representing the old number of actions supported and the
new value will be an

Integer

representing the new number of
actions supported.

**See Also:** AccessibleAction

,

Constant Field Values

- ACCESSIBLE_HYPERTEXT_OFFSET

```java
public static final
String
ACCESSIBLE_HYPERTEXT_OFFSET
```

Constant used to indicate that a hypertext element has received focus.
The old value in the

PropertyChangeEvent

will be an

Integer

representing the start index in the document of the
previous element that had focus and the new value will be an

Integer

representing the start index in the document of the
current element that has focus. A value of -1 indicates that an element
does not or did not have focus.

**See Also:** AccessibleHyperlink

,

Constant Field Values

- ACCESSIBLE_TEXT_PROPERTY

```java
public static final
String
ACCESSIBLE_TEXT_PROPERTY
```

PropertyChangeEvent

which indicates that text has changed.

For text insertion, the

oldValue

is

null

and the

newValue

is an

AccessibleTextSequence

specifying the text
that was inserted.

For text deletion, the

oldValue

is an

AccessibleTextSequence

specifying the text that was deleted and
the

newValue

is

null

.

For text replacement, the

oldValue

is an

AccessibleTextSequence

specifying the old text and the

newValue

is an

AccessibleTextSequence

specifying the new
text.

**See Also:** getAccessibleText()

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

,

AccessibleTextSequence

,

Constant Field Values

- ACCESSIBLE_INVALIDATE_CHILDREN

```java
public static final
String
ACCESSIBLE_INVALIDATE_CHILDREN
```

PropertyChangeEvent

which indicates that a significant change has
occurred to the children of a component like a tree or text. This change
notifies the event listener that it needs to reacquire the state of the
subcomponents. The

oldValue

is

null

and the

newValue

is the component whose children have become invalid.

**Since:** 1.5
**See Also:** getAccessibleText()

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

,

AccessibleTextSequence

,

Constant Field Values

- ACCESSIBLE_TEXT_ATTRIBUTES_CHANGED

```java
public static final
String
ACCESSIBLE_TEXT_ATTRIBUTES_CHANGED
```

PropertyChangeEvent

which indicates that text attributes have
changed.

For attribute insertion, the

oldValue

is

null

and the

newValue

is an

AccessibleAttributeSequence

specifying the
attributes that were inserted.

For attribute deletion, the

oldValue

is an

AccessibleAttributeSequence

specifying the attributes that were
deleted and the

newValue

is

null

.

For attribute replacement, the

oldValue

is an

AccessibleAttributeSequence

specifying the old attributes and the

newValue

is an

AccessibleAttributeSequence

specifying the
new attributes.

**Since:** 1.5
**See Also:** getAccessibleText()

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

,

AccessibleAttributeSequence

,

Constant Field Values

- ACCESSIBLE_COMPONENT_BOUNDS_CHANGED

```java
public static final
String
ACCESSIBLE_COMPONENT_BOUNDS_CHANGED
```

PropertyChangeEvent

which indicates that a change has occurred in
a component's bounds. The

oldValue

is the old component bounds
and the

newValue

is the new component bounds.

**Since:** 1.5
**See Also:** addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Constant Field Values

- accessibleParent

```java
protected
Accessible
accessibleParent
```

The accessible parent of this object.

**See Also:** getAccessibleParent()

,

setAccessibleParent(javax.accessibility.Accessible)

- accessibleName

```java
protected
String
accessibleName
```

A localized String containing the name of the object.

**See Also:** getAccessibleName()

,

setAccessibleName(java.lang.String)

- accessibleDescription

```java
protected
String
accessibleDescription
```

A localized String containing the description of the object.

**See Also:** getAccessibleDescription()

,

setAccessibleDescription(java.lang.String)

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AccessibleContext

```java
public AccessibleContext()
```

============ METHOD DETAIL ==========

- Method Detail

- getAccessibleName

```java
public
String
getAccessibleName()
```

Gets the

accessibleName

property of this object. The

accessibleName

property of an object is a localized

String

that designates the purpose of the object. For example,
the

accessibleName

property of a label or button might be the
text of the label or button itself. In the case of an object that doesn't
display its name, the

accessibleName

should still be set. For
example, in the case of a text field used to enter the name of a city,
the

accessibleName

for the

en_US

locale could be 'city.'

**Returns:** the localized name of the object;

null

if this object
does not have a name
**See Also:** setAccessibleName(java.lang.String)

- setAccessibleName

```java
@BeanProperty
(
preferred
=true,

description
="Sets the accessible name for the component.")
public void setAccessibleName​(
String
s)
```

Sets the localized accessible name of this object. Changing the name will
cause a

PropertyChangeEvent

to be fired for the

ACCESSIBLE_NAME_PROPERTY

property.

**Parameters:** s

- the new localized name of the object
**See Also:** getAccessibleName()

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

- getAccessibleDescription

```java
public
String
getAccessibleDescription()
```

Gets the

accessibleDescription

property of this object. The

accessibleDescription

property of this object is a short
localized phrase describing the purpose of the object. For example, in
the case of a 'Cancel' button, the

accessibleDescription

could be
'Ignore changes and close dialog box.'

**Returns:** the localized description of the object;

null

if this
object does not have a description
**See Also:** setAccessibleDescription(java.lang.String)

- setAccessibleDescription

```java
@BeanProperty
(
preferred
=true,

description
="Sets the accessible description for the component.")
public void setAccessibleDescription​(
String
s)
```

Sets the accessible description of this object. Changing the name will
cause a

PropertyChangeEvent

to be fired for the

ACCESSIBLE_DESCRIPTION_PROPERTY

property.

**Parameters:** s

- the new localized description of the object
**See Also:** setAccessibleName(java.lang.String)

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

- getAccessibleRole

```java
public abstract
AccessibleRole
getAccessibleRole()
```

Gets the role of this object. The role of the object is the generic
purpose or use of the class of this object. For example, the role of a
push button is

AccessibleRole.PUSH_BUTTON

. The roles in

AccessibleRole

are provided so component developers can pick from
a set of predefined roles. This enables assistive technologies to provide
a consistent interface to various tweaked subclasses of components (e.g.,
use

AccessibleRole.PUSH_BUTTON

for all components that act like a
push button) as well as distinguish between subclasses that behave
differently (e.g.,

AccessibleRole.CHECK_BOX

for check boxes and

AccessibleRole.RADIO_BUTTON

for radio buttons).

Note that the

AccessibleRole

class is also extensible, so custom
component developers can define their own

AccessibleRole

's if the
set of predefined roles is inadequate.

**Returns:** an instance of

AccessibleRole

describing the role of the
object
**See Also:** AccessibleRole

- getAccessibleStateSet

```java
public abstract
AccessibleStateSet
getAccessibleStateSet()
```

Gets the state set of this object. The

AccessibleStateSet

of an
object is composed of a set of unique

AccessibleStates

. A change
in the

AccessibleStateSet

of an object will cause a

PropertyChangeEvent

to be fired for the

ACCESSIBLE_STATE_PROPERTY

property.

**Returns:** an instance of

AccessibleStateSet

containing the current
state set of the object
**See Also:** AccessibleStateSet

,

AccessibleState

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

- getAccessibleParent

```java
public
Accessible
getAccessibleParent()
```

Gets the

Accessible

parent of this object.

**Returns:** the

Accessible

parent of this object;

null

if
this object does not have an

Accessible

parent

- setAccessibleParent

```java
public void setAccessibleParent​(
Accessible
a)
```

Sets the

Accessible

parent of this object. This is meant to be
used only in the situations where the actual component's parent should
not be treated as the component's accessible parent and is a method that
should only be called by the parent of the accessible child.

**Parameters:** a

- -

Accessible

to be set as the parent

- getAccessibleIndexInParent

```java
public abstract int getAccessibleIndexInParent()
```

Gets the 0-based index of this object in its accessible parent.

**Returns:** the 0-based index of this object in its parent; -1 if this object
does not have an accessible parent.
**See Also:** getAccessibleParent()

,

getAccessibleChildrenCount()

,

getAccessibleChild(int)

- getAccessibleChildrenCount

```java
public abstract int getAccessibleChildrenCount()
```

Returns the number of accessible children of the object.

**Returns:** the number of accessible children of the object.

- getAccessibleChild

```java
public abstract
Accessible
getAccessibleChild​(int i)
```

Returns the specified

Accessible

child of the object. The

Accessible

children of an

Accessible

object are
zero-based, so the first child of an

Accessible

child is at index
0, the second child is at index 1, and so on.

**Parameters:** i

- zero-based index of child
**Returns:** the

Accessible

child of the object
**See Also:** getAccessibleChildrenCount()

- getLocale

```java
public abstract
Locale
getLocale()
throws
IllegalComponentStateException
```

Gets the locale of the component. If the component does not have a
locale, then the locale of its parent is returned.

**Returns:** this component's locale. If this component does not have a
locale, the locale of its parent is returned.
**Throws:** IllegalComponentStateException

- If the component does not have its
own locale and has not yet been added to a containment hierarchy
such that the locale can be determined from the containing
parent

- addPropertyChangeListener

```java
public void addPropertyChangeListener​(
PropertyChangeListener
listener)
```

Adds a

PropertyChangeListener

to the listener list. The listener
is registered for all

Accessible

properties and will be called
when those properties change.

**Parameters:** listener

- The PropertyChangeListener to be added
**See Also:** ACCESSIBLE_NAME_PROPERTY

,

ACCESSIBLE_DESCRIPTION_PROPERTY

,

ACCESSIBLE_STATE_PROPERTY

,

ACCESSIBLE_VALUE_PROPERTY

,

ACCESSIBLE_SELECTION_PROPERTY

,

ACCESSIBLE_TEXT_PROPERTY

,

ACCESSIBLE_VISIBLE_DATA_PROPERTY

- removePropertyChangeListener

```java
public void removePropertyChangeListener​(
PropertyChangeListener
listener)
```

Removes a

PropertyChangeListener

from the listener list. This
removes a

PropertyChangeListener

that was registered for all
properties.

**Parameters:** listener

- The PropertyChangeListener to be removed

- getAccessibleAction

```java
public
AccessibleAction
getAccessibleAction()
```

Gets the

AccessibleAction

associated with this object that
supports one or more actions.

**Returns:** AccessibleAction

if supported by object; else return

null
**See Also:** AccessibleAction

- getAccessibleComponent

```java
public
AccessibleComponent
getAccessibleComponent()
```

Gets the

AccessibleComponent

associated with this object that has
a graphical representation.

**Returns:** AccessibleComponent

if supported by object; else return

null
**See Also:** AccessibleComponent

- getAccessibleSelection

```java
public
AccessibleSelection
getAccessibleSelection()
```

Gets the

AccessibleSelection

associated with this object which
allows its

Accessible

children to be selected.

**Returns:** AccessibleSelection

if supported by object; else return

null
**See Also:** AccessibleSelection

- getAccessibleText

```java
public
AccessibleText
getAccessibleText()
```

Gets the

AccessibleText

associated with this object presenting
text on the display.

**Returns:** AccessibleText

if supported by object; else return

null
**See Also:** AccessibleText

- getAccessibleEditableText

```java
public
AccessibleEditableText
getAccessibleEditableText()
```

Gets the

AccessibleEditableText

associated with this object
presenting editable text on the display.

**Returns:** AccessibleEditableText

if supported by object; else
return

null
**Since:** 1.4
**See Also:** AccessibleEditableText

- getAccessibleValue

```java
public
AccessibleValue
getAccessibleValue()
```

Gets the

AccessibleValue

associated with this object that
supports a

Numerical

value.

**Returns:** AccessibleValue

if supported by object; else return

null
**See Also:** AccessibleValue

- getAccessibleIcon

```java
public
AccessibleIcon
[] getAccessibleIcon()
```

Gets the

AccessibleIcons

associated with an object that has one
or more associated icons.

**Returns:** an array of

AccessibleIcon

if supported by object;
otherwise return

null
**Since:** 1.3
**See Also:** AccessibleIcon

- getAccessibleRelationSet

```java
public
AccessibleRelationSet
getAccessibleRelationSet()
```

Gets the

AccessibleRelationSet

associated with an object.

**Returns:** an

AccessibleRelationSet

if supported by object;
otherwise return

null
**Since:** 1.3
**See Also:** AccessibleRelationSet

- getAccessibleTable

```java
public
AccessibleTable
getAccessibleTable()
```

Gets the

AccessibleTable

associated with an object.

**Returns:** an

AccessibleTable

if supported by object; otherwise return

null
**Since:** 1.3
**See Also:** AccessibleTable

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,

Object
oldValue,

Object
newValue)
```

Support for reporting bound property changes. If

oldValue

and

newValue

are not equal and the

PropertyChangeEvent

listener list is not empty, then fire a

PropertyChange

event to
each listener. In general, this is for use by the

Accessible

objects themselves and should not be called by an application program.

**Parameters:** propertyName

- The programmatic name of the property that was
changed
**Parameters:** oldValue

- The old value of the property
**Parameters:** newValue

- The new value of the property
**See Also:** PropertyChangeSupport

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

,

removePropertyChangeListener(java.beans.PropertyChangeListener)

,

ACCESSIBLE_NAME_PROPERTY

,

ACCESSIBLE_DESCRIPTION_PROPERTY

,

ACCESSIBLE_STATE_PROPERTY

,

ACCESSIBLE_VALUE_PROPERTY

,

ACCESSIBLE_SELECTION_PROPERTY

,

ACCESSIBLE_TEXT_PROPERTY

,

ACCESSIBLE_VISIBLE_DATA_PROPERTY

Field Detail

- ACCESSIBLE_NAME_PROPERTY

```java
public static final
String
ACCESSIBLE_NAME_PROPERTY
```

Constant used to determine when the

accessibleName

property has
changed. The old value in the

PropertyChangeEvent

will be the old

accessibleName

and the new value will be the new

accessibleName

.

**See Also:** getAccessibleName()

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Constant Field Values

- ACCESSIBLE_DESCRIPTION_PROPERTY

```java
public static final
String
ACCESSIBLE_DESCRIPTION_PROPERTY
```

Constant used to determine when the

accessibleDescription

property has changed. The old value in the

PropertyChangeEvent

will be the old

accessibleDescription

and the new value will be
the new

accessibleDescription

.

**See Also:** getAccessibleDescription()

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Constant Field Values

- ACCESSIBLE_STATE_PROPERTY

```java
public static final
String
ACCESSIBLE_STATE_PROPERTY
```

Constant used to determine when the

accessibleStateSet

property
has changed. The old value will be the old

AccessibleState

and
the new value will be the new

AccessibleState

in the

accessibleStateSet

. For example, if a component that supports the
vertical and horizontal states changes its orientation from vertical to
horizontal, the old value will be

AccessibleState.VERTICAL

and
the new value will be

AccessibleState.HORIZONTAL

. Please note
that either value can also be

null

. For example, when a component
changes from being enabled to disabled, the old value will be

AccessibleState.ENABLED

and the new value will be

null

.

**See Also:** getAccessibleStateSet()

,

AccessibleState

,

AccessibleStateSet

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Constant Field Values

- ACCESSIBLE_VALUE_PROPERTY

```java
public static final
String
ACCESSIBLE_VALUE_PROPERTY
```

Constant used to determine when the

accessibleValue

property has
changed. The old value in the

PropertyChangeEvent

will be a

Number

representing the old value and the new value will be a

Number

representing the new value.

**See Also:** getAccessibleValue()

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Constant Field Values

- ACCESSIBLE_SELECTION_PROPERTY

```java
public static final
String
ACCESSIBLE_SELECTION_PROPERTY
```

Constant used to determine when the

accessibleSelection

has
changed. The old and new values in the

PropertyChangeEvent

are
currently reserved for future use.

**See Also:** getAccessibleSelection()

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Constant Field Values

- ACCESSIBLE_CARET_PROPERTY

```java
public static final
String
ACCESSIBLE_CARET_PROPERTY
```

Constant used to determine when the

accessibleText

caret has
changed. The old value in the

PropertyChangeEvent

will be an
integer representing the old caret position, and the new value will be an
integer representing the new/current caret position.

**See Also:** addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Constant Field Values

- ACCESSIBLE_VISIBLE_DATA_PROPERTY

```java
public static final
String
ACCESSIBLE_VISIBLE_DATA_PROPERTY
```

Constant used to determine when the visual appearance of the object has
changed. The old and new values in the

PropertyChangeEvent

are
currently reserved for future use.

**See Also:** addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Constant Field Values

- ACCESSIBLE_CHILD_PROPERTY

```java
public static final
String
ACCESSIBLE_CHILD_PROPERTY
```

Constant used to determine when

Accessible

children are
added/removed from the object. If an

Accessible

child is being
added, the old value will be

null

and the new value will be the

Accessible

child. If an

Accessible

child is being
removed, the old value will be the

Accessible

child, and the new
value will be

null

.

**See Also:** addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Constant Field Values

- ACCESSIBLE_ACTIVE_DESCENDANT_PROPERTY

```java
public static final
String
ACCESSIBLE_ACTIVE_DESCENDANT_PROPERTY
```

Constant used to determine when the active descendant of a component has
changed. The active descendant is used for objects such as list, tree,
and table, which may have transient children. When the active descendant
has changed, the old value of the property change event will be the

Accessible

representing the previous active child, and the new
value will be the

Accessible

representing the current active
child.

**See Also:** addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Constant Field Values

- ACCESSIBLE_TABLE_CAPTION_CHANGED

```java
public static final
String
ACCESSIBLE_TABLE_CAPTION_CHANGED
```

Constant used to indicate that the table caption has changed. The old
value in the

PropertyChangeEvent

will be an

Accessible

representing the previous table caption and the new value will be an

Accessible

representing the new table caption.

**See Also:** Accessible

,

AccessibleTable

,

Constant Field Values

- ACCESSIBLE_TABLE_SUMMARY_CHANGED

```java
public static final
String
ACCESSIBLE_TABLE_SUMMARY_CHANGED
```

Constant used to indicate that the table summary has changed. The old
value in the

PropertyChangeEvent

will be an

Accessible

representing the previous table summary and the new value will be an

Accessible

representing the new table summary.

**See Also:** Accessible

,

AccessibleTable

,

Constant Field Values

- ACCESSIBLE_TABLE_MODEL_CHANGED

```java
public static final
String
ACCESSIBLE_TABLE_MODEL_CHANGED
```

Constant used to indicate that table data has changed. The old value in
the

PropertyChangeEvent

will be

null

and the new value
will be an

AccessibleTableModelChange

representing the table
change.

**See Also:** AccessibleTable

,

AccessibleTableModelChange

,

Constant Field Values

- ACCESSIBLE_TABLE_ROW_HEADER_CHANGED

```java
public static final
String
ACCESSIBLE_TABLE_ROW_HEADER_CHANGED
```

Constant used to indicate that the row header has changed. The old value
in the

PropertyChangeEvent

will be

null

and the new value
will be an

AccessibleTableModelChange

representing the header
change.

**See Also:** AccessibleTable

,

AccessibleTableModelChange

,

Constant Field Values

- ACCESSIBLE_TABLE_ROW_DESCRIPTION_CHANGED

```java
public static final
String
ACCESSIBLE_TABLE_ROW_DESCRIPTION_CHANGED
```

Constant used to indicate that the row description has changed. The old
value in the

PropertyChangeEvent

will be

null

and the new
value will be an

Integer

representing the row index.

**See Also:** AccessibleTable

,

Constant Field Values

- ACCESSIBLE_TABLE_COLUMN_HEADER_CHANGED

```java
public static final
String
ACCESSIBLE_TABLE_COLUMN_HEADER_CHANGED
```

Constant used to indicate that the column header has changed. The old
value in the

PropertyChangeEvent

will be

null

and the new
value will be an

AccessibleTableModelChange

representing the
header change.

**See Also:** AccessibleTable

,

AccessibleTableModelChange

,

Constant Field Values

- ACCESSIBLE_TABLE_COLUMN_DESCRIPTION_CHANGED

```java
public static final
String
ACCESSIBLE_TABLE_COLUMN_DESCRIPTION_CHANGED
```

Constant used to indicate that the column description has changed. The
old value in the

PropertyChangeEvent

will be

null

and the
new value will be an

Integer

representing the column index.

**See Also:** AccessibleTable

,

Constant Field Values

- ACCESSIBLE_ACTION_PROPERTY

```java
public static final
String
ACCESSIBLE_ACTION_PROPERTY
```

Constant used to indicate that the supported set of actions has changed.
The old value in the

PropertyChangeEvent

will be an

Integer

representing the old number of actions supported and the
new value will be an

Integer

representing the new number of
actions supported.

**See Also:** AccessibleAction

,

Constant Field Values

- ACCESSIBLE_HYPERTEXT_OFFSET

```java
public static final
String
ACCESSIBLE_HYPERTEXT_OFFSET
```

Constant used to indicate that a hypertext element has received focus.
The old value in the

PropertyChangeEvent

will be an

Integer

representing the start index in the document of the
previous element that had focus and the new value will be an

Integer

representing the start index in the document of the
current element that has focus. A value of -1 indicates that an element
does not or did not have focus.

**See Also:** AccessibleHyperlink

,

Constant Field Values

- ACCESSIBLE_TEXT_PROPERTY

```java
public static final
String
ACCESSIBLE_TEXT_PROPERTY
```

PropertyChangeEvent

which indicates that text has changed.

For text insertion, the

oldValue

is

null

and the

newValue

is an

AccessibleTextSequence

specifying the text
that was inserted.

For text deletion, the

oldValue

is an

AccessibleTextSequence

specifying the text that was deleted and
the

newValue

is

null

.

For text replacement, the

oldValue

is an

AccessibleTextSequence

specifying the old text and the

newValue

is an

AccessibleTextSequence

specifying the new
text.

**See Also:** getAccessibleText()

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

,

AccessibleTextSequence

,

Constant Field Values

- ACCESSIBLE_INVALIDATE_CHILDREN

```java
public static final
String
ACCESSIBLE_INVALIDATE_CHILDREN
```

PropertyChangeEvent

which indicates that a significant change has
occurred to the children of a component like a tree or text. This change
notifies the event listener that it needs to reacquire the state of the
subcomponents. The

oldValue

is

null

and the

newValue

is the component whose children have become invalid.

**Since:** 1.5
**See Also:** getAccessibleText()

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

,

AccessibleTextSequence

,

Constant Field Values

- ACCESSIBLE_TEXT_ATTRIBUTES_CHANGED

```java
public static final
String
ACCESSIBLE_TEXT_ATTRIBUTES_CHANGED
```

PropertyChangeEvent

which indicates that text attributes have
changed.

For attribute insertion, the

oldValue

is

null

and the

newValue

is an

AccessibleAttributeSequence

specifying the
attributes that were inserted.

For attribute deletion, the

oldValue

is an

AccessibleAttributeSequence

specifying the attributes that were
deleted and the

newValue

is

null

.

For attribute replacement, the

oldValue

is an

AccessibleAttributeSequence

specifying the old attributes and the

newValue

is an

AccessibleAttributeSequence

specifying the
new attributes.

**Since:** 1.5
**See Also:** getAccessibleText()

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

,

AccessibleAttributeSequence

,

Constant Field Values

- ACCESSIBLE_COMPONENT_BOUNDS_CHANGED

```java
public static final
String
ACCESSIBLE_COMPONENT_BOUNDS_CHANGED
```

PropertyChangeEvent

which indicates that a change has occurred in
a component's bounds. The

oldValue

is the old component bounds
and the

newValue

is the new component bounds.

**Since:** 1.5
**See Also:** addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Constant Field Values

- accessibleParent

```java
protected
Accessible
accessibleParent
```

The accessible parent of this object.

**See Also:** getAccessibleParent()

,

setAccessibleParent(javax.accessibility.Accessible)

- accessibleName

```java
protected
String
accessibleName
```

A localized String containing the name of the object.

**See Also:** getAccessibleName()

,

setAccessibleName(java.lang.String)

- accessibleDescription

```java
protected
String
accessibleDescription
```

A localized String containing the description of the object.

**See Also:** getAccessibleDescription()

,

setAccessibleDescription(java.lang.String)

---

#### Field Detail

ACCESSIBLE_NAME_PROPERTY

```java
public static final
String
ACCESSIBLE_NAME_PROPERTY
```

Constant used to determine when the

accessibleName

property has
changed. The old value in the

PropertyChangeEvent

will be the old

accessibleName

and the new value will be the new

accessibleName

.

**See Also:** getAccessibleName()

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Constant Field Values

---

#### ACCESSIBLE_NAME_PROPERTY

public static final

String

ACCESSIBLE_NAME_PROPERTY

Constant used to determine when the

accessibleName

property has
changed. The old value in the

PropertyChangeEvent

will be the old

accessibleName

and the new value will be the new

accessibleName

.

ACCESSIBLE_DESCRIPTION_PROPERTY

```java
public static final
String
ACCESSIBLE_DESCRIPTION_PROPERTY
```

Constant used to determine when the

accessibleDescription

property has changed. The old value in the

PropertyChangeEvent

will be the old

accessibleDescription

and the new value will be
the new

accessibleDescription

.

**See Also:** getAccessibleDescription()

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Constant Field Values

---

#### ACCESSIBLE_DESCRIPTION_PROPERTY

public static final

String

ACCESSIBLE_DESCRIPTION_PROPERTY

Constant used to determine when the

accessibleDescription

property has changed. The old value in the

PropertyChangeEvent

will be the old

accessibleDescription

and the new value will be
the new

accessibleDescription

.

ACCESSIBLE_STATE_PROPERTY

```java
public static final
String
ACCESSIBLE_STATE_PROPERTY
```

Constant used to determine when the

accessibleStateSet

property
has changed. The old value will be the old

AccessibleState

and
the new value will be the new

AccessibleState

in the

accessibleStateSet

. For example, if a component that supports the
vertical and horizontal states changes its orientation from vertical to
horizontal, the old value will be

AccessibleState.VERTICAL

and
the new value will be

AccessibleState.HORIZONTAL

. Please note
that either value can also be

null

. For example, when a component
changes from being enabled to disabled, the old value will be

AccessibleState.ENABLED

and the new value will be

null

.

**See Also:** getAccessibleStateSet()

,

AccessibleState

,

AccessibleStateSet

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Constant Field Values

---

#### ACCESSIBLE_STATE_PROPERTY

public static final

String

ACCESSIBLE_STATE_PROPERTY

Constant used to determine when the

accessibleStateSet

property
has changed. The old value will be the old

AccessibleState

and
the new value will be the new

AccessibleState

in the

accessibleStateSet

. For example, if a component that supports the
vertical and horizontal states changes its orientation from vertical to
horizontal, the old value will be

AccessibleState.VERTICAL

and
the new value will be

AccessibleState.HORIZONTAL

. Please note
that either value can also be

null

. For example, when a component
changes from being enabled to disabled, the old value will be

AccessibleState.ENABLED

and the new value will be

null

.

ACCESSIBLE_VALUE_PROPERTY

```java
public static final
String
ACCESSIBLE_VALUE_PROPERTY
```

Constant used to determine when the

accessibleValue

property has
changed. The old value in the

PropertyChangeEvent

will be a

Number

representing the old value and the new value will be a

Number

representing the new value.

**See Also:** getAccessibleValue()

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Constant Field Values

---

#### ACCESSIBLE_VALUE_PROPERTY

public static final

String

ACCESSIBLE_VALUE_PROPERTY

Constant used to determine when the

accessibleValue

property has
changed. The old value in the

PropertyChangeEvent

will be a

Number

representing the old value and the new value will be a

Number

representing the new value.

ACCESSIBLE_SELECTION_PROPERTY

```java
public static final
String
ACCESSIBLE_SELECTION_PROPERTY
```

Constant used to determine when the

accessibleSelection

has
changed. The old and new values in the

PropertyChangeEvent

are
currently reserved for future use.

**See Also:** getAccessibleSelection()

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Constant Field Values

---

#### ACCESSIBLE_SELECTION_PROPERTY

public static final

String

ACCESSIBLE_SELECTION_PROPERTY

Constant used to determine when the

accessibleSelection

has
changed. The old and new values in the

PropertyChangeEvent

are
currently reserved for future use.

ACCESSIBLE_CARET_PROPERTY

```java
public static final
String
ACCESSIBLE_CARET_PROPERTY
```

Constant used to determine when the

accessibleText

caret has
changed. The old value in the

PropertyChangeEvent

will be an
integer representing the old caret position, and the new value will be an
integer representing the new/current caret position.

**See Also:** addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Constant Field Values

---

#### ACCESSIBLE_CARET_PROPERTY

public static final

String

ACCESSIBLE_CARET_PROPERTY

Constant used to determine when the

accessibleText

caret has
changed. The old value in the

PropertyChangeEvent

will be an
integer representing the old caret position, and the new value will be an
integer representing the new/current caret position.

ACCESSIBLE_VISIBLE_DATA_PROPERTY

```java
public static final
String
ACCESSIBLE_VISIBLE_DATA_PROPERTY
```

Constant used to determine when the visual appearance of the object has
changed. The old and new values in the

PropertyChangeEvent

are
currently reserved for future use.

**See Also:** addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Constant Field Values

---

#### ACCESSIBLE_VISIBLE_DATA_PROPERTY

public static final

String

ACCESSIBLE_VISIBLE_DATA_PROPERTY

Constant used to determine when the visual appearance of the object has
changed. The old and new values in the

PropertyChangeEvent

are
currently reserved for future use.

ACCESSIBLE_CHILD_PROPERTY

```java
public static final
String
ACCESSIBLE_CHILD_PROPERTY
```

Constant used to determine when

Accessible

children are
added/removed from the object. If an

Accessible

child is being
added, the old value will be

null

and the new value will be the

Accessible

child. If an

Accessible

child is being
removed, the old value will be the

Accessible

child, and the new
value will be

null

.

**See Also:** addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Constant Field Values

---

#### ACCESSIBLE_CHILD_PROPERTY

public static final

String

ACCESSIBLE_CHILD_PROPERTY

Constant used to determine when

Accessible

children are
added/removed from the object. If an

Accessible

child is being
added, the old value will be

null

and the new value will be the

Accessible

child. If an

Accessible

child is being
removed, the old value will be the

Accessible

child, and the new
value will be

null

.

ACCESSIBLE_ACTIVE_DESCENDANT_PROPERTY

```java
public static final
String
ACCESSIBLE_ACTIVE_DESCENDANT_PROPERTY
```

Constant used to determine when the active descendant of a component has
changed. The active descendant is used for objects such as list, tree,
and table, which may have transient children. When the active descendant
has changed, the old value of the property change event will be the

Accessible

representing the previous active child, and the new
value will be the

Accessible

representing the current active
child.

**See Also:** addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Constant Field Values

---

#### ACCESSIBLE_ACTIVE_DESCENDANT_PROPERTY

public static final

String

ACCESSIBLE_ACTIVE_DESCENDANT_PROPERTY

Constant used to determine when the active descendant of a component has
changed. The active descendant is used for objects such as list, tree,
and table, which may have transient children. When the active descendant
has changed, the old value of the property change event will be the

Accessible

representing the previous active child, and the new
value will be the

Accessible

representing the current active
child.

ACCESSIBLE_TABLE_CAPTION_CHANGED

```java
public static final
String
ACCESSIBLE_TABLE_CAPTION_CHANGED
```

Constant used to indicate that the table caption has changed. The old
value in the

PropertyChangeEvent

will be an

Accessible

representing the previous table caption and the new value will be an

Accessible

representing the new table caption.

**See Also:** Accessible

,

AccessibleTable

,

Constant Field Values

---

#### ACCESSIBLE_TABLE_CAPTION_CHANGED

public static final

String

ACCESSIBLE_TABLE_CAPTION_CHANGED

Constant used to indicate that the table caption has changed. The old
value in the

PropertyChangeEvent

will be an

Accessible

representing the previous table caption and the new value will be an

Accessible

representing the new table caption.

ACCESSIBLE_TABLE_SUMMARY_CHANGED

```java
public static final
String
ACCESSIBLE_TABLE_SUMMARY_CHANGED
```

Constant used to indicate that the table summary has changed. The old
value in the

PropertyChangeEvent

will be an

Accessible

representing the previous table summary and the new value will be an

Accessible

representing the new table summary.

**See Also:** Accessible

,

AccessibleTable

,

Constant Field Values

---

#### ACCESSIBLE_TABLE_SUMMARY_CHANGED

public static final

String

ACCESSIBLE_TABLE_SUMMARY_CHANGED

Constant used to indicate that the table summary has changed. The old
value in the

PropertyChangeEvent

will be an

Accessible

representing the previous table summary and the new value will be an

Accessible

representing the new table summary.

ACCESSIBLE_TABLE_MODEL_CHANGED

```java
public static final
String
ACCESSIBLE_TABLE_MODEL_CHANGED
```

Constant used to indicate that table data has changed. The old value in
the

PropertyChangeEvent

will be

null

and the new value
will be an

AccessibleTableModelChange

representing the table
change.

**See Also:** AccessibleTable

,

AccessibleTableModelChange

,

Constant Field Values

---

#### ACCESSIBLE_TABLE_MODEL_CHANGED

public static final

String

ACCESSIBLE_TABLE_MODEL_CHANGED

Constant used to indicate that table data has changed. The old value in
the

PropertyChangeEvent

will be

null

and the new value
will be an

AccessibleTableModelChange

representing the table
change.

ACCESSIBLE_TABLE_ROW_HEADER_CHANGED

```java
public static final
String
ACCESSIBLE_TABLE_ROW_HEADER_CHANGED
```

Constant used to indicate that the row header has changed. The old value
in the

PropertyChangeEvent

will be

null

and the new value
will be an

AccessibleTableModelChange

representing the header
change.

**See Also:** AccessibleTable

,

AccessibleTableModelChange

,

Constant Field Values

---

#### ACCESSIBLE_TABLE_ROW_HEADER_CHANGED

public static final

String

ACCESSIBLE_TABLE_ROW_HEADER_CHANGED

Constant used to indicate that the row header has changed. The old value
in the

PropertyChangeEvent

will be

null

and the new value
will be an

AccessibleTableModelChange

representing the header
change.

ACCESSIBLE_TABLE_ROW_DESCRIPTION_CHANGED

```java
public static final
String
ACCESSIBLE_TABLE_ROW_DESCRIPTION_CHANGED
```

Constant used to indicate that the row description has changed. The old
value in the

PropertyChangeEvent

will be

null

and the new
value will be an

Integer

representing the row index.

**See Also:** AccessibleTable

,

Constant Field Values

---

#### ACCESSIBLE_TABLE_ROW_DESCRIPTION_CHANGED

public static final

String

ACCESSIBLE_TABLE_ROW_DESCRIPTION_CHANGED

Constant used to indicate that the row description has changed. The old
value in the

PropertyChangeEvent

will be

null

and the new
value will be an

Integer

representing the row index.

ACCESSIBLE_TABLE_COLUMN_HEADER_CHANGED

```java
public static final
String
ACCESSIBLE_TABLE_COLUMN_HEADER_CHANGED
```

Constant used to indicate that the column header has changed. The old
value in the

PropertyChangeEvent

will be

null

and the new
value will be an

AccessibleTableModelChange

representing the
header change.

**See Also:** AccessibleTable

,

AccessibleTableModelChange

,

Constant Field Values

---

#### ACCESSIBLE_TABLE_COLUMN_HEADER_CHANGED

public static final

String

ACCESSIBLE_TABLE_COLUMN_HEADER_CHANGED

Constant used to indicate that the column header has changed. The old
value in the

PropertyChangeEvent

will be

null

and the new
value will be an

AccessibleTableModelChange

representing the
header change.

ACCESSIBLE_TABLE_COLUMN_DESCRIPTION_CHANGED

```java
public static final
String
ACCESSIBLE_TABLE_COLUMN_DESCRIPTION_CHANGED
```

Constant used to indicate that the column description has changed. The
old value in the

PropertyChangeEvent

will be

null

and the
new value will be an

Integer

representing the column index.

**See Also:** AccessibleTable

,

Constant Field Values

---

#### ACCESSIBLE_TABLE_COLUMN_DESCRIPTION_CHANGED

public static final

String

ACCESSIBLE_TABLE_COLUMN_DESCRIPTION_CHANGED

Constant used to indicate that the column description has changed. The
old value in the

PropertyChangeEvent

will be

null

and the
new value will be an

Integer

representing the column index.

ACCESSIBLE_ACTION_PROPERTY

```java
public static final
String
ACCESSIBLE_ACTION_PROPERTY
```

Constant used to indicate that the supported set of actions has changed.
The old value in the

PropertyChangeEvent

will be an

Integer

representing the old number of actions supported and the
new value will be an

Integer

representing the new number of
actions supported.

**See Also:** AccessibleAction

,

Constant Field Values

---

#### ACCESSIBLE_ACTION_PROPERTY

public static final

String

ACCESSIBLE_ACTION_PROPERTY

Constant used to indicate that the supported set of actions has changed.
The old value in the

PropertyChangeEvent

will be an

Integer

representing the old number of actions supported and the
new value will be an

Integer

representing the new number of
actions supported.

ACCESSIBLE_HYPERTEXT_OFFSET

```java
public static final
String
ACCESSIBLE_HYPERTEXT_OFFSET
```

Constant used to indicate that a hypertext element has received focus.
The old value in the

PropertyChangeEvent

will be an

Integer

representing the start index in the document of the
previous element that had focus and the new value will be an

Integer

representing the start index in the document of the
current element that has focus. A value of -1 indicates that an element
does not or did not have focus.

**See Also:** AccessibleHyperlink

,

Constant Field Values

---

#### ACCESSIBLE_HYPERTEXT_OFFSET

public static final

String

ACCESSIBLE_HYPERTEXT_OFFSET

Constant used to indicate that a hypertext element has received focus.
The old value in the

PropertyChangeEvent

will be an

Integer

representing the start index in the document of the
previous element that had focus and the new value will be an

Integer

representing the start index in the document of the
current element that has focus. A value of -1 indicates that an element
does not or did not have focus.

ACCESSIBLE_TEXT_PROPERTY

```java
public static final
String
ACCESSIBLE_TEXT_PROPERTY
```

PropertyChangeEvent

which indicates that text has changed.

For text insertion, the

oldValue

is

null

and the

newValue

is an

AccessibleTextSequence

specifying the text
that was inserted.

For text deletion, the

oldValue

is an

AccessibleTextSequence

specifying the text that was deleted and
the

newValue

is

null

.

For text replacement, the

oldValue

is an

AccessibleTextSequence

specifying the old text and the

newValue

is an

AccessibleTextSequence

specifying the new
text.

**See Also:** getAccessibleText()

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

,

AccessibleTextSequence

,

Constant Field Values

---

#### ACCESSIBLE_TEXT_PROPERTY

public static final

String

ACCESSIBLE_TEXT_PROPERTY

PropertyChangeEvent

which indicates that text has changed.

For text insertion, the

oldValue

is

null

and the

newValue

is an

AccessibleTextSequence

specifying the text
that was inserted.

For text deletion, the

oldValue

is an

AccessibleTextSequence

specifying the text that was deleted and
the

newValue

is

null

.

For text replacement, the

oldValue

is an

AccessibleTextSequence

specifying the old text and the

newValue

is an

AccessibleTextSequence

specifying the new
text.

ACCESSIBLE_INVALIDATE_CHILDREN

```java
public static final
String
ACCESSIBLE_INVALIDATE_CHILDREN
```

PropertyChangeEvent

which indicates that a significant change has
occurred to the children of a component like a tree or text. This change
notifies the event listener that it needs to reacquire the state of the
subcomponents. The

oldValue

is

null

and the

newValue

is the component whose children have become invalid.

**Since:** 1.5
**See Also:** getAccessibleText()

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

,

AccessibleTextSequence

,

Constant Field Values

---

#### ACCESSIBLE_INVALIDATE_CHILDREN

public static final

String

ACCESSIBLE_INVALIDATE_CHILDREN

PropertyChangeEvent

which indicates that a significant change has
occurred to the children of a component like a tree or text. This change
notifies the event listener that it needs to reacquire the state of the
subcomponents. The

oldValue

is

null

and the

newValue

is the component whose children have become invalid.

ACCESSIBLE_TEXT_ATTRIBUTES_CHANGED

```java
public static final
String
ACCESSIBLE_TEXT_ATTRIBUTES_CHANGED
```

PropertyChangeEvent

which indicates that text attributes have
changed.

For attribute insertion, the

oldValue

is

null

and the

newValue

is an

AccessibleAttributeSequence

specifying the
attributes that were inserted.

For attribute deletion, the

oldValue

is an

AccessibleAttributeSequence

specifying the attributes that were
deleted and the

newValue

is

null

.

For attribute replacement, the

oldValue

is an

AccessibleAttributeSequence

specifying the old attributes and the

newValue

is an

AccessibleAttributeSequence

specifying the
new attributes.

**Since:** 1.5
**See Also:** getAccessibleText()

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

,

AccessibleAttributeSequence

,

Constant Field Values

---

#### ACCESSIBLE_TEXT_ATTRIBUTES_CHANGED

public static final

String

ACCESSIBLE_TEXT_ATTRIBUTES_CHANGED

PropertyChangeEvent

which indicates that text attributes have
changed.

For attribute insertion, the

oldValue

is

null

and the

newValue

is an

AccessibleAttributeSequence

specifying the
attributes that were inserted.

For attribute deletion, the

oldValue

is an

AccessibleAttributeSequence

specifying the attributes that were
deleted and the

newValue

is

null

.

For attribute replacement, the

oldValue

is an

AccessibleAttributeSequence

specifying the old attributes and the

newValue

is an

AccessibleAttributeSequence

specifying the
new attributes.

ACCESSIBLE_COMPONENT_BOUNDS_CHANGED

```java
public static final
String
ACCESSIBLE_COMPONENT_BOUNDS_CHANGED
```

PropertyChangeEvent

which indicates that a change has occurred in
a component's bounds. The

oldValue

is the old component bounds
and the

newValue

is the new component bounds.

**Since:** 1.5
**See Also:** addPropertyChangeListener(java.beans.PropertyChangeListener)

,

Constant Field Values

---

#### ACCESSIBLE_COMPONENT_BOUNDS_CHANGED

public static final

String

ACCESSIBLE_COMPONENT_BOUNDS_CHANGED

PropertyChangeEvent

which indicates that a change has occurred in
a component's bounds. The

oldValue

is the old component bounds
and the

newValue

is the new component bounds.

accessibleParent

```java
protected
Accessible
accessibleParent
```

The accessible parent of this object.

**See Also:** getAccessibleParent()

,

setAccessibleParent(javax.accessibility.Accessible)

---

#### accessibleParent

protected

Accessible

accessibleParent

The accessible parent of this object.

accessibleName

```java
protected
String
accessibleName
```

A localized String containing the name of the object.

**See Also:** getAccessibleName()

,

setAccessibleName(java.lang.String)

---

#### accessibleName

protected

String

accessibleName

A localized String containing the name of the object.

accessibleDescription

```java
protected
String
accessibleDescription
```

A localized String containing the description of the object.

**See Also:** getAccessibleDescription()

,

setAccessibleDescription(java.lang.String)

---

#### accessibleDescription

protected

String

accessibleDescription

A localized String containing the description of the object.

Constructor Detail

- AccessibleContext

```java
public AccessibleContext()
```

---

#### Constructor Detail

AccessibleContext

```java
public AccessibleContext()
```

---

#### AccessibleContext

public AccessibleContext()

Method Detail

- getAccessibleName

```java
public
String
getAccessibleName()
```

Gets the

accessibleName

property of this object. The

accessibleName

property of an object is a localized

String

that designates the purpose of the object. For example,
the

accessibleName

property of a label or button might be the
text of the label or button itself. In the case of an object that doesn't
display its name, the

accessibleName

should still be set. For
example, in the case of a text field used to enter the name of a city,
the

accessibleName

for the

en_US

locale could be 'city.'

**Returns:** the localized name of the object;

null

if this object
does not have a name
**See Also:** setAccessibleName(java.lang.String)

- setAccessibleName

```java
@BeanProperty
(
preferred
=true,

description
="Sets the accessible name for the component.")
public void setAccessibleName​(
String
s)
```

Sets the localized accessible name of this object. Changing the name will
cause a

PropertyChangeEvent

to be fired for the

ACCESSIBLE_NAME_PROPERTY

property.

**Parameters:** s

- the new localized name of the object
**See Also:** getAccessibleName()

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

- getAccessibleDescription

```java
public
String
getAccessibleDescription()
```

Gets the

accessibleDescription

property of this object. The

accessibleDescription

property of this object is a short
localized phrase describing the purpose of the object. For example, in
the case of a 'Cancel' button, the

accessibleDescription

could be
'Ignore changes and close dialog box.'

**Returns:** the localized description of the object;

null

if this
object does not have a description
**See Also:** setAccessibleDescription(java.lang.String)

- setAccessibleDescription

```java
@BeanProperty
(
preferred
=true,

description
="Sets the accessible description for the component.")
public void setAccessibleDescription​(
String
s)
```

Sets the accessible description of this object. Changing the name will
cause a

PropertyChangeEvent

to be fired for the

ACCESSIBLE_DESCRIPTION_PROPERTY

property.

**Parameters:** s

- the new localized description of the object
**See Also:** setAccessibleName(java.lang.String)

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

- getAccessibleRole

```java
public abstract
AccessibleRole
getAccessibleRole()
```

Gets the role of this object. The role of the object is the generic
purpose or use of the class of this object. For example, the role of a
push button is

AccessibleRole.PUSH_BUTTON

. The roles in

AccessibleRole

are provided so component developers can pick from
a set of predefined roles. This enables assistive technologies to provide
a consistent interface to various tweaked subclasses of components (e.g.,
use

AccessibleRole.PUSH_BUTTON

for all components that act like a
push button) as well as distinguish between subclasses that behave
differently (e.g.,

AccessibleRole.CHECK_BOX

for check boxes and

AccessibleRole.RADIO_BUTTON

for radio buttons).

Note that the

AccessibleRole

class is also extensible, so custom
component developers can define their own

AccessibleRole

's if the
set of predefined roles is inadequate.

**Returns:** an instance of

AccessibleRole

describing the role of the
object
**See Also:** AccessibleRole

- getAccessibleStateSet

```java
public abstract
AccessibleStateSet
getAccessibleStateSet()
```

Gets the state set of this object. The

AccessibleStateSet

of an
object is composed of a set of unique

AccessibleStates

. A change
in the

AccessibleStateSet

of an object will cause a

PropertyChangeEvent

to be fired for the

ACCESSIBLE_STATE_PROPERTY

property.

**Returns:** an instance of

AccessibleStateSet

containing the current
state set of the object
**See Also:** AccessibleStateSet

,

AccessibleState

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

- getAccessibleParent

```java
public
Accessible
getAccessibleParent()
```

Gets the

Accessible

parent of this object.

**Returns:** the

Accessible

parent of this object;

null

if
this object does not have an

Accessible

parent

- setAccessibleParent

```java
public void setAccessibleParent​(
Accessible
a)
```

Sets the

Accessible

parent of this object. This is meant to be
used only in the situations where the actual component's parent should
not be treated as the component's accessible parent and is a method that
should only be called by the parent of the accessible child.

**Parameters:** a

- -

Accessible

to be set as the parent

- getAccessibleIndexInParent

```java
public abstract int getAccessibleIndexInParent()
```

Gets the 0-based index of this object in its accessible parent.

**Returns:** the 0-based index of this object in its parent; -1 if this object
does not have an accessible parent.
**See Also:** getAccessibleParent()

,

getAccessibleChildrenCount()

,

getAccessibleChild(int)

- getAccessibleChildrenCount

```java
public abstract int getAccessibleChildrenCount()
```

Returns the number of accessible children of the object.

**Returns:** the number of accessible children of the object.

- getAccessibleChild

```java
public abstract
Accessible
getAccessibleChild​(int i)
```

Returns the specified

Accessible

child of the object. The

Accessible

children of an

Accessible

object are
zero-based, so the first child of an

Accessible

child is at index
0, the second child is at index 1, and so on.

**Parameters:** i

- zero-based index of child
**Returns:** the

Accessible

child of the object
**See Also:** getAccessibleChildrenCount()

- getLocale

```java
public abstract
Locale
getLocale()
throws
IllegalComponentStateException
```

Gets the locale of the component. If the component does not have a
locale, then the locale of its parent is returned.

**Returns:** this component's locale. If this component does not have a
locale, the locale of its parent is returned.
**Throws:** IllegalComponentStateException

- If the component does not have its
own locale and has not yet been added to a containment hierarchy
such that the locale can be determined from the containing
parent

- addPropertyChangeListener

```java
public void addPropertyChangeListener​(
PropertyChangeListener
listener)
```

Adds a

PropertyChangeListener

to the listener list. The listener
is registered for all

Accessible

properties and will be called
when those properties change.

**Parameters:** listener

- The PropertyChangeListener to be added
**See Also:** ACCESSIBLE_NAME_PROPERTY

,

ACCESSIBLE_DESCRIPTION_PROPERTY

,

ACCESSIBLE_STATE_PROPERTY

,

ACCESSIBLE_VALUE_PROPERTY

,

ACCESSIBLE_SELECTION_PROPERTY

,

ACCESSIBLE_TEXT_PROPERTY

,

ACCESSIBLE_VISIBLE_DATA_PROPERTY

- removePropertyChangeListener

```java
public void removePropertyChangeListener​(
PropertyChangeListener
listener)
```

Removes a

PropertyChangeListener

from the listener list. This
removes a

PropertyChangeListener

that was registered for all
properties.

**Parameters:** listener

- The PropertyChangeListener to be removed

- getAccessibleAction

```java
public
AccessibleAction
getAccessibleAction()
```

Gets the

AccessibleAction

associated with this object that
supports one or more actions.

**Returns:** AccessibleAction

if supported by object; else return

null
**See Also:** AccessibleAction

- getAccessibleComponent

```java
public
AccessibleComponent
getAccessibleComponent()
```

Gets the

AccessibleComponent

associated with this object that has
a graphical representation.

**Returns:** AccessibleComponent

if supported by object; else return

null
**See Also:** AccessibleComponent

- getAccessibleSelection

```java
public
AccessibleSelection
getAccessibleSelection()
```

Gets the

AccessibleSelection

associated with this object which
allows its

Accessible

children to be selected.

**Returns:** AccessibleSelection

if supported by object; else return

null
**See Also:** AccessibleSelection

- getAccessibleText

```java
public
AccessibleText
getAccessibleText()
```

Gets the

AccessibleText

associated with this object presenting
text on the display.

**Returns:** AccessibleText

if supported by object; else return

null
**See Also:** AccessibleText

- getAccessibleEditableText

```java
public
AccessibleEditableText
getAccessibleEditableText()
```

Gets the

AccessibleEditableText

associated with this object
presenting editable text on the display.

**Returns:** AccessibleEditableText

if supported by object; else
return

null
**Since:** 1.4
**See Also:** AccessibleEditableText

- getAccessibleValue

```java
public
AccessibleValue
getAccessibleValue()
```

Gets the

AccessibleValue

associated with this object that
supports a

Numerical

value.

**Returns:** AccessibleValue

if supported by object; else return

null
**See Also:** AccessibleValue

- getAccessibleIcon

```java
public
AccessibleIcon
[] getAccessibleIcon()
```

Gets the

AccessibleIcons

associated with an object that has one
or more associated icons.

**Returns:** an array of

AccessibleIcon

if supported by object;
otherwise return

null
**Since:** 1.3
**See Also:** AccessibleIcon

- getAccessibleRelationSet

```java
public
AccessibleRelationSet
getAccessibleRelationSet()
```

Gets the

AccessibleRelationSet

associated with an object.

**Returns:** an

AccessibleRelationSet

if supported by object;
otherwise return

null
**Since:** 1.3
**See Also:** AccessibleRelationSet

- getAccessibleTable

```java
public
AccessibleTable
getAccessibleTable()
```

Gets the

AccessibleTable

associated with an object.

**Returns:** an

AccessibleTable

if supported by object; otherwise return

null
**Since:** 1.3
**See Also:** AccessibleTable

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,

Object
oldValue,

Object
newValue)
```

Support for reporting bound property changes. If

oldValue

and

newValue

are not equal and the

PropertyChangeEvent

listener list is not empty, then fire a

PropertyChange

event to
each listener. In general, this is for use by the

Accessible

objects themselves and should not be called by an application program.

**Parameters:** propertyName

- The programmatic name of the property that was
changed
**Parameters:** oldValue

- The old value of the property
**Parameters:** newValue

- The new value of the property
**See Also:** PropertyChangeSupport

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

,

removePropertyChangeListener(java.beans.PropertyChangeListener)

,

ACCESSIBLE_NAME_PROPERTY

,

ACCESSIBLE_DESCRIPTION_PROPERTY

,

ACCESSIBLE_STATE_PROPERTY

,

ACCESSIBLE_VALUE_PROPERTY

,

ACCESSIBLE_SELECTION_PROPERTY

,

ACCESSIBLE_TEXT_PROPERTY

,

ACCESSIBLE_VISIBLE_DATA_PROPERTY

---

#### Method Detail

getAccessibleName

```java
public
String
getAccessibleName()
```

Gets the

accessibleName

property of this object. The

accessibleName

property of an object is a localized

String

that designates the purpose of the object. For example,
the

accessibleName

property of a label or button might be the
text of the label or button itself. In the case of an object that doesn't
display its name, the

accessibleName

should still be set. For
example, in the case of a text field used to enter the name of a city,
the

accessibleName

for the

en_US

locale could be 'city.'

**Returns:** the localized name of the object;

null

if this object
does not have a name
**See Also:** setAccessibleName(java.lang.String)

---

#### getAccessibleName

public

String

getAccessibleName()

Gets the

accessibleName

property of this object. The

accessibleName

property of an object is a localized

String

that designates the purpose of the object. For example,
the

accessibleName

property of a label or button might be the
text of the label or button itself. In the case of an object that doesn't
display its name, the

accessibleName

should still be set. For
example, in the case of a text field used to enter the name of a city,
the

accessibleName

for the

en_US

locale could be 'city.'

setAccessibleName

```java
@BeanProperty
(
preferred
=true,

description
="Sets the accessible name for the component.")
public void setAccessibleName​(
String
s)
```

Sets the localized accessible name of this object. Changing the name will
cause a

PropertyChangeEvent

to be fired for the

ACCESSIBLE_NAME_PROPERTY

property.

**Parameters:** s

- the new localized name of the object
**See Also:** getAccessibleName()

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

---

#### setAccessibleName

@BeanProperty

(

preferred

=true,

description

="Sets the accessible name for the component.")
public void setAccessibleName​(

String

s)

Sets the localized accessible name of this object. Changing the name will
cause a

PropertyChangeEvent

to be fired for the

ACCESSIBLE_NAME_PROPERTY

property.

getAccessibleDescription

```java
public
String
getAccessibleDescription()
```

Gets the

accessibleDescription

property of this object. The

accessibleDescription

property of this object is a short
localized phrase describing the purpose of the object. For example, in
the case of a 'Cancel' button, the

accessibleDescription

could be
'Ignore changes and close dialog box.'

**Returns:** the localized description of the object;

null

if this
object does not have a description
**See Also:** setAccessibleDescription(java.lang.String)

---

#### getAccessibleDescription

public

String

getAccessibleDescription()

Gets the

accessibleDescription

property of this object. The

accessibleDescription

property of this object is a short
localized phrase describing the purpose of the object. For example, in
the case of a 'Cancel' button, the

accessibleDescription

could be
'Ignore changes and close dialog box.'

setAccessibleDescription

```java
@BeanProperty
(
preferred
=true,

description
="Sets the accessible description for the component.")
public void setAccessibleDescription​(
String
s)
```

Sets the accessible description of this object. Changing the name will
cause a

PropertyChangeEvent

to be fired for the

ACCESSIBLE_DESCRIPTION_PROPERTY

property.

**Parameters:** s

- the new localized description of the object
**See Also:** setAccessibleName(java.lang.String)

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

---

#### setAccessibleDescription

@BeanProperty

(

preferred

=true,

description

="Sets the accessible description for the component.")
public void setAccessibleDescription​(

String

s)

Sets the accessible description of this object. Changing the name will
cause a

PropertyChangeEvent

to be fired for the

ACCESSIBLE_DESCRIPTION_PROPERTY

property.

getAccessibleRole

```java
public abstract
AccessibleRole
getAccessibleRole()
```

Gets the role of this object. The role of the object is the generic
purpose or use of the class of this object. For example, the role of a
push button is

AccessibleRole.PUSH_BUTTON

. The roles in

AccessibleRole

are provided so component developers can pick from
a set of predefined roles. This enables assistive technologies to provide
a consistent interface to various tweaked subclasses of components (e.g.,
use

AccessibleRole.PUSH_BUTTON

for all components that act like a
push button) as well as distinguish between subclasses that behave
differently (e.g.,

AccessibleRole.CHECK_BOX

for check boxes and

AccessibleRole.RADIO_BUTTON

for radio buttons).

Note that the

AccessibleRole

class is also extensible, so custom
component developers can define their own

AccessibleRole

's if the
set of predefined roles is inadequate.

**Returns:** an instance of

AccessibleRole

describing the role of the
object
**See Also:** AccessibleRole

---

#### getAccessibleRole

public abstract

AccessibleRole

getAccessibleRole()

Gets the role of this object. The role of the object is the generic
purpose or use of the class of this object. For example, the role of a
push button is

AccessibleRole.PUSH_BUTTON

. The roles in

AccessibleRole

are provided so component developers can pick from
a set of predefined roles. This enables assistive technologies to provide
a consistent interface to various tweaked subclasses of components (e.g.,
use

AccessibleRole.PUSH_BUTTON

for all components that act like a
push button) as well as distinguish between subclasses that behave
differently (e.g.,

AccessibleRole.CHECK_BOX

for check boxes and

AccessibleRole.RADIO_BUTTON

for radio buttons).

Note that the

AccessibleRole

class is also extensible, so custom
component developers can define their own

AccessibleRole

's if the
set of predefined roles is inadequate.

Note that the

AccessibleRole

class is also extensible, so custom
component developers can define their own

AccessibleRole

's if the
set of predefined roles is inadequate.

getAccessibleStateSet

```java
public abstract
AccessibleStateSet
getAccessibleStateSet()
```

Gets the state set of this object. The

AccessibleStateSet

of an
object is composed of a set of unique

AccessibleStates

. A change
in the

AccessibleStateSet

of an object will cause a

PropertyChangeEvent

to be fired for the

ACCESSIBLE_STATE_PROPERTY

property.

**Returns:** an instance of

AccessibleStateSet

containing the current
state set of the object
**See Also:** AccessibleStateSet

,

AccessibleState

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

---

#### getAccessibleStateSet

public abstract

AccessibleStateSet

getAccessibleStateSet()

Gets the state set of this object. The

AccessibleStateSet

of an
object is composed of a set of unique

AccessibleStates

. A change
in the

AccessibleStateSet

of an object will cause a

PropertyChangeEvent

to be fired for the

ACCESSIBLE_STATE_PROPERTY

property.

getAccessibleParent

```java
public
Accessible
getAccessibleParent()
```

Gets the

Accessible

parent of this object.

**Returns:** the

Accessible

parent of this object;

null

if
this object does not have an

Accessible

parent

---

#### getAccessibleParent

public

Accessible

getAccessibleParent()

Gets the

Accessible

parent of this object.

setAccessibleParent

```java
public void setAccessibleParent​(
Accessible
a)
```

Sets the

Accessible

parent of this object. This is meant to be
used only in the situations where the actual component's parent should
not be treated as the component's accessible parent and is a method that
should only be called by the parent of the accessible child.

**Parameters:** a

- -

Accessible

to be set as the parent

---

#### setAccessibleParent

public void setAccessibleParent​(

Accessible

a)

Sets the

Accessible

parent of this object. This is meant to be
used only in the situations where the actual component's parent should
not be treated as the component's accessible parent and is a method that
should only be called by the parent of the accessible child.

getAccessibleIndexInParent

```java
public abstract int getAccessibleIndexInParent()
```

Gets the 0-based index of this object in its accessible parent.

**Returns:** the 0-based index of this object in its parent; -1 if this object
does not have an accessible parent.
**See Also:** getAccessibleParent()

,

getAccessibleChildrenCount()

,

getAccessibleChild(int)

---

#### getAccessibleIndexInParent

public abstract int getAccessibleIndexInParent()

Gets the 0-based index of this object in its accessible parent.

getAccessibleChildrenCount

```java
public abstract int getAccessibleChildrenCount()
```

Returns the number of accessible children of the object.

**Returns:** the number of accessible children of the object.

---

#### getAccessibleChildrenCount

public abstract int getAccessibleChildrenCount()

Returns the number of accessible children of the object.

getAccessibleChild

```java
public abstract
Accessible
getAccessibleChild​(int i)
```

Returns the specified

Accessible

child of the object. The

Accessible

children of an

Accessible

object are
zero-based, so the first child of an

Accessible

child is at index
0, the second child is at index 1, and so on.

**Parameters:** i

- zero-based index of child
**Returns:** the

Accessible

child of the object
**See Also:** getAccessibleChildrenCount()

---

#### getAccessibleChild

public abstract

Accessible

getAccessibleChild​(int i)

Returns the specified

Accessible

child of the object. The

Accessible

children of an

Accessible

object are
zero-based, so the first child of an

Accessible

child is at index
0, the second child is at index 1, and so on.

getLocale

```java
public abstract
Locale
getLocale()
throws
IllegalComponentStateException
```

Gets the locale of the component. If the component does not have a
locale, then the locale of its parent is returned.

**Returns:** this component's locale. If this component does not have a
locale, the locale of its parent is returned.
**Throws:** IllegalComponentStateException

- If the component does not have its
own locale and has not yet been added to a containment hierarchy
such that the locale can be determined from the containing
parent

---

#### getLocale

public abstract

Locale

getLocale()
throws

IllegalComponentStateException

Gets the locale of the component. If the component does not have a
locale, then the locale of its parent is returned.

addPropertyChangeListener

```java
public void addPropertyChangeListener​(
PropertyChangeListener
listener)
```

Adds a

PropertyChangeListener

to the listener list. The listener
is registered for all

Accessible

properties and will be called
when those properties change.

**Parameters:** listener

- The PropertyChangeListener to be added
**See Also:** ACCESSIBLE_NAME_PROPERTY

,

ACCESSIBLE_DESCRIPTION_PROPERTY

,

ACCESSIBLE_STATE_PROPERTY

,

ACCESSIBLE_VALUE_PROPERTY

,

ACCESSIBLE_SELECTION_PROPERTY

,

ACCESSIBLE_TEXT_PROPERTY

,

ACCESSIBLE_VISIBLE_DATA_PROPERTY

---

#### addPropertyChangeListener

public void addPropertyChangeListener​(

PropertyChangeListener

listener)

Adds a

PropertyChangeListener

to the listener list. The listener
is registered for all

Accessible

properties and will be called
when those properties change.

removePropertyChangeListener

```java
public void removePropertyChangeListener​(
PropertyChangeListener
listener)
```

Removes a

PropertyChangeListener

from the listener list. This
removes a

PropertyChangeListener

that was registered for all
properties.

**Parameters:** listener

- The PropertyChangeListener to be removed

---

#### removePropertyChangeListener

public void removePropertyChangeListener​(

PropertyChangeListener

listener)

Removes a

PropertyChangeListener

from the listener list. This
removes a

PropertyChangeListener

that was registered for all
properties.

getAccessibleAction

```java
public
AccessibleAction
getAccessibleAction()
```

Gets the

AccessibleAction

associated with this object that
supports one or more actions.

**Returns:** AccessibleAction

if supported by object; else return

null
**See Also:** AccessibleAction

---

#### getAccessibleAction

public

AccessibleAction

getAccessibleAction()

Gets the

AccessibleAction

associated with this object that
supports one or more actions.

getAccessibleComponent

```java
public
AccessibleComponent
getAccessibleComponent()
```

Gets the

AccessibleComponent

associated with this object that has
a graphical representation.

**Returns:** AccessibleComponent

if supported by object; else return

null
**See Also:** AccessibleComponent

---

#### getAccessibleComponent

public

AccessibleComponent

getAccessibleComponent()

Gets the

AccessibleComponent

associated with this object that has
a graphical representation.

getAccessibleSelection

```java
public
AccessibleSelection
getAccessibleSelection()
```

Gets the

AccessibleSelection

associated with this object which
allows its

Accessible

children to be selected.

**Returns:** AccessibleSelection

if supported by object; else return

null
**See Also:** AccessibleSelection

---

#### getAccessibleSelection

public

AccessibleSelection

getAccessibleSelection()

Gets the

AccessibleSelection

associated with this object which
allows its

Accessible

children to be selected.

getAccessibleText

```java
public
AccessibleText
getAccessibleText()
```

Gets the

AccessibleText

associated with this object presenting
text on the display.

**Returns:** AccessibleText

if supported by object; else return

null
**See Also:** AccessibleText

---

#### getAccessibleText

public

AccessibleText

getAccessibleText()

Gets the

AccessibleText

associated with this object presenting
text on the display.

getAccessibleEditableText

```java
public
AccessibleEditableText
getAccessibleEditableText()
```

Gets the

AccessibleEditableText

associated with this object
presenting editable text on the display.

**Returns:** AccessibleEditableText

if supported by object; else
return

null
**Since:** 1.4
**See Also:** AccessibleEditableText

---

#### getAccessibleEditableText

public

AccessibleEditableText

getAccessibleEditableText()

Gets the

AccessibleEditableText

associated with this object
presenting editable text on the display.

getAccessibleValue

```java
public
AccessibleValue
getAccessibleValue()
```

Gets the

AccessibleValue

associated with this object that
supports a

Numerical

value.

**Returns:** AccessibleValue

if supported by object; else return

null
**See Also:** AccessibleValue

---

#### getAccessibleValue

public

AccessibleValue

getAccessibleValue()

Gets the

AccessibleValue

associated with this object that
supports a

Numerical

value.

getAccessibleIcon

```java
public
AccessibleIcon
[] getAccessibleIcon()
```

Gets the

AccessibleIcons

associated with an object that has one
or more associated icons.

**Returns:** an array of

AccessibleIcon

if supported by object;
otherwise return

null
**Since:** 1.3
**See Also:** AccessibleIcon

---

#### getAccessibleIcon

public

AccessibleIcon

[] getAccessibleIcon()

Gets the

AccessibleIcons

associated with an object that has one
or more associated icons.

getAccessibleRelationSet

```java
public
AccessibleRelationSet
getAccessibleRelationSet()
```

Gets the

AccessibleRelationSet

associated with an object.

**Returns:** an

AccessibleRelationSet

if supported by object;
otherwise return

null
**Since:** 1.3
**See Also:** AccessibleRelationSet

---

#### getAccessibleRelationSet

public

AccessibleRelationSet

getAccessibleRelationSet()

Gets the

AccessibleRelationSet

associated with an object.

getAccessibleTable

```java
public
AccessibleTable
getAccessibleTable()
```

Gets the

AccessibleTable

associated with an object.

**Returns:** an

AccessibleTable

if supported by object; otherwise return

null
**Since:** 1.3
**See Also:** AccessibleTable

---

#### getAccessibleTable

public

AccessibleTable

getAccessibleTable()

Gets the

AccessibleTable

associated with an object.

firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,

Object
oldValue,

Object
newValue)
```

Support for reporting bound property changes. If

oldValue

and

newValue

are not equal and the

PropertyChangeEvent

listener list is not empty, then fire a

PropertyChange

event to
each listener. In general, this is for use by the

Accessible

objects themselves and should not be called by an application program.

**Parameters:** propertyName

- The programmatic name of the property that was
changed
**Parameters:** oldValue

- The old value of the property
**Parameters:** newValue

- The new value of the property
**See Also:** PropertyChangeSupport

,

addPropertyChangeListener(java.beans.PropertyChangeListener)

,

removePropertyChangeListener(java.beans.PropertyChangeListener)

,

ACCESSIBLE_NAME_PROPERTY

,

ACCESSIBLE_DESCRIPTION_PROPERTY

,

ACCESSIBLE_STATE_PROPERTY

,

ACCESSIBLE_VALUE_PROPERTY

,

ACCESSIBLE_SELECTION_PROPERTY

,

ACCESSIBLE_TEXT_PROPERTY

,

ACCESSIBLE_VISIBLE_DATA_PROPERTY

---

#### firePropertyChange

public void firePropertyChange​(

String

propertyName,

Object

oldValue,

Object

newValue)

Support for reporting bound property changes. If

oldValue

and

newValue

are not equal and the

PropertyChangeEvent

listener list is not empty, then fire a

PropertyChange

event to
each listener. In general, this is for use by the

Accessible

objects themselves and should not be called by an application program.

---

