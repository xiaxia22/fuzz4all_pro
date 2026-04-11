# Class TextAction

**Source:** `java.desktop\javax\swing\text\TextAction.html`

### Class Description

```java
public abstract class
TextAction

extends
AbstractAction
```

An Action implementation useful for key bindings that are
shared across a number of different text components. Because
the action is shared, it must have a way of getting it's
target to act upon. This class provides support to try and
find a text component to operate on. The preferred way of
getting the component to act upon is through the ActionEvent
that is received. If the Object returned by getSource can
be narrowed to a text component, it will be used. If the
action event is null or can't be narrowed, the last focused
text component is tried. This is determined by being
used in conjunction with a JTextController which
arranges to share that information with a TextAction.

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

*No entries found.*

### Constructor Details

#### public TextAction​(
String
name)

Creates a new JTextAction object.

**Parameters:**
- name

- the name of the action

---

### Method Details

#### protected final
JTextComponent
getTextComponent​(
ActionEvent
e)

Determines the component to use for the action.
This if fetched from the source of the ActionEvent
if it's not null and can be narrowed. Otherwise,
the last focused component is used.

**Parameters:**
- e

- the ActionEvent

**Returns:**
- the component

---

#### public static final
Action
[] augmentList​(
Action
[] list1,

Action
[] list2)

Takes one list of
commands and augments it with another list
of commands. The second list takes precedence
over the first list; that is, when both lists
contain a command with the same name, the command
from the second list is used.

**Parameters:**
- list1

- the first list, may be empty but not

null
- list2

- the second list, may be empty but not

null

**Returns:**
- the augmented list

---

#### protected final
JTextComponent
getFocusedComponent()

Fetches the text component that currently has focus.
This allows actions to be shared across text components
which is useful for key-bindings where a large set of
actions are defined, but generally used the same way
across many different components.

**Returns:**
- the component

---

### Additional Sections

#### Class TextAction

java.lang.Object

- javax.swing.AbstractAction
- - javax.swing.text.TextAction

javax.swing.AbstractAction

- javax.swing.text.TextAction

javax.swing.text.TextAction

**All Implemented Interfaces:** ActionListener

,

Serializable

,

Cloneable

,

EventListener

,

Action

**Direct Known Subclasses:** DefaultEditorKit.BeepAction

,

DefaultEditorKit.CopyAction

,

DefaultEditorKit.CutAction

,

DefaultEditorKit.DefaultKeyTypedAction

,

DefaultEditorKit.InsertBreakAction

,

DefaultEditorKit.InsertContentAction

,

DefaultEditorKit.InsertTabAction

,

DefaultEditorKit.PasteAction

,

StyledEditorKit.StyledTextAction

```java
public abstract class
TextAction

extends
AbstractAction
```

An Action implementation useful for key bindings that are
shared across a number of different text components. Because
the action is shared, it must have a way of getting it's
target to act upon. This class provides support to try and
find a text component to operate on. The preferred way of
getting the component to act upon is through the ActionEvent
that is received. If the Object returned by getSource can
be narrowed to a text component, it will be used. If the
action event is null or can't be narrowed, the last focused
text component is tried. This is determined by being
used in conjunction with a JTextController which
arranges to share that information with a TextAction.

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

**See Also:** Serialized Form

public abstract class

TextAction

extends

AbstractAction

An Action implementation useful for key bindings that are
shared across a number of different text components. Because
the action is shared, it must have a way of getting it's
target to act upon. This class provides support to try and
find a text component to operate on. The preferred way of
getting the component to act upon is through the ActionEvent
that is received. If the Object returned by getSource can
be narrowed to a text component, it will be used. If the
action event is null or can't be narrowed, the last focused
text component is tried. This is determined by being
used in conjunction with a JTextController which
arranges to share that information with a TextAction.

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

- Fields declared in class javax.swing.

AbstractAction

changeSupport

,

enabled

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

TextAction

​(

String

name)

Creates a new JTextAction object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

Action

[]

augmentList

​(

Action

[] list1,

Action

[] list2)

Takes one list of
commands and augments it with another list
of commands.

protected

JTextComponent

getFocusedComponent

()

Fetches the text component that currently has focus.

protected

JTextComponent

getTextComponent

​(

ActionEvent

e)

Determines the component to use for the action.

- Methods declared in class javax.swing.

AbstractAction

addPropertyChangeListener

,

clone

,

firePropertyChange

,

getKeys

,

getPropertyChangeListeners

,

getValue

,

isEnabled

,

putValue

,

removePropertyChangeListener

,

setEnabled

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

- Fields declared in class javax.swing.

AbstractAction

changeSupport

,

enabled

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

Fields declared in class javax.swing.

AbstractAction

changeSupport

,

enabled

---

#### Fields declared in class javax.swing. AbstractAction

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

TextAction

​(

String

name)

Creates a new JTextAction object.

---

#### Constructor Summary

Creates a new JTextAction object.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

Action

[]

augmentList

​(

Action

[] list1,

Action

[] list2)

Takes one list of
commands and augments it with another list
of commands.

protected

JTextComponent

getFocusedComponent

()

Fetches the text component that currently has focus.

protected

JTextComponent

getTextComponent

​(

ActionEvent

e)

