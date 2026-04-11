# Class HTMLEditorKit.HTMLTextAction

**Source:** `java.desktop\javax\swing\text\html\HTMLEditorKit.HTMLTextAction.html`

### Class Description

```java
public abstract static class
HTMLEditorKit.HTMLTextAction

extends
StyledEditorKit.StyledTextAction
```

An abstract Action providing some convenience methods that may
be useful in inserting HTML into an existing document.

NOTE: None of the convenience methods obtain a lock on the
document. If you have another thread modifying the text these
methods may have inconsistent behavior, or return the wrong thing.

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

#### public HTMLTextAction​(
String
name)

Creates a new HTMLTextAction from a string action name.

**Parameters:**
- name

- the name of the action

---

### Method Details

#### protected
HTMLDocument
getHTMLDocument​(
JEditorPane
e)

**Parameters:**
- e

- the JEditorPane

**Returns:**
- HTMLDocument of

e

.

---

#### protected
HTMLEditorKit
getHTMLEditorKit​(
JEditorPane
e)

**Parameters:**
- e

- the JEditorPane

**Returns:**
- HTMLEditorKit for

e

.

---

#### protected
Element
[] getElementsAt​(
HTMLDocument
doc,
int offset)

Returns an array of the Elements that contain

offset

.
The first elements corresponds to the root.

**Parameters:**
- doc

- an instance of HTMLDocument
- offset

- value of offset

**Returns:**
- an array of the Elements that contain

offset

---

#### protected int elementCountToTag​(
HTMLDocument
doc,
int offset,

HTML.Tag
tag)

Returns number of elements, starting at the deepest leaf, needed
to get to an element representing

tag

. This will
return -1 if no elements is found representing

tag

,
or 0 if the parent of the leaf at

offset

represents

tag

.

**Parameters:**
- doc

- an instance of HTMLDocument
- offset

- an offset to start from
- tag

- tag to represent

**Returns:**
- number of elements

---

#### protected
Element
findElementMatchingTag​(
HTMLDocument
doc,
int offset,

HTML.Tag
tag)

Returns the deepest element at

offset

matching

tag

.

**Parameters:**
- doc

- an instance of HTMLDocument
- offset

- the specified offset >= 0
- tag

- an instance of HTML.Tag

**Returns:**
- the deepest element

---

### Additional Sections

#### Class HTMLEditorKit.HTMLTextAction

java.lang.Object

- javax.swing.AbstractAction
- - javax.swing.text.TextAction
- - javax.swing.text.StyledEditorKit.StyledTextAction
- - javax.swing.text.html.HTMLEditorKit.HTMLTextAction

javax.swing.AbstractAction

- javax.swing.text.TextAction
- - javax.swing.text.StyledEditorKit.StyledTextAction
- - javax.swing.text.html.HTMLEditorKit.HTMLTextAction

javax.swing.text.TextAction

- javax.swing.text.StyledEditorKit.StyledTextAction
- - javax.swing.text.html.HTMLEditorKit.HTMLTextAction

javax.swing.text.StyledEditorKit.StyledTextAction

- javax.swing.text.html.HTMLEditorKit.HTMLTextAction

javax.swing.text.html.HTMLEditorKit.HTMLTextAction

**All Implemented Interfaces:** ActionListener

,

Serializable

,

Cloneable

,

EventListener

,

Action

**Direct Known Subclasses:** HTMLEditorKit.InsertHTMLTextAction

**Enclosing class:** HTMLEditorKit

```java
public abstract static class
HTMLEditorKit.HTMLTextAction

extends
StyledEditorKit.StyledTextAction
```

An abstract Action providing some convenience methods that may
be useful in inserting HTML into an existing document.

NOTE: None of the convenience methods obtain a lock on the
document. If you have another thread modifying the text these
methods may have inconsistent behavior, or return the wrong thing.

**See Also:** Serialized Form

public abstract static class

HTMLEditorKit.HTMLTextAction

extends

StyledEditorKit.StyledTextAction

An abstract Action providing some convenience methods that may
be useful in inserting HTML into an existing document.

NOTE: None of the convenience methods obtain a lock on the
document. If you have another thread modifying the text these
methods may have inconsistent behavior, or return the wrong thing.

NOTE: None of the convenience methods obtain a lock on the
document. If you have another thread modifying the text these
methods may have inconsistent behavior, or return the wrong thing.

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

HTMLTextAction

​(

String

name)

Creates a new HTMLTextAction from a string action name.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected int

