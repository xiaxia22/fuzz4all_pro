# Class AccessibleState

**Source:** `java.desktop\javax\accessibility\AccessibleState.html`

### Class Description

```java
public class
AccessibleState

extends
AccessibleBundle
```

Class

AccessibleState

describes a component's particular state. The
actual state of the component is defined as an

AccessibleStateSet

,
which is a composed set of

AccessibleStates

.

The

AccessibleBundle.toDisplayString()

method allows you to obtain the localized
string for a locale independent key from a predefined

ResourceBundle

for the keys defined in this class.

The constants in this class present a strongly typed enumeration of common
object roles. A public constructor for this class has been purposely omitted
and applications should use one of the constants from this class. If the
constants in this class are not sufficient to describe the role of an object,
a subclass should be generated from this class and it should provide
constants in a similar manner.

---

### Field Details

#### public static final
AccessibleState
ACTIVE

Indicates a window is currently the active window. This includes windows,
dialogs, frames, etc. In addition, this state is used to indicate the
currently active child of a component such as a list, table, or tree. For
example, the active child of a list is the child that is drawn with a
rectangle around it.

**See Also:**
- AccessibleRole.WINDOW

,

AccessibleRole.FRAME

,

AccessibleRole.DIALOG

---

#### public static final
AccessibleState
PRESSED

Indicates this object is currently pressed. This is usually associated
with buttons and indicates the user has pressed a mouse button while the
pointer was over the button and has not yet released the mouse button.

**See Also:**
- AccessibleRole.PUSH_BUTTON

---

#### public static final
AccessibleState
ARMED

Indicates that the object is armed. This is usually used on buttons that
have been pressed but not yet released, and the mouse pointer is still
over the button.

**See Also:**
- AccessibleRole.PUSH_BUTTON

---

#### public static final
AccessibleState
BUSY

Indicates the current object is busy. This is usually used on objects
such as progress bars, sliders, or scroll bars to indicate they are in a
state of transition.

**See Also:**
- AccessibleRole.PROGRESS_BAR

,

AccessibleRole.SCROLL_BAR

,

AccessibleRole.SLIDER

---

#### public static final
AccessibleState
CHECKED

Indicates this object is currently checked. This is usually used on
objects such as toggle buttons, radio buttons, and check boxes.

**See Also:**
- AccessibleRole.TOGGLE_BUTTON

,

AccessibleRole.RADIO_BUTTON

,

AccessibleRole.CHECK_BOX

---

#### public static final
AccessibleState
EDITABLE

Indicates the user can change the contents of this object. This is
usually used primarily for objects that allow the user to enter text.
Other objects, such as scroll bars and sliders, are automatically
editable if they are enabled.

**See Also:**
- ENABLED

---

#### public static final
AccessibleState
EXPANDABLE

Indicates this object allows progressive disclosure of its children. This
is usually used with hierarchical objects such as trees and is often
paired with the

EXPANDED

or

COLLAPSED

states.

**See Also:**
- EXPANDED

,

COLLAPSED

,

AccessibleRole.TREE

---

#### public static final
AccessibleState
COLLAPSED

Indicates this object is collapsed. This is usually paired with the

EXPANDABLE

state and is used on objects that provide progressive
disclosure such as trees.

**See Also:**
- EXPANDABLE

,

EXPANDED

,

AccessibleRole.TREE

---

#### public static final
AccessibleState
EXPANDED

Indicates this object is expanded. This is usually paired with the

EXPANDABLE

state and is used on objects that provide progressive
disclosure such as trees.

**See Also:**
- EXPANDABLE

,

COLLAPSED

,

AccessibleRole.TREE

---

#### public static final
AccessibleState
ENABLED

Indicates this object is enabled. The absence of this state from an
object's state set indicates this object is not enabled. An object that
is not enabled cannot be manipulated by the user. In a graphical display,
it is usually grayed out.

---

#### public static final
AccessibleState
FOCUSABLE

Indicates this object can accept keyboard focus, which means all events
resulting from typing on the keyboard will normally be passed to it when
it has focus.

**See Also:**
- FOCUSED

---

#### public static final
AccessibleState
FOCUSED

Indicates this object currently has the keyboard focus.

**See Also:**
- FOCUSABLE

---

#### public static final
AccessibleState
ICONIFIED

Indicates this object is minimized and is represented only by an icon.
This is usually only associated with frames and internal frames.

**See Also:**
- AccessibleRole.FRAME

,

AccessibleRole.INTERNAL_FRAME

---

#### public static final
AccessibleState
MODAL

Indicates something must be done with this object before the user can
interact with an object in a different window. This is usually associated
only with dialogs.

**See Also:**
- AccessibleRole.DIALOG

---

#### public static final
AccessibleState
OPAQUE

Indicates this object paints every pixel within its rectangular region. A
non-opaque component paints only some of its pixels, allowing the pixels
underneath it to "show through". A component that does not fully paint
its pixels therefore provides a degree of transparency.

**See Also:**
- Accessible.getAccessibleContext()

,

AccessibleContext.getAccessibleComponent()

,

AccessibleComponent.getBounds()

---

#### public static final
AccessibleState
RESIZABLE

Indicates the size of this object is not fixed.

**See Also:**
- Accessible.getAccessibleContext()

,

AccessibleContext.getAccessibleComponent()

,

AccessibleComponent.getSize()

,

AccessibleComponent.setSize(java.awt.Dimension)

---

#### public static final
AccessibleState
MULTISELECTABLE

Indicates this object allows more than one of its children to be selected
at the same time.

**See Also:**
- Accessible.getAccessibleContext()

,

AccessibleContext.getAccessibleSelection()

,

AccessibleSelection

---

#### public static final
AccessibleState
SELECTABLE

Indicates this object is the child of an object that allows its children
to be selected, and that this child is one of those children that can be
selected.

**See Also:**
- SELECTED

,

Accessible.getAccessibleContext()

,

AccessibleContext.getAccessibleSelection()

,

AccessibleSelection

---

#### public static final
AccessibleState
SELECTED

Indicates this object is the child of an object that allows its children
to be selected, and that this child is one of those children that has
been selected.

**See Also:**
- SELECTABLE

,

Accessible.getAccessibleContext()

,

AccessibleContext.getAccessibleSelection()

,

AccessibleSelection

---

#### public static final
AccessibleState
SHOWING

Indicates this object, the object's parent, the object's parent's parent,
and so on, are all visible. Note that this does not necessarily mean the
object is painted on the screen. It might be occluded by some other
showing object.

**See Also:**
- VISIBLE

---

#### public static final
AccessibleState
VISIBLE

Indicates this object is visible. Note: this means that the object
intends to be visible; however, it may not in fact be showing on the
screen because one of the objects that this object is contained by is not
visible.

**See Also:**
- SHOWING

---

#### public static final
AccessibleState
VERTICAL

