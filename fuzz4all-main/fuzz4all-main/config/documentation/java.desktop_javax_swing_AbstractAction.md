# Class AbstractAction

**Source:** `java.desktop\javax\swing\AbstractAction.html`

### Class Description

```java
public abstract class
AbstractAction

extends
Object

implements
Action
,
Cloneable
,
Serializable
```

This class provides default implementations for the JFC

Action

interface. Standard behaviors like the get and set methods for

Action

object properties (icon, text, and enabled) are defined
here. The developer need only subclass this abstract class and
define the

actionPerformed

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

**All Implemented Interfaces:** ActionListener

,

Serializable

,

Cloneable

,

EventListener

,

Action

---

### Field Details

#### protected boolean enabled

Specifies whether action is enabled; the default is true.

---

#### protected
SwingPropertyChangeSupport
changeSupport

If any

PropertyChangeListeners

have been registered, the

changeSupport

field describes them.

---

### Constructor Details

#### public AbstractAction()

Creates an

Action

.

---

#### public AbstractAction​(
String
name)

Creates an

Action

with the specified name.

**Parameters:**
- name

- the name (

Action.NAME

) for the action; a
value of

null

is ignored

---

#### public AbstractAction​(
String
name,

Icon
icon)

Creates an

Action

with the specified name and small icon.

**Parameters:**
- name

- the name (

Action.NAME

) for the action; a
value of

null

is ignored
- icon

- the small icon (

Action.SMALL_ICON

) for the action; a
value of

null

is ignored

---

### Method Details

#### public
Object
getValue​(
String
key)

Gets the

Object

associated with the specified key.

**Specified by:**
- getValue

in interface

Action

**Parameters:**
- key

- a string containing the specified

key

**Returns:**
- the binding

Object

stored with this key; if there
are no keys, it will return

null

**See Also:**
- Action.getValue(java.lang.String)

---

#### public void putValue​(
String
key,

Object
newValue)

Sets the

Value

associated with the specified key.

**Specified by:**
- putValue

in interface

Action

**Parameters:**
- key

- the

String

that identifies the stored object
- newValue

- the

Object

to store using this key

**See Also:**
- Action.putValue(java.lang.String, java.lang.Object)

---

#### public boolean isEnabled()

Returns true if the action is enabled.

**Specified by:**
- isEnabled

in interface

Action

**Returns:**
- true if the action is enabled, false otherwise

**See Also:**
- Action.isEnabled()

---

#### public void setEnabled​(boolean newValue)

Sets whether the

Action

is enabled. The default is

true

.

**Specified by:**
- setEnabled

in interface

Action

**Parameters:**
- newValue

-

true

to enable the action,

false

to
disable it

**See Also:**
- Action.setEnabled(boolean)

---

#### public
Object
[] getKeys()

Returns an array of

Object

s which are keys for
which values have been set for this

AbstractAction

,
or

null

if no keys have values set.

**Returns:**
- an array of key objects, or

null

if no
keys have values set

**Since:**
- 1.3

---

#### protected void firePropertyChange​(
String
propertyName,

Object
oldValue,

Object
newValue)

Supports reporting bound property changes. This method can be called
when a bound property has changed and it will send the appropriate

PropertyChangeEvent

to any registered

PropertyChangeListeners

.

**Parameters:**
- propertyName

- the name of the property that has changed
- oldValue

- the old value of the property
- newValue

- the new value of the property

---

#### public void addPropertyChangeListener​(
PropertyChangeListener
listener)

Adds a

PropertyChangeListener

to the listener list.
The listener is registered for all properties.

A

PropertyChangeEvent

will get fired in response to setting
a bound property, e.g.

setFont

,

setBackground

,
or

setForeground

.
Note that if the current component is inheriting its foreground,
background, or font from its container, then no event will be
fired in response to a change in the inherited property.

**Specified by:**
- addPropertyChangeListener

in interface

Action

**Parameters:**
- listener

- The

PropertyChangeListener

to be added

**See Also:**
- Action.addPropertyChangeListener(java.beans.PropertyChangeListener)

---

#### public void removePropertyChangeListener​(
PropertyChangeListener
listener)

Removes a

PropertyChangeListener

from the listener list.
This removes a

PropertyChangeListener

that was registered
for all properties.

**Specified by:**
- removePropertyChangeListener

in interface

Action

**Parameters:**
- listener

- the

