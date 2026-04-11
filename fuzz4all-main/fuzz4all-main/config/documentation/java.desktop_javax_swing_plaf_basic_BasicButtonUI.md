# Class BasicButtonUI

**Source:** `java.desktop\javax\swing\plaf\basic\BasicButtonUI.html`

### Class Description

```java
public class
BasicButtonUI

extends
ButtonUI
```

BasicButton implementation

**Direct Known Subclasses:** BasicToggleButtonUI

,

MetalButtonUI

,

SynthButtonUI

---

### Field Details

#### protected int defaultTextIconGap

The default gap between a text and an icon.

---

#### protected int defaultTextShiftOffset

The default offset of a text.

---

### Constructor Details

#### public BasicButtonUI()

*No description found.*

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
c)

Returns an instance of

BasicButtonUI

.

**Parameters:**
- c

- a component

**Returns:**
- an instance of

BasicButtonUI

---

#### protected
String
getPropertyPrefix()

Returns the property prefix.

**Returns:**
- the property prefix

---

#### protected void installDefaults​(
AbstractButton
b)

Installs default properties.

**Parameters:**
- b

- an abstract button

---

#### protected void installListeners​(
AbstractButton
b)

Registers listeners.

**Parameters:**
- b

- an abstract button

---

#### protected void installKeyboardActions​(
AbstractButton
b)

Registers keyboard actions.

**Parameters:**
- b

- an abstract button

---

#### protected void uninstallKeyboardActions​(
AbstractButton
b)

Unregisters keyboard actions.

**Parameters:**
- b

- an abstract button

---

#### protected void uninstallListeners​(
AbstractButton
b)

Unregisters listeners.

**Parameters:**
- b

- an abstract button

---

#### protected void uninstallDefaults​(
AbstractButton
b)

Uninstalls default properties.

**Parameters:**
- b

- an abstract button

---

#### protected
BasicButtonListener
createButtonListener​(
AbstractButton
b)

Returns a new instance of

BasicButtonListener

.

**Parameters:**
- b

- an abstract button

**Returns:**
- a new instance of

BasicButtonListener

---

#### public int getDefaultTextIconGap​(
AbstractButton
b)

Returns the default gap between a text and an icon.

**Parameters:**
- b

- an abstract button

**Returns:**
- the default gap between text and an icon

---

#### protected void paintIcon​(
Graphics
g,

JComponent
c,

Rectangle
iconRect)

Paints an icon of the current button.

**Parameters:**
- g

- an instance of

Graphics
- c

- a component
- iconRect

- a bounding rectangle to render the icon

---

#### protected void paintText​(
Graphics
g,

JComponent
c,

Rectangle
textRect,

String
text)

Method which renders the text of the current button.

As of Java 2 platform v 1.4 this method should not be used or overriden.
Use the paintText method which takes the AbstractButton argument.

**Parameters:**
- g

- an instance of

Graphics
- c

- a component
- textRect

- a bounding rectangle to render the text
- text

- a string to render

---

#### protected void paintText​(
Graphics
g,

AbstractButton
b,

Rectangle
textRect,

String
text)

Method which renders the text of the current button.

**Parameters:**
- g

- Graphics context
- b

- Current button to render
- textRect

- Bounding rectangle to render the text
- text

- String to render

**Since:**
- 1.4

---

#### protected void paintFocus​(
Graphics
g,

AbstractButton
b,

Rectangle
viewRect,

Rectangle
textRect,

Rectangle
iconRect)

Paints a focused button.

**Parameters:**
- g

- an instance of

Graphics
- b

- an abstract button
- viewRect

- a bounding rectangle to render the button
- textRect

- a bounding rectangle to render the text
- iconRect

- a bounding rectangle to render the icon

---

#### protected void paintButtonPressed​(
Graphics
g,

AbstractButton
b)

Paints a pressed button.

**Parameters:**
- g

- an instance of