Indicates the orientation of this object is vertical. This is usually
associated with objects such as scrollbars, sliders, and progress bars.

**See Also:**
- VERTICAL

,

AccessibleRole.SCROLL_BAR

,

AccessibleRole.SLIDER

,

AccessibleRole.PROGRESS_BAR

---

#### public static final
AccessibleState
HORIZONTAL

Indicates the orientation of this object is horizontal. This is usually
associated with objects such as scrollbars, sliders, and progress bars.

**See Also:**
- HORIZONTAL

,

AccessibleRole.SCROLL_BAR

,

AccessibleRole.SLIDER

,

AccessibleRole.PROGRESS_BAR

---

#### public static final
AccessibleState
SINGLE_LINE

Indicates this (text) object can contain only a single line of text.

---

#### public static final
AccessibleState
MULTI_LINE

Indicates this (text) object can contain multiple lines of text.

---

#### public static final
AccessibleState
TRANSIENT

Indicates this object is transient. An assistive technology should not
add a

PropertyChange

listener to an object with transient state,
as that object will never generate any events. Transient objects are
typically created to answer Java Accessibility method queries, but
otherwise do not remain linked to the underlying object (for example,
those objects underneath lists, tables, and trees in Swing, where only
one actual

UI Component

does shared rendering duty for all of the
data objects underneath the actual list/table/tree elements).

**Since:**
- 1.5

---

#### public static final
AccessibleState
MANAGES_DESCENDANTS

Indicates this object is responsible for managing its subcomponents. This
is typically used for trees and tables that have a large number of
subcomponents and where the objects are created only when needed and
otherwise remain virtual. The application should not manage the
subcomponents directly.

**Since:**
- 1.5

---

#### public static final
AccessibleState
INDETERMINATE

Indicates that the object state is indeterminate. An example is selected
text that is partially bold and partially not bold. In this case the
attributes associated with the selected text are indeterminate.

**Since:**
- 1.5

---

#### public static final
AccessibleState
TRUNCATED

A state indicating that text is truncated by a bounding rectangle and
that some of the text is not displayed on the screen. An example is text
in a spreadsheet cell that is truncated by the bounds of the cell.

**Since:**
- 1.5

---

### Constructor Details

#### protected AccessibleState​(
String
key)

Creates a new

AccessibleState

using the given locale independent
key. This should not be a public method. Instead, it is used to create
the constants in this file to make it a strongly typed enumeration.
Subclasses of this class should enforce similar policy.

The key

String

should be a locale independent key for the state.
It is not intended to be used as the actual

String

to display to
the user. To get the localized string, use

AccessibleBundle.toDisplayString()

.

**Parameters:**
- key

- the locale independent name of the state

**See Also:**
- AccessibleBundle.toDisplayString(java.lang.String, java.util.Locale)

---

### Method Details

*No entries found.*

### Additional Sections

#### Class AccessibleState

java.lang.Object

- javax.accessibility.AccessibleBundle
- - javax.accessibility.AccessibleState

javax.accessibility.AccessibleBundle

- javax.accessibility.AccessibleState

javax.accessibility.AccessibleState

```java
public class
AccessibleState

extends
AccessibleBundle
```

Class

AccessibleState

describes a component's particular state. The
actual state of the component is defined as an

AccessibleStateSet

,
which is a composed set of

AccessibleStates

.

The

AccessibleBundle.toDisplayString()

method allows you to obtain the localized
string for a locale independent key from a predefined

ResourceBundle

for the keys defined in this class.

The constants in this class present a strongly typed enumeration of common
object roles. A public constructor for this class has been purposely omitted
and applications should use one of the constants from this class. If the
constants in this class are not sufficient to describe the role of an object,
a subclass should be generated from this class and it should provide
constants in a similar manner.

public class

AccessibleState

extends

AccessibleBundle

Class

AccessibleState

describes a component's particular state. The
actual state of the component is defined as an

AccessibleStateSet

,
which is a composed set of

AccessibleStates

.

The

AccessibleBundle.toDisplayString()

method allows you to obtain the localized
string for a locale independent key from a predefined

ResourceBundle

for the keys defined in this class.

The constants in this class present a strongly typed enumeration of common
object roles. A public constructor for this class has been purposely omitted
and applications should use one of the constants from this class. If the
constants in this class are not sufficient to describe the role of an object,
a subclass should be generated from this class and it should provide
constants in a similar manner.

The

AccessibleBundle.toDisplayString()

method allows you to obtain the localized
string for a locale independent key from a predefined

ResourceBundle

for the keys defined in this class.

The constants in this class present a strongly typed enumeration of common
object roles. A public constructor for this class has been purposely omitted
and applications should use one of the constants from this class. If the
constants in this class are not sufficient to describe the role of an object,
a subclass should be generated from this class and it should provide
constants in a similar manner.

The constants in this class present a strongly typed enumeration of common
object roles. A public constructor for this class has been purposely omitted
and applications should use one of the constants from this class. If the
constants in this class are not sufficient to describe the role of an object,
a subclass should be generated from this class and it should provide
constants in a similar manner.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

AccessibleState

ACTIVE

Indicates a window is currently the active window.

static

AccessibleState

ARMED

Indicates that the object is armed.

static

AccessibleState

BUSY

Indicates the current object is busy.

static

AccessibleState

CHECKED

Indicates this object is currently checked.

static

AccessibleState

COLLAPSED

Indicates this object is collapsed.

static

AccessibleState

EDITABLE

Indicates the user can change the contents of this object.

static

AccessibleState

ENABLED

Indicates this object is enabled.

static

AccessibleState

EXPANDABLE

Indicates this object allows progressive disclosure of its children.

static

AccessibleState

EXPANDED

Indicates this object is expanded.

static

AccessibleState

FOCUSABLE

Indicates this object can accept keyboard focus, which means all events
resulting from typing on the keyboard will normally be passed to it when
it has focus.

static

AccessibleState

FOCUSED

Indicates this object currently has the keyboard focus.

static

AccessibleState

HORIZONTAL

Indicates the orientation of this object is horizontal.

static

AccessibleState

ICONIFIED

Indicates this object is minimized and is represented only by an icon.

static

AccessibleState

INDETERMINATE

Indicates that the object state is indeterminate.

static

AccessibleState

MANAGES_DESCENDANTS

Indicates this object is responsible for managing its subcomponents.

static

AccessibleState

MODAL

Indicates something must be done with this object before the user can
interact with an object in a different window.

static

AccessibleState

MULTI_LINE

Indicates this (text) object can contain multiple lines of text.

static

AccessibleState

MULTISELECTABLE

Indicates this object allows more than one of its children to be selected
at the same time.

static

AccessibleState

OPAQUE

Indicates this object paints every pixel within its rectangular region.

static

AccessibleState

PRESSED

Indicates this object is currently pressed.

static

AccessibleState

RESIZABLE