PropertyChangeListener

to be removed

**See Also:**
- Action.removePropertyChangeListener(java.beans.PropertyChangeListener)

---

#### public
PropertyChangeListener
[] getPropertyChangeListeners()

Returns an array of all the

PropertyChangeListener

s added
to this AbstractAction with addPropertyChangeListener().

**Returns:**
- all of the

PropertyChangeListener

s added or an empty
array if no listeners have been added

**Since:**
- 1.4

---

#### protected
Object
clone()
throws
CloneNotSupportedException

Clones the abstract action. This gives the clone
its own copy of the key/value list,
which is not handled for you by

Object.clone()

.

**Overrides:**
- clone

in class

Object

**Returns:**
- a clone of this instance.

**Throws:**
- CloneNotSupportedException

- if the object's class does not
support the

Cloneable

interface. Subclasses
that override the

clone

method can also
throw this exception to indicate that an instance cannot
be cloned.

**See Also:**
- Cloneable

---

### Additional Sections

#### Class AbstractAction

java.lang.Object

- javax.swing.AbstractAction

javax.swing.AbstractAction

**All Implemented Interfaces:** ActionListener

,

Serializable

,

Cloneable

,

EventListener

,

Action

**Direct Known Subclasses:** BasicDesktopPaneUI.CloseAction

,

BasicDesktopPaneUI.MaximizeAction

,

BasicDesktopPaneUI.MinimizeAction

,

BasicDesktopPaneUI.NavigateAction

,

BasicDesktopPaneUI.OpenAction

,

BasicFileChooserUI.ApproveSelectionAction

,

BasicFileChooserUI.CancelSelectionAction

,

BasicFileChooserUI.ChangeToParentDirectoryAction

,

BasicFileChooserUI.GoHomeAction

,

BasicFileChooserUI.NewFolderAction

,

BasicFileChooserUI.UpdateAction

,

BasicInternalFrameTitlePane.CloseAction

,

BasicInternalFrameTitlePane.IconifyAction

,

BasicInternalFrameTitlePane.MaximizeAction

,

BasicInternalFrameTitlePane.MoveAction

,

BasicInternalFrameTitlePane.RestoreAction

,

BasicInternalFrameTitlePane.SizeAction

,

BasicSliderUI.ActionScroller

,

BasicTreeUI.TreeCancelEditingAction

,

BasicTreeUI.TreeHomeAction

,

BasicTreeUI.TreeIncrementAction

,

BasicTreeUI.TreePageAction

,

BasicTreeUI.TreeToggleAction

,

BasicTreeUI.TreeTraverseAction

,

MetalFileChooserUI.DirectoryComboBoxAction

,

TextAction

```java
public abstract class
AbstractAction

extends
Object

implements
Action
,
Cloneable
,
Serializable
```

This class provides default implementations for the JFC

Action

interface. Standard behaviors like the get and set methods for

Action

object properties (icon, text, and enabled) are defined
here. The developer need only subclass this abstract class and
define the

actionPerformed

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

**Since:** 1.2
**See Also:** Action

,

Serialized Form

public abstract class

AbstractAction

extends

Object

implements

Action

,

Cloneable

,

Serializable

This class provides default implementations for the JFC

Action

interface. Standard behaviors like the get and set methods for

Action

object properties (icon, text, and enabled) are defined
here. The developer need only subclass this abstract class and
define the

actionPerformed

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

protected

SwingPropertyChangeSupport

changeSupport

If any

PropertyChangeListeners

have been registered, the

changeSupport

field describes them.

protected boolean

enabled

Specifies whether action is enabled; the default is true.

- Fields declared in interface javax.swing.

Action

ACCELERATOR_KEY

,

ACTION_COMMAND_KEY

,

DEFAULT

,

DISPLAYED_MNEMONIC_INDEX_KEY

,

LARGE_ICON_KEY

,

LONG_DESCRIPTION

,

MNEMONIC_KEY

,

NAME

,

SELECTED_KEY

,

SHORT_DESCRIPTION

,

SMALL_ICON

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AbstractAction

()

Creates an

Action

.

AbstractAction

​(

String

name)

Creates an

Action

with the specified name.

AbstractAction

​(

String

name,

Icon

icon)

Creates an

Action

with the specified name and small icon.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

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

protected

Object

clone

()

Clones the abstract action.

protected void

firePropertyChange

