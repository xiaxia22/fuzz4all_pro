# Class DefaultEditorKit.InsertBreakAction

**Source:** `java.desktop\javax\swing\text\DefaultEditorKit.InsertBreakAction.html`

### Class Description

```java
public static class
DefaultEditorKit.InsertBreakAction

extends
TextAction
```

Places a line/paragraph break into the document.
If there is a selection, it is removed before
the break is added.

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

#### public InsertBreakAction()

Creates this object with the appropriate identifier.

---

### Method Details

#### public void actionPerformed​(
ActionEvent
e)

The operation to perform when this action is triggered.

**Parameters:**
- e

- the action event

---

### Additional Sections

#### Class DefaultEditorKit.InsertBreakAction

java.lang.Object

- javax.swing.AbstractAction
- - javax.swing.text.TextAction
- - javax.swing.text.DefaultEditorKit.InsertBreakAction

javax.swing.AbstractAction

- javax.swing.text.TextAction
- - javax.swing.text.DefaultEditorKit.InsertBreakAction

javax.swing.text.TextAction

- javax.swing.text.DefaultEditorKit.InsertBreakAction

javax.swing.text.DefaultEditorKit.InsertBreakAction

**All Implemented Interfaces:** ActionListener

,

Serializable

,

Cloneable

,

EventListener

,

Action

**Enclosing class:** DefaultEditorKit

```java
public static class
DefaultEditorKit.InsertBreakAction

extends
TextAction
```

Places a line/paragraph break into the document.
If there is a selection, it is removed before
the break is added.

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

**See Also:** DefaultEditorKit.insertBreakAction

,

DefaultEditorKit.getActions()

,

Serialized Form

public static class

DefaultEditorKit.InsertBreakAction

extends

TextAction

Places a line/paragraph break into the document.
If there is a selection, it is removed before
the break is added.

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

InsertBreakAction

()

Creates this object with the appropriate identifier.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

actionPerformed

​(

ActionEvent

e)

The operation to perform when this action is triggered.

- Methods declared in class javax.swing.text.

TextAction

augmentList

,

getFocusedComponent

,

getTextComponent

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

InsertBreakAction

()

Creates this object with the appropriate identifier.

---

#### Constructor Summary

Creates this object with the appropriate identifier.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

actionPerformed

​(

ActionEvent

e)

The operation to perform when this action is triggered.

- Methods declared in class javax.swing.text.

TextAction

augmentList

,

getFocusedComponent

,

getTextComponent

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

---

#### Method Summary

The operation to perform when this action is triggered.

Methods declared in class javax.swing.text.

TextAction

augmentList

,

getFocusedComponent

,

getTextComponent

---

#### Methods declared in class javax.swing.text. TextAction

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- InsertBreakAction

```java
public InsertBreakAction()
```

Creates this object with the appropriate identifier.

============ METHOD DETAIL ==========

- Method Detail

- actionPerformed

```java
public void actionPerformed​(
ActionEvent
e)
```

The operation to perform when this action is triggered.

**Parameters:** e

- the action event

Constructor Detail

- InsertBreakAction

```java
public InsertBreakAction()
```

Creates this object with the appropriate identifier.

---

#### Constructor Detail

InsertBreakAction

```java
public InsertBreakAction()
```

Creates this object with the appropriate identifier.

---

#### InsertBreakAction

public InsertBreakAction()

Creates this object with the appropriate identifier.

Method Detail

- actionPerformed

```java
public void actionPerformed​(
ActionEvent
e)
```

The operation to perform when this action is triggered.

**Parameters:** e

- the action event

---

#### Method Detail

actionPerformed

```java
public void actionPerformed​(
ActionEvent
e)
```

The operation to perform when this action is triggered.

**Parameters:** e

- the action event

---

#### actionPerformed

public void actionPerformed​(

ActionEvent

e)

The operation to perform when this action is triggered.

---