Graphics
- b

- an abstract button

---

#### protected void clearTextShiftOffset()

Clears the offset of the text.

---

#### protected void setTextShiftOffset()

Sets the offset of the text.

---

#### protected int getTextShiftOffset()

Returns the offset of the text.

**Returns:**
- the offset of the text

---

#### public int getBaseline​(
JComponent
c,
int width,
int height)

Returns the baseline.

**Overrides:**
- getBaseline

in class

ComponentUI

**Parameters:**
- c

-

JComponent

baseline is being requested for
- width

- the width to get the baseline for
- height

- the height to get the baseline for

**Returns:**
- baseline or a value < 0 indicating there is no reasonable
baseline

**Throws:**
- NullPointerException

- if

c

is

null
- IllegalArgumentException

- if width or height is < 0

**See Also:**
- JComponent.getBaseline(int, int)

**Since:**
- 1.6

---

#### public
Component.BaselineResizeBehavior
getBaselineResizeBehavior​(
JComponent
c)

Returns an enum indicating how the baseline of the component
changes as the size changes.

**Overrides:**
- getBaselineResizeBehavior

in class

ComponentUI

**Parameters:**
- c

-

JComponent

to return baseline resize behavior for

**Returns:**
- an enum indicating how the baseline changes as the component
size changes

**Throws:**
- NullPointerException

- if

c

is

null

**See Also:**
- JComponent.getBaseline(int, int)

**Since:**
- 1.6

---

### Additional Sections

#### Class BasicButtonUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.ButtonUI
- - javax.swing.plaf.basic.BasicButtonUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.ButtonUI
- - javax.swing.plaf.basic.BasicButtonUI

javax.swing.plaf.ButtonUI

- javax.swing.plaf.basic.BasicButtonUI

javax.swing.plaf.basic.BasicButtonUI

**Direct Known Subclasses:** BasicToggleButtonUI

,

MetalButtonUI

,

SynthButtonUI

```java
public class
BasicButtonUI

extends
ButtonUI
```

BasicButton implementation

public class

BasicButtonUI

extends

ButtonUI

BasicButton implementation

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected int

defaultTextIconGap

The default gap between a text and an icon.

protected int

defaultTextShiftOffset

The default offset of a text.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BasicButtonUI

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

clearTextShiftOffset

()

Clears the offset of the text.

protected

BasicButtonListener

createButtonListener

​(

AbstractButton

b)

Returns a new instance of

BasicButtonListener

.

static

ComponentUI

createUI

​(

JComponent

c)

Returns an instance of

BasicButtonUI

.

int

getBaseline

​(

JComponent

c,
int width,
int height)

Returns the baseline.

Component.BaselineResizeBehavior

getBaselineResizeBehavior

​(

JComponent

c)

Returns an enum indicating how the baseline of the component
changes as the size changes.

int

getDefaultTextIconGap

​(

AbstractButton

b)

Returns the default gap between a text and an icon.

protected

String

getPropertyPrefix

()

Returns the property prefix.

protected int

getTextShiftOffset

()

Returns the offset of the text.

protected void

installDefaults

​(

AbstractButton

b)

Installs default properties.

protected void

installKeyboardActions

​(

AbstractButton

b)

Registers keyboard actions.

protected void

installListeners

​(

AbstractButton

b)

Registers listeners.

protected void

paintButtonPressed

​(

Graphics

g,

AbstractButton

b)

Paints a pressed button.

protected void

paintFocus

​(

Graphics

g,

AbstractButton

b,

Rectangle

viewRect,

Rectangle

textRect,

Rectangle

iconRect)

Paints a focused button.

protected void

paintIcon

​(

Graphics

g,

JComponent

c,

Rectangle

iconRect)

Paints an icon of the current button.

protected void

paintText

​(

Graphics

g,

AbstractButton

b,

Rectangle

textRect,

String

text)

Method which renders the text of the current button.

protected void