​(

String

propertyName,

Object

oldValue,

Object

newValue)

Supports reporting bound property changes.

Object

[]

getKeys

()

Returns an array of

Object

s which are keys for
which values have been set for this

AbstractAction

,
or

null

if no keys have values set.

PropertyChangeListener

[]

getPropertyChangeListeners

()

Returns an array of all the

PropertyChangeListener

s added
to this AbstractAction with addPropertyChangeListener().

Object

getValue

​(

String

key)

Gets the

Object

associated with the specified key.

boolean

isEnabled

()

Returns true if the action is enabled.

void

putValue

​(

String

key,

Object

newValue)

Sets the

Value

associated with the specified key.

void

removePropertyChangeListener

​(

PropertyChangeListener

listener)

Removes a

PropertyChangeListener

from the listener list.

void

setEnabled

​(boolean newValue)

Sets whether the

Action

is enabled.

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

- Methods declared in interface javax.swing.

Action

accept

- Methods declared in interface java.awt.event.

ActionListener

actionPerformed

Field Summary

Fields

Modifier and Type

Field

Description

protected

SwingPropertyChangeSupport

changeSupport

If any

PropertyChangeListeners

have been registered, the

changeSupport

field describes them.

protected boolean

enabled

Specifies whether action is enabled; the default is true.

- Fields declared in interface javax.swing.

Action

ACCELERATOR_KEY

,

ACTION_COMMAND_KEY

,

DEFAULT

,

DISPLAYED_MNEMONIC_INDEX_KEY

,

LARGE_ICON_KEY

,

LONG_DESCRIPTION

,

MNEMONIC_KEY

,

NAME

,

SELECTED_KEY

,

SHORT_DESCRIPTION

,

SMALL_ICON

---

#### Field Summary

If any

PropertyChangeListeners

have been registered, the

changeSupport

field describes them.

Specifies whether action is enabled; the default is true.

Fields declared in interface javax.swing.

Action

ACCELERATOR_KEY

,

ACTION_COMMAND_KEY

,

DEFAULT

,

DISPLAYED_MNEMONIC_INDEX_KEY

,

LARGE_ICON_KEY

,

LONG_DESCRIPTION

,

MNEMONIC_KEY

,

NAME

,

SELECTED_KEY

,

SHORT_DESCRIPTION

,

SMALL_ICON

---

#### Fields declared in interface javax.swing. Action

Constructor Summary

Constructors

Constructor

Description

AbstractAction

()

Creates an

Action

.

AbstractAction

​(

String

name)

Creates an

Action

with the specified name.

AbstractAction

​(

String

name,

Icon

icon)

Creates an

Action

with the specified name and small icon.

---

#### Constructor Summary

Creates an

Action

.

Creates an

Action

with the specified name.

Creates an

Action

with the specified name and small icon.

Method Summary

All Methods

Instance Methods

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

protected

Object

clone

()

Clones the abstract action.

protected void

firePropertyChange

​(

String

propertyName,

Object

oldValue,

Object

newValue)

Supports reporting bound property changes.

Object

[]

getKeys

()

Returns an array of

Object

s which are keys for
which values have been set for this

AbstractAction

,
or

null

if no keys have values set.

PropertyChangeListener

[]

getPropertyChangeListeners

()

Returns an array of all the

PropertyChangeListener

s added
to this AbstractAction with addPropertyChangeListener().

Object

getValue

​(

String

key)

Gets the

Object

associated with the specified key.

boolean

isEnabled

()

Returns true if the action is enabled.

void

putValue

​(

String

key,

Object

newValue)

Sets the

Value

associated with the specified key.

void

removePropertyChangeListener

​(

PropertyChangeListener

listener)

Removes a

PropertyChangeListener

from the listener list.

void

setEnabled

​(boolean newValue)

Sets whether the

Action

is enabled.

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

- Methods declared in interface javax.swing.

Action

accept

- Methods declared in interface java.awt.event.

ActionListener

actionPerformed

---

#### Method Summary

Adds a

PropertyChangeListener

to the listener list.

Clones the abstract action.

Supports reporting bound property changes.

Returns an array of

Object

s which are keys for
which values have been set for this

AbstractAction

,
or

null

if no keys have values set.

Returns an array of all the

PropertyChangeListener

s added
to this AbstractAction with addPropertyChangeListener().

Gets the

Object

associated with the specified key.

Returns true if the action is enabled.

