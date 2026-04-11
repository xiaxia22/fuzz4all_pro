# Interface InputMethodContext

**Source:** `java.desktop\java\awt\im\spi\InputMethodContext.html`

### Class Description

```java
public interface
InputMethodContext

extends
InputMethodRequests
```

Provides methods that input methods
can use to communicate with their client components or to request
other services. This interface is implemented by the input method
framework, and input methods call its methods on the instance they
receive through

InputMethod.setInputMethodContext(java.awt.im.spi.InputMethodContext)

.
There should be no other implementors or callers.

**All Superinterfaces:** InputMethodRequests

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void dispatchInputMethodEvent​(int id,

AttributedCharacterIterator
text,
int committedCharacterCount,

TextHitInfo
caret,

TextHitInfo
visiblePosition)

Creates an input method event from the arguments given
and dispatches it to the client component. For arguments,
see

InputMethodEvent(java.awt.Component, int, java.awt.font.TextHitInfo, java.awt.font.TextHitInfo)

.

**Parameters:**
- id

- the event type
- text

- the combined committed and composed text
- committedCharacterCount

- the number of committed characters in the text
- caret

- the caret (a.k.a. insertion point); null if
there's no caret within current composed text
- visiblePosition

- the position that's most important to be
visible; null if there's no recommendation for a visible
position within current composed text

---

#### Window
createInputMethodWindow​(
String
title,
boolean attachToInputContext)

Creates a top-level window for use by the input method.
The intended behavior of this window is:

- it floats above all document windows and dialogs

it and all components that it contains do not receive the focus

it has lightweight decorations, such as a reduced drag region without title

However, the actual behavior with respect to these three items is platform dependent.

The title may or may not be displayed, depending on the actual type of window created.

If attachToInputContext is true, the new window will share the input context that
corresponds to this input method context, so that events for components in the window
are automatically dispatched to the input method.
Also, when the window is opened using setVisible(true), the input context will prevent
deactivate and activate calls to the input method that might otherwise be caused.

Input methods must call

Window.dispose

on the
returned input method window when it is no longer needed.

**Parameters:**
- title

- the title to be displayed in the window's title bar,
if there is such a title bar.
A

null

value is treated as an empty string, "".
- attachToInputContext

- whether this window should share the input context
that corresponds to this input method context

**Returns:**
- a window with special characteristics for use by input methods

**Throws:**
- HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true

---

#### JFrame
createInputMethodJFrame​(
String
title,
boolean attachToInputContext)

Creates a top-level Swing JFrame for use by the input method.
The intended behavior of this window is:

- it floats above all document windows and dialogs

it and all components that it contains do not receive the focus

it has lightweight decorations, such as a reduced drag region without title

However, the actual behavior with respect to these three items is platform dependent.

The title may or may not be displayed, depending on the actual type of window created.

If attachToInputContext is true, the new window will share the input context that
corresponds to this input method context, so that events for components in the window
are automatically dispatched to the input method.
Also, when the window is opened using setVisible(true), the input context will prevent
deactivate and activate calls to the input method that might otherwise be caused.

Input methods must call

Window.dispose

on the
returned input method window when it is no longer needed.

**Parameters:**
- title

- the title to be displayed in the window's title bar,
if there is such a title bar.
A

null

value is treated as an empty string, "".
- attachToInputContext

- whether this window should share the input context
that corresponds to this input method context

**Returns:**
- a JFrame with special characteristics for use by input methods

**Throws:**
- HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true

**Since:**
- 1.4

---

#### void enableClientWindowNotification​(
InputMethod
inputMethod,
boolean enable)

Enables or disables notification of the current client window's
location and state for the specified input method. When
notification is enabled, the input method's

notifyClientWindowChange

method is called as described in that
method's specification. Notification is automatically disabled
when the input method is disposed.

**Parameters:**
- inputMethod

- the input method for which notifications are
enabled or disabled
- enable

- true to enable, false to disable

---

### Additional Sections

#### Interface InputMethodContext

**All Superinterfaces:** InputMethodRequests

```java
public interface
InputMethodContext

extends
InputMethodRequests
```

Provides methods that input methods
can use to communicate with their client components or to request
other services. This interface is implemented by the input method
framework, and input methods call its methods on the instance they
receive through

InputMethod.setInputMethodContext(java.awt.im.spi.InputMethodContext)

.
There should be no other implementors or callers.

**Since:** 1.3