paintText

​(

Graphics

g,

JComponent

c,

Rectangle

textRect,

String

text)

Method which renders the text of the current button.

protected void

setTextShiftOffset

()

Sets the offset of the text.

protected void

uninstallDefaults

​(

AbstractButton

b)

Uninstalls default properties.

protected void

uninstallKeyboardActions

​(

AbstractButton

b)

Unregisters keyboard actions.

protected void

uninstallListeners

​(

AbstractButton

b)

Unregisters listeners.

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getMaximumSize

,

getMinimumSize

,

getPreferredSize

,

installUI

,

paint

,

uninstallUI

,

update

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

protected int

defaultTextIconGap

The default gap between a text and an icon.

protected int

defaultTextShiftOffset

The default offset of a text.

---

#### Field Summary

The default gap between a text and an icon.

The default offset of a text.

Constructor Summary

Constructors

Constructor

Description

BasicButtonUI

()

---

#### Constructor Summary

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

clearTextShiftOffset

()

Clears the offset of the text.

protected

BasicButtonListener

createButtonListener

​(

AbstractButton

b)

Returns a new instance of

BasicButtonListener

.

static

ComponentUI

createUI

​(

JComponent

c)

Returns an instance of

BasicButtonUI

.

int

getBaseline

​(

JComponent

c,
int width,
int height)

Returns the baseline.

Component.BaselineResizeBehavior

getBaselineResizeBehavior

​(

JComponent

c)

Returns an enum indicating how the baseline of the component
changes as the size changes.

int

getDefaultTextIconGap

​(

AbstractButton

b)

Returns the default gap between a text and an icon.

protected

String

getPropertyPrefix

()

Returns the property prefix.

protected int

getTextShiftOffset

()

Returns the offset of the text.

protected void

installDefaults

​(

AbstractButton

b)

Installs default properties.

protected void

installKeyboardActions

​(

AbstractButton

b)

Registers keyboard actions.

protected void

installListeners

​(

AbstractButton

b)

Registers listeners.

protected void

paintButtonPressed

​(

Graphics

g,

AbstractButton

b)

Paints a pressed button.

protected void

paintFocus

​(

Graphics

g,

AbstractButton

b,

Rectangle

viewRect,

Rectangle

textRect,

Rectangle

iconRect)

Paints a focused button.

protected void

paintIcon

​(

Graphics

g,

JComponent

c,

Rectangle

iconRect)

Paints an icon of the current button.

protected void

paintText

​(

Graphics

g,

AbstractButton

b,

Rectangle

textRect,

String

text)

Method which renders the text of the current button.

protected void

paintText

​(

Graphics

g,

JComponent

c,

Rectangle

textRect,

String

text)

Method which renders the text of the current button.

protected void

setTextShiftOffset

()

Sets the offset of the text.

protected void

uninstallDefaults

​(

AbstractButton

b)

Uninstalls default properties.

protected void

uninstallKeyboardActions

​(

AbstractButton

b)

Unregisters keyboard actions.

protected void

uninstallListeners

​(

AbstractButton

b)

Unregisters listeners.

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getMaximumSize

,

getMinimumSize

,

getPreferredSize

,

installUI

,

paint

,

uninstallUI

,

update

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

Clears the offset of the text.

Returns a new instance of

BasicButtonListener

.

Returns an instance of

BasicButtonUI

.

Returns the baseline.

Returns an enum indicating how the baseline of the component
changes as the size changes.

Returns the default gap between a text and an icon.

Returns the property prefix.

Returns the offset of the text.

Installs default properties.

Registers keyboard actions.

Registers listeners.

Paints a pressed button.

Paints a focused button.

Paints an icon of the current button.

Method which renders the text of the current button.

Sets the offset of the text.

Uninstalls default properties.

Unregisters keyboard actions.

Unregisters listeners.

Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getMaximumSize

,

getMinimumSize

,

getPreferredSize