Indicates the size of this object is not fixed.

static

AccessibleState

SELECTABLE

Indicates this object is the child of an object that allows its children
to be selected, and that this child is one of those children that can be
selected.

static

AccessibleState

SELECTED

Indicates this object is the child of an object that allows its children
to be selected, and that this child is one of those children that has
been selected.

static

AccessibleState

SHOWING

Indicates this object, the object's parent, the object's parent's parent,
and so on, are all visible.

static

AccessibleState

SINGLE_LINE

Indicates this (text) object can contain only a single line of text.

static

AccessibleState

TRANSIENT

Indicates this object is transient.

static

AccessibleState

TRUNCATED

A state indicating that text is truncated by a bounding rectangle and
that some of the text is not displayed on the screen.

static

AccessibleState

VERTICAL

Indicates the orientation of this object is vertical.

static

AccessibleState

VISIBLE

Indicates this object is visible.

- Fields declared in class javax.accessibility.

AccessibleBundle

key

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AccessibleState

​(

String

key)

Creates a new

AccessibleState

using the given locale independent
key.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class javax.accessibility.

AccessibleBundle

toDisplayString

,

toDisplayString

,

toDisplayString

,

toString

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

Field Summary

Fields

Modifier and Type

Field

Description

static

AccessibleState

ACTIVE

Indicates a window is currently the active window.

static

AccessibleState

ARMED

Indicates that the object is armed.

static

AccessibleState

BUSY

Indicates the current object is busy.

static

AccessibleState

CHECKED

Indicates this object is currently checked.

static

AccessibleState

COLLAPSED

Indicates this object is collapsed.

static

AccessibleState

EDITABLE

Indicates the user can change the contents of this object.

static

AccessibleState

ENABLED

Indicates this object is enabled.

static

AccessibleState

EXPANDABLE

Indicates this object allows progressive disclosure of its children.

static

AccessibleState

EXPANDED

Indicates this object is expanded.

static

AccessibleState

FOCUSABLE

Indicates this object can accept keyboard focus, which means all events
resulting from typing on the keyboard will normally be passed to it when
it has focus.

static

AccessibleState

FOCUSED

Indicates this object currently has the keyboard focus.

static

AccessibleState

HORIZONTAL

Indicates the orientation of this object is horizontal.

static

AccessibleState

ICONIFIED

Indicates this object is minimized and is represented only by an icon.

static

AccessibleState

INDETERMINATE

Indicates that the object state is indeterminate.

static

AccessibleState

MANAGES_DESCENDANTS

Indicates this object is responsible for managing its subcomponents.

static

AccessibleState

MODAL

Indicates something must be done with this object before the user can
interact with an object in a different window.

static

AccessibleState

MULTI_LINE

Indicates this (text) object can contain multiple lines of text.

static

AccessibleState

MULTISELECTABLE

Indicates this object allows more than one of its children to be selected
at the same time.

static

AccessibleState

OPAQUE

Indicates this object paints every pixel within its rectangular region.

static

AccessibleState

PRESSED

Indicates this object is currently pressed.

static

AccessibleState

RESIZABLE

Indicates the size of this object is not fixed.

static

AccessibleState

SELECTABLE

Indicates this object is the child of an object that allows its children
to be selected, and that this child is one of those children that can be
selected.

static

AccessibleState

SELECTED

Indicates this object is the child of an object that allows its children
to be selected, and that this child is one of those children that has
been selected.

static

AccessibleState

SHOWING

Indicates this object, the object's parent, the object's parent's parent,
and so on, are all visible.

static

AccessibleState

SINGLE_LINE

Indicates this (text) object can contain only a single line of text.

static

AccessibleState

TRANSIENT

Indicates this object is transient.

static

AccessibleState

TRUNCATED

A state indicating that text is truncated by a bounding rectangle and
that some of the text is not displayed on the screen.

static

AccessibleState

VERTICAL

Indicates the orientation of this object is vertical.

static

AccessibleState

VISIBLE

Indicates this object is visible.

- Fields declared in class javax.accessibility.

AccessibleBundle

key

---

#### Field Summary

Indicates a window is currently the active window.

Indicates that the object is armed.

Indicates the current object is busy.

Indicates this object is currently checked.

Indicates this object is collapsed.

Indicates the user can change the contents of this object.

Indicates this object is enabled.

Indicates this object allows progressive disclosure of its children.

Indicates this object is expanded.

Indicates this object can accept keyboard focus, which means all events
resulting from typing on the keyboard will normally be passed to it when
it has focus.

Indicates this object currently has the keyboard focus.

Indicates the orientation of this object is horizontal.

Indicates this object is minimized and is represented only by an icon.

Indicates that the object state is indeterminate.

Indicates this object is responsible for managing its subcomponents.

Indicates something must be done with this object before the user can
interact with an object in a different window.

Indicates this (text) object can contain multiple lines of text.

Indicates this object allows more than one of its children to be selected
at the same time.

Indicates this object paints every pixel within its rectangular region.

Indicates this object is currently pressed.

Indicates the size of this object is not fixed.

Indicates this object is the child of an object that allows its children
to be selected, and that this child is one of those children that can be
selected.

Indicates this object is the child of an object that allows its children
to be selected, and that this child is one of those children that has
been selected.

Indicates this object, the object's parent, the object's parent's parent,
and so on, are all visible.

Indicates this (text) object can contain only a single line of text.

Indicates this object is transient.

A state indicating that text is truncated by a bounding rectangle and
that some of the text is not displayed on the screen.

Indicates the orientation of this object is vertical.

Indicates this object is visible.

Fields declared in class javax.accessibility.

AccessibleBundle

key

---

#### Fields declared in class javax.accessibility. AccessibleBundle

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AccessibleState

​(

String

key)

Creates a new

AccessibleState

using the given locale independent
key.

---

#### Constructor Summary

Creates a new

AccessibleState

using the given locale independent
key.

Method Summary

- Methods declared in class javax.accessibility.

AccessibleBundle

toDisplayString

,

toDisplayString

,

toDisplayString

,

toString

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

Methods declared in class javax.accessibility.

AccessibleBundle

toDisplayString

,

toDisplayString

,

toDisplayString

,

toString

---

#### Methods declared in class javax.accessibility. AccessibleBundle

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

- ACTIVE

```java
public static final
AccessibleState
ACTIVE
```

Indicates a window is currently the active window. This includes windows,
dialogs, frames, etc. In addition, this state is used to indicate the
currently active child of a component such as a list, table, or tree. For
example, the active child of a list is the child that is drawn with a
rectangle around it.

**See Also:** AccessibleRole.WINDOW

,

AccessibleRole.FRAME

,

AccessibleRole.DIALOG

- PRESSED

```java
public static final
AccessibleState
PRESSED
```

Indicates this object is currently pressed. This is usually associated
with buttons and indicates the user has pressed a mouse button while the
pointer was over the button and has not yet released the mouse button.