Sets the

Value

associated with the specified key.

Removes a

PropertyChangeListener

from the listener list.

Sets whether the

Action

is enabled.

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

Methods declared in interface javax.swing.

Action

accept

---

#### Methods declared in interface javax.swing. Action

Methods declared in interface java.awt.event.

ActionListener

actionPerformed

---

#### Methods declared in interface java.awt.event. ActionListener

============ FIELD DETAIL ===========

- Field Detail

- enabled

```java
protected boolean enabled
```

Specifies whether action is enabled; the default is true.

- changeSupport

```java
protected
SwingPropertyChangeSupport
changeSupport
```

If any

PropertyChangeListeners

have been registered, the

changeSupport

field describes them.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AbstractAction

```java
public AbstractAction()
```

Creates an

Action

.

- AbstractAction

```java
public AbstractAction​(
String
name)
```

Creates an

Action

with the specified name.

**Parameters:** name

- the name (

Action.NAME

) for the action; a
value of

null

is ignored

- AbstractAction

```java
public AbstractAction​(
String
name,

Icon
icon)
```

Creates an

Action

with the specified name and small icon.

**Parameters:** name

- the name (

Action.NAME

) for the action; a
value of

null

is ignored
**Parameters:** icon

- the small icon (

Action.SMALL_ICON

) for the action; a
value of

null

is ignored

============ METHOD DETAIL ==========

- Method Detail

- getValue

```java
public
Object
getValue​(
String
key)
```

Gets the

Object

associated with the specified key.

**Specified by:** getValue

in interface

Action
**Parameters:** key

- a string containing the specified

key
**Returns:** the binding

Object

stored with this key; if there
are no keys, it will return

null
**See Also:** Action.getValue(java.lang.String)

- putValue

```java
public void putValue​(
String
key,

Object
newValue)
```

Sets the

Value

associated with the specified key.

**Specified by:** putValue

in interface

Action
**Parameters:** key

- the

String

that identifies the stored object
**Parameters:** newValue

- the

Object

to store using this key
**See Also:** Action.putValue(java.lang.String, java.lang.Object)

- isEnabled

```java
public boolean isEnabled()
```

Returns true if the action is enabled.

**Specified by:** isEnabled

in interface

Action
**Returns:** true if the action is enabled, false otherwise
**See Also:** Action.isEnabled()

- setEnabled

```java
public void setEnabled​(boolean newValue)
```

Sets whether the

Action

is enabled. The default is

true

.

**Specified by:** setEnabled

in interface

Action
**Parameters:** newValue

-

true

to enable the action,

false

to
disable it
**See Also:** Action.setEnabled(boolean)

- getKeys

```java
public
Object
[] getKeys()
```

Returns an array of

Object

s which are keys for
which values have been set for this

AbstractAction

,
or

null

if no keys have values set.

**Returns:** an array of key objects, or

null

if no
keys have values set
**Since:** 1.3

- firePropertyChange

```java
protected void firePropertyChange​(
String
propertyName,

Object
oldValue,

Object
newValue)
```

Supports reporting bound property changes. This method can be called
when a bound property has changed and it will send the appropriate

PropertyChangeEvent

to any registered

PropertyChangeListeners

.

**Parameters:** propertyName

- the name of the property that has changed
**Parameters:** oldValue

- the old value of the property
**Parameters:** newValue

- the new value of the property

- addPropertyChangeListener

```java
public void addPropertyChangeListener​(
PropertyChangeListener
listener)
```

Adds a

PropertyChangeListener

to the listener list.
The listener is registered for all properties.

A

PropertyChangeEvent

will get fired in response to setting
a bound property, e.g.

setFont

,

setBackground

,
or

setForeground

.
Note that if the current component is inheriting its foreground,
background, or font from its container, then no event will be
fired in response to a change in the inherited property.

**Specified by:** addPropertyChangeListener

in interface

Action
**Parameters:** listener

- The

PropertyChangeListener

to be added
**See Also:** Action.addPropertyChangeListener(java.beans.PropertyChangeListener)

- removePropertyChangeListener

```java
public void removePropertyChangeListener​(
PropertyChangeListener
listener)
```

Removes a

PropertyChangeListener

from the listener list.
This removes a

PropertyChangeListener

that was registered
for all properties.

**Specified by:** removePropertyChangeListener

in interface

Action
**Parameters:** listener

- the

