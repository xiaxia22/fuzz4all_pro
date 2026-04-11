# Class StyledEditorKit.ForegroundAction

**Source:** `java.desktop\javax\swing\text\StyledEditorKit.ForegroundAction.html`

### Class Description

```java
public static class
StyledEditorKit.ForegroundAction

extends
StyledEditorKit.StyledTextAction
```

An action to set foreground color. This sets the

StyleConstants.Foreground

attribute for the
currently selected range of the target JEditorPane.
This is done by calling

StyledDocument.setCharacterAttributes

on the styled document associated with the target
JEditorPane.

If the target text component is specified as the
source of the ActionEvent and there is a command string,
the command string will be interpreted as the foreground
color. It will be interpreted by called

Color.decode

, and should therefore be
legal input for that method.

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

#### public ForegroundAction​(
String
nm,

Color
fg)

Creates a new ForegroundAction.

**Parameters:**
- nm

- the action name
- fg

- the foreground color

---

### Method Details

#### public void actionPerformed​(
ActionEvent
e)

Sets the foreground color.

**Parameters:**
- e

- the action event

---

### Additional Sections

#### Class StyledEditorKit.ForegroundAction

java.lang.Object

- javax.swing.AbstractAction
- - javax.swing.text.TextAction
- - javax.swing.text.StyledEditorKit.StyledTextAction
- - javax.swing.text.StyledEditorKit.ForegroundAction

javax.swing.AbstractAction

- javax.swing.text.TextAction
- - javax.swing.text.StyledEditorKit.StyledTextAction
- - javax.swing.text.StyledEditorKit.ForegroundAction

javax.swing.text.TextAction

- javax.swing.text.StyledEditorKit.StyledTextAction
- - javax.swing.text.StyledEditorKit.ForegroundAction

javax.swing.text.StyledEditorKit.StyledTextAction

- javax.swing.text.StyledEditorKit.ForegroundAction

javax.swing.text.StyledEditorKit.ForegroundAction

**All Implemented Interfaces:** ActionListener

,

Serializable

,

Cloneable

,

EventListener

,

Action

**Enclosing class:** StyledEditorKit

```java
public static class
StyledEditorKit.ForegroundAction

extends
StyledEditorKit.StyledTextAction
```

An action to set foreground color. This sets the

StyleConstants.Foreground

attribute for the
currently selected range of the target JEditorPane.
This is done by calling

StyledDocument.setCharacterAttributes

on the styled document associated with the target
JEditorPane.

If the target text component is specified as the
source of the ActionEvent and there is a command string,
the command string will be interpreted as the foreground
color. It will be interpreted by called

Color.decode

, and should therefore be
legal input for that method.

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

public static class

StyledEditorKit.ForegroundAction

extends

StyledEditorKit.StyledTextAction

An action to set foreground color. This sets the

StyleConstants.Foreground

attribute for the
currently selected range of the target JEditorPane.
This is done by calling

StyledDocument.setCharacterAttributes

on the styled document associated with the target
JEditorPane.

If the target text component is specified as the
source of the ActionEvent and there is a command string,
the command string will be interpreted as the foreground
color. It will be interpreted by called

Color.decode

, and should therefore be
legal input for that method.

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

If the target text component is specified as the
source of the ActionEvent and there is a command string,
the command string will be interpreted as the foreground
color. It will be interpreted by called

Color.decode

, and should therefore be
legal input for that method.

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

ForegroundAction

​(

String

nm,

Color

fg)

Creates a new ForegroundAction.

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

Sets the foreground color.

- Methods declared in class javax.swing.text.

StyledEditorKit.StyledTextAction

getEditor

,

getStyledDocument

,

getStyledEditorKit

,

setCharacterAttributes

,

setParagraphAttributes

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

ForegroundAction

​(

String

nm,

Color

fg)

Creates a new ForegroundAction.

---

#### Constructor Summary

Creates a new ForegroundAction.

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

Sets the foreground color.

- Methods declared in class javax.swing.text.

StyledEditorKit.StyledTextAction

getEditor

,

getStyledDocument

,

getStyledEditorKit

,

setCharacterAttributes

,

setParagraphAttributes

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

Sets the foreground color.

Methods declared in class javax.swing.text.

StyledEditorKit.StyledTextAction

getEditor

,

getStyledDocument

,

getStyledEditorKit

,

setCharacterAttributes

,

setParagraphAttributes

---

#### Methods declared in class javax.swing.text. StyledEditorKit.StyledTextAction

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

- ForegroundAction

```java
public ForegroundAction​(
String
nm,

Color
fg)
```

Creates a new ForegroundAction.

**Parameters:** nm

- the action name
**Parameters:** fg

- the foreground color

============ METHOD DETAIL ==========

- Method Detail

- actionPerformed

```java
public void actionPerformed​(
ActionEvent
e)
```

Sets the foreground color.

**Parameters:** e

- the action event

Constructor Detail

- ForegroundAction

```java
public ForegroundAction​(
String
nm,

Color
fg)
```

Creates a new ForegroundAction.

**Parameters:** nm

- the action name
**Parameters:** fg

- the foreground color

---

#### Constructor Detail

ForegroundAction

```java
public ForegroundAction​(
String
nm,

Color
fg)
```

Creates a new ForegroundAction.

**Parameters:** nm

- the action name
**Parameters:** fg

- the foreground color

---

#### ForegroundAction

public ForegroundAction​(

String

nm,

Color

fg)

Creates a new ForegroundAction.

Method Detail

- actionPerformed

```java
public void actionPerformed​(
ActionEvent
e)
```

Sets the foreground color.

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

Sets the foreground color.

**Parameters:** e

- the action event

---

#### actionPerformed

public void actionPerformed​(

ActionEvent

e)

Sets the foreground color.

---