,

installUI

,

paint

,

uninstallUI

,

update

---

#### Methods declared in class javax.swing.plaf. ComponentUI

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

- defaultTextIconGap

```java
protected int defaultTextIconGap
```

The default gap between a text and an icon.

- defaultTextShiftOffset

```java
protected int defaultTextShiftOffset
```

The default offset of a text.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BasicButtonUI

```java
public BasicButtonUI()
```

============ METHOD DETAIL ==========

- Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Returns an instance of

BasicButtonUI

.

**Parameters:** c

- a component
**Returns:** an instance of

BasicButtonUI

- getPropertyPrefix

```java
protected
String
getPropertyPrefix()
```

Returns the property prefix.

**Returns:** the property prefix

- installDefaults

```java
protected void installDefaults​(
AbstractButton
b)
```

Installs default properties.

**Parameters:** b

- an abstract button

- installListeners

```java
protected void installListeners​(
AbstractButton
b)
```

Registers listeners.

**Parameters:** b

- an abstract button

- installKeyboardActions

```java
protected void installKeyboardActions​(
AbstractButton
b)
```

Registers keyboard actions.

**Parameters:** b

- an abstract button

- uninstallKeyboardActions

```java
protected void uninstallKeyboardActions​(
AbstractButton
b)
```

Unregisters keyboard actions.

**Parameters:** b

- an abstract button

- uninstallListeners

```java
protected void uninstallListeners​(
AbstractButton
b)
```

Unregisters listeners.

**Parameters:** b

- an abstract button

- uninstallDefaults

```java
protected void uninstallDefaults​(
AbstractButton
b)
```

Uninstalls default properties.

**Parameters:** b

- an abstract button

- createButtonListener

```java
protected
BasicButtonListener
createButtonListener​(
AbstractButton
b)
```

Returns a new instance of

BasicButtonListener

.

**Parameters:** b

- an abstract button
**Returns:** a new instance of

BasicButtonListener

- getDefaultTextIconGap

```java
public int getDefaultTextIconGap​(
AbstractButton
b)
```

Returns the default gap between a text and an icon.

**Parameters:** b

- an abstract button
**Returns:** the default gap between text and an icon

- paintIcon

```java
protected void paintIcon​(
Graphics
g,

JComponent
c,

Rectangle
iconRect)
```

Paints an icon of the current button.

**Parameters:** g

- an instance of

Graphics
**Parameters:** c

- a component
**Parameters:** iconRect

- a bounding rectangle to render the icon

- paintText

```java
protected void paintText​(
Graphics
g,

JComponent
c,

Rectangle
textRect,

String
text)
```

Method which renders the text of the current button.

As of Java 2 platform v 1.4 this method should not be used or overriden.
Use the paintText method which takes the AbstractButton argument.

**Parameters:** g

- an instance of

Graphics
**Parameters:** c

- a component
**Parameters:** textRect

- a bounding rectangle to render the text
**Parameters:** text

- a string to render

- paintText

```java
protected void paintText​(
Graphics
g,

AbstractButton
b,

Rectangle
textRect,

String
text)
```

Method which renders the text of the current button.

**Parameters:** g

- Graphics context
**Parameters:** b

- Current button to render
**Parameters:** textRect

- Bounding rectangle to render the text
**Parameters:** text

- String to render
**Since:** 1.4

- paintFocus

```java
protected void paintFocus​(
Graphics
g,

AbstractButton
b,

Rectangle
viewRect,

Rectangle
textRect,

Rectangle
iconRect)
```

Paints a focused button.

**Parameters:** g

- an instance of

Graphics
**Parameters:** b

- an abstract button
**Parameters:** viewRect

- a bounding rectangle to render the button
**Parameters:** textRect

- a bounding rectangle to render the text
**Parameters:** iconRect

- a bounding rectangle to render the icon

- paintButtonPressed

```java
protected void paintButtonPressed​(
Graphics
g,

AbstractButton
b)
```