PropertyChangeListener

to be removed
**See Also:** Action.removePropertyChangeListener(java.beans.PropertyChangeListener)

- getPropertyChangeListeners

```java
public
PropertyChangeListener
[] getPropertyChangeListeners()
```

Returns an array of all the

PropertyChangeListener

s added
to this AbstractAction with addPropertyChangeListener().

**Returns:** all of the

PropertyChangeListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

- clone

```java
protected
Object
clone()
throws
CloneNotSupportedException
```

Clones the abstract action. This gives the clone
its own copy of the key/value list,
which is not handled for you by

Object.clone()

.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**Throws:** CloneNotSupportedException

- if the object's class does not
support the

Cloneable

interface. Subclasses
that override the

clone

method can also
throw this exception to indicate that an instance cannot
be cloned.
**See Also:** Cloneable

Field Detail

- enabled

```java
protected boolean enabled
```

Specifies whether action is enabled; the default is true.

- changeSupport

```java
protected
SwingPropertyChangeSupport
changeSupport
```

If any

PropertyChangeListeners

have been registered, the

changeSupport

field describes them.

---

#### Field Detail

enabled

```java
protected boolean enabled
```

Specifies whether action is enabled; the default is true.

---

#### enabled

protected boolean enabled

Specifies whether action is enabled; the default is true.

changeSupport

```java
protected
SwingPropertyChangeSupport
changeSupport
```

If any

PropertyChangeListeners

have been registered, the

changeSupport

field describes them.

---

#### changeSupport

protected

SwingPropertyChangeSupport

changeSupport

If any

PropertyChangeListeners

have been registered, the

changeSupport

field describes them.

Constructor Detail

- AbstractAction

```java
public AbstractAction()
```

Creates an

Action

.

- AbstractAction

```java
public AbstractAction​(
String
name)
```

Creates an

Action

with the specified name.

**Parameters:** name

- the name (

Action.NAME

) for the action; a
value of

null

is ignored

- AbstractAction

```java
public AbstractAction​(
String
name,

Icon
icon)
```

Creates an

Action

with the specified name and small icon.

**Parameters:** name

- the name (

Action.NAME

) for the action; a
value of

null

is ignored
**Parameters:** icon

- the small icon (

Action.SMALL_ICON

) for the action; a
value of

null

is ignored

---

#### Constructor Detail

AbstractAction

```java
public AbstractAction()
```

Creates an

Action

.

---

#### AbstractAction

public AbstractAction()

Creates an

Action

.

AbstractAction

```java
public AbstractAction​(
String
name)
```

Creates an

Action

with the specified name.

**Parameters:** name

- the name (

Action.NAME

) for the action; a
value of

null

is ignored

---

#### AbstractAction

public AbstractAction​(

String

name)

Creates an

Action

with the specified name.

AbstractAction

```java
public AbstractAction​(
String
name,

Icon
icon)
```

Creates an

Action

with the specified name and small icon.

**Parameters:** name

- the name (

Action.NAME

) for the action; a
value of

null

is ignored
**Parameters:** icon

- the small icon (

Action.SMALL_ICON

) for the action; a
value of

null

is ignored

---

#### AbstractAction

public AbstractAction​(

String

name,

Icon

icon)

Creates an

Action

with the specified name and small icon.

Method Detail

- getValue

```java
public
Object
getValue​(
String
key)
```

Gets the

Object

associated with the specified key.

**Specified by:** getValue

in interface

Action
**Parameters:** key

- a string containing the specified

key
**Returns:** the binding

Object

stored with this key; if there
are no keys, it will return

null
**See Also:** Action.getValue(java.lang.String)

- putValue

```java
public void putValue​(
String
key,

Object
newValue)
```

Sets the

Value

associated with the specified key.

**Specified by:** putValue

in interface

Action
**Parameters:** key

- the

String

that identifies the stored object
**Parameters:** newValue

- the

Object

to store using this key
**See Also:** Action.putValue(java.lang.String, java.lang.Object)

- isEnabled

```java
public boolean isEnabled()
```

Returns true if the action is enabled.

**Specified by:** isEnabled

in interface

Action
**Returns:** true if the action is enabled, false otherwise
**See Also:** Action.isEnabled()

- setEnabled

```java
public void setEnabled​(boolean newValue)
```

Sets whether the

Action

is enabled. The default is

true

.

**Specified by:** setEnabled