elementCountToTag

​(

HTMLDocument

doc,
int offset,

HTML.Tag

tag)

Returns number of elements, starting at the deepest leaf, needed
to get to an element representing

tag

.

protected

Element

findElementMatchingTag

​(

HTMLDocument

doc,
int offset,

HTML.Tag

tag)

Returns the deepest element at

offset

matching

tag

.

protected

Element

[]

getElementsAt

​(

HTMLDocument

doc,
int offset)

Returns an array of the Elements that contain

offset

.

protected

HTMLDocument

getHTMLDocument

​(

JEditorPane

e)

protected

HTMLEditorKit

getHTMLEditorKit

​(

JEditorPane

e)

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

HTMLTextAction

​(

String

name)

Creates a new HTMLTextAction from a string action name.

---

#### Constructor Summary

Creates a new HTMLTextAction from a string action name.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected int

elementCountToTag

​(

HTMLDocument

doc,
int offset,

HTML.Tag

tag)

Returns number of elements, starting at the deepest leaf, needed
to get to an element representing

tag

.

protected

Element

findElementMatchingTag

​(

HTMLDocument

doc,
int offset,

HTML.Tag

tag)

Returns the deepest element at

offset

matching

tag

.

protected

Element

[]

getElementsAt

​(

HTMLDocument

doc,
int offset)

Returns an array of the Elements that contain

offset

.

protected

HTMLDocument

getHTMLDocument

​(

JEditorPane

e)

protected

HTMLEditorKit

getHTMLEditorKit

​(

JEditorPane

e)

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

- Methods declared in interface java.awt.event.

ActionListener

actionPerformed

---

#### Method Summary

Returns number of elements, starting at the deepest leaf, needed
to get to an element representing

tag

.

Returns the deepest element at

offset

matching

tag

.

Returns an array of the Elements that contain

offset

.

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

Methods declared in interface java.awt.event.

ActionListener

actionPerformed

---

#### Methods declared in interface java.awt.event. ActionListener

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- HTMLTextAction

```java
public HTMLTextAction​(
String
name)
```

Creates a new HTMLTextAction from a string action name.

**Parameters:** name

- the name of the action

============ METHOD DETAIL ==========

- Method Detail

- getHTMLDocument

```java
protected
HTMLDocument
getHTMLDocument​(
JEditorPane
e)
```

**Parameters:** e

- the JEditorPane
**Returns:** HTMLDocument of

e

.

- getHTMLEditorKit

```java
protected
HTMLEditorKit
getHTMLEditorKit​(
JEditorPane
e)
```

**Parameters:** e

- the JEditorPane
**Returns:** HTMLEditorKit for

e

.

- getElementsAt

```java
protected
Element
[] getElementsAt​(
HTMLDocument
doc,
int offset)
```

Returns an array of the Elements that contain

offset

.
The first elements corresponds to the root.

**Parameters:** doc

- an instance of HTMLDocument
**Parameters:** offset

- value of offset
**Returns:** an array of the Elements that contain

offset

- elementCountToTag

```java
protected int elementCountToTag​(
HTMLDocument
doc,
int offset,

HTML.Tag
tag)
```

Returns number of elements, starting at the deepest leaf, needed
to get to an element representing

tag

. This will
return -1 if no elements is found representing

tag

,
or 0 if the parent of the leaf at

offset

represents

tag

.

**Parameters:** doc

- an instance of HTMLDocument
**Parameters:** offset

- an offset to start from
**Parameters:** tag

- tag to represent
**Returns:** number of elements

- findElementMatchingTag

```java
protected
Element
findElementMatchingTag​(
HTMLDocument
doc,
int offset,

HTML.Tag
tag)
```

Returns the deepest element at

offset

matching

tag

.

**Parameters:** doc

- an instance of HTMLDocument
**Parameters:** offset

- the specified offset >= 0
**Parameters:** tag

- an instance of HTML.Tag
**Returns:** the deepest element

Constructor Detail

- HTMLTextAction

```java
public HTMLTextAction​(
String
name)
```

Creates a new HTMLTextAction from a string action name.

**Parameters:** name

- the name of the action

---

#### Constructor Detail

HTMLTextAction

```java
public HTMLTextAction​(
String
name)
```

Creates a new HTMLTextAction from a string action name.

**Parameters:** name

- the name of the action

---

#### HTMLTextAction

public HTMLTextAction​(

String

name)

Creates a new HTMLTextAction from a string action name.

