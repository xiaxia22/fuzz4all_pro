# Class BasicLabelUI

**Source:** `java.desktop\javax\swing\plaf\basic\BasicLabelUI.html`

### Class Description

```java
public class
BasicLabelUI

extends
LabelUI

implements
PropertyChangeListener
```

A Windows L&F implementation of LabelUI. This implementation
is completely static, i.e. there's only one UIView implementation
that's shared by all JLabel objects.

**All Implemented Interfaces:** PropertyChangeListener

,

EventListener

---

### Field Details

#### protected static
BasicLabelUI
labelUI

The default

BasicLabelUI

instance. This field might
not be used. To change the default instance use a subclass which
overrides the

createUI

method, and place that class
name in defaults table under the key "LabelUI".

---

### Constructor Details

#### public BasicLabelUI()

*No description found.*

---

### Method Details

#### protected
String
layoutCL​(
JLabel
label,

FontMetrics
fontMetrics,

String
text,

Icon
icon,

Rectangle
viewR,

Rectangle
iconR,

Rectangle
textR)

Forwards the call to SwingUtilities.layoutCompoundLabel().
This method is here so that a subclass could do Label specific
layout and to shorten the method name a little.

**Parameters:**
- label

- an instance of

JLabel
- fontMetrics

- a font metrics
- text

- a text
- icon

- an icon
- viewR

- a bounding rectangle to lay out label
- iconR

- a bounding rectangle to lay out icon
- textR

- a bounding rectangle to lay out text

**Returns:**
- a possibly clipped version of the compound labels string

**See Also:**
- SwingUtilities.layoutCompoundLabel(javax.swing.JComponent, java.awt.FontMetrics, java.lang.String, javax.swing.Icon, int, int, int, int, java.awt.Rectangle, java.awt.Rectangle, java.awt.Rectangle, int)

---

#### protected void paintEnabledText​(
JLabel
l,

Graphics
g,

String
s,
int textX,
int textY)

Paint clippedText at textX, textY with the labels foreground color.

**Parameters:**
- l

- an instance of

JLabel
- g

- an instance of

Graphics
- s

- a text
- textX

- an X coordinate
- textY

- an Y coordinate

**See Also:**
- paint(java.awt.Graphics, javax.swing.JComponent)

,

paintDisabledText(javax.swing.JLabel, java.awt.Graphics, java.lang.String, int, int)

---

#### protected void paintDisabledText​(
JLabel
l,

Graphics
g,

String
s,
int textX,
int textY)

Paint clippedText at textX, textY with background.lighter() and then
shifted down and to the right by one pixel with background.darker().

**Parameters:**
- l

- an instance of

JLabel
- g

- an instance of

Graphics
- s

- a text
- textX

- an X coordinate
- textY

- an Y coordinate

**See Also:**
- paint(java.awt.Graphics, javax.swing.JComponent)

,

paintEnabledText(javax.swing.JLabel, java.awt.Graphics, java.lang.String, int, int)

---

#### public void paint​(
Graphics
g,

JComponent
c)

Paints the label text with the foreground color, if the label is opaque
then paints the entire background with the background color. The Label
text is drawn by

paintEnabledText(javax.swing.JLabel, java.awt.Graphics, java.lang.String, int, int)

or

paintDisabledText(javax.swing.JLabel, java.awt.Graphics, java.lang.String, int, int)

.
The locations of the label parts are computed by

layoutCL(javax.swing.JLabel, java.awt.FontMetrics, java.lang.String, javax.swing.Icon, java.awt.Rectangle, java.awt.Rectangle, java.awt.Rectangle)

.

**Overrides:**
- paint

in class

ComponentUI

**Parameters:**
- g

- the

Graphics

context in which to paint
- c

- the component being painted;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components

**See Also:**
- paintEnabledText(javax.swing.JLabel, java.awt.Graphics, java.lang.String, int, int)

,

paintDisabledText(javax.swing.JLabel, java.awt.Graphics, java.lang.String, int, int)

,

layoutCL(javax.swing.JLabel, java.awt.FontMetrics, java.lang.String, javax.swing.Icon, java.awt.Rectangle, java.awt.Rectangle, java.awt.Rectangle)

---

#### public
Dimension
getMinimumSize​(
JComponent
c)

Description copied from class:

ComponentUI

**Overrides:**
- getMinimumSize

in class

ComponentUI

**Parameters:**
- c

- the component whose minimum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components

**Returns:**
- getPreferredSize(c)

**See Also:**
- JComponent.getMinimumSize()

,

LayoutManager.minimumLayoutSize(java.awt.Container)