**See Also:** AccessibleRole.PUSH_BUTTON

- ARMED

```java
public static final
AccessibleState
ARMED
```

Indicates that the object is armed. This is usually used on buttons that
have been pressed but not yet released, and the mouse pointer is still
over the button.

**See Also:** AccessibleRole.PUSH_BUTTON

- BUSY

```java
public static final
AccessibleState
BUSY
```

Indicates the current object is busy. This is usually used on objects
such as progress bars, sliders, or scroll bars to indicate they are in a
state of transition.

**See Also:** AccessibleRole.PROGRESS_BAR

,

AccessibleRole.SCROLL_BAR

,

AccessibleRole.SLIDER

- CHECKED

```java
public static final
AccessibleState
CHECKED
```

Indicates this object is currently checked. This is usually used on
objects such as toggle buttons, radio buttons, and check boxes.

**See Also:** AccessibleRole.TOGGLE_BUTTON

,

AccessibleRole.RADIO_BUTTON

,

AccessibleRole.CHECK_BOX

- EDITABLE

```java
public static final
AccessibleState
EDITABLE
```

Indicates the user can change the contents of this object. This is
usually used primarily for objects that allow the user to enter text.
Other objects, such as scroll bars and sliders, are automatically
editable if they are enabled.

**See Also:** ENABLED

- EXPANDABLE

```java
public static final
AccessibleState
EXPANDABLE
```

Indicates this object allows progressive disclosure of its children. This
is usually used with hierarchical objects such as trees and is often
paired with the

EXPANDED

or

COLLAPSED

states.

**See Also:** EXPANDED

,

COLLAPSED

,

AccessibleRole.TREE

- COLLAPSED

```java
public static final
AccessibleState
COLLAPSED
```

Indicates this object is collapsed. This is usually paired with the

EXPANDABLE

state and is used on objects that provide progressive
disclosure such as trees.

**See Also:** EXPANDABLE

,

EXPANDED

,

AccessibleRole.TREE

- EXPANDED

```java
public static final
AccessibleState
EXPANDED
```

Indicates this object is expanded. This is usually paired with the

EXPANDABLE

state and is used on objects that provide progressive
disclosure such as trees.

**See Also:** EXPANDABLE

,

COLLAPSED

,

AccessibleRole.TREE

- ENABLED

```java
public static final
AccessibleState
ENABLED
```

Indicates this object is enabled. The absence of this state from an
object's state set indicates this object is not enabled. An object that
is not enabled cannot be manipulated by the user. In a graphical display,
it is usually grayed out.

- FOCUSABLE

```java
public static final
AccessibleState
FOCUSABLE
```

Indicates this object can accept keyboard focus, which means all events
resulting from typing on the keyboard will normally be passed to it when
it has focus.

**See Also:** FOCUSED

- FOCUSED

```java
public static final
AccessibleState
FOCUSED
```

Indicates this object currently has the keyboard focus.

**See Also:** FOCUSABLE

- ICONIFIED

```java
public static final
AccessibleState
ICONIFIED
```

Indicates this object is minimized and is represented only by an icon.
This is usually only associated with frames and internal frames.

**See Also:** AccessibleRole.FRAME

,

AccessibleRole.INTERNAL_FRAME

- MODAL

```java
public static final
AccessibleState
MODAL
```

Indicates something must be done with this object before the user can
interact with an object in a different window. This is usually associated
only with dialogs.

**See Also:** AccessibleRole.DIALOG

- OPAQUE

```java
public static final
AccessibleState
OPAQUE
```

Indicates this object paints every pixel within its rectangular region. A
non-opaque component paints only some of its pixels, allowing the pixels
underneath it to "show through". A component that does not fully paint
its pixels therefore provides a degree of transparency.

**See Also:** Accessible.getAccessibleContext()

,

AccessibleContext.getAccessibleComponent()

,

AccessibleComponent.getBounds()

- RESIZABLE

```java
public static final
AccessibleState
RESIZABLE
```

Indicates the size of this object is not fixed.

**See Also:** Accessible.getAccessibleContext()

,

AccessibleContext.getAccessibleComponent()

,

AccessibleComponent.getSize()

,

AccessibleComponent.setSize(java.awt.Dimension)

- MULTISELECTABLE

```java
public static final
AccessibleState
MULTISELECTABLE
```

Indicates this object allows more than one of its children to be selected
at the same time.

**See Also:** Accessible.getAccessibleContext()

,

AccessibleContext.getAccessibleSelection()

,

AccessibleSelection

- SELECTABLE

```java
public static final
AccessibleState
SELECTABLE
```

Indicates this object is the child of an object that allows its children
to be selected, and that this child is one of those children that can be
selected.

**See Also:** SELECTED

,

Accessible.getAccessibleContext()

,

AccessibleContext.getAccessibleSelection()

,

AccessibleSelection

- SELECTED

```java
public static final
AccessibleState
SELECTED
```

Indicates this object is the child of an object that allows its children
to be selected, and that this child is one of those children that has
been selected.

**See Also:** SELECTABLE

,

Accessible.getAccessibleContext()

,

AccessibleContext.getAccessibleSelection()

,

AccessibleSelection

- SHOWING

```java
public static final
AccessibleState
SHOWING
```

Indicates this object, the object's parent, the object's parent's parent,
and so on, are all visible. Note that this does not necessarily mean the
object is painted on the screen. It might be occluded by some other
showing object.

**See Also:** VISIBLE

- VISIBLE

```java
public static final
AccessibleState
VISIBLE
```

Indicates this object is visible. Note: this means that the object
intends to be visible; however, it may not in fact be showing on the
screen because one of the objects that this object is contained by is not
visible.

**See Also:** SHOWING

- VERTICAL

```java
public static final
AccessibleState
VERTICAL
```

Indicates the orientation of this object is vertical. This is usually
associated with objects such as scrollbars, sliders, and progress bars.

**See Also:** VERTICAL

,

AccessibleRole.SCROLL_BAR

,

AccessibleRole.SLIDER

,

AccessibleRole.PROGRESS_BAR

- HORIZONTAL

```java
public static final
AccessibleState
HORIZONTAL
```

Indicates the orientation of this object is horizontal. This is usually
associated with objects such as scrollbars, sliders, and progress bars.

**See Also:** HORIZONTAL

,

AccessibleRole.SCROLL_BAR

,

AccessibleRole.SLIDER

,

AccessibleRole.PROGRESS_BAR

- SINGLE_LINE

```java
public static final
AccessibleState
SINGLE_LINE
```

Indicates this (text) object can contain only a single line of text.

- MULTI_LINE

```java
public static final
AccessibleState
MULTI_LINE
```

Indicates this (text) object can contain multiple lines of text.

- TRANSIENT

```java
public static final
AccessibleState
TRANSIENT
```