Paints a pressed button.

**Parameters:** g

- an instance of

Graphics
**Parameters:** b

- an abstract button

- clearTextShiftOffset

```java
protected void clearTextShiftOffset()
```

Clears the offset of the text.

- setTextShiftOffset

```java
protected void setTextShiftOffset()
```

Sets the offset of the text.

- getTextShiftOffset

```java
protected int getTextShiftOffset()
```

Returns the offset of the text.

**Returns:** the offset of the text

- getBaseline

```java
public int getBaseline​(
JComponent
c,
int width,
int height)
```

Returns the baseline.

**Overrides:** getBaseline

in class

ComponentUI
**Parameters:** c

-

JComponent

baseline is being requested for
**Parameters:** width

- the width to get the baseline for
**Parameters:** height

- the height to get the baseline for
**Returns:** baseline or a value < 0 indicating there is no reasonable
baseline
**Throws:** NullPointerException

- if

c

is

null
**Throws:** IllegalArgumentException

- if width or height is < 0
**Since:** 1.6
**See Also:** JComponent.getBaseline(int, int)

- getBaselineResizeBehavior

```java
public
Component.BaselineResizeBehavior
getBaselineResizeBehavior​(
JComponent
c)
```

Returns an enum indicating how the baseline of the component
changes as the size changes.

**Overrides:** getBaselineResizeBehavior

in class

ComponentUI
**Parameters:** c

-

JComponent

to return baseline resize behavior for
**Returns:** an enum indicating how the baseline changes as the component
size changes
**Throws:** NullPointerException

- if

c

is

null
**Since:** 1.6
**See Also:** JComponent.getBaseline(int, int)

Field Detail

- defaultTextIconGap

```java
protected int defaultTextIconGap
```

The default gap between a text and an icon.

- defaultTextShiftOffset

```java
protected int defaultTextShiftOffset
```

The default offset of a text.

---

#### Field Detail

defaultTextIconGap

```java
protected int defaultTextIconGap
```

The default gap between a text and an icon.

---

#### defaultTextIconGap

protected int defaultTextIconGap

The default gap between a text and an icon.

defaultTextShiftOffset

```java
protected int defaultTextShiftOffset
```

The default offset of a text.

---

#### defaultTextShiftOffset

protected int defaultTextShiftOffset

The default offset of a text.

Constructor Detail

- BasicButtonUI

```java
public BasicButtonUI()
```

---

#### Constructor Detail

BasicButtonUI

```java
public BasicButtonUI()
```

---

#### BasicButtonUI

public BasicButtonUI()

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Returns an instance of

BasicButtonUI

.

**Parameters:** c

- a component
**Returns:** an instance of

BasicButtonUI

- getPropertyPrefix

```java
protected
String
getPropertyPrefix()
```

Returns the property prefix.

**Returns:** the property prefix

- installDefaults

```java
protected void installDefaults​(
AbstractButton
b)
```

Installs default properties.

**Parameters:** b

- an abstract button

- installListeners

```java
protected void installListeners​(
AbstractButton
b)
```

Registers listeners.

**Parameters:** b

- an abstract button

- installKeyboardActions

```java
protected void installKeyboardActions​(
AbstractButton
b)
```

Registers keyboard actions.

**Parameters:** b

- an abstract button

- uninstallKeyboardActions

```java
protected void uninstallKeyboardActions​(
AbstractButton
b)
```

Unregisters keyboard actions.

**Parameters:** b

- an abstract button

- uninstallListeners

```java
protected void uninstallListeners​(
AbstractButton
b)
```

Unregisters listeners.

**Parameters:** b

- an abstract button

- uninstallDefaults

```java
protected void uninstallDefaults​(
AbstractButton
b)
```

Uninstalls default properties.

**Parameters:** b

- an abstract button

- createButtonListener

```java
protected
BasicButtonListener
createButtonListener​(
AbstractButton
b)
```