,

ComponentUI.getPreferredSize(javax.swing.JComponent)

---

#### public
Dimension
getMaximumSize​(
JComponent
c)

Description copied from class:

ComponentUI

**Overrides:**
- getMaximumSize

in class

ComponentUI

**Parameters:**
- c

- the component whose maximum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components

**Returns:**
- getPreferredSize(c)

**See Also:**
- JComponent.getMaximumSize()

,

LayoutManager2.maximumLayoutSize(java.awt.Container)

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

#### protected void installDefaults​(
JLabel
c)

Installs default properties.

**Parameters:**
- c

- an instance of

JLabel

---

#### protected void installListeners​(
JLabel
c)

Registers listeners.

**Parameters:**
- c

- an instance of

JLabel

---

#### protected void installComponents​(
JLabel
c)

Registers components.

**Parameters:**
- c

- an instance of

JLabel

---

#### protected void installKeyboardActions​(
JLabel
l)

Registers keyboard actions.

**Parameters:**
- l

- an instance of

JLabel

---

#### protected void uninstallDefaults​(
JLabel
c)

Uninstalls default properties.

**Parameters:**
- c

- an instance of

JLabel

---

#### protected void uninstallListeners​(
JLabel
c)

Unregisters listeners.

**Parameters:**
- c

- an instance of

JLabel

---

#### protected void uninstallComponents​(
JLabel
c)

Unregisters components.

**Parameters:**
- c

- an instance of

JLabel

---

#### protected void uninstallKeyboardActions​(
JLabel
c)

Unregisters keyboard actions.

**Parameters:**
- c

- an instance of

JLabel

---

#### public static
ComponentUI
createUI​(
JComponent
c)

Returns an instance of

BasicLabelUI

.

**Parameters:**
- c

- a component

**Returns:**
- an instance of

BasicLabelUI

---

### Additional Sections

#### Class BasicLabelUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.LabelUI
- - javax.swing.plaf.basic.BasicLabelUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.LabelUI
- - javax.swing.plaf.basic.BasicLabelUI

javax.swing.plaf.LabelUI

- javax.swing.plaf.basic.BasicLabelUI

javax.swing.plaf.basic.BasicLabelUI

**All Implemented Interfaces:** PropertyChangeListener

,

EventListener

**Direct Known Subclasses:** MetalLabelUI

,

SynthLabelUI

```java
public class
BasicLabelUI

extends
LabelUI

implements
PropertyChangeListener
```

A Windows L&F implementation of LabelUI. This implementation
is completely static, i.e. there's only one UIView implementation
that's shared by all JLabel objects.

public class

BasicLabelUI

extends

LabelUI

implements

PropertyChangeListener

A Windows L&F implementation of LabelUI. This implementation
is completely static, i.e. there's only one UIView implementation
that's shared by all JLabel objects.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected static

BasicLabelUI

labelUI

The default

BasicLabelUI

instance.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BasicLabelUI

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

static

ComponentUI

createUI

​(

JComponent

c)

Returns an instance of

BasicLabelUI

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

Dimension

getMaximumSize

​(

JComponent

c)

Returns the specified component's maximum size appropriate for
the look and feel.

Dimension

getMinimumSize

​(

JComponent

c)

Returns the specified component's minimum size appropriate for
the look and feel.

protected void

installComponents

​(

JLabel

c)

Registers components.

protected void

installDefaults

​(

JLabel

c)

Installs default properties.

protected void

installKeyboardActions

​(

JLabel

l)

Registers keyboard actions.

protected void

installListeners

​(

JLabel

c)

Registers listeners.

protected

String

layoutCL

​(

JLabel

label,

FontMetrics

fontMetrics,

String

text,

Icon

icon,

Rectangle

viewR,

Rectangle

iconR,

Rectangle

textR)

Forwards the call to SwingUtilities.layoutCompoundLabel().

void

paint

​(

Graphics

g,

JComponent

c)

Paints the label text with the foreground color, if the label is opaque
then paints the entire background with the background color.

protected void

paintDisabledText

​(

JLabel

l,

Graphics

g,

String

s,
int textX,
int textY)

Paint clippedText at textX, textY with background.lighter() and then
shifted down and to the right by one pixel with background.darker().

protected void

paintEnabledText

​(

JLabel

l,

Graphics

g,

String

s,
int textX,
int textY)

Paint clippedText at textX, textY with the labels foreground color.

protected void

uninstallComponents

​(

JLabel

c)

Unregisters components.

protected void

uninstallDefaults

​(

JLabel

c)