public interface

InputMethodContext

extends

InputMethodRequests

Provides methods that input methods
can use to communicate with their client components or to request
other services. This interface is implemented by the input method
framework, and input methods call its methods on the instance they
receive through

InputMethod.setInputMethodContext(java.awt.im.spi.InputMethodContext)

.
There should be no other implementors or callers.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

JFrame

createInputMethodJFrame

​(

String

title,
boolean attachToInputContext)

Creates a top-level Swing JFrame for use by the input method.

Window

createInputMethodWindow

​(

String

title,
boolean attachToInputContext)

Creates a top-level window for use by the input method.

void

dispatchInputMethodEvent

​(int id,

AttributedCharacterIterator

text,
int committedCharacterCount,

TextHitInfo

caret,

TextHitInfo

visiblePosition)

Creates an input method event from the arguments given
and dispatches it to the client component.

void

enableClientWindowNotification

​(

InputMethod

inputMethod,
boolean enable)

Enables or disables notification of the current client window's
location and state for the specified input method.

- Methods declared in interface java.awt.im.

InputMethodRequests

cancelLatestCommittedText

,

getCommittedText

,

getCommittedTextLength

,

getInsertPositionOffset

,

getLocationOffset

,

getSelectedText

,

getTextLocation

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

JFrame

createInputMethodJFrame

​(

String

title,
boolean attachToInputContext)

Creates a top-level Swing JFrame for use by the input method.

Window

createInputMethodWindow

​(

String

title,
boolean attachToInputContext)

Creates a top-level window for use by the input method.

void

dispatchInputMethodEvent

​(int id,

AttributedCharacterIterator

text,
int committedCharacterCount,

TextHitInfo

caret,

TextHitInfo

visiblePosition)

Creates an input method event from the arguments given
and dispatches it to the client component.

void

enableClientWindowNotification

​(

InputMethod

inputMethod,
boolean enable)

Enables or disables notification of the current client window's
location and state for the specified input method.

- Methods declared in interface java.awt.im.

InputMethodRequests

cancelLatestCommittedText

,

getCommittedText

,

getCommittedTextLength

,

getInsertPositionOffset

,

getLocationOffset

,

getSelectedText

,

getTextLocation

---

#### Method Summary

Creates a top-level Swing JFrame for use by the input method.

Creates a top-level window for use by the input method.

Creates an input method event from the arguments given
and dispatches it to the client component.

Enables or disables notification of the current client window's
location and state for the specified input method.

Methods declared in interface java.awt.im.

InputMethodRequests

cancelLatestCommittedText

,

getCommittedText

,

getCommittedTextLength

,

getInsertPositionOffset

,

getLocationOffset

,

getSelectedText

,

getTextLocation

---

#### Methods declared in interface java.awt.im. InputMethodRequests

============ METHOD DETAIL ==========

- Method Detail

- dispatchInputMethodEvent

```java
void dispatchInputMethodEvent​(int id,

AttributedCharacterIterator
text,
int committedCharacterCount,

TextHitInfo
caret,

TextHitInfo
visiblePosition)
```

Creates an input method event from the arguments given
and dispatches it to the client component. For arguments,
see

InputMethodEvent(java.awt.Component, int, java.awt.font.TextHitInfo, java.awt.font.TextHitInfo)

.

**Parameters:** id

- the event type
**Parameters:** text

- the combined committed and composed text
**Parameters:** committedCharacterCount

- the number of committed characters in the text
**Parameters:** caret

- the caret (a.k.a. insertion point); null if
there's no caret within current composed text
**Parameters:** visiblePosition

- the position that's most important to be
visible; null if there's no recommendation for a visible
position within current composed text

- createInputMethodWindow

```java
Window
createInputMethodWindow​(
String
title,
boolean attachToInputContext)
```

Creates a top-level window for use by the input method.
The intended behavior of this window is:

- it floats above all document windows and dialogs

it and all components that it contains do not receive the focus

it has lightweight decorations, such as a reduced drag region without title

However, the actual behavior with respect to these three items is platform dependent.

The title may or may not be displayed, depending on the actual type of window created.

If attachToInputContext is true, the new window will share the input context that
corresponds to this input method context, so that events for components in the window
are automatically dispatched to the input method.
Also, when the window is opened using setVisible(true), the input context will prevent
deactivate and activate calls to the input method that might otherwise be caused.

Input methods must call

Window.dispose