Returns a new instance of

BasicButtonListener

.

**Parameters:** b

- an abstract button
**Returns:** a new instance of

BasicButtonListener

- getDefaultTextIconGap

```java
public int getDefaultTextIconGap​(
AbstractButton
b)
```

Returns the default gap between a text and an icon.

**Parameters:** b

- an abstract button
**Returns:** the default gap between text and an icon

- paintIcon

```java
protected void paintIcon​(
Graphics
g,

JComponent
c,

Rectangle
iconRect)
```

Paints an icon of the current button.

**Parameters:** g

- an instance of

Graphics
**Parameters:** c

- a component
**Parameters:** iconRect

- a bounding rectangle to render the icon

- paintText

```java
protected void paintText​(
Graphics
g,

JComponent
c,

Rectangle
textRect,

String
text)
```

Method which renders the text of the current button.

As of Java 2 platform v 1.4 this method should not be used or overriden.
Use the paintText method which takes the AbstractButton argument.

**Parameters:** g

- an instance of

Graphics
**Parameters:** c

- a component
**Parameters:** textRect

- a bounding rectangle to render the text
**Parameters:** text

- a string to render

- paintText

```java
protected void paintText​(
Graphics
g,

AbstractButton
b,

Rectangle
textRect,

String
text)
```

Method which renders the text of the current button.

**Parameters:** g

- Graphics context
**Parameters:** b

- Current button to render
**Parameters:** textRect

- Bounding rectangle to render the text
**Parameters:** text

- String to render
**Since:** 1.4

- paintFocus

```java
protected void paintFocus​(
Graphics
g,

AbstractButton
b,

Rectangle
viewRect,

Rectangle
textRect,

Rectangle
iconRect)
```

Paints a focused button.

**Parameters:** g

- an instance of

Graphics
**Parameters:** b

- an abstract button
**Parameters:** viewRect

- a bounding rectangle to render the button
**Parameters:** textRect

- a bounding rectangle to render the text
**Parameters:** iconRect

- a bounding rectangle to render the icon

- paintButtonPressed

```java
protected void paintButtonPressed​(
Graphics
g,

AbstractButton
b)
```

Paints a pressed button.

**Parameters:** g

- an instance of

Graphics
**Parameters:** b

- an abstract button

- clearTextShiftOffset

```java
protected void clearTextShiftOffset()
```

Clears the offset of the text.

- setTextShiftOffset

```java
protected void setTextShiftOffset()
```

Sets the offset of the text.

- getTextShiftOffset

```java
protected int getTextShiftOffset()
```

Returns the offset of the text.

**Returns:** the offset of the text

- getBaseline

```java
public int getBaseline​(
JComponent
c,
int width,
int height)
```

Returns the baseline.

**Overrides:** getBaseline

in class

ComponentUI
**Parameters:** c

-

JComponent

baseline is being requested for
**Parameters:** width

- the width to get the baseline for
**Parameters:** height

- the height to get the baseline for
**Returns:** baseline or a value < 0 indicating there is no reasonable
baseline
**Throws:** NullPointerException

- if

c

is

null
**Throws:** IllegalArgumentException

- if width or height is < 0
**Since:** 1.6
**See Also:** JComponent.getBaseline(int, int)

- getBaselineResizeBehavior

```java
public
Component.BaselineResizeBehavior
getBaselineResizeBehavior​(
JComponent
c)
```

Returns an enum indicating how the baseline of the component
changes as the size changes.

**Overrides:** getBaselineResizeBehavior

in class

ComponentUI
**Parameters:** c

-

JComponent

to return baseline resize behavior for
**Returns:** an enum indicating how the baseline changes as the component
size changes
**Throws:** NullPointerException

- if

c

is

null
**Since:** 1.6
**See Also:** JComponent.getBaseline(int, int)

---

#### Method Detail

createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Returns an instance of