Uninstalls default properties.

protected void

uninstallKeyboardActions

​(

JLabel

c)

Unregisters keyboard actions.

protected void

uninstallListeners

​(

JLabel

c)

Unregisters listeners.

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getPreferredSize

,

installUI

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

- Methods declared in interface java.beans.

PropertyChangeListener

propertyChange

Field Summary

Fields

Modifier and Type

Field

Description

protected static

BasicLabelUI

labelUI

The default

BasicLabelUI

instance.

---

#### Field Summary

The default

BasicLabelUI

instance.

Constructor Summary

Constructors

Constructor

Description

BasicLabelUI

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

static

ComponentUI

createUI

​(

JComponent

c)

Returns an instance of

BasicLabelUI

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

Dimension

getMaximumSize

​(

JComponent

c)

Returns the specified component's maximum size appropriate for
the look and feel.

Dimension

getMinimumSize

​(

JComponent

c)

Returns the specified component's minimum size appropriate for
the look and feel.

protected void

installComponents

​(

JLabel

c)

Registers components.

protected void

installDefaults

​(

JLabel

c)

Installs default properties.

protected void

installKeyboardActions

​(

JLabel

l)

Registers keyboard actions.

protected void

installListeners

​(

JLabel

c)

Registers listeners.

protected

String

layoutCL

​(

JLabel

label,

FontMetrics

fontMetrics,

String

text,

Icon

icon,

Rectangle

viewR,

Rectangle

iconR,

Rectangle

textR)

Forwards the call to SwingUtilities.layoutCompoundLabel().

void

paint

​(

Graphics

g,

JComponent

c)

Paints the label text with the foreground color, if the label is opaque
then paints the entire background with the background color.

protected void

paintDisabledText

​(

JLabel

l,

Graphics

g,

String

s,
int textX,
int textY)

Paint clippedText at textX, textY with background.lighter() and then
shifted down and to the right by one pixel with background.darker().

protected void

paintEnabledText

​(

JLabel

l,

Graphics

g,

String

s,
int textX,
int textY)

Paint clippedText at textX, textY with the labels foreground color.

protected void

uninstallComponents

​(

JLabel

c)

Unregisters components.

protected void

uninstallDefaults

​(

JLabel

c)

Uninstalls default properties.

protected void

uninstallKeyboardActions

​(

JLabel

c)

Unregisters keyboard actions.

protected void

uninstallListeners

​(

JLabel

c)

Unregisters listeners.

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getPreferredSize

,

installUI

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

- Methods declared in interface java.beans.

PropertyChangeListener

propertyChange

---

#### Method Summary

Returns an instance of

BasicLabelUI

.

Returns the baseline.

Returns an enum indicating how the baseline of the component
changes as the size changes.

Returns the specified component's maximum size appropriate for
the look and feel.

Returns the specified component's minimum size appropriate for
the look and feel.

Registers components.

Installs default properties.

Registers keyboard actions.

Registers listeners.

Forwards the call to SwingUtilities.layoutCompoundLabel().

Paints the label text with the foreground color, if the label is opaque
then paints the entire background with the background color.

Paint clippedText at textX, textY with background.lighter() and then
shifted down and to the right by one pixel with background.darker().

Paint clippedText at textX, textY with the labels foreground color.

Unregisters components.

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

getPreferredSize

,

installUI

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

Methods declared in interface java.beans.

PropertyChangeListener

propertyChange

---

#### Methods declared in interface java.beans. PropertyChangeListener

============ FIELD DETAIL ===========

- Field Detail

- labelUI

```java
protected static
BasicLabelUI
labelUI
```

The default

BasicLabelUI

instance. This field might
not be used. To change the default instance use a subclass which
overrides the

createUI

method, and place that class
name in defaults table under the key "LabelUI".

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BasicLabelUI

```java
public BasicLabelUI()
```

============ METHOD DETAIL ==========

- Method Detail

- layoutCL

```java
protected
String
layoutCL​(
JLabel
label,

FontMetrics
fontMetrics,

String
text,

Icon
icon,

Rectangle
viewR,

Rectangle
iconR,

Rectangle
textR)
```

Forwards the call to SwingUtilities.layoutCompoundLabel().
This method is here so that a subclass could do Label specific
layout and to shorten the method name a little.

**Parameters:** label

- an instance of

JLabel
**Parameters:** fontMetrics

- a font metrics
**Parameters:** text

- a text
**Parameters:** icon

- an icon
**Parameters:** viewR

- a bounding rectangle to lay out label
**Parameters:** iconR

- a bounding rectangle to lay out icon
**Parameters:** textR