on the
returned input method window when it is no longer needed.

**Parameters:** title

- the title to be displayed in the window's title bar,
if there is such a title bar.
A

null

value is treated as an empty string, "".
**Parameters:** attachToInputContext

- whether this window should share the input context
that corresponds to this input method context
**Returns:** a window with special characteristics for use by input methods
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true

- createInputMethodJFrame

```java
JFrame
createInputMethodJFrame​(
String
title,
boolean attachToInputContext)
```

Creates a top-level Swing JFrame for use by the input method.
The intended behavior of this window is:

- it floats above all document windows and dialogs

it and all components that it contains do not receive the focus

it has lightweight decorations, such as a reduced drag region without title

However, the actual behavior with respect to these three items is platform dependent.

The title may or may not be displayed, depending on the actual type of window created.

If attachToInputContext is true, the new window will share the input context that
corresponds to this input method context, so that events for components in the window
are automatically dispatched to the input method.
Also, when the window is opened using setVisible(true), the input context will prevent
deactivate and activate calls to the input method that might otherwise be caused.

Input methods must call

Window.dispose

on the
returned input method window when it is no longer needed.

**Parameters:** title

- the title to be displayed in the window's title bar,
if there is such a title bar.
A

null

value is treated as an empty string, "".
**Parameters:** attachToInputContext

- whether this window should share the input context
that corresponds to this input method context
**Returns:** a JFrame with special characteristics for use by input methods
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**Since:** 1.4

- enableClientWindowNotification

```java
void enableClientWindowNotification​(
InputMethod
inputMethod,
boolean enable)
```

Enables or disables notification of the current client window's
location and state for the specified input method. When
notification is enabled, the input method's

notifyClientWindowChange

method is called as described in that
method's specification. Notification is automatically disabled
when the input method is disposed.

**Parameters:** inputMethod

- the input method for which notifications are
enabled or disabled
**Parameters:** enable

- true to enable, false to disable

Method Detail

- dispatchInputMethodEvent

```java
void dispatchInputMethodEvent​(int id,

AttributedCharacterIterator
text,
int committedCharacterCount,

TextHitInfo
caret,

TextHitInfo
visiblePosition)
```

Creates an input method event from the arguments given
and dispatches it to the client component. For arguments,
see

InputMethodEvent(java.awt.Component, int, java.awt.font.TextHitInfo, java.awt.font.TextHitInfo)

.

**Parameters:** id

- the event type
**Parameters:** text

- the combined committed and composed text
**Parameters:** committedCharacterCount

- the number of committed characters in the text
**Parameters:** caret

- the caret (a.k.a. insertion point); null if
there's no caret within current composed text
**Parameters:** visiblePosition

- the position that's most important to be
visible; null if there's no recommendation for a visible
position within current composed text

- createInputMethodWindow

```java
Window
createInputMethodWindow​(
String
title,
boolean attachToInputContext)
```

Creates a top-level window for use by the input method.
The intended behavior of this window is:

- it floats above all document windows and dialogs

it and all components that it contains do not receive the focus

it has lightweight decorations, such as a reduced drag region without title

However, the actual behavior with respect to these three items is platform dependent.

The title may or may not be displayed, depending on the actual type of window created.

If attachToInputContext is true, the new window will share the input context that
corresponds to this input method context, so that events for components in the window
are automatically dispatched to the input method.
Also, when the window is opened using setVisible(true), the input context will prevent
deactivate and activate calls to the input method that might otherwise be caused.

Input methods must call

Window.dispose

on the
returned input method window when it is no longer needed.

**Parameters:** title

- the title to be displayed in the window's title bar,
if there is such a title bar.
A

null

value is treated as an empty string, "".
**Parameters:** attachToInputContext

- whether this window should share the input context
that corresponds to this input method context
**Returns:** a window with special characteristics for use by input methods
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true

- createInputMethodJFrame

```java
JFrame
createInputMethodJFrame​(
String
title,
boolean attachToInputContext)
```

Creates a top-level Swing JFrame for use by the input method.
The intended behavior of this window is:

- it floats above all document windows and dialogs

it and all components that it contains do not receive the focus

it has lightweight decorations, such as a reduced drag region without title

However, the actual behavior with respect to these three items is platform dependent.

The title may or may not be displayed, depending on the actual type of window created.