Method Detail

- getHTMLDocument

```java
protected
HTMLDocument
getHTMLDocument​(
JEditorPane
e)
```

**Parameters:** e

- the JEditorPane
**Returns:** HTMLDocument of

e

.

- getHTMLEditorKit

```java
protected
HTMLEditorKit
getHTMLEditorKit​(
JEditorPane
e)
```

**Parameters:** e

- the JEditorPane
**Returns:** HTMLEditorKit for

e

.

- getElementsAt

```java
protected
Element
[] getElementsAt​(
HTMLDocument
doc,
int offset)
```

Returns an array of the Elements that contain

offset

.
The first elements corresponds to the root.

**Parameters:** doc

- an instance of HTMLDocument
**Parameters:** offset

- value of offset
**Returns:** an array of the Elements that contain

offset

- elementCountToTag

```java
protected int elementCountToTag​(
HTMLDocument
doc,
int offset,

HTML.Tag
tag)
```

Returns number of elements, starting at the deepest leaf, needed
to get to an element representing

tag

. This will
return -1 if no elements is found representing

tag

,
or 0 if the parent of the leaf at

offset

represents

tag

.

**Parameters:** doc

- an instance of HTMLDocument
**Parameters:** offset

- an offset to start from
**Parameters:** tag

- tag to represent
**Returns:** number of elements

- findElementMatchingTag

```java
protected
Element
findElementMatchingTag​(
HTMLDocument
doc,
int offset,

HTML.Tag
tag)
```

Returns the deepest element at

offset

matching

tag

.

**Parameters:** doc

- an instance of HTMLDocument
**Parameters:** offset

- the specified offset >= 0
**Parameters:** tag

- an instance of HTML.Tag
**Returns:** the deepest element

---

#### Method Detail

getHTMLDocument

```java
protected
HTMLDocument
getHTMLDocument​(
JEditorPane
e)
```

**Parameters:** e

- the JEditorPane
**Returns:** HTMLDocument of

e

.

---

#### getHTMLDocument

protected

HTMLDocument

getHTMLDocument​(

JEditorPane

e)

getHTMLEditorKit

```java
protected
HTMLEditorKit
getHTMLEditorKit​(
JEditorPane
e)
```

**Parameters:** e

- the JEditorPane
**Returns:** HTMLEditorKit for

e

.

---

#### getHTMLEditorKit

protected

HTMLEditorKit

getHTMLEditorKit​(

JEditorPane

e)

getElementsAt

```java
protected
Element
[] getElementsAt​(
HTMLDocument
doc,
int offset)
```

Returns an array of the Elements that contain

offset

.
The first elements corresponds to the root.

**Parameters:** doc

- an instance of HTMLDocument
**Parameters:** offset

- value of offset
**Returns:** an array of the Elements that contain

offset

---

#### getElementsAt

protected

Element

[] getElementsAt​(

HTMLDocument

doc,
int offset)

Returns an array of the Elements that contain

offset

.
The first elements corresponds to the root.

elementCountToTag

```java
protected int elementCountToTag​(
HTMLDocument
doc,
int offset,

HTML.Tag
tag)
```

Returns number of elements, starting at the deepest leaf, needed
to get to an element representing

tag

. This will
return -1 if no elements is found representing

tag

,
or 0 if the parent of the leaf at

offset

represents

tag

.

**Parameters:** doc

- an instance of HTMLDocument
**Parameters:** offset

- an offset to start from
**Parameters:** tag

- tag to represent
**Returns:** number of elements

---

#### elementCountToTag

protected int elementCountToTag​(

HTMLDocument

doc,
int offset,

HTML.Tag

tag)

Returns number of elements, starting at the deepest leaf, needed
to get to an element representing

tag

. This will
return -1 if no elements is found representing

tag

,
or 0 if the parent of the leaf at

offset

represents

tag

.

findElementMatchingTag

```java
protected
Element
findElementMatchingTag​(
HTMLDocument
doc,
int offset,

HTML.Tag
tag)
```

Returns the deepest element at

offset

matching

tag

.

**Parameters:** doc

- an instance of HTMLDocument
**Parameters:** offset

- the specified offset >= 0
**Parameters:** tag

- an instance of HTML.Tag
**Returns:** the deepest element

---

#### findElementMatchingTag

protected

Element

findElementMatchingTag​(

HTMLDocument

doc,
int offset,

HTML.Tag

tag)

Returns the deepest element at

offset

matching

tag

.

---