- a bounding rectangle to lay out text
**Returns:** a possibly clipped version of the compound labels string
**See Also:** SwingUtilities.layoutCompoundLabel(javax.swing.JComponent, java.awt.FontMetrics, java.lang.String, javax.swing.Icon, int, int, int, int, java.awt.Rectangle, java.awt.Rectangle, java.awt.Rectangle, int)

- paintEnabledText

```java
protected void paintEnabledText​(
JLabel
l,

Graphics
g,

String
s,
int textX,
int textY)
```

Paint clippedText at textX, textY with the labels foreground color.

**Parameters:** l

- an instance of

JLabel
**Parameters:** g

- an instance of

Graphics
**Parameters:** s

- a text
**Parameters:** textX

- an X coordinate
**Parameters:** textY

- an Y coordinate
**See Also:** paint(java.awt.Graphics, javax.swing.JComponent)

,

paintDisabledText(javax.swing.JLabel, java.awt.Graphics, java.lang.String, int, int)

- paintDisabledText

```java
protected void paintDisabledText​(
JLabel
l,

Graphics
g,

String
s,
int textX,
int textY)
```

Paint clippedText at textX, textY with background.lighter() and then
shifted down and to the right by one pixel with background.darker().

**Parameters:** l

- an instance of

JLabel
**Parameters:** g

- an instance of

Graphics
**Parameters:** s

- a text
**Parameters:** textX

- an X coordinate
**Parameters:** textY

- an Y coordinate
**See Also:** paint(java.awt.Graphics, javax.swing.JComponent)

,

paintEnabledText(javax.swing.JLabel, java.awt.Graphics, java.lang.String, int, int)

- paint

```java
public void paint​(
Graphics
g,

JComponent
c)
```

Paints the label text with the foreground color, if the label is opaque
then paints the entire background with the background color. The Label
text is drawn by

paintEnabledText(javax.swing.JLabel, java.awt.Graphics, java.lang.String, int, int)

or

paintDisabledText(javax.swing.JLabel, java.awt.Graphics, java.lang.String, int, int)

.
The locations of the label parts are computed by

layoutCL(javax.swing.JLabel, java.awt.FontMetrics, java.lang.String, javax.swing.Icon, java.awt.Rectangle, java.awt.Rectangle, java.awt.Rectangle)

.

**Overrides:** paint

in class

ComponentUI
**Parameters:** g

- the

Graphics

context in which to paint
**Parameters:** c

- the component being painted;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**See Also:** paintEnabledText(javax.swing.JLabel, java.awt.Graphics, java.lang.String, int, int)

,

paintDisabledText(javax.swing.JLabel, java.awt.Graphics, java.lang.String, int, int)

,

layoutCL(javax.swing.JLabel, java.awt.FontMetrics, java.lang.String, javax.swing.Icon, java.awt.Rectangle, java.awt.Rectangle, java.awt.Rectangle)

- getMinimumSize

```java
public
Dimension
getMinimumSize​(
JComponent
c)
```

Description copied from class:

ComponentUI

Returns the specified component's minimum size appropriate for
the look and feel. If

null

is returned, the minimum
size will be calculated by the component's layout manager instead
(this is the preferred approach for any component with a specific
layout manager installed). The default implementation of this
method invokes

getPreferredSize

and returns that value.

**Overrides:** getMinimumSize

in class

ComponentUI
**Parameters:** c

- the component whose minimum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Returns:** getPreferredSize(c)
**See Also:** JComponent.getMinimumSize()

,

LayoutManager.minimumLayoutSize(java.awt.Container)

,

ComponentUI.getPreferredSize(javax.swing.JComponent)

- getMaximumSize

```java
public
Dimension
getMaximumSize​(
JComponent
c)
```

Description copied from class:

ComponentUI

Returns the specified component's maximum size appropriate for
the look and feel. If

null

is returned, the maximum
size will be calculated by the component's layout manager instead
(this is the preferred approach for any component with a specific
layout manager installed). The default implementation of this
method invokes

getPreferredSize

and returns that value.

**Overrides:** getMaximumSize

in class

ComponentUI
**Parameters:** c

- the component whose maximum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Returns:** getPreferredSize(c)
**See Also:** JComponent.getMaximumSize()

,

LayoutManager2.maximumLayoutSize(java.awt.Container)

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

- installDefaults

```java
protected void installDefaults​(
JLabel
c)
```

Installs default properties.

**Parameters:** c

- an instance of

JLabel

- installListeners

```java
protected void installListeners​(
JLabel
c)
```