in interface

Action
**Parameters:** newValue

-

true

to enable the action,

false

to
disable it
**See Also:** Action.setEnabled(boolean)

- getKeys

```java
public
Object
[] getKeys()
```

Returns an array of

Object

s which are keys for
which values have been set for this

AbstractAction

,
or

null

if no keys have values set.

**Returns:** an array of key objects, or

null

if no
keys have values set
**Since:** 1.3

- firePropertyChange

```java
protected void firePropertyChange​(
String
propertyName,

Object
oldValue,

Object
newValue)
```

Supports reporting bound property changes. This method can be called
when a bound property has changed and it will send the appropriate

PropertyChangeEvent

to any registered

PropertyChangeListeners

.

**Parameters:** propertyName

- the name of the property that has changed
**Parameters:** oldValue

- the old value of the property
**Parameters:** newValue

- the new value of the property

- addPropertyChangeListener

```java
public void addPropertyChangeListener​(
PropertyChangeListener
listener)
```

Adds a

PropertyChangeListener

to the listener list.
The listener is registered for all properties.

A

PropertyChangeEvent

will get fired in response to setting
a bound property, e.g.

setFont

,

setBackground

,
or

setForeground

.
Note that if the current component is inheriting its foreground,
background, or font from its container, then no event will be
fired in response to a change in the inherited property.

**Specified by:** addPropertyChangeListener

in interface

Action
**Parameters:** listener

- The

PropertyChangeListener

to be added
**See Also:** Action.addPropertyChangeListener(java.beans.PropertyChangeListener)

- removePropertyChangeListener

```java
public void removePropertyChangeListener​(
PropertyChangeListener
listener)
```

Removes a

PropertyChangeListener

from the listener list.
This removes a

PropertyChangeListener

that was registered
for all properties.

**Specified by:** removePropertyChangeListener

in interface

Action
**Parameters:** listener

- the

PropertyChangeListener

to be removed
**See Also:** Action.removePropertyChangeListener(java.beans.PropertyChangeListener)

- getPropertyChangeListeners

```java
public
PropertyChangeListener
[] getPropertyChangeListeners()
```

Returns an array of all the

PropertyChangeListener

s added
to this AbstractAction with addPropertyChangeListener().

**Returns:** all of the

PropertyChangeListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

- clone

```java
protected
Object
clone()
throws
CloneNotSupportedException
```

Clones the abstract action. This gives the clone
its own copy of the key/value list,
which is not handled for you by

Object.clone()

.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**Throws:** CloneNotSupportedException

- if the object's class does not
support the

Cloneable

interface. Subclasses
that override the

clone

method can also
throw this exception to indicate that an instance cannot
be cloned.
**See Also:** Cloneable

---

#### Method Detail

getValue

```java
public
Object
getValue​(
String
key)
```

Gets the

Object

associated with the specified key.

**Specified by:** getValue

in interface

Action
**Parameters:** key

- a string containing the specified

key
**Returns:** the binding

Object

stored with this key; if there
are no keys, it will return

null
**See Also:** Action.getValue(java.lang.String)

---

#### getValue

public

Object

getValue​(

String

key)

Gets the

Object

associated with the specified key.

putValue

```java
public void putValue​(
String
key,

Object
newValue)
```

Sets the

Value

associated with the specified key.

**Specified by:** putValue

in interface

Action
**Parameters:** key

- the

String

that identifies the stored object
**Parameters:** newValue

- the

Object

to store using this key
**See Also:** Action.putValue(java.lang.String, java.lang.Object)

---

#### putValue

public void putValue​(

String

key,

Object

newValue)

Sets the

Value

associated with the specified key.

isEnabled

```java
public boolean isEnabled()
```

Returns true if the action is enabled.

**Specified by:** isEnabled

in interface

Action
**Returns:** true if the action is enabled, false otherwise
**See Also:** Action.isEnabled()

---

#### isEnabled

public boolean isEnabled()

Returns true if the action is enabled.

setEnabled

```java
public void setEnabled​(boolean newValue)
```

Sets whether the

Action

is enabled. The default is

true

.

**Specified by:** setEnabled

in interface

Action
**Parameters:** newValue

-

true

to enable the action,

false

to
disable it
**See Also:** Action.setEnabled(boolean)

---

#### setEnabled

public void setEnabled​(boolean newValue)

Sets whether the

Action

is enabled. The default is