Indicates this object is transient. An assistive technology should not
add a

PropertyChange

listener to an object with transient state,
as that object will never generate any events. Transient objects are
typically created to answer Java Accessibility method queries, but
otherwise do not remain linked to the underlying object (for example,
those objects underneath lists, tables, and trees in Swing, where only
one actual

UI Component

does shared rendering duty for all of the
data objects underneath the actual list/table/tree elements).

**Since:** 1.5

- MANAGES_DESCENDANTS

```java
public static final
AccessibleState
MANAGES_DESCENDANTS
```

Indicates this object is responsible for managing its subcomponents. This
is typically used for trees and tables that have a large number of
subcomponents and where the objects are created only when needed and
otherwise remain virtual. The application should not manage the
subcomponents directly.

**Since:** 1.5

- INDETERMINATE

```java
public static final
AccessibleState
INDETERMINATE
```

Indicates that the object state is indeterminate. An example is selected
text that is partially bold and partially not bold. In this case the
attributes associated with the selected text are indeterminate.

**Since:** 1.5

- TRUNCATED

```java
public static final
AccessibleState
TRUNCATED
```

A state indicating that text is truncated by a bounding rectangle and
that some of the text is not displayed on the screen. An example is text
in a spreadsheet cell that is truncated by the bounds of the cell.

**Since:** 1.5

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AccessibleState

```java
protected AccessibleState​(
String
key)
```

Creates a new

AccessibleState

using the given locale independent
key. This should not be a public method. Instead, it is used to create
the constants in this file to make it a strongly typed enumeration.
Subclasses of this class should enforce similar policy.

The key

String

should be a locale independent key for the state.
It is not intended to be used as the actual

String

to display to
the user. To get the localized string, use

AccessibleBundle.toDisplayString()

.

**Parameters:** key

- the locale independent name of the state
**See Also:** AccessibleBundle.toDisplayString(java.lang.String, java.util.Locale)

Field Detail

- ACTIVE

```java
public static final
AccessibleState
ACTIVE
```

Indicates a window is currently the active window. This includes windows,
dialogs, frames, etc. In addition, this state is used to indicate the
currently active child of a component such as a list, table, or tree. For
example, the active child of a list is the child that is drawn with a
rectangle around it.

**See Also:** AccessibleRole.WINDOW

,

AccessibleRole.FRAME

,

AccessibleRole.DIALOG

- PRESSED

```java
public static final
AccessibleState
PRESSED
```

Indicates this object is currently pressed. This is usually associated
with buttons and indicates the user has pressed a mouse button while the
pointer was over the button and has not yet released the mouse button.

**See Also:** AccessibleRole.PUSH_BUTTON

- ARMED

```java
public static final
AccessibleState
ARMED
```

Indicates that the object is armed. This is usually used on buttons that
have been pressed but not yet released, and the mouse pointer is still
over the button.

**See Also:** AccessibleRole.PUSH_BUTTON

- BUSY

```java
public static final
AccessibleState
BUSY
```

Indicates the current object is busy. This is usually used on objects
such as progress bars, sliders, or scroll bars to indicate they are in a
state of transition.

**See Also:** AccessibleRole.PROGRESS_BAR

,

AccessibleRole.SCROLL_BAR

,

AccessibleRole.SLIDER

- CHECKED

```java
public static final
AccessibleState
CHECKED
```

Indicates this object is currently checked. This is usually used on
objects such as toggle buttons, radio buttons, and check boxes.

**See Also:** AccessibleRole.TOGGLE_BUTTON

,

AccessibleRole.RADIO_BUTTON

,

AccessibleRole.CHECK_BOX

- EDITABLE

```java
public static final
AccessibleState
EDITABLE
```

Indicates the user can change the contents of this object. This is
usually used primarily for objects that allow the user to enter text.
Other objects, such as scroll bars and sliders, are automatically
editable if they are enabled.

**See Also:** ENABLED

- EXPANDABLE

```java
public static final
AccessibleState
EXPANDABLE
```

Indicates this object allows progressive disclosure of its children. This
is usually used with hierarchical objects such as trees and is often
paired with the

EXPANDED

or

COLLAPSED

states.

**See Also:** EXPANDED

,

COLLAPSED

,

AccessibleRole.TREE

- COLLAPSED

```java
public static final
AccessibleState
COLLAPSED
```

Indicates this object is collapsed. This is usually paired with the

EXPANDABLE

state and is used on objects that provide progressive
disclosure such as trees.

**See Also:** EXPANDABLE

,

EXPANDED

,

AccessibleRole.TREE

- EXPANDED

```java
public static final
AccessibleState
EXPANDED
```

Indicates this object is expanded. This is usually paired with the

EXPANDABLE

state and is used on objects that provide progressive
disclosure such as trees.

**See Also:** EXPANDABLE

,

COLLAPSED

,

AccessibleRole.TREE

- ENABLED

```java
public static final
AccessibleState
ENABLED
```

Indicates this object is enabled. The absence of this state from an
object's state set indicates this object is not enabled. An object that
is not enabled cannot be manipulated by the user. In a graphical display,
it is usually grayed out.

- FOCUSABLE

```java
public static final
AccessibleState
FOCUSABLE
```

Indicates this object can accept keyboard focus, which means all events
resulting from typing on the keyboard will normally be passed to it when
it has focus.

**See Also:** FOCUSED

- FOCUSED

```java
public static final
AccessibleState
FOCUSED
```

Indicates this object currently has the keyboard focus.

**See Also:** FOCUSABLE

- ICONIFIED

```java
public static final
AccessibleState
ICONIFIED
```

Indicates this object is minimized and is represented only by an icon.
This is usually only associated with frames and internal frames.

**See Also:** AccessibleRole.FRAME

,

AccessibleRole.INTERNAL_FRAME

- MODAL

```java
public static final
AccessibleState
MODAL
```

Indicates something must be done with this object before the user can
interact with an object in a different window. This is usually associated
only with dialogs.

**See Also:** AccessibleRole.DIALOG

- OPAQUE

```java
public static final
AccessibleState
OPAQUE
```

Indicates this object paints every pixel within its rectangular region. A
non-opaque component paints only some of its pixels, allowing the pixels
underneath it to "show through". A component that does not fully paint
its pixels therefore provides a degree of transparency.

**See Also:** Accessible.getAccessibleContext()

,

AccessibleContext.getAccessibleComponent()

,

AccessibleComponent.getBounds()

- RESIZABLE

```java
public static final
AccessibleState
RESIZABLE
```

Indicates the size of this object is not fixed.

**See Also:** Accessible.getAccessibleContext()

,

AccessibleContext.getAccessibleComponent()

,

AccessibleComponent.getSize()

,

AccessibleComponent.setSize(java.awt.Dimension)

- MULTISELECTABLE

```java
public static final
AccessibleState
MULTISELECTABLE
```