Determines the component to use for the action.

- Methods declared in class javax.swing.

AbstractAction

addPropertyChangeListener

,

clone

,

firePropertyChange

,

getKeys

,

getPropertyChangeListeners

,

getValue

,

isEnabled

,

putValue

,

removePropertyChangeListener

,

setEnabled

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

Takes one list of
commands and augments it with another list
of commands.

Fetches the text component that currently has focus.

Determines the component to use for the action.

Methods declared in class javax.swing.

AbstractAction

addPropertyChangeListener

,

clone

,

firePropertyChange

,

getKeys

,

getPropertyChangeListeners

,

getValue

,

isEnabled

,

putValue

,

removePropertyChangeListener

,

setEnabled

---

#### Methods declared in class javax.swing. AbstractAction

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- TextAction

```java
public TextAction​(
String
name)
```

Creates a new JTextAction object.

**Parameters:** name

- the name of the action

============ METHOD DETAIL ==========

- Method Detail

- getTextComponent

```java
protected final
JTextComponent
getTextComponent​(
ActionEvent
e)
```

Determines the component to use for the action.
This if fetched from the source of the ActionEvent
if it's not null and can be narrowed. Otherwise,
the last focused component is used.

**Parameters:** e

- the ActionEvent
**Returns:** the component

- augmentList

```java
public static final
Action
[] augmentList​(
Action
[] list1,

Action
[] list2)
```

Takes one list of
commands and augments it with another list
of commands. The second list takes precedence
over the first list; that is, when both lists
contain a command with the same name, the command
from the second list is used.

**Parameters:** list1

- the first list, may be empty but not

null
**Parameters:** list2

- the second list, may be empty but not

null
**Returns:** the augmented list

- getFocusedComponent

```java
protected final
JTextComponent
getFocusedComponent()
```

Fetches the text component that currently has focus.
This allows actions to be shared across text components
which is useful for key-bindings where a large set of
actions are defined, but generally used the same way
across many different components.

**Returns:** the component

Constructor Detail

- TextAction

```java
public TextAction​(
String
name)
```

Creates a new JTextAction object.

**Parameters:** name

- the name of the action

---

#### Constructor Detail

TextAction

```java
public TextAction​(
String
name)
```

Creates a new JTextAction object.

**Parameters:** name

- the name of the action

---

#### TextAction

public TextAction​(

String

name)

Creates a new JTextAction object.

Method Detail

- getTextComponent

```java
protected final
JTextComponent
getTextComponent​(
ActionEvent
e)
```

Determines the component to use for the action.
This if fetched from the source of the ActionEvent
if it's not null and can be narrowed. Otherwise,
the last focused component is used.

**Parameters:** e

- the ActionEvent
**Returns:** the component

- augmentList

```java
public static final
Action
[] augmentList​(
Action
[] list1,

Action
[] list2)
```

Takes one list of
commands and augments it with another list
of commands. The second list takes precedence
over the first list; that is, when both lists
contain a command with the same name, the command
from the second list is used.

**Parameters:** list1

- the first list, may be empty but not

null
**Parameters:** list2

- the second list, may be empty but not

null
**Returns:** the augmented list

- getFocusedComponent

```java
protected final
JTextComponent
getFocusedComponent()
```

Fetches the text component that currently has focus.
This allows actions to be shared across text components
which is useful for key-bindings where a large set of
actions are defined, but generally used the same way
across many different components.

**Returns:** the component

---

#### Method Detail

getTextComponent

```java
protected final
JTextComponent
getTextComponent​(
ActionEvent
e)
```

Determines the component to use for the action.
This if fetched from the source of the ActionEvent
if it's not null and can be narrowed. Otherwise,
the last focused component is used.

**Parameters:** e

- the ActionEvent
**Returns:** the component

---

#### getTextComponent

protected final

JTextComponent

getTextComponent​(

ActionEvent

e)

Determines the component to use for the action.
This if fetched from the source of the ActionEvent
if it's not null and can be narrowed. Otherwise,
the last focused component is used.

augmentList

```java
public static final
Action
[] augmentList​(
Action
[] list1,

Action
[] list2)
```

Takes one list of
commands and augments it with another list
of commands. The second list takes precedence
over the first list; that is, when both lists
contain a command with the same name, the command
from the second list is used.

**Parameters:** list1

- the first list, may be empty but not

null
**Parameters:** list2

- the second list, may be empty but not

null
**Returns:** the augmented list

---

#### augmentList

public static final

Action

[] augmentList​(

Action

[] list1,

Action

[] list2)

Takes one list of
commands and augments it with another list
of commands. The second list takes precedence
over the first list; that is, when both lists
contain a command with the same name, the command
from the second list is used.

getFocusedComponent

```java
protected final
JTextComponent
getFocusedComponent()
```

Fetches the text component that currently has focus.
This allows actions to be shared across text components
which is useful for key-bindings where a large set of
actions are defined, but generally used the same way
across many different components.

**Returns:** the component

---

#### getFocusedComponent

protected final

JTextComponent

getFocusedComponent()

Fetches the text component that currently has focus.
This allows actions to be shared across text components
which is useful for key-bindings where a large set of
actions are defined, but generally used the same way
across many different components.

---