true

.

getKeys

```java
public
Object
[] getKeys()
```

Returns an array of

Object

s which are keys for
which values have been set for this

AbstractAction

,
or

null

if no keys have values set.

**Returns:** an array of key objects, or

null

if no
keys have values set
**Since:** 1.3

---

#### getKeys

public

Object

[] getKeys()

Returns an array of

Object

s which are keys for
which values have been set for this

AbstractAction

,
or

null

if no keys have values set.

firePropertyChange

```java
protected void firePropertyChange​(
String
propertyName,

Object
oldValue,

Object
newValue)
```

Supports reporting bound property changes. This method can be called
when a bound property has changed and it will send the appropriate

PropertyChangeEvent

to any registered

PropertyChangeListeners

.

**Parameters:** propertyName

- the name of the property that has changed
**Parameters:** oldValue

- the old value of the property
**Parameters:** newValue

- the new value of the property

---

#### firePropertyChange

protected void firePropertyChange​(

String

propertyName,

Object

oldValue,

Object

newValue)

Supports reporting bound property changes. This method can be called
when a bound property has changed and it will send the appropriate

PropertyChangeEvent

to any registered

PropertyChangeListeners

.

addPropertyChangeListener

```java
public void addPropertyChangeListener​(
PropertyChangeListener
listener)
```

Adds a

PropertyChangeListener

to the listener list.
The listener is registered for all properties.

A

PropertyChangeEvent

will get fired in response to setting
a bound property, e.g.

setFont

,

setBackground

,
or

setForeground

.
Note that if the current component is inheriting its foreground,
background, or font from its container, then no event will be
fired in response to a change in the inherited property.

**Specified by:** addPropertyChangeListener

in interface

Action
**Parameters:** listener

- The

PropertyChangeListener

to be added
**See Also:** Action.addPropertyChangeListener(java.beans.PropertyChangeListener)

---

#### addPropertyChangeListener

public void addPropertyChangeListener​(

PropertyChangeListener

listener)

Adds a

PropertyChangeListener

to the listener list.
The listener is registered for all properties.

A

PropertyChangeEvent

will get fired in response to setting
a bound property, e.g.

setFont

,

setBackground

,
or

setForeground

.
Note that if the current component is inheriting its foreground,
background, or font from its container, then no event will be
fired in response to a change in the inherited property.

A

PropertyChangeEvent

will get fired in response to setting
a bound property, e.g.

setFont

,

setBackground

,
or

setForeground

.
Note that if the current component is inheriting its foreground,
background, or font from its container, then no event will be
fired in response to a change in the inherited property.

removePropertyChangeListener

```java
public void removePropertyChangeListener​(
PropertyChangeListener
listener)
```

Removes a

PropertyChangeListener

from the listener list.
This removes a

PropertyChangeListener

that was registered
for all properties.

**Specified by:** removePropertyChangeListener

in interface

Action
**Parameters:** listener

- the

PropertyChangeListener

to be removed
**See Also:** Action.removePropertyChangeListener(java.beans.PropertyChangeListener)

---

#### removePropertyChangeListener

public void removePropertyChangeListener​(

PropertyChangeListener

listener)

Removes a

PropertyChangeListener

from the listener list.
This removes a

PropertyChangeListener

that was registered
for all properties.

getPropertyChangeListeners

```java
public
PropertyChangeListener
[] getPropertyChangeListeners()
```

Returns an array of all the

PropertyChangeListener

s added
to this AbstractAction with addPropertyChangeListener().

**Returns:** all of the

PropertyChangeListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

---

#### getPropertyChangeListeners

public

PropertyChangeListener

[] getPropertyChangeListeners()

Returns an array of all the

PropertyChangeListener

s added
to this AbstractAction with addPropertyChangeListener().

clone

```java
protected
Object
clone()
throws
CloneNotSupportedException
```

Clones the abstract action. This gives the clone
its own copy of the key/value list,
which is not handled for you by

Object.clone()

.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**Throws:** CloneNotSupportedException

- if the object's class does not
support the

Cloneable

interface. Subclasses
that override the

clone

method can also
throw this exception to indicate that an instance cannot
be cloned.
**See Also:** Cloneable

---

#### clone

protected

Object

clone()
throws

CloneNotSupportedException

Clones the abstract action. This gives the clone
its own copy of the key/value list,
which is not handled for you by

Object.clone()

.

---