Indicates this object allows more than one of its children to be selected
at the same time.

**See Also:** Accessible.getAccessibleContext()

,

AccessibleContext.getAccessibleSelection()

,

AccessibleSelection

- SELECTABLE

```java
public static final
AccessibleState
SELECTABLE
```

Indicates this object is the child of an object that allows its children
to be selected, and that this child is one of those children that can be
selected.

**See Also:** SELECTED

,

Accessible.getAccessibleContext()

,

AccessibleContext.getAccessibleSelection()

,

AccessibleSelection

- SELECTED

```java
public static final
AccessibleState
SELECTED
```

Indicates this object is the child of an object that allows its children
to be selected, and that this child is one of those children that has
been selected.

**See Also:** SELECTABLE

,

Accessible.getAccessibleContext()

,

AccessibleContext.getAccessibleSelection()

,

AccessibleSelection

- SHOWING

```java
public static final
AccessibleState
SHOWING
```

Indicates this object, the object's parent, the object's parent's parent,
and so on, are all visible. Note that this does not necessarily mean the
object is painted on the screen. It might be occluded by some other
showing object.

**See Also:** VISIBLE

- VISIBLE

```java
public static final
AccessibleState
VISIBLE
```

Indicates this object is visible. Note: this means that the object
intends to be visible; however, it may not in fact be showing on the
screen because one of the objects that this object is contained by is not
visible.

**See Also:** SHOWING

- VERTICAL

```java
public static final
AccessibleState
VERTICAL
```

Indicates the orientation of this object is vertical. This is usually
associated with objects such as scrollbars, sliders, and progress bars.

**See Also:** VERTICAL

,

AccessibleRole.SCROLL_BAR

,

AccessibleRole.SLIDER

,

AccessibleRole.PROGRESS_BAR

- HORIZONTAL

```java
public static final
AccessibleState
HORIZONTAL
```

Indicates the orientation of this object is horizontal. This is usually
associated with objects such as scrollbars, sliders, and progress bars.

**See Also:** HORIZONTAL

,

AccessibleRole.SCROLL_BAR

,

AccessibleRole.SLIDER

,

AccessibleRole.PROGRESS_BAR

- SINGLE_LINE

```java
public static final
AccessibleState
SINGLE_LINE
```

Indicates this (text) object can contain only a single line of text.

- MULTI_LINE

```java
public static final
AccessibleState
MULTI_LINE
```

Indicates this (text) object can contain multiple lines of text.

- TRANSIENT

```java
public static final
AccessibleState
TRANSIENT
```

Indicates this object is transient. An assistive technology should not
add a

PropertyChange

listener to an object with transient state,
as that object will never generate any events. Transient objects are
typically created to answer Java Accessibility method queries, but
otherwise do not remain linked to the underlying object (for example,
those objects underneath lists, tables, and trees in Swing, where only
one actual

UI Component

does shared rendering duty for all of the
data objects underneath the actual list/table/tree elements).

**Since:** 1.5

- MANAGES_DESCENDANTS

```java
public static final
AccessibleState
MANAGES_DESCENDANTS
```

Indicates this object is responsible for managing its subcomponents. This
is typically used for trees and tables that have a large number of
subcomponents and where the objects are created only when needed and
otherwise remain virtual. The application should not manage the
subcomponents directly.

**Since:** 1.5

- INDETERMINATE

```java
public static final
AccessibleState
INDETERMINATE
```

Indicates that the object state is indeterminate. An example is selected
text that is partially bold and partially not bold. In this case the
attributes associated with the selected text are indeterminate.

**Since:** 1.5

- TRUNCATED

```java
public static final
AccessibleState
TRUNCATED
```

A state indicating that text is truncated by a bounding rectangle and
that some of the text is not displayed on the screen. An example is text
in a spreadsheet cell that is truncated by the bounds of the cell.

**Since:** 1.5

---

#### Field Detail

ACTIVE

```java
public static final
AccessibleState
ACTIVE
```

Indicates a window is currently the active window. This includes windows,
dialogs, frames, etc. In addition, this state is used to indicate the
currently active child of a component such as a list, table, or tree. For
example, the active child of a list is the child that is drawn with a
rectangle around it.

**See Also:** AccessibleRole.WINDOW

,

AccessibleRole.FRAME

,

AccessibleRole.DIALOG

---

#### ACTIVE

public static final

AccessibleState

ACTIVE

Indicates a window is currently the active window. This includes windows,
dialogs, frames, etc. In addition, this state is used to indicate the
currently active child of a component such as a list, table, or tree. For
example, the active child of a list is the child that is drawn with a
rectangle around it.

PRESSED

```java
public static final
AccessibleState
PRESSED
```

Indicates this object is currently pressed. This is usually associated
with buttons and indicates the user has pressed a mouse button while the
pointer was over the button and has not yet released the mouse button.

**See Also:** AccessibleRole.PUSH_BUTTON

---

#### PRESSED

public static final

AccessibleState

PRESSED

Indicates this object is currently pressed. This is usually associated
with buttons and indicates the user has pressed a mouse button while the
pointer was over the button and has not yet released the mouse button.

ARMED

```java
public static final
AccessibleState
ARMED
```

Indicates that the object is armed. This is usually used on buttons that
have been pressed but not yet released, and the mouse pointer is still
over the button.

**See Also:** AccessibleRole.PUSH_BUTTON

---

#### ARMED

public static final

AccessibleState

ARMED

Indicates that the object is armed. This is usually used on buttons that
have been pressed but not yet released, and the mouse pointer is still
over the button.

BUSY

```java
public static final
AccessibleState
BUSY
```

Indicates the current object is busy. This is usually used on objects
such as progress bars, sliders, or scroll bars to indicate they are in a
state of transition.

**See Also:** AccessibleRole.PROGRESS_BAR

,

AccessibleRole.SCROLL_BAR

,

AccessibleRole.SLIDER

---

#### BUSY

public static final

AccessibleState

BUSY

Indicates the current object is busy. This is usually used on objects
such as progress bars, sliders, or scroll bars to indicate they are in a
state of transition.

CHECKED

```java
public static final
AccessibleState
CHECKED
```

Indicates this object is currently checked. This is usually used on
objects such as toggle buttons, radio buttons, and check boxes.

**See Also:** AccessibleRole.TOGGLE_BUTTON

,

AccessibleRole.RADIO_BUTTON

,

AccessibleRole.CHECK_BOX

---

#### CHECKED

public static final

AccessibleState

CHECKED

Indicates this object is currently checked. This is usually used on
objects such as toggle buttons, radio buttons, and check boxes.

EDITABLE

```java
public static final
AccessibleState
EDITABLE
```

Indicates the user can change the contents of this object. This is
usually used primarily for objects that allow the user to enter text.
Other objects, such as scroll bars and sliders, are automatically
editable if they are enabled.

**See Also:** ENABLED