Registers listeners.

**Parameters:** c

- an instance of

JLabel

- installComponents

```java
protected void installComponents​(
JLabel
c)
```

Registers components.

**Parameters:** c

- an instance of

JLabel

- installKeyboardActions

```java
protected void installKeyboardActions​(
JLabel
l)
```

Registers keyboard actions.

**Parameters:** l

- an instance of

JLabel

- uninstallDefaults

```java
protected void uninstallDefaults​(
JLabel
c)
```

Uninstalls default properties.

**Parameters:** c

- an instance of

JLabel

- uninstallListeners

```java
protected void uninstallListeners​(
JLabel
c)
```

Unregisters listeners.

**Parameters:** c

- an instance of

JLabel

- uninstallComponents

```java
protected void uninstallComponents​(
JLabel
c)
```

Unregisters components.

**Parameters:** c

- an instance of

JLabel

- uninstallKeyboardActions

```java
protected void uninstallKeyboardActions​(
JLabel
c)
```

Unregisters keyboard actions.

**Parameters:** c

- an instance of

JLabel

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Returns an instance of

BasicLabelUI

.

**Parameters:** c

- a component
**Returns:** an instance of

BasicLabelUI

Field Detail

- labelUI

```java
protected static
BasicLabelUI
labelUI
```

The default

BasicLabelUI

instance. This field might
not be used. To change the default instance use a subclass which
overrides the

createUI

method, and place that class
name in defaults table under the key "LabelUI".

---

#### Field Detail

labelUI

```java
protected static
BasicLabelUI
labelUI
```

The default

BasicLabelUI

instance. This field might
not be used. To change the default instance use a subclass which
overrides the

createUI

method, and place that class
name in defaults table under the key "LabelUI".

---

#### labelUI

protected static

BasicLabelUI

labelUI

The default

BasicLabelUI

instance. This field might
not be used. To change the default instance use a subclass which
overrides the

createUI

method, and place that class
name in defaults table under the key "LabelUI".

Constructor Detail

- BasicLabelUI

```java
public BasicLabelUI()
```

---

#### Constructor Detail

BasicLabelUI

```java
public BasicLabelUI()
```

---

#### BasicLabelUI

public BasicLabelUI()

Method Detail

- layoutCL

```java
protected
String
layoutCL​(
JLabel
label,

FontMetrics
fontMetrics,

String
text,

Icon
icon,

Rectangle
viewR,

Rectangle
iconR,

Rectangle
textR)
```

Forwards the call to SwingUtilities.layoutCompoundLabel().
This method is here so that a subclass could do Label specific
layout and to shorten the method name a little.

**Parameters:** label

- an instance of

JLabel
**Parameters:** fontMetrics

- a font metrics
**Parameters:** text

- a text
**Parameters:** icon

- an icon
**Parameters:** viewR

- a bounding rectangle to lay out label
**Parameters:** iconR

- a bounding rectangle to lay out icon
**Parameters:** textR

- a bounding rectangle to lay out text
**Returns:** a possibly clipped version of the compound labels string
**See Also:** SwingUtilities.layoutCompoundLabel(javax.swing.JComponent, java.awt.FontMetrics, java.lang.String, javax.swing.Icon, int, int, int, int, java.awt.Rectangle, java.awt.Rectangle, java.awt.Rectangle, int)

- paintEnabledText

```java
protected void paintEnabledText​(
JLabel
l,

Graphics
g,

String
s,
int textX,
int textY)
```

Paint clippedText at textX, textY with the labels foreground color.

**Parameters:** l

- an instance of

JLabel
**Parameters:** g

- an instance of

Graphics
**Parameters:** s

- a text
**Parameters:** textX

- an X coordinate
**Parameters:** textY

- an Y coordinate
**See Also:** paint(java.awt.Graphics, javax.swing.JComponent)

,

paintDisabledText(javax.swing.JLabel, java.awt.Graphics, java.lang.String, int, int)

- paintDisabledText

```java
protected void paintDisabledText​(
JLabel
l,

Graphics
g,

String
s,
int textX,
int textY)
```

Paint clippedText at textX, textY with background.lighter() and then
shifted down and to the right by one pixel with background.darker().

**Parameters:** l

- an instance of

JLabel
**Parameters:** g

- an instance of

Graphics
**Parameters:** s

- a text
**Parameters:** textX

- an X coordinate
**Parameters:** textY

- an Y coordinate
**See Also:** paint(java.awt.Graphics, javax.swing.JComponent)

,

paintEnabledText(javax.swing.JLabel, java.awt.Graphics, java.lang.String, int, int)