If attachToInputContext is true, the new window will share the input context that
corresponds to this input method context, so that events for components in the window
are automatically dispatched to the input method.
Also, when the window is opened using setVisible(true), the input context will prevent
deactivate and activate calls to the input method that might otherwise be caused.

Input methods must call

Window.dispose

on the
returned input method window when it is no longer needed.

**Parameters:** title

- the title to be displayed in the window's title bar,
if there is such a title bar.
A

null

value is treated as an empty string, "".
**Parameters:** attachToInputContext

- whether this window should share the input context
that corresponds to this input method context
**Returns:** a JFrame with special characteristics for use by input methods
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**Since:** 1.4

- enableClientWindowNotification

```java
void enableClientWindowNotification​(
InputMethod
inputMethod,
boolean enable)
```

Enables or disables notification of the current client window's
location and state for the specified input method. When
notification is enabled, the input method's

notifyClientWindowChange

method is called as described in that
method's specification. Notification is automatically disabled
when the input method is disposed.

**Parameters:** inputMethod

- the input method for which notifications are
enabled or disabled
**Parameters:** enable

- true to enable, false to disable

---

#### Method Detail

dispatchInputMethodEvent

```java
void dispatchInputMethodEvent​(int id,

AttributedCharacterIterator
text,
int committedCharacterCount,

TextHitInfo
caret,

TextHitInfo
visiblePosition)
```

Creates an input method event from the arguments given
and dispatches it to the client component. For arguments,
see

InputMethodEvent(java.awt.Component, int, java.awt.font.TextHitInfo, java.awt.font.TextHitInfo)

.

**Parameters:** id

- the event type
**Parameters:** text

- the combined committed and composed text
**Parameters:** committedCharacterCount

- the number of committed characters in the text
**Parameters:** caret

- the caret (a.k.a. insertion point); null if
there's no caret within current composed text
**Parameters:** visiblePosition

- the position that's most important to be
visible; null if there's no recommendation for a visible
position within current composed text

---

#### dispatchInputMethodEvent

void dispatchInputMethodEvent​(int id,

AttributedCharacterIterator

text,
int committedCharacterCount,

TextHitInfo

caret,

TextHitInfo

visiblePosition)

Creates an input method event from the arguments given
and dispatches it to the client component. For arguments,
see

InputMethodEvent(java.awt.Component, int, java.awt.font.TextHitInfo, java.awt.font.TextHitInfo)

.

createInputMethodWindow

```java
Window
createInputMethodWindow​(
String
title,
boolean attachToInputContext)
```

Creates a top-level window for use by the input method.
The intended behavior of this window is:

- it floats above all document windows and dialogs

it and all components that it contains do not receive the focus

it has lightweight decorations, such as a reduced drag region without title

However, the actual behavior with respect to these three items is platform dependent.

The title may or may not be displayed, depending on the actual type of window created.

If attachToInputContext is true, the new window will share the input context that
corresponds to this input method context, so that events for components in the window
are automatically dispatched to the input method.
Also, when the window is opened using setVisible(true), the input context will prevent
deactivate and activate calls to the input method that might otherwise be caused.

Input methods must call

Window.dispose

on the
returned input method window when it is no longer needed.

**Parameters:** title

- the title to be displayed in the window's title bar,
if there is such a title bar.
A

null

value is treated as an empty string, "".
**Parameters:** attachToInputContext

- whether this window should share the input context
that corresponds to this input method context
**Returns:** a window with special characteristics for use by input methods
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true

---

#### createInputMethodWindow

Window

createInputMethodWindow​(

String

title,
boolean attachToInputContext)

Creates a top-level window for use by the input method.
The intended behavior of this window is:

- it floats above all document windows and dialogs

it and all components that it contains do not receive the focus

it has lightweight decorations, such as a reduced drag region without title

However, the actual behavior with respect to these three items is platform dependent.

The title may or may not be displayed, depending on the actual type of window created.

If attachToInputContext is true, the new window will share the input context that
corresponds to this input method context, so that events for components in the window
are automatically dispatched to the input method.
Also, when the window is opened using setVisible(true), the input context will prevent
deactivate and activate calls to the input method that might otherwise be caused.

Input methods must call

Window.dispose

on the
returned input method window when it is no longer needed.

it floats above all document windows and dialogs

it and all components that it contains do not receive the focus

it has lightweight decorations, such as a reduced drag region without title

The title may or may not be displayed, depending on the actual type of window created.