---

#### EDITABLE

public static final

AccessibleState

EDITABLE

Indicates the user can change the contents of this object. This is
usually used primarily for objects that allow the user to enter text.
Other objects, such as scroll bars and sliders, are automatically
editable if they are enabled.

EXPANDABLE

```java
public static final
AccessibleState
EXPANDABLE
```

Indicates this object allows progressive disclosure of its children. This
is usually used with hierarchical objects such as trees and is often
paired with the

EXPANDED

or

COLLAPSED

states.

**See Also:** EXPANDED

,

COLLAPSED

,

AccessibleRole.TREE

---

#### EXPANDABLE

public static final

AccessibleState

EXPANDABLE

Indicates this object allows progressive disclosure of its children. This
is usually used with hierarchical objects such as trees and is often
paired with the

EXPANDED

or

COLLAPSED

states.

COLLAPSED

```java
public static final
AccessibleState
COLLAPSED
```

Indicates this object is collapsed. This is usually paired with the

EXPANDABLE

state and is used on objects that provide progressive
disclosure such as trees.

**See Also:** EXPANDABLE

,

EXPANDED

,

AccessibleRole.TREE

---

#### COLLAPSED

public static final

AccessibleState

COLLAPSED

Indicates this object is collapsed. This is usually paired with the

EXPANDABLE

state and is used on objects that provide progressive
disclosure such as trees.

EXPANDED

```java
public static final
AccessibleState
EXPANDED
```

Indicates this object is expanded. This is usually paired with the

EXPANDABLE

state and is used on objects that provide progressive
disclosure such as trees.

**See Also:** EXPANDABLE

,

COLLAPSED

,

AccessibleRole.TREE

---

#### EXPANDED

public static final

AccessibleState

EXPANDED

Indicates this object is expanded. This is usually paired with the

EXPANDABLE

state and is used on objects that provide progressive
disclosure such as trees.

ENABLED

```java
public static final
AccessibleState
ENABLED
```

Indicates this object is enabled. The absence of this state from an
object's state set indicates this object is not enabled. An object that
is not enabled cannot be manipulated by the user. In a graphical display,
it is usually grayed out.

---

#### ENABLED

public static final

AccessibleState

ENABLED

Indicates this object is enabled. The absence of this state from an
object's state set indicates this object is not enabled. An object that
is not enabled cannot be manipulated by the user. In a graphical display,
it is usually grayed out.

FOCUSABLE

```java
public static final
AccessibleState
FOCUSABLE
```

Indicates this object can accept keyboard focus, which means all events
resulting from typing on the keyboard will normally be passed to it when
it has focus.

**See Also:** FOCUSED

---

#### FOCUSABLE

public static final

AccessibleState

FOCUSABLE

Indicates this object can accept keyboard focus, which means all events
resulting from typing on the keyboard will normally be passed to it when
it has focus.

FOCUSED

```java
public static final
AccessibleState
FOCUSED
```

Indicates this object currently has the keyboard focus.

**See Also:** FOCUSABLE

---

#### FOCUSED

public static final

AccessibleState

FOCUSED

Indicates this object currently has the keyboard focus.

ICONIFIED

```java
public static final
AccessibleState
ICONIFIED
```

Indicates this object is minimized and is represented only by an icon.
This is usually only associated with frames and internal frames.

**See Also:** AccessibleRole.FRAME

,

AccessibleRole.INTERNAL_FRAME

---

#### ICONIFIED

public static final

AccessibleState

ICONIFIED

Indicates this object is minimized and is represented only by an icon.
This is usually only associated with frames and internal frames.

MODAL

```java
public static final
AccessibleState
MODAL
```

Indicates something must be done with this object before the user can
interact with an object in a different window. This is usually associated
only with dialogs.

**See Also:** AccessibleRole.DIALOG

---

#### MODAL

public static final

AccessibleState

MODAL

Indicates something must be done with this object before the user can
interact with an object in a different window. This is usually associated
only with dialogs.

OPAQUE

```java
public static final
AccessibleState
OPAQUE
```

Indicates this object paints every pixel within its rectangular region. A
non-opaque component paints only some of its pixels, allowing the pixels
underneath it to "show through". A component that does not fully paint
its pixels therefore provides a degree of transparency.

**See Also:** Accessible.getAccessibleContext()

,

AccessibleContext.getAccessibleComponent()

,

AccessibleComponent.getBounds()

---

#### OPAQUE

public static final

AccessibleState

OPAQUE

Indicates this object paints every pixel within its rectangular region. A
non-opaque component paints only some of its pixels, allowing the pixels
underneath it to "show through". A component that does not fully paint
its pixels therefore provides a degree of transparency.

RESIZABLE

```java
public static final
AccessibleState
RESIZABLE
```

Indicates the size of this object is not fixed.

**See Also:** Accessible.getAccessibleContext()

,

AccessibleContext.getAccessibleComponent()

,

AccessibleComponent.getSize()

,

AccessibleComponent.setSize(java.awt.Dimension)

---

#### RESIZABLE

public static final

AccessibleState

RESIZABLE

Indicates the size of this object is not fixed.

MULTISELECTABLE

```java
public static final
AccessibleState
MULTISELECTABLE
```

Indicates this object allows more than one of its children to be selected
at the same time.

**See Also:** Accessible.getAccessibleContext()

,

AccessibleContext.getAccessibleSelection()

,

AccessibleSelection

---

#### MULTISELECTABLE

public static final

AccessibleState

MULTISELECTABLE

Indicates this object allows more than one of its children to be selected
at the same time.

SELECTABLE

```java
public static final
AccessibleState
SELECTABLE
```

Indicates this object is the child of an object that allows its children
to be selected, and that this child is one of those children that can be
selected.

**See Also:** SELECTED

,

Accessible.getAccessibleContext()

,

AccessibleContext.getAccessibleSelection()

,

AccessibleSelection

---

#### SELECTABLE

public static final

AccessibleState

SELECTABLE

Indicates this object is the child of an object that allows its children
to be selected, and that this child is one of those children that can be
selected.

SELECTED

```java
public static final
AccessibleState
SELECTED
```

Indicates this object is the child of an object that allows its children
to be selected, and that this child is one of those children that has
been selected.

**See Also:** SELECTABLE

,

Accessible.getAccessibleContext()

,

AccessibleContext.getAccessibleSelection()

,

AccessibleSelection

---

#### SELECTED

public static final

AccessibleState

SELECTED

Indicates this object is the child of an object that allows its children
to be selected, and that this child is one of those children that has
been selected.

SHOWING

```java
public static final
AccessibleState
SHOWING
```

Indicates this object, the object's parent, the object's parent's parent,
and so on, are all visible. Note that this does not necessarily mean the
object is painted on the screen. It might be occluded by some other
showing object.

**See Also:** VISIBLE

---

#### SHOWING

public static final