- paint

```java
public void paint​(
Graphics
g,

JComponent
c)
```

Paints the label text with the foreground color, if the label is opaque
then paints the entire background with the background color. The Label
text is drawn by

paintEnabledText(javax.swing.JLabel, java.awt.Graphics, java.lang.String, int, int)

or

paintDisabledText(javax.swing.JLabel, java.awt.Graphics, java.lang.String, int, int)

.
The locations of the label parts are computed by

layoutCL(javax.swing.JLabel, java.awt.FontMetrics, java.lang.String, javax.swing.Icon, java.awt.Rectangle, java.awt.Rectangle, java.awt.Rectangle)

.

**Overrides:** paint

in class

ComponentUI
**Parameters:** g

- the

Graphics

context in which to paint
**Parameters:** c

- the component being painted;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**See Also:** paintEnabledText(javax.swing.JLabel, java.awt.Graphics, java.lang.String, int, int)

,

paintDisabledText(javax.swing.JLabel, java.awt.Graphics, java.lang.String, int, int)

,

layoutCL(javax.swing.JLabel, java.awt.FontMetrics, java.lang.String, javax.swing.Icon, java.awt.Rectangle, java.awt.Rectangle, java.awt.Rectangle)

- getMinimumSize

```java
public
Dimension
getMinimumSize​(
JComponent
c)
```

Description copied from class:

ComponentUI

Returns the specified component's minimum size appropriate for
the look and feel. If

null

is returned, the minimum
size will be calculated by the component's layout manager instead
(this is the preferred approach for any component with a specific
layout manager installed). The default implementation of this
method invokes

getPreferredSize

and returns that value.

**Overrides:** getMinimumSize

in class

ComponentUI
**Parameters:** c

- the component whose minimum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Returns:** getPreferredSize(c)
**See Also:** JComponent.getMinimumSize()

,

LayoutManager.minimumLayoutSize(java.awt.Container)

,

ComponentUI.getPreferredSize(javax.swing.JComponent)

- getMaximumSize

```java
public
Dimension
getMaximumSize​(
JComponent
c)
```

Description copied from class:

ComponentUI

Returns the specified component's maximum size appropriate for
the look and feel. If

null

is returned, the maximum
size will be calculated by the component's layout manager instead
(this is the preferred approach for any component with a specific
layout manager installed). The default implementation of this
method invokes

getPreferredSize

and returns that value.

**Overrides:** getMaximumSize

in class

ComponentUI
**Parameters:** c

- the component whose maximum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Returns:** getPreferredSize(c)
**See Also:** JComponent.getMaximumSize()

,

LayoutManager2.maximumLayoutSize(java.awt.Container)

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

- installDefaults

```java
protected void installDefaults​(
JLabel
c)
```

Installs default properties.

**Parameters:** c

- an instance of

JLabel

- installListeners

```java
protected void installListeners​(
JLabel
c)
```

Registers listeners.

**Parameters:** c

- an instance of

JLabel

- installComponents

```java
protected void installComponents​(
JLabel
c)
```

Registers components.

**Parameters:** c

- an instance of

JLabel

- installKeyboardActions

```java
protected void installKeyboardActions​(
JLabel
l)
```

Registers keyboard actions.

**Parameters:** l

- an instance of

JLabel

- uninstallDefaults

```java
protected void uninstallDefaults​(
JLabel
c)
```

Uninstalls default properties.

**Parameters:** c

- an instance of

JLabel

- uninstallListeners

```java
protected void uninstallListeners​(
JLabel
c)
```

Unregisters listeners.

**Parameters:** c

- an instance of

JLabel

- uninstallComponents

```java
protected void uninstallComponents​(
JLabel
c)
```

Unregisters components.

**Parameters:** c

- an instance of

JLabel

- uninstallKeyboardActions

```java
protected void uninstallKeyboardActions​(
JLabel
c)
```

Unregisters keyboard actions.

**Parameters:** c

- an instance of

JLabel

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Returns an instance of

BasicLabelUI

.

**Parameters:** c

- a component
**Returns:** an instance of

BasicLabelUI

---

#### Method Detail

layoutCL

```java
protected
String
layoutCL​(
JLabel
label,

FontMetrics
fontMetrics,

String
text,

Icon
icon,

Rectangle
viewR,

Rectangle
iconR,

Rectangle
textR)
```

Forwards the call to SwingUtilities.layoutCompoundLabel().
This method is here so that a subclass could do Label specific
layout and to shorten the method name a little.

**Parameters:** label

- an instance of

JLabel
**Parameters:** fontMetrics