BasicButtonUI

.

**Parameters:** c

- a component
**Returns:** an instance of

BasicButtonUI

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

c)

Returns an instance of

BasicButtonUI

.

getPropertyPrefix

```java
protected
String
getPropertyPrefix()
```

Returns the property prefix.

**Returns:** the property prefix

---

#### getPropertyPrefix

protected

String

getPropertyPrefix()

Returns the property prefix.

installDefaults

```java
protected void installDefaults​(
AbstractButton
b)
```

Installs default properties.

**Parameters:** b

- an abstract button

---

#### installDefaults

protected void installDefaults​(

AbstractButton

b)

Installs default properties.

installListeners

```java
protected void installListeners​(
AbstractButton
b)
```

Registers listeners.

**Parameters:** b

- an abstract button

---

#### installListeners

protected void installListeners​(

AbstractButton

b)

Registers listeners.

installKeyboardActions

```java
protected void installKeyboardActions​(
AbstractButton
b)
```

Registers keyboard actions.

**Parameters:** b

- an abstract button

---

#### installKeyboardActions

protected void installKeyboardActions​(

AbstractButton

b)

Registers keyboard actions.

uninstallKeyboardActions

```java
protected void uninstallKeyboardActions​(
AbstractButton
b)
```

Unregisters keyboard actions.

**Parameters:** b

- an abstract button

---

#### uninstallKeyboardActions

protected void uninstallKeyboardActions​(

AbstractButton

b)

Unregisters keyboard actions.

uninstallListeners

```java
protected void uninstallListeners​(
AbstractButton
b)
```

Unregisters listeners.

**Parameters:** b

- an abstract button

---

#### uninstallListeners

protected void uninstallListeners​(

AbstractButton

b)

Unregisters listeners.

uninstallDefaults

```java
protected void uninstallDefaults​(
AbstractButton
b)
```

Uninstalls default properties.

**Parameters:** b

- an abstract button

---

#### uninstallDefaults

protected void uninstallDefaults​(

AbstractButton

b)

Uninstalls default properties.

createButtonListener

```java
protected
BasicButtonListener
createButtonListener​(
AbstractButton
b)
```

Returns a new instance of

BasicButtonListener

.

**Parameters:** b

- an abstract button
**Returns:** a new instance of

BasicButtonListener

---

#### createButtonListener

protected

BasicButtonListener

createButtonListener​(

AbstractButton

b)

Returns a new instance of

BasicButtonListener

.

getDefaultTextIconGap

```java
public int getDefaultTextIconGap​(
AbstractButton
b)
```

Returns the default gap between a text and an icon.

**Parameters:** b

- an abstract button
**Returns:** the default gap between text and an icon

---

#### getDefaultTextIconGap

public int getDefaultTextIconGap​(

AbstractButton

b)

Returns the default gap between a text and an icon.

paintIcon

```java
protected void paintIcon​(
Graphics
g,

JComponent
c,

Rectangle
iconRect)
```

Paints an icon of the current button.

**Parameters:** g

- an instance of

Graphics
**Parameters:** c

- a component
**Parameters:** iconRect

- a bounding rectangle to render the icon

---

#### paintIcon

protected void paintIcon​(

Graphics

g,

JComponent

c,

Rectangle

iconRect)

Paints an icon of the current button.

paintText

```java
protected void paintText​(
Graphics
g,

JComponent
c,

Rectangle
textRect,

String
text)
```

Method which renders the text of the current button.

As of Java 2 platform v 1.4 this method should not be used or overriden.
Use the paintText method which takes the AbstractButton argument.

**Parameters:** g

- an instance of

Graphics
**Parameters:** c

- a component
**Parameters:** textRect

- a bounding rectangle to render the text
**Parameters:** text

- a string to render

---

#### paintText

protected void paintText​(

Graphics

g,

JComponent

c,

Rectangle

textRect,

String

text)

Method which renders the text of the current button.