If attachToInputContext is true, the new window will share the input context that
corresponds to this input method context, so that events for components in the window
are automatically dispatched to the input method.
Also, when the window is opened using setVisible(true), the input context will prevent
deactivate and activate calls to the input method that might otherwise be caused.

Input methods must call

Window.dispose

on the
returned input method window when it is no longer needed.

If attachToInputContext is true, the new window will share the input context that
corresponds to this input method context, so that events for components in the window
are automatically dispatched to the input method.
Also, when the window is opened using setVisible(true), the input context will prevent
deactivate and activate calls to the input method that might otherwise be caused.

Input methods must call

Window.dispose

on the
returned input method window when it is no longer needed.

Input methods must call

Window.dispose

on the
returned input method window when it is no longer needed.

createInputMethodJFrame

```java
JFrame
createInputMethodJFrame​(
String
title,
boolean attachToInputContext)
```

Creates a top-level Swing JFrame for use by the input method.
The intended behavior of this window is:

- it floats above all document windows and dialogs

it and all components that it contains do not receive the focus

it has lightweight decorations, such as a reduced drag region without title

However, the actual behavior with respect to these three items is platform dependent.

The title may or may not be displayed, depending on the actual type of window created.

If attachToInputContext is true, the new window will share the input context that
corresponds to this input method context, so that events for components in the window
are automatically dispatched to the input method.
Also, when the window is opened using setVisible(true), the input context will prevent
deactivate and activate calls to the input method that might otherwise be caused.

Input methods must call

Window.dispose

on the
returned input method window when it is no longer needed.

**Parameters:** title

- the title to be displayed in the window's title bar,
if there is such a title bar.
A

null

value is treated as an empty string, "".
**Parameters:** attachToInputContext

- whether this window should share the input context
that corresponds to this input method context
**Returns:** a JFrame with special characteristics for use by input methods
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless

returns

true
**Since:** 1.4

---

#### createInputMethodJFrame

JFrame

createInputMethodJFrame​(

String

title,
boolean attachToInputContext)

Creates a top-level Swing JFrame for use by the input method.
The intended behavior of this window is:

- it floats above all document windows and dialogs

it and all components that it contains do not receive the focus

it has lightweight decorations, such as a reduced drag region without title

However, the actual behavior with respect to these three items is platform dependent.

The title may or may not be displayed, depending on the actual type of window created.

If attachToInputContext is true, the new window will share the input context that
corresponds to this input method context, so that events for components in the window
are automatically dispatched to the input method.
Also, when the window is opened using setVisible(true), the input context will prevent
deactivate and activate calls to the input method that might otherwise be caused.

Input methods must call

Window.dispose

on the
returned input method window when it is no longer needed.

it floats above all document windows and dialogs

it and all components that it contains do not receive the focus

it has lightweight decorations, such as a reduced drag region without title

The title may or may not be displayed, depending on the actual type of window created.

If attachToInputContext is true, the new window will share the input context that
corresponds to this input method context, so that events for components in the window
are automatically dispatched to the input method.
Also, when the window is opened using setVisible(true), the input context will prevent
deactivate and activate calls to the input method that might otherwise be caused.

Input methods must call

Window.dispose

on the
returned input method window when it is no longer needed.

If attachToInputContext is true, the new window will share the input context that
corresponds to this input method context, so that events for components in the window
are automatically dispatched to the input method.
Also, when the window is opened using setVisible(true), the input context will prevent
deactivate and activate calls to the input method that might otherwise be caused.

Input methods must call

Window.dispose

on the
returned input method window when it is no longer needed.

Input methods must call

Window.dispose

on the
returned input method window when it is no longer needed.

enableClientWindowNotification

```java
void enableClientWindowNotification​(
InputMethod
inputMethod,
boolean enable)
```

Enables or disables notification of the current client window's
location and state for the specified input method. When
notification is enabled, the input method's

notifyClientWindowChange

method is called as described in that
method's specification. Notification is automatically disabled
when the input method is disposed.

**Parameters:** inputMethod

- the input method for which notifications are
enabled or disabled
**Parameters:** enable

- true to enable, false to disable

---

#### enableClientWindowNotification

void enableClientWindowNotification​(

InputMethod

inputMethod,
boolean enable)

Enables or disables notification of the current client window's
location and state for the specified input method. When
notification is enabled, the input method's

notifyClientWindowChange

method is called as described in that
method's specification. Notification is automatically disabled
when the input method is disposed.

---