- a font metrics
**Parameters:** text

- a text
**Parameters:** icon

- an icon
**Parameters:** viewR

- a bounding rectangle to lay out label
**Parameters:** iconR

- a bounding rectangle to lay out icon
**Parameters:** textR

- a bounding rectangle to lay out text
**Returns:** a possibly clipped version of the compound labels string
**See Also:** SwingUtilities.layoutCompoundLabel(javax.swing.JComponent, java.awt.FontMetrics, java.lang.String, javax.swing.Icon, int, int, int, int, java.awt.Rectangle, java.awt.Rectangle, java.awt.Rectangle, int)

---

#### layoutCL

protected

String

layoutCL​(

JLabel

label,

FontMetrics

fontMetrics,

String

text,

Icon

icon,

Rectangle

viewR,

Rectangle

iconR,

Rectangle

textR)

Forwards the call to SwingUtilities.layoutCompoundLabel().
This method is here so that a subclass could do Label specific
layout and to shorten the method name a little.

paintEnabledText

```java
protected void paintEnabledText​(
JLabel
l,

Graphics
g,

String
s,
int textX,
int textY)
```

Paint clippedText at textX, textY with the labels foreground color.

**Parameters:** l

- an instance of

JLabel
**Parameters:** g

- an instance of

Graphics
**Parameters:** s

- a text
**Parameters:** textX

- an X coordinate
**Parameters:** textY

- an Y coordinate
**See Also:** paint(java.awt.Graphics, javax.swing.JComponent)

,

paintDisabledText(javax.swing.JLabel, java.awt.Graphics, java.lang.String, int, int)

---

#### paintEnabledText

protected void paintEnabledText​(

JLabel

l,

Graphics

g,

String

s,
int textX,
int textY)

Paint clippedText at textX, textY with the labels foreground color.

paintDisabledText

```java
protected void paintDisabledText​(
JLabel
l,

Graphics
g,

String
s,
int textX,
int textY)
```

Paint clippedText at textX, textY with background.lighter() and then
shifted down and to the right by one pixel with background.darker().

**Parameters:** l

- an instance of

JLabel
**Parameters:** g

- an instance of

Graphics
**Parameters:** s

- a text
**Parameters:** textX

- an X coordinate
**Parameters:** textY

- an Y coordinate
**See Also:** paint(java.awt.Graphics, javax.swing.JComponent)

,

paintEnabledText(javax.swing.JLabel, java.awt.Graphics, java.lang.String, int, int)

---

#### paintDisabledText

protected void paintDisabledText​(

JLabel

l,

Graphics

g,

String

s,
int textX,
int textY)

Paint clippedText at textX, textY with background.lighter() and then
shifted down and to the right by one pixel with background.darker().

paint

```java
public void paint​(
Graphics
g,

JComponent
c)
```

Paints the label text with the foreground color, if the label is opaque
then paints the entire background with the background color. The Label
text is drawn by

paintEnabledText(javax.swing.JLabel, java.awt.Graphics, java.lang.String, int, int)

or

paintDisabledText(javax.swing.JLabel, java.awt.Graphics, java.lang.String, int, int)

.
The locations of the label parts are computed by

layoutCL(javax.swing.JLabel, java.awt.FontMetrics, java.lang.String, javax.swing.Icon, java.awt.Rectangle, java.awt.Rectangle, java.awt.Rectangle)

.

**Overrides:** paint

in class

ComponentUI
**Parameters:** g

- the

Graphics

context in which to paint
**Parameters:** c

- the component being painted;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**See Also:** paintEnabledText(javax.swing.JLabel, java.awt.Graphics, java.lang.String, int, int)

,

paintDisabledText(javax.swing.JLabel, java.awt.Graphics, java.lang.String, int, int)

,

layoutCL(javax.swing.JLabel, java.awt.FontMetrics, java.lang.String, javax.swing.Icon, java.awt.Rectangle, java.awt.Rectangle, java.awt.Rectangle)

---

#### paint

public void paint​(

Graphics

g,

JComponent

c)

Paints the label text with the foreground color, if the label is opaque
then paints the entire background with the background color. The Label
text is drawn by

paintEnabledText(javax.swing.JLabel, java.awt.Graphics, java.lang.String, int, int)

or

paintDisabledText(javax.swing.JLabel, java.awt.Graphics, java.lang.String, int, int)

.
The locations of the label parts are computed by

layoutCL(javax.swing.JLabel, java.awt.FontMetrics, java.lang.String, javax.swing.Icon, java.awt.Rectangle, java.awt.Rectangle, java.awt.Rectangle)