As of Java 2 platform v 1.4 this method should not be used or overriden.
Use the paintText method which takes the AbstractButton argument.

paintText

```java
protected void paintText​(
Graphics
g,

AbstractButton
b,

Rectangle
textRect,

String
text)
```

Method which renders the text of the current button.

**Parameters:** g

- Graphics context
**Parameters:** b

- Current button to render
**Parameters:** textRect

- Bounding rectangle to render the text
**Parameters:** text

- String to render
**Since:** 1.4

---

#### paintText

protected void paintText​(

Graphics

g,

AbstractButton

b,

Rectangle

textRect,

String

text)

Method which renders the text of the current button.

paintFocus

```java
protected void paintFocus​(
Graphics
g,

AbstractButton
b,

Rectangle
viewRect,

Rectangle
textRect,

Rectangle
iconRect)
```

Paints a focused button.

**Parameters:** g

- an instance of

Graphics
**Parameters:** b

- an abstract button
**Parameters:** viewRect

- a bounding rectangle to render the button
**Parameters:** textRect

- a bounding rectangle to render the text
**Parameters:** iconRect

- a bounding rectangle to render the icon

---

#### paintFocus

protected void paintFocus​(

Graphics

g,

AbstractButton

b,

Rectangle

viewRect,

Rectangle

textRect,

Rectangle

iconRect)

Paints a focused button.

paintButtonPressed

```java
protected void paintButtonPressed​(
Graphics
g,

AbstractButton
b)
```

Paints a pressed button.

**Parameters:** g

- an instance of

Graphics
**Parameters:** b

- an abstract button

---

#### paintButtonPressed

protected void paintButtonPressed​(

Graphics

g,

AbstractButton

b)

Paints a pressed button.

clearTextShiftOffset

```java
protected void clearTextShiftOffset()
```

Clears the offset of the text.

---

#### clearTextShiftOffset

protected void clearTextShiftOffset()

Clears the offset of the text.

setTextShiftOffset

```java
protected void setTextShiftOffset()
```

Sets the offset of the text.

---

#### setTextShiftOffset

protected void setTextShiftOffset()

Sets the offset of the text.

getTextShiftOffset

```java
protected int getTextShiftOffset()
```

Returns the offset of the text.

**Returns:** the offset of the text

---

#### getTextShiftOffset

protected int getTextShiftOffset()

Returns the offset of the text.

getBaseline

```java
public int getBaseline​(
JComponent
c,
int width,
int height)
```

Returns the baseline.

**Overrides:** getBaseline

in class

ComponentUI
**Parameters:** c

-

JComponent

baseline is being requested for
**Parameters:** width

- the width to get the baseline for
**Parameters:** height

- the height to get the baseline for
**Returns:** baseline or a value < 0 indicating there is no reasonable
baseline
**Throws:** NullPointerException

- if

c

is

null
**Throws:** IllegalArgumentException

- if width or height is < 0
**Since:** 1.6
**See Also:** JComponent.getBaseline(int, int)

---

#### getBaseline

public int getBaseline​(

JComponent

c,
int width,
int height)

Returns the baseline.

getBaselineResizeBehavior

```java
public
Component.BaselineResizeBehavior
getBaselineResizeBehavior​(
JComponent
c)
```

Returns an enum indicating how the baseline of the component
changes as the size changes.

**Overrides:** getBaselineResizeBehavior

in class

ComponentUI
**Parameters:** c

-

JComponent

to return baseline resize behavior for
**Returns:** an enum indicating how the baseline changes as the component
size changes
**Throws:** NullPointerException

- if

c

is

null
**Since:** 1.6
**See Also:** JComponent.getBaseline(int, int)

---

#### getBaselineResizeBehavior

public

Component.BaselineResizeBehavior

getBaselineResizeBehavior​(

JComponent

c)

Returns an enum indicating how the baseline of the component
changes as the size changes.

---