AccessibleState

SHOWING

Indicates this object, the object's parent, the object's parent's parent,
and so on, are all visible. Note that this does not necessarily mean the
object is painted on the screen. It might be occluded by some other
showing object.

VISIBLE

```java
public static final
AccessibleState
VISIBLE
```

Indicates this object is visible. Note: this means that the object
intends to be visible; however, it may not in fact be showing on the
screen because one of the objects that this object is contained by is not
visible.

**See Also:** SHOWING

---

#### VISIBLE

public static final

AccessibleState

VISIBLE

Indicates this object is visible. Note: this means that the object
intends to be visible; however, it may not in fact be showing on the
screen because one of the objects that this object is contained by is not
visible.

VERTICAL

```java
public static final
AccessibleState
VERTICAL
```

Indicates the orientation of this object is vertical. This is usually
associated with objects such as scrollbars, sliders, and progress bars.

**See Also:** VERTICAL

,

AccessibleRole.SCROLL_BAR

,

AccessibleRole.SLIDER

,

AccessibleRole.PROGRESS_BAR

---

#### VERTICAL

public static final

AccessibleState

VERTICAL

Indicates the orientation of this object is vertical. This is usually
associated with objects such as scrollbars, sliders, and progress bars.

HORIZONTAL

```java
public static final
AccessibleState
HORIZONTAL
```

Indicates the orientation of this object is horizontal. This is usually
associated with objects such as scrollbars, sliders, and progress bars.

**See Also:** HORIZONTAL

,

AccessibleRole.SCROLL_BAR

,

AccessibleRole.SLIDER

,

AccessibleRole.PROGRESS_BAR

---

#### HORIZONTAL

public static final

AccessibleState

HORIZONTAL

Indicates the orientation of this object is horizontal. This is usually
associated with objects such as scrollbars, sliders, and progress bars.

SINGLE_LINE

```java
public static final
AccessibleState
SINGLE_LINE
```

Indicates this (text) object can contain only a single line of text.

---

#### SINGLE_LINE

public static final

AccessibleState

SINGLE_LINE

Indicates this (text) object can contain only a single line of text.

MULTI_LINE

```java
public static final
AccessibleState
MULTI_LINE
```

Indicates this (text) object can contain multiple lines of text.

---

#### MULTI_LINE

public static final

AccessibleState

MULTI_LINE

Indicates this (text) object can contain multiple lines of text.

TRANSIENT

```java
public static final
AccessibleState
TRANSIENT
```

Indicates this object is transient. An assistive technology should not
add a

PropertyChange

listener to an object with transient state,
as that object will never generate any events. Transient objects are
typically created to answer Java Accessibility method queries, but
otherwise do not remain linked to the underlying object (for example,
those objects underneath lists, tables, and trees in Swing, where only
one actual

UI Component

does shared rendering duty for all of the
data objects underneath the actual list/table/tree elements).

**Since:** 1.5

---

#### TRANSIENT

public static final

AccessibleState

TRANSIENT

Indicates this object is transient. An assistive technology should not
add a

PropertyChange

listener to an object with transient state,
as that object will never generate any events. Transient objects are
typically created to answer Java Accessibility method queries, but
otherwise do not remain linked to the underlying object (for example,
those objects underneath lists, tables, and trees in Swing, where only
one actual

UI Component

does shared rendering duty for all of the
data objects underneath the actual list/table/tree elements).

MANAGES_DESCENDANTS

```java
public static final
AccessibleState
MANAGES_DESCENDANTS
```

Indicates this object is responsible for managing its subcomponents. This
is typically used for trees and tables that have a large number of
subcomponents and where the objects are created only when needed and
otherwise remain virtual. The application should not manage the
subcomponents directly.

**Since:** 1.5

---

#### MANAGES_DESCENDANTS

public static final

AccessibleState

MANAGES_DESCENDANTS

Indicates this object is responsible for managing its subcomponents. This
is typically used for trees and tables that have a large number of
subcomponents and where the objects are created only when needed and
otherwise remain virtual. The application should not manage the
subcomponents directly.

INDETERMINATE

```java
public static final
AccessibleState
INDETERMINATE
```

Indicates that the object state is indeterminate. An example is selected
text that is partially bold and partially not bold. In this case the
attributes associated with the selected text are indeterminate.

**Since:** 1.5

---

#### INDETERMINATE

public static final

AccessibleState

INDETERMINATE

Indicates that the object state is indeterminate. An example is selected
text that is partially bold and partially not bold. In this case the
attributes associated with the selected text are indeterminate.

TRUNCATED

```java
public static final
AccessibleState
TRUNCATED
```

A state indicating that text is truncated by a bounding rectangle and
that some of the text is not displayed on the screen. An example is text
in a spreadsheet cell that is truncated by the bounds of the cell.

**Since:** 1.5

---

#### TRUNCATED

public static final

AccessibleState

TRUNCATED

A state indicating that text is truncated by a bounding rectangle and
that some of the text is not displayed on the screen. An example is text
in a spreadsheet cell that is truncated by the bounds of the cell.

Constructor Detail

- AccessibleState

```java
protected AccessibleState​(
String
key)
```

Creates a new

AccessibleState

using the given locale independent
key. This should not be a public method. Instead, it is used to create
the constants in this file to make it a strongly typed enumeration.
Subclasses of this class should enforce similar policy.

The key

String

should be a locale independent key for the state.
It is not intended to be used as the actual

String

to display to
the user. To get the localized string, use

AccessibleBundle.toDisplayString()

.

**Parameters:** key

- the locale independent name of the state
**See Also:** AccessibleBundle.toDisplayString(java.lang.String, java.util.Locale)

---

#### Constructor Detail

AccessibleState

```java
protected AccessibleState​(
String
key)
```

Creates a new

AccessibleState

using the given locale independent
key. This should not be a public method. Instead, it is used to create
the constants in this file to make it a strongly typed enumeration.
Subclasses of this class should enforce similar policy.

The key

String

should be a locale independent key for the state.
It is not intended to be used as the actual

String

to display to
the user. To get the localized string, use

AccessibleBundle.toDisplayString()

.

**Parameters:** key

- the locale independent name of the state
**See Also:** AccessibleBundle.toDisplayString(java.lang.String, java.util.Locale)

---

#### AccessibleState

protected AccessibleState​(

String

key)

Creates a new

AccessibleState

using the given locale independent
key. This should not be a public method. Instead, it is used to create
the constants in this file to make it a strongly typed enumeration.
Subclasses of this class should enforce similar policy.

The key

String

should be a locale independent key for the state.
It is not intended to be used as the actual

String

to display to
the user. To get the localized string, use

AccessibleBundle.toDisplayString()

.

The key

String

should be a locale independent key for the state.
It is not intended to be used as the actual

String

to display to
the user. To get the localized string, use

AccessibleBundle.toDisplayString()

.

---