.

getMinimumSize

```java
public
Dimension
getMinimumSize​(
JComponent
c)
```

Description copied from class:

ComponentUI

Returns the specified component's minimum size appropriate for
the look and feel. If

null

is returned, the minimum
size will be calculated by the component's layout manager instead
(this is the preferred approach for any component with a specific
layout manager installed). The default implementation of this
method invokes

getPreferredSize

and returns that value.

**Overrides:** getMinimumSize

in class

ComponentUI
**Parameters:** c

- the component whose minimum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Returns:** getPreferredSize(c)
**See Also:** JComponent.getMinimumSize()

,

LayoutManager.minimumLayoutSize(java.awt.Container)

,

ComponentUI.getPreferredSize(javax.swing.JComponent)

---

#### getMinimumSize

public

Dimension

getMinimumSize​(

JComponent

c)

Description copied from class:

ComponentUI

Returns the specified component's minimum size appropriate for
the look and feel. If

null

is returned, the minimum
size will be calculated by the component's layout manager instead
(this is the preferred approach for any component with a specific
layout manager installed). The default implementation of this
method invokes

getPreferredSize

and returns that value.

getMaximumSize

```java
public
Dimension
getMaximumSize​(
JComponent
c)
```

Description copied from class:

ComponentUI

Returns the specified component's maximum size appropriate for
the look and feel. If

null

is returned, the maximum
size will be calculated by the component's layout manager instead
(this is the preferred approach for any component with a specific
layout manager installed). The default implementation of this
method invokes

getPreferredSize

and returns that value.

**Overrides:** getMaximumSize

in class

ComponentUI
**Parameters:** c

- the component whose maximum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Returns:** getPreferredSize(c)
**See Also:** JComponent.getMaximumSize()

,

LayoutManager2.maximumLayoutSize(java.awt.Container)

---

#### getMaximumSize

public

Dimension

getMaximumSize​(

JComponent

c)

Description copied from class:

ComponentUI

Returns the specified component's maximum size appropriate for
the look and feel. If

null

is returned, the maximum
size will be calculated by the component's layout manager instead
(this is the preferred approach for any component with a specific
layout manager installed). The default implementation of this
method invokes

getPreferredSize

and returns that value.

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

installDefaults

```java
protected void installDefaults​(
JLabel
c)
```

Installs default properties.

**Parameters:** c

- an instance of

JLabel

---

#### installDefaults

protected void installDefaults​(

JLabel

c)

Installs default properties.

installListeners

```java
protected void installListeners​(
JLabel
c)
```

Registers listeners.

**Parameters:** c

- an instance of

JLabel

---

#### installListeners

protected void installListeners​(

JLabel

c)

Registers listeners.

installComponents

```java
protected void installComponents​(
JLabel
c)
```

Registers components.

**Parameters:** c

- an instance of

JLabel

---

#### installComponents

protected void installComponents​(

JLabel

c)

Registers components.

installKeyboardActions

```java
protected void installKeyboardActions​(
JLabel
l)
```

Registers keyboard actions.

**Parameters:** l

- an instance of

JLabel

---

#### installKeyboardActions

protected void installKeyboardActions​(

JLabel

l)

Registers keyboard actions.

uninstallDefaults

```java
protected void uninstallDefaults​(
JLabel
c)
```

Uninstalls default properties.

**Parameters:** c

- an instance of

JLabel

---

#### uninstallDefaults

protected void uninstallDefaults​(

JLabel

c)

Uninstalls default properties.

uninstallListeners

```java
protected void uninstallListeners​(
JLabel
c)
```

Unregisters listeners.

**Parameters:** c

- an instance of

JLabel

---

#### uninstallListeners

protected void uninstallListeners​(

JLabel

c)

Unregisters listeners.

uninstallComponents

```java
protected void uninstallComponents​(
JLabel
c)
```

Unregisters components.

**Parameters:** c

- an instance of

JLabel

---

#### uninstallComponents

protected void uninstallComponents​(

JLabel

c)

Unregisters components.

uninstallKeyboardActions

```java
protected void uninstallKeyboardActions​(
JLabel
c)
```

Unregisters keyboard actions.

**Parameters:** c

- an instance of

JLabel

---

#### uninstallKeyboardActions

protected void uninstallKeyboardActions​(

JLabel

c)

Unregisters keyboard actions.

createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Returns an instance of

BasicLabelUI

.

**Parameters:** c

- a component
**Returns:** an instance of

BasicLabelUI

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

c)

Returns an instance of

BasicLabelUI

.

---

