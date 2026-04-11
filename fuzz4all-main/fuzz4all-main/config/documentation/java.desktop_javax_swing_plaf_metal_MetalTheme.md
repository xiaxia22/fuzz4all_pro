# Class MetalTheme

**Source:** `java.desktop\javax\swing\plaf\metal\MetalTheme.html`

### Class Description

```java
public abstract class
MetalTheme

extends
Object
```

MetalTheme

provides the color palette and fonts used by
the Java Look and Feel.

MetalTheme

is abstract, see

DefaultMetalTheme

and

OceanTheme

for concrete implementations.

MetalLookAndFeel

maintains the current theme that the
the

ComponentUI

implementations for metal use. Refer to

MetalLookAndFeel.setCurrentTheme(MetalTheme)

for details on changing
the current theme.

MetalTheme

provides a number of public methods for getting
colors. These methods are implemented in terms of a
handful of protected abstract methods. A subclass need only override
the protected abstract methods (

getPrimary1

,

getPrimary2

,

getPrimary3

,

getSecondary1

,

getSecondary2

, and

getSecondary3

); although a subclass
may override the other public methods for more control over the set of
colors that are used.

Concrete implementations of

MetalTheme

must return

non-null

values from all methods. While the behavior of returning

null

is
not specified, returning

null

will result in incorrect behavior.

It is strongly recommended that subclasses return completely opaque colors.
To do otherwise may result in rendering problems, such as visual garbage.

**Direct Known Subclasses:** DefaultMetalTheme

---

### Field Details

*No entries found.*

### Constructor Details

#### public MetalTheme()

*No description found.*

---

### Method Details

#### public abstract
String
getName()

Returns the name of this theme.

**Returns:**
- the name of this theme

---

#### protected abstract
ColorUIResource
getPrimary1()

Returns the primary 1 color.

**Returns:**
- the primary 1 color

---

#### protected abstract
ColorUIResource
getPrimary2()

Returns the primary 2 color.

**Returns:**
- the primary 2 color

---

#### protected abstract
ColorUIResource
getPrimary3()

Returns the primary 3 color.

**Returns:**
- the primary 3 color

---

#### protected abstract
ColorUIResource
getSecondary1()

Returns the secondary 1 color.

**Returns:**
- the secondary 1 color

---

#### protected abstract
ColorUIResource
getSecondary2()

Returns the secondary 2 color.

**Returns:**
- the secondary 2 color

---

#### protected abstract
ColorUIResource
getSecondary3()

Returns the secondary 3 color.

**Returns:**
- the secondary 3 color

---

#### public abstract
FontUIResource
getControlTextFont()

Returns the control text font.

**Returns:**
- the control text font

---

#### public abstract
FontUIResource
getSystemTextFont()

Returns the system text font.

**Returns:**
- the system text font

---

#### public abstract
FontUIResource
getUserTextFont()

Returns the user text font.

**Returns:**
- the user text font

---

#### public abstract
FontUIResource
getMenuTextFont()

Returns the menu text font.

**Returns:**
- the menu text font

---

#### public abstract
FontUIResource
getWindowTitleFont()

Returns the window title font.

**Returns:**
- the window title font

---

#### public abstract
FontUIResource
getSubTextFont()

Returns the sub-text font.

**Returns:**
- the sub-text font

---

#### protected
ColorUIResource
getWhite()

Returns the white color. This returns opaque white
(

0xFFFFFFFF

).

**Returns:**
- the white color

---

#### protected
ColorUIResource
getBlack()

Returns the black color. This returns opaque black
(

0xFF000000

).

**Returns:**
- the black color

---

#### public
ColorUIResource
getFocusColor()

Returns the focus color. This returns the value of

getPrimary2()

.

**Returns:**
- the focus color

---

#### public
ColorUIResource
getDesktopColor()

Returns the desktop color. This returns the value of

getPrimary2()

.

**Returns:**
- the desktop color

---

#### public
ColorUIResource
getControl()

Returns the control color. This returns the value of

getSecondary3()

.

**Returns:**
- the control color

---

#### public
ColorUIResource
getControlShadow()

Returns the control shadow color. This returns
the value of

getSecondary2()

.

**Returns:**
- the control shadow color

---

#### public
ColorUIResource
getControlDarkShadow()

Returns the control dark shadow color. This returns
the value of

getSecondary1()

.

**Returns:**
- the control dark shadow color

---

#### public
ColorUIResource
getControlInfo()

Returns the control info color. This returns
the value of

getBlack()

.

**Returns:**
- the control info color

---

#### public
ColorUIResource
getControlHighlight()

Returns the control highlight color. This returns
the value of

getWhite()

.

**Returns:**
- the control highlight color

---

#### public
ColorUIResource
getControlDisabled()

Returns the control disabled color. This returns
the value of

getSecondary2()

.

**Returns:**
- the control disabled color

---

#### public
ColorUIResource
getPrimaryControl()

Returns the primary control color. This returns
the value of

getPrimary3()

.

**Returns:**
- the primary control color

---

#### public
ColorUIResource
getPrimaryControlShadow()

Returns the primary control shadow color. This returns
the value of

getPrimary2()

.

**Returns:**
- the primary control shadow color

---

#### public
ColorUIResource
getPrimaryControlDarkShadow()

Returns the primary control dark shadow color. This
returns the value of

getPrimary1()

.

**Returns:**
- the primary control dark shadow color

---

#### public
ColorUIResource
getPrimaryControlInfo()

Returns the primary control info color. This
returns the value of

getBlack()

.

**Returns:**
- the primary control info color

---

#### public
ColorUIResource
getPrimaryControlHighlight()

Returns the primary control highlight color. This
returns the value of

getWhite()

.

**Returns:**
- the primary control highlight color

---

#### public
ColorUIResource
getSystemTextColor()

Returns the system text color. This returns the value of

getBlack()

.

**Returns:**
- the system text color

---

#### public
ColorUIResource
getControlTextColor()

Returns the control text color. This returns the value of

getControlInfo()

.

**Returns:**
- the control text color

---

#### public
ColorUIResource
getInactiveControlTextColor()

Returns the inactive control text color. This returns the value of

getControlDisabled()

.

**Returns:**
- the inactive control text color

---

#### public
ColorUIResource
getInactiveSystemTextColor()

Returns the inactive system text color. This returns the value of

getSecondary2()

.

**Returns:**
- the inactive system text color

---

#### public
ColorUIResource
getUserTextColor()

Returns the user text color. This returns the value of

getBlack()

.

**Returns:**
- the user text color

---

#### public
ColorUIResource
getTextHighlightColor()

Returns the text highlight color. This returns the value of

getPrimary3()

.

**Returns:**
- the text highlight color

---

#### public
ColorUIResource
getHighlightedTextColor()

Returns the highlighted text color. This returns the value of

getControlTextColor()

.

**Returns:**
- the highlighted text color

---

#### public
ColorUIResource
getWindowBackground()

Returns the window background color. This returns the value of

getWhite()

.

**Returns:**
- the window background color

---

#### public
ColorUIResource
getWindowTitleBackground()

Returns the window title background color. This returns the value of

getPrimary3()

.

**Returns:**
- the window title background color

---

#### public
ColorUIResource
getWindowTitleForeground()

Returns the window title foreground color. This returns the value of

getBlack()

.

**Returns:**
- the window title foreground color

---

#### public
ColorUIResource
getWindowTitleInactiveBackground()

Returns the window title inactive background color. This
returns the value of

getSecondary3()

.

**Returns:**
- the window title inactive background color

---

#### public
ColorUIResource
getWindowTitleInactiveForeground()

Returns the window title inactive foreground color. This
returns the value of

getBlack()

.

**Returns:**
- the window title inactive foreground color

---

#### public
ColorUIResource
getMenuBackground()

Returns the menu background color. This
returns the value of

getSecondary3()

.

**Returns:**
- the menu background color

---

#### public
ColorUIResource
getMenuForeground()

Returns the menu foreground color. This
returns the value of

getBlack()

.

**Returns:**
- the menu foreground color

---

#### public
ColorUIResource
getMenuSelectedBackground()

Returns the menu selected background color. This
returns the value of

getPrimary2()

.

**Returns:**
- the menu selected background color

---

#### public
ColorUIResource
getMenuSelectedForeground()

Returns the menu selected foreground color. This
returns the value of

getBlack()

.

**Returns:**
- the menu selected foreground color

---

#### public
ColorUIResource
getMenuDisabledForeground()

Returns the menu disabled foreground color. This
returns the value of

getSecondary2()

.

**Returns:**
- the menu disabled foreground color

---

#### public
ColorUIResource
getSeparatorBackground()

Returns the separator background color. This
returns the value of

getWhite()

.

**Returns:**
- the separator background color

---

#### public
ColorUIResource
getSeparatorForeground()

Returns the separator foreground color. This
returns the value of

getPrimary1()

.

**Returns:**
- the separator foreground color

---

#### public
ColorUIResource
getAcceleratorForeground()

Returns the accelerator foreground color. This
returns the value of

getPrimary1()

.

**Returns:**
- the accelerator foreground color

---

#### public
ColorUIResource
getAcceleratorSelectedForeground()

Returns the accelerator selected foreground color. This
returns the value of

getBlack()

.

**Returns:**
- the accelerator selected foreground color

---

#### public void addCustomEntriesToTable​(
UIDefaults
table)

Adds values specific to this theme to the defaults table. This method
is invoked when the look and feel defaults are obtained from

MetalLookAndFeel

.

This implementation does nothing; it is provided for subclasses
that wish to customize the defaults table.

**Parameters:**
- table

- the

UIDefaults

to add the values to

**See Also:**
- MetalLookAndFeel.getDefaults()

---

### Additional Sections

#### Class MetalTheme

java.lang.Object

- javax.swing.plaf.metal.MetalTheme

javax.swing.plaf.metal.MetalTheme

**Direct Known Subclasses:** DefaultMetalTheme

```java
public abstract class
MetalTheme

extends
Object
```

MetalTheme

provides the color palette and fonts used by
the Java Look and Feel.

MetalTheme

is abstract, see

DefaultMetalTheme

and

OceanTheme

for concrete implementations.

MetalLookAndFeel

maintains the current theme that the
the

ComponentUI

implementations for metal use. Refer to

MetalLookAndFeel.setCurrentTheme(MetalTheme)

for details on changing
the current theme.

MetalTheme

provides a number of public methods for getting
colors. These methods are implemented in terms of a
handful of protected abstract methods. A subclass need only override
the protected abstract methods (

getPrimary1

,

getPrimary2

,

getPrimary3

,

getSecondary1

,

getSecondary2

, and

getSecondary3

); although a subclass
may override the other public methods for more control over the set of
colors that are used.

Concrete implementations of

MetalTheme

must return

non-null

values from all methods. While the behavior of returning

null

is
not specified, returning

null

will result in incorrect behavior.

It is strongly recommended that subclasses return completely opaque colors.
To do otherwise may result in rendering problems, such as visual garbage.

**See Also:** DefaultMetalTheme

,

OceanTheme

,

MetalLookAndFeel.setCurrentTheme(javax.swing.plaf.metal.MetalTheme)

public abstract class

MetalTheme

extends

Object

MetalTheme

provides the color palette and fonts used by
the Java Look and Feel.

MetalTheme

is abstract, see

DefaultMetalTheme

and

OceanTheme

for concrete implementations.

MetalLookAndFeel

maintains the current theme that the
the

ComponentUI

implementations for metal use. Refer to

MetalLookAndFeel.setCurrentTheme(MetalTheme)

for details on changing
the current theme.

MetalTheme

provides a number of public methods for getting
colors. These methods are implemented in terms of a
handful of protected abstract methods. A subclass need only override
the protected abstract methods (

getPrimary1

,

getPrimary2

,

getPrimary3

,

getSecondary1

,

getSecondary2

, and

getSecondary3

); although a subclass
may override the other public methods for more control over the set of
colors that are used.

Concrete implementations of

MetalTheme

must return

non-null

values from all methods. While the behavior of returning

null

is
not specified, returning

null

will result in incorrect behavior.

It is strongly recommended that subclasses return completely opaque colors.
To do otherwise may result in rendering problems, such as visual garbage.

MetalTheme

is abstract, see

DefaultMetalTheme

and

OceanTheme

for concrete implementations.

MetalLookAndFeel

maintains the current theme that the
the

ComponentUI

implementations for metal use. Refer to

MetalLookAndFeel.setCurrentTheme(MetalTheme)

for details on changing
the current theme.

MetalTheme

provides a number of public methods for getting
colors. These methods are implemented in terms of a
handful of protected abstract methods. A subclass need only override
the protected abstract methods (

getPrimary1

,

getPrimary2

,

getPrimary3

,

getSecondary1

,

getSecondary2

, and

getSecondary3

); although a subclass
may override the other public methods for more control over the set of
colors that are used.

Concrete implementations of

MetalTheme

must return

non-null

values from all methods. While the behavior of returning

null

is
not specified, returning

null

will result in incorrect behavior.

It is strongly recommended that subclasses return completely opaque colors.
To do otherwise may result in rendering problems, such as visual garbage.

MetalLookAndFeel

maintains the current theme that the
the

ComponentUI

implementations for metal use. Refer to

MetalLookAndFeel.setCurrentTheme(MetalTheme)

for details on changing
the current theme.

MetalTheme

provides a number of public methods for getting
colors. These methods are implemented in terms of a
handful of protected abstract methods. A subclass need only override
the protected abstract methods (

getPrimary1

,

getPrimary2

,

getPrimary3

,

getSecondary1

,

getSecondary2

, and

getSecondary3

); although a subclass
may override the other public methods for more control over the set of
colors that are used.

Concrete implementations of

MetalTheme

must return

non-null

values from all methods. While the behavior of returning

null

is
not specified, returning

null

will result in incorrect behavior.

It is strongly recommended that subclasses return completely opaque colors.
To do otherwise may result in rendering problems, such as visual garbage.

MetalTheme

provides a number of public methods for getting
colors. These methods are implemented in terms of a
handful of protected abstract methods. A subclass need only override
the protected abstract methods (

getPrimary1

,

getPrimary2

,

getPrimary3

,

getSecondary1

,

getSecondary2

, and

getSecondary3

); although a subclass
may override the other public methods for more control over the set of
colors that are used.

Concrete implementations of

MetalTheme

must return

non-null

values from all methods. While the behavior of returning

null

is
not specified, returning

null

will result in incorrect behavior.

It is strongly recommended that subclasses return completely opaque colors.
To do otherwise may result in rendering problems, such as visual garbage.

Concrete implementations of

MetalTheme

must return

non-null

values from all methods. While the behavior of returning

null

is
not specified, returning

null

will result in incorrect behavior.

It is strongly recommended that subclasses return completely opaque colors.
To do otherwise may result in rendering problems, such as visual garbage.

It is strongly recommended that subclasses return completely opaque colors.
To do otherwise may result in rendering problems, such as visual garbage.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MetalTheme

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

addCustomEntriesToTable

​(

UIDefaults

table)

Adds values specific to this theme to the defaults table.

ColorUIResource

getAcceleratorForeground

()

Returns the accelerator foreground color.

ColorUIResource

getAcceleratorSelectedForeground

()

Returns the accelerator selected foreground color.

protected

ColorUIResource

getBlack

()

Returns the black color.

ColorUIResource

getControl

()

Returns the control color.

ColorUIResource

getControlDarkShadow

()

Returns the control dark shadow color.

ColorUIResource

getControlDisabled

()

Returns the control disabled color.

ColorUIResource

getControlHighlight

()

Returns the control highlight color.

ColorUIResource

getControlInfo

()

Returns the control info color.

ColorUIResource

getControlShadow

()

Returns the control shadow color.

ColorUIResource

getControlTextColor

()

Returns the control text color.

abstract

FontUIResource

getControlTextFont

()

Returns the control text font.

ColorUIResource

getDesktopColor

()

Returns the desktop color.

ColorUIResource

getFocusColor

()

Returns the focus color.

ColorUIResource

getHighlightedTextColor

()

Returns the highlighted text color.

ColorUIResource

getInactiveControlTextColor

()

Returns the inactive control text color.

ColorUIResource

getInactiveSystemTextColor

()

Returns the inactive system text color.

ColorUIResource

getMenuBackground

()

Returns the menu background color.

ColorUIResource

getMenuDisabledForeground

()

Returns the menu disabled foreground color.

ColorUIResource

getMenuForeground

()

Returns the menu foreground color.

ColorUIResource

getMenuSelectedBackground

()

Returns the menu selected background color.

ColorUIResource

getMenuSelectedForeground

()

Returns the menu selected foreground color.

abstract

FontUIResource

getMenuTextFont

()

Returns the menu text font.

abstract

String

getName

()

Returns the name of this theme.

protected abstract

ColorUIResource

getPrimary1

()

Returns the primary 1 color.

protected abstract

ColorUIResource

getPrimary2

()

Returns the primary 2 color.

protected abstract

ColorUIResource

getPrimary3

()

Returns the primary 3 color.

ColorUIResource

getPrimaryControl

()

Returns the primary control color.

ColorUIResource

getPrimaryControlDarkShadow

()

Returns the primary control dark shadow color.

ColorUIResource

getPrimaryControlHighlight

()

Returns the primary control highlight color.

ColorUIResource

getPrimaryControlInfo

()

Returns the primary control info color.

ColorUIResource

getPrimaryControlShadow

()

Returns the primary control shadow color.

protected abstract

ColorUIResource

getSecondary1

()

Returns the secondary 1 color.

protected abstract

ColorUIResource

getSecondary2

()

Returns the secondary 2 color.

protected abstract

ColorUIResource

getSecondary3

()

Returns the secondary 3 color.

ColorUIResource

getSeparatorBackground

()

Returns the separator background color.

ColorUIResource

getSeparatorForeground

()

Returns the separator foreground color.

abstract

FontUIResource

getSubTextFont

()

Returns the sub-text font.

ColorUIResource

getSystemTextColor

()

Returns the system text color.

abstract

FontUIResource

getSystemTextFont

()

Returns the system text font.

ColorUIResource

getTextHighlightColor

()

Returns the text highlight color.

ColorUIResource

getUserTextColor

()

Returns the user text color.

abstract

FontUIResource

getUserTextFont

()

Returns the user text font.

protected

ColorUIResource

getWhite

()

Returns the white color.

ColorUIResource

getWindowBackground

()

Returns the window background color.

ColorUIResource

getWindowTitleBackground

()

Returns the window title background color.

abstract

FontUIResource

getWindowTitleFont

()

Returns the window title font.

ColorUIResource

getWindowTitleForeground

()

Returns the window title foreground color.

ColorUIResource

getWindowTitleInactiveBackground

()

Returns the window title inactive background color.

ColorUIResource

getWindowTitleInactiveForeground

()

Returns the window title inactive foreground color.

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

Constructor Summary

Constructors

Constructor

Description

MetalTheme

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

addCustomEntriesToTable

​(

UIDefaults

table)

Adds values specific to this theme to the defaults table.

ColorUIResource

getAcceleratorForeground

()

Returns the accelerator foreground color.

ColorUIResource

getAcceleratorSelectedForeground

()

Returns the accelerator selected foreground color.

protected

ColorUIResource

getBlack

()

Returns the black color.

ColorUIResource

getControl

()

Returns the control color.

ColorUIResource

getControlDarkShadow

()

Returns the control dark shadow color.

ColorUIResource

getControlDisabled

()

Returns the control disabled color.

ColorUIResource

getControlHighlight

()

Returns the control highlight color.

ColorUIResource

getControlInfo

()

Returns the control info color.

ColorUIResource

getControlShadow

()

Returns the control shadow color.

ColorUIResource

getControlTextColor

()

Returns the control text color.

abstract

FontUIResource

getControlTextFont

()

Returns the control text font.

ColorUIResource

getDesktopColor

()

Returns the desktop color.

ColorUIResource

getFocusColor

()

Returns the focus color.

ColorUIResource

getHighlightedTextColor

()

Returns the highlighted text color.

ColorUIResource

getInactiveControlTextColor

()

Returns the inactive control text color.

ColorUIResource

getInactiveSystemTextColor

()

Returns the inactive system text color.

ColorUIResource

getMenuBackground

()

Returns the menu background color.

ColorUIResource

getMenuDisabledForeground

()

Returns the menu disabled foreground color.

ColorUIResource

getMenuForeground

()

Returns the menu foreground color.

ColorUIResource

getMenuSelectedBackground

()

Returns the menu selected background color.

ColorUIResource

getMenuSelectedForeground

()

Returns the menu selected foreground color.

abstract

FontUIResource

getMenuTextFont

()

Returns the menu text font.

abstract

String

getName

()

Returns the name of this theme.

protected abstract

ColorUIResource

getPrimary1

()

Returns the primary 1 color.

protected abstract

ColorUIResource

getPrimary2

()

Returns the primary 2 color.

protected abstract

ColorUIResource

getPrimary3

()

Returns the primary 3 color.

ColorUIResource

getPrimaryControl

()

Returns the primary control color.

ColorUIResource

getPrimaryControlDarkShadow

()

Returns the primary control dark shadow color.

ColorUIResource

getPrimaryControlHighlight

()

Returns the primary control highlight color.

ColorUIResource

getPrimaryControlInfo

()

Returns the primary control info color.

ColorUIResource

getPrimaryControlShadow

()

Returns the primary control shadow color.

protected abstract

ColorUIResource

getSecondary1

()

Returns the secondary 1 color.

protected abstract

ColorUIResource

getSecondary2

()

Returns the secondary 2 color.

protected abstract

ColorUIResource

getSecondary3

()

Returns the secondary 3 color.

ColorUIResource

getSeparatorBackground

()

Returns the separator background color.

ColorUIResource

getSeparatorForeground

()

Returns the separator foreground color.

abstract

FontUIResource

getSubTextFont

()

Returns the sub-text font.

ColorUIResource

getSystemTextColor

()

Returns the system text color.

abstract

FontUIResource

getSystemTextFont

()

Returns the system text font.

ColorUIResource

getTextHighlightColor

()

Returns the text highlight color.

ColorUIResource

getUserTextColor

()

Returns the user text color.

abstract

FontUIResource

getUserTextFont

()

Returns the user text font.

protected

ColorUIResource

getWhite

()

Returns the white color.

ColorUIResource

getWindowBackground

()

Returns the window background color.

ColorUIResource

getWindowTitleBackground

()

Returns the window title background color.

abstract

FontUIResource

getWindowTitleFont

()

Returns the window title font.

ColorUIResource

getWindowTitleForeground

()

Returns the window title foreground color.

ColorUIResource

getWindowTitleInactiveBackground

()

Returns the window title inactive background color.

ColorUIResource

getWindowTitleInactiveForeground

()

Returns the window title inactive foreground color.

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

Adds values specific to this theme to the defaults table.

Returns the accelerator foreground color.

Returns the accelerator selected foreground color.

Returns the black color.

Returns the control color.

Returns the control dark shadow color.

Returns the control disabled color.

Returns the control highlight color.

Returns the control info color.

Returns the control shadow color.

Returns the control text color.

Returns the control text font.

Returns the desktop color.

Returns the focus color.

Returns the highlighted text color.

Returns the inactive control text color.

Returns the inactive system text color.

Returns the menu background color.

Returns the menu disabled foreground color.

Returns the menu foreground color.

Returns the menu selected background color.

Returns the menu selected foreground color.

Returns the menu text font.

Returns the name of this theme.

Returns the primary 1 color.

Returns the primary 2 color.

Returns the primary 3 color.

Returns the primary control color.

Returns the primary control dark shadow color.

Returns the primary control highlight color.

Returns the primary control info color.

Returns the primary control shadow color.

Returns the secondary 1 color.

Returns the secondary 2 color.

Returns the secondary 3 color.

Returns the separator background color.

Returns the separator foreground color.

Returns the sub-text font.

Returns the system text color.

Returns the system text font.

Returns the text highlight color.

Returns the user text color.

Returns the user text font.

Returns the white color.

Returns the window background color.

Returns the window title background color.

Returns the window title font.

Returns the window title foreground color.

Returns the window title inactive background color.

Returns the window title inactive foreground color.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- MetalTheme

```java
public MetalTheme()
```

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
public abstract
String
getName()
```

Returns the name of this theme.

**Returns:** the name of this theme

- getPrimary1

```java
protected abstract
ColorUIResource
getPrimary1()
```

Returns the primary 1 color.

**Returns:** the primary 1 color

- getPrimary2

```java
protected abstract
ColorUIResource
getPrimary2()
```

Returns the primary 2 color.

**Returns:** the primary 2 color

- getPrimary3

```java
protected abstract
ColorUIResource
getPrimary3()
```

Returns the primary 3 color.

**Returns:** the primary 3 color

- getSecondary1

```java
protected abstract
ColorUIResource
getSecondary1()
```

Returns the secondary 1 color.

**Returns:** the secondary 1 color

- getSecondary2

```java
protected abstract
ColorUIResource
getSecondary2()
```

Returns the secondary 2 color.

**Returns:** the secondary 2 color

- getSecondary3

```java
protected abstract
ColorUIResource
getSecondary3()
```

Returns the secondary 3 color.

**Returns:** the secondary 3 color

- getControlTextFont

```java
public abstract
FontUIResource
getControlTextFont()
```

Returns the control text font.

**Returns:** the control text font

- getSystemTextFont

```java
public abstract
FontUIResource
getSystemTextFont()
```

Returns the system text font.

**Returns:** the system text font

- getUserTextFont

```java
public abstract
FontUIResource
getUserTextFont()
```

Returns the user text font.

**Returns:** the user text font

- getMenuTextFont

```java
public abstract
FontUIResource
getMenuTextFont()
```

Returns the menu text font.

**Returns:** the menu text font

- getWindowTitleFont

```java
public abstract
FontUIResource
getWindowTitleFont()
```

Returns the window title font.

**Returns:** the window title font

- getSubTextFont

```java
public abstract
FontUIResource
getSubTextFont()
```

Returns the sub-text font.

**Returns:** the sub-text font

- getWhite

```java
protected
ColorUIResource
getWhite()
```

Returns the white color. This returns opaque white
(

0xFFFFFFFF

).

**Returns:** the white color

- getBlack

```java
protected
ColorUIResource
getBlack()
```

Returns the black color. This returns opaque black
(

0xFF000000

).

**Returns:** the black color

- getFocusColor

```java
public
ColorUIResource
getFocusColor()
```

Returns the focus color. This returns the value of

getPrimary2()

.

**Returns:** the focus color

- getDesktopColor

```java
public
ColorUIResource
getDesktopColor()
```

Returns the desktop color. This returns the value of

getPrimary2()

.

**Returns:** the desktop color

- getControl

```java
public
ColorUIResource
getControl()
```

Returns the control color. This returns the value of

getSecondary3()

.

**Returns:** the control color

- getControlShadow

```java
public
ColorUIResource
getControlShadow()
```

Returns the control shadow color. This returns
the value of

getSecondary2()

.

**Returns:** the control shadow color

- getControlDarkShadow

```java
public
ColorUIResource
getControlDarkShadow()
```

Returns the control dark shadow color. This returns
the value of

getSecondary1()

.

**Returns:** the control dark shadow color

- getControlInfo

```java
public
ColorUIResource
getControlInfo()
```

Returns the control info color. This returns
the value of

getBlack()

.

**Returns:** the control info color

- getControlHighlight

```java
public
ColorUIResource
getControlHighlight()
```

Returns the control highlight color. This returns
the value of

getWhite()

.

**Returns:** the control highlight color

- getControlDisabled

```java
public
ColorUIResource
getControlDisabled()
```

Returns the control disabled color. This returns
the value of

getSecondary2()

.

**Returns:** the control disabled color

- getPrimaryControl

```java
public
ColorUIResource
getPrimaryControl()
```

Returns the primary control color. This returns
the value of

getPrimary3()

.

**Returns:** the primary control color

- getPrimaryControlShadow

```java
public
ColorUIResource
getPrimaryControlShadow()
```

Returns the primary control shadow color. This returns
the value of

getPrimary2()

.

**Returns:** the primary control shadow color

- getPrimaryControlDarkShadow

```java
public
ColorUIResource
getPrimaryControlDarkShadow()
```

Returns the primary control dark shadow color. This
returns the value of

getPrimary1()

.

**Returns:** the primary control dark shadow color

- getPrimaryControlInfo

```java
public
ColorUIResource
getPrimaryControlInfo()
```

Returns the primary control info color. This
returns the value of

getBlack()

.

**Returns:** the primary control info color

- getPrimaryControlHighlight

```java
public
ColorUIResource
getPrimaryControlHighlight()
```

Returns the primary control highlight color. This
returns the value of

getWhite()

.

**Returns:** the primary control highlight color

- getSystemTextColor

```java
public
ColorUIResource
getSystemTextColor()
```

Returns the system text color. This returns the value of

getBlack()

.

**Returns:** the system text color

- getControlTextColor

```java
public
ColorUIResource
getControlTextColor()
```

Returns the control text color. This returns the value of

getControlInfo()

.

**Returns:** the control text color

- getInactiveControlTextColor

```java
public
ColorUIResource
getInactiveControlTextColor()
```

Returns the inactive control text color. This returns the value of

getControlDisabled()

.

**Returns:** the inactive control text color

- getInactiveSystemTextColor

```java
public
ColorUIResource
getInactiveSystemTextColor()
```

Returns the inactive system text color. This returns the value of

getSecondary2()

.

**Returns:** the inactive system text color

- getUserTextColor

```java
public
ColorUIResource
getUserTextColor()
```

Returns the user text color. This returns the value of

getBlack()

.

**Returns:** the user text color

- getTextHighlightColor

```java
public
ColorUIResource
getTextHighlightColor()
```

Returns the text highlight color. This returns the value of

getPrimary3()

.

**Returns:** the text highlight color

- getHighlightedTextColor

```java
public
ColorUIResource
getHighlightedTextColor()
```

Returns the highlighted text color. This returns the value of

getControlTextColor()

.

**Returns:** the highlighted text color

- getWindowBackground

```java
public
ColorUIResource
getWindowBackground()
```

Returns the window background color. This returns the value of

getWhite()

.

**Returns:** the window background color

- getWindowTitleBackground

```java
public
ColorUIResource
getWindowTitleBackground()
```

Returns the window title background color. This returns the value of

getPrimary3()

.

**Returns:** the window title background color

- getWindowTitleForeground

```java
public
ColorUIResource
getWindowTitleForeground()
```

Returns the window title foreground color. This returns the value of

getBlack()

.

**Returns:** the window title foreground color

- getWindowTitleInactiveBackground

```java
public
ColorUIResource
getWindowTitleInactiveBackground()
```

Returns the window title inactive background color. This
returns the value of

getSecondary3()

.

**Returns:** the window title inactive background color

- getWindowTitleInactiveForeground

```java
public
ColorUIResource
getWindowTitleInactiveForeground()
```

Returns the window title inactive foreground color. This
returns the value of

getBlack()

.

**Returns:** the window title inactive foreground color

- getMenuBackground

```java
public
ColorUIResource
getMenuBackground()
```

Returns the menu background color. This
returns the value of

getSecondary3()

.

**Returns:** the menu background color

- getMenuForeground

```java
public
ColorUIResource
getMenuForeground()
```

Returns the menu foreground color. This
returns the value of

getBlack()

.

**Returns:** the menu foreground color

- getMenuSelectedBackground

```java
public
ColorUIResource
getMenuSelectedBackground()
```

Returns the menu selected background color. This
returns the value of

getPrimary2()

.

**Returns:** the menu selected background color

- getMenuSelectedForeground

```java
public
ColorUIResource
getMenuSelectedForeground()
```

Returns the menu selected foreground color. This
returns the value of

getBlack()

.

**Returns:** the menu selected foreground color

- getMenuDisabledForeground

```java
public
ColorUIResource
getMenuDisabledForeground()
```

Returns the menu disabled foreground color. This
returns the value of

getSecondary2()

.

**Returns:** the menu disabled foreground color

- getSeparatorBackground

```java
public
ColorUIResource
getSeparatorBackground()
```

Returns the separator background color. This
returns the value of

getWhite()

.

**Returns:** the separator background color

- getSeparatorForeground

```java
public
ColorUIResource
getSeparatorForeground()
```

Returns the separator foreground color. This
returns the value of

getPrimary1()

.

**Returns:** the separator foreground color

- getAcceleratorForeground

```java
public
ColorUIResource
getAcceleratorForeground()
```

Returns the accelerator foreground color. This
returns the value of

getPrimary1()

.

**Returns:** the accelerator foreground color

- getAcceleratorSelectedForeground

```java
public
ColorUIResource
getAcceleratorSelectedForeground()
```

Returns the accelerator selected foreground color. This
returns the value of

getBlack()

.

**Returns:** the accelerator selected foreground color

- addCustomEntriesToTable

```java
public void addCustomEntriesToTable​(
UIDefaults
table)
```

Adds values specific to this theme to the defaults table. This method
is invoked when the look and feel defaults are obtained from

MetalLookAndFeel

.

This implementation does nothing; it is provided for subclasses
that wish to customize the defaults table.

**Parameters:** table

- the

UIDefaults

to add the values to
**See Also:** MetalLookAndFeel.getDefaults()

Constructor Detail

- MetalTheme

```java
public MetalTheme()
```

---

#### Constructor Detail

MetalTheme

```java
public MetalTheme()
```

---

#### MetalTheme

public MetalTheme()

Method Detail

- getName

```java
public abstract
String
getName()
```

Returns the name of this theme.

**Returns:** the name of this theme

- getPrimary1

```java
protected abstract
ColorUIResource
getPrimary1()
```

Returns the primary 1 color.

**Returns:** the primary 1 color

- getPrimary2

```java
protected abstract
ColorUIResource
getPrimary2()
```

Returns the primary 2 color.

**Returns:** the primary 2 color

- getPrimary3

```java
protected abstract
ColorUIResource
getPrimary3()
```

Returns the primary 3 color.

**Returns:** the primary 3 color

- getSecondary1

```java
protected abstract
ColorUIResource
getSecondary1()
```

Returns the secondary 1 color.

**Returns:** the secondary 1 color

- getSecondary2

```java
protected abstract
ColorUIResource
getSecondary2()
```

Returns the secondary 2 color.

**Returns:** the secondary 2 color

- getSecondary3

```java
protected abstract
ColorUIResource
getSecondary3()
```

Returns the secondary 3 color.

**Returns:** the secondary 3 color

- getControlTextFont

```java
public abstract
FontUIResource
getControlTextFont()
```

Returns the control text font.

**Returns:** the control text font

- getSystemTextFont

```java
public abstract
FontUIResource
getSystemTextFont()
```

Returns the system text font.

**Returns:** the system text font

- getUserTextFont

```java
public abstract
FontUIResource
getUserTextFont()
```

Returns the user text font.

**Returns:** the user text font

- getMenuTextFont

```java
public abstract
FontUIResource
getMenuTextFont()
```

Returns the menu text font.

**Returns:** the menu text font

- getWindowTitleFont

```java
public abstract
FontUIResource
getWindowTitleFont()
```

Returns the window title font.

**Returns:** the window title font

- getSubTextFont

```java
public abstract
FontUIResource
getSubTextFont()
```

Returns the sub-text font.

**Returns:** the sub-text font

- getWhite

```java
protected
ColorUIResource
getWhite()
```

Returns the white color. This returns opaque white
(

0xFFFFFFFF

).

**Returns:** the white color

- getBlack

```java
protected
ColorUIResource
getBlack()
```

Returns the black color. This returns opaque black
(

0xFF000000

).

**Returns:** the black color

- getFocusColor

```java
public
ColorUIResource
getFocusColor()
```

Returns the focus color. This returns the value of

getPrimary2()

.

**Returns:** the focus color

- getDesktopColor

```java
public
ColorUIResource
getDesktopColor()
```

Returns the desktop color. This returns the value of

getPrimary2()

.

**Returns:** the desktop color

- getControl

```java
public
ColorUIResource
getControl()
```

Returns the control color. This returns the value of

getSecondary3()

.

**Returns:** the control color

- getControlShadow

```java
public
ColorUIResource
getControlShadow()
```

Returns the control shadow color. This returns
the value of

getSecondary2()

.

**Returns:** the control shadow color

- getControlDarkShadow

```java
public
ColorUIResource
getControlDarkShadow()
```

Returns the control dark shadow color. This returns
the value of

getSecondary1()

.

**Returns:** the control dark shadow color

- getControlInfo

```java
public
ColorUIResource
getControlInfo()
```

Returns the control info color. This returns
the value of

getBlack()

.

**Returns:** the control info color

- getControlHighlight

```java
public
ColorUIResource
getControlHighlight()
```

Returns the control highlight color. This returns
the value of

getWhite()

.

**Returns:** the control highlight color

- getControlDisabled

```java
public
ColorUIResource
getControlDisabled()
```

Returns the control disabled color. This returns
the value of

getSecondary2()

.

**Returns:** the control disabled color

- getPrimaryControl

```java
public
ColorUIResource
getPrimaryControl()
```

Returns the primary control color. This returns
the value of

getPrimary3()

.

**Returns:** the primary control color

- getPrimaryControlShadow

```java
public
ColorUIResource
getPrimaryControlShadow()
```

Returns the primary control shadow color. This returns
the value of

getPrimary2()

.

**Returns:** the primary control shadow color

- getPrimaryControlDarkShadow

```java
public
ColorUIResource
getPrimaryControlDarkShadow()
```

Returns the primary control dark shadow color. This
returns the value of

getPrimary1()

.

**Returns:** the primary control dark shadow color

- getPrimaryControlInfo

```java
public
ColorUIResource
getPrimaryControlInfo()
```

Returns the primary control info color. This
returns the value of

getBlack()

.

**Returns:** the primary control info color

- getPrimaryControlHighlight

```java
public
ColorUIResource
getPrimaryControlHighlight()
```

Returns the primary control highlight color. This
returns the value of

getWhite()

.

**Returns:** the primary control highlight color

- getSystemTextColor

```java
public
ColorUIResource
getSystemTextColor()
```

Returns the system text color. This returns the value of

getBlack()

.

**Returns:** the system text color

- getControlTextColor

```java
public
ColorUIResource
getControlTextColor()
```

Returns the control text color. This returns the value of

getControlInfo()

.

**Returns:** the control text color

- getInactiveControlTextColor

```java
public
ColorUIResource
getInactiveControlTextColor()
```

Returns the inactive control text color. This returns the value of

getControlDisabled()

.

**Returns:** the inactive control text color

- getInactiveSystemTextColor

```java
public
ColorUIResource
getInactiveSystemTextColor()
```

Returns the inactive system text color. This returns the value of

getSecondary2()

.

**Returns:** the inactive system text color

- getUserTextColor

```java
public
ColorUIResource
getUserTextColor()
```

Returns the user text color. This returns the value of

getBlack()

.

**Returns:** the user text color

- getTextHighlightColor

```java
public
ColorUIResource
getTextHighlightColor()
```

Returns the text highlight color. This returns the value of

getPrimary3()

.

**Returns:** the text highlight color

- getHighlightedTextColor

```java
public
ColorUIResource
getHighlightedTextColor()
```

Returns the highlighted text color. This returns the value of

getControlTextColor()

.

**Returns:** the highlighted text color

- getWindowBackground

```java
public
ColorUIResource
getWindowBackground()
```

Returns the window background color. This returns the value of

getWhite()

.

**Returns:** the window background color

- getWindowTitleBackground

```java
public
ColorUIResource
getWindowTitleBackground()
```

Returns the window title background color. This returns the value of

getPrimary3()

.

**Returns:** the window title background color

- getWindowTitleForeground

```java
public
ColorUIResource
getWindowTitleForeground()
```

Returns the window title foreground color. This returns the value of

getBlack()

.

**Returns:** the window title foreground color

- getWindowTitleInactiveBackground

```java
public
ColorUIResource
getWindowTitleInactiveBackground()
```

Returns the window title inactive background color. This
returns the value of

getSecondary3()

.

**Returns:** the window title inactive background color

- getWindowTitleInactiveForeground

```java
public
ColorUIResource
getWindowTitleInactiveForeground()
```

Returns the window title inactive foreground color. This
returns the value of

getBlack()

.

**Returns:** the window title inactive foreground color

- getMenuBackground

```java
public
ColorUIResource
getMenuBackground()
```

Returns the menu background color. This
returns the value of

getSecondary3()

.

**Returns:** the menu background color

- getMenuForeground

```java
public
ColorUIResource
getMenuForeground()
```

Returns the menu foreground color. This
returns the value of

getBlack()

.

**Returns:** the menu foreground color

- getMenuSelectedBackground

```java
public
ColorUIResource
getMenuSelectedBackground()
```

Returns the menu selected background color. This
returns the value of

getPrimary2()

.

**Returns:** the menu selected background color

- getMenuSelectedForeground

```java
public
ColorUIResource
getMenuSelectedForeground()
```

Returns the menu selected foreground color. This
returns the value of

getBlack()

.

**Returns:** the menu selected foreground color

- getMenuDisabledForeground

```java
public
ColorUIResource
getMenuDisabledForeground()
```

Returns the menu disabled foreground color. This
returns the value of

getSecondary2()

.

**Returns:** the menu disabled foreground color

- getSeparatorBackground

```java
public
ColorUIResource
getSeparatorBackground()
```

Returns the separator background color. This
returns the value of

getWhite()

.

**Returns:** the separator background color

- getSeparatorForeground

```java
public
ColorUIResource
getSeparatorForeground()
```

Returns the separator foreground color. This
returns the value of

getPrimary1()

.

**Returns:** the separator foreground color

- getAcceleratorForeground

```java
public
ColorUIResource
getAcceleratorForeground()
```

Returns the accelerator foreground color. This
returns the value of

getPrimary1()

.

**Returns:** the accelerator foreground color

- getAcceleratorSelectedForeground

```java
public
ColorUIResource
getAcceleratorSelectedForeground()
```

Returns the accelerator selected foreground color. This
returns the value of

getBlack()

.

**Returns:** the accelerator selected foreground color

- addCustomEntriesToTable

```java
public void addCustomEntriesToTable​(
UIDefaults
table)
```

Adds values specific to this theme to the defaults table. This method
is invoked when the look and feel defaults are obtained from

MetalLookAndFeel

.

This implementation does nothing; it is provided for subclasses
that wish to customize the defaults table.

**Parameters:** table

- the

UIDefaults

to add the values to
**See Also:** MetalLookAndFeel.getDefaults()

---

#### Method Detail

getName

```java
public abstract
String
getName()
```

Returns the name of this theme.

**Returns:** the name of this theme

---

#### getName

public abstract

String

getName()

Returns the name of this theme.

getPrimary1

```java
protected abstract
ColorUIResource
getPrimary1()
```

Returns the primary 1 color.

**Returns:** the primary 1 color

---

#### getPrimary1

protected abstract

ColorUIResource

getPrimary1()

Returns the primary 1 color.

getPrimary2

```java
protected abstract
ColorUIResource
getPrimary2()
```

Returns the primary 2 color.

**Returns:** the primary 2 color

---

#### getPrimary2

protected abstract

ColorUIResource

getPrimary2()

Returns the primary 2 color.

getPrimary3

```java
protected abstract
ColorUIResource
getPrimary3()
```

Returns the primary 3 color.

**Returns:** the primary 3 color

---

#### getPrimary3

protected abstract

ColorUIResource

getPrimary3()

Returns the primary 3 color.

getSecondary1

```java
protected abstract
ColorUIResource
getSecondary1()
```

Returns the secondary 1 color.

**Returns:** the secondary 1 color

---

#### getSecondary1

protected abstract

ColorUIResource

getSecondary1()

Returns the secondary 1 color.

getSecondary2

```java
protected abstract
ColorUIResource
getSecondary2()
```

Returns the secondary 2 color.

**Returns:** the secondary 2 color

---

#### getSecondary2

protected abstract

ColorUIResource

getSecondary2()

Returns the secondary 2 color.

getSecondary3

```java
protected abstract
ColorUIResource
getSecondary3()
```

Returns the secondary 3 color.

**Returns:** the secondary 3 color

---

#### getSecondary3

protected abstract

ColorUIResource

getSecondary3()

Returns the secondary 3 color.

getControlTextFont

```java
public abstract
FontUIResource
getControlTextFont()
```

Returns the control text font.

**Returns:** the control text font

---

#### getControlTextFont

public abstract

FontUIResource

getControlTextFont()

Returns the control text font.

getSystemTextFont

```java
public abstract
FontUIResource
getSystemTextFont()
```

Returns the system text font.

**Returns:** the system text font

---

#### getSystemTextFont

public abstract

FontUIResource

getSystemTextFont()

Returns the system text font.

getUserTextFont

```java
public abstract
FontUIResource
getUserTextFont()
```

Returns the user text font.

**Returns:** the user text font

---

#### getUserTextFont

public abstract

FontUIResource

getUserTextFont()

Returns the user text font.

getMenuTextFont

```java
public abstract
FontUIResource
getMenuTextFont()
```

Returns the menu text font.

**Returns:** the menu text font

---

#### getMenuTextFont

public abstract

FontUIResource

getMenuTextFont()

Returns the menu text font.

getWindowTitleFont

```java
public abstract
FontUIResource
getWindowTitleFont()
```

Returns the window title font.

**Returns:** the window title font

---

#### getWindowTitleFont

public abstract

FontUIResource

getWindowTitleFont()

Returns the window title font.

getSubTextFont

```java
public abstract
FontUIResource
getSubTextFont()
```

Returns the sub-text font.

**Returns:** the sub-text font

---

#### getSubTextFont

public abstract

FontUIResource

getSubTextFont()

Returns the sub-text font.

getWhite

```java
protected
ColorUIResource
getWhite()
```

Returns the white color. This returns opaque white
(

0xFFFFFFFF

).

**Returns:** the white color

---

#### getWhite

protected

ColorUIResource

getWhite()

Returns the white color. This returns opaque white
(

0xFFFFFFFF

).

getBlack

```java
protected
ColorUIResource
getBlack()
```

Returns the black color. This returns opaque black
(

0xFF000000

).

**Returns:** the black color

---

#### getBlack

protected

ColorUIResource

getBlack()

Returns the black color. This returns opaque black
(

0xFF000000

).

getFocusColor

```java
public
ColorUIResource
getFocusColor()
```

Returns the focus color. This returns the value of

getPrimary2()

.

**Returns:** the focus color

---

#### getFocusColor

public

ColorUIResource

getFocusColor()

Returns the focus color. This returns the value of

getPrimary2()

.

getDesktopColor

```java
public
ColorUIResource
getDesktopColor()
```

Returns the desktop color. This returns the value of

getPrimary2()

.

**Returns:** the desktop color

---

#### getDesktopColor

public

ColorUIResource

getDesktopColor()

Returns the desktop color. This returns the value of

getPrimary2()

.

getControl

```java
public
ColorUIResource
getControl()
```

Returns the control color. This returns the value of

getSecondary3()

.

**Returns:** the control color

---

#### getControl

public

ColorUIResource

getControl()

Returns the control color. This returns the value of

getSecondary3()

.

getControlShadow

```java
public
ColorUIResource
getControlShadow()
```

Returns the control shadow color. This returns
the value of

getSecondary2()

.

**Returns:** the control shadow color

---

#### getControlShadow

public

ColorUIResource

getControlShadow()

Returns the control shadow color. This returns
the value of

getSecondary2()

.

getControlDarkShadow

```java
public
ColorUIResource
getControlDarkShadow()
```

Returns the control dark shadow color. This returns
the value of

getSecondary1()

.

**Returns:** the control dark shadow color

---

#### getControlDarkShadow

public

ColorUIResource

getControlDarkShadow()

Returns the control dark shadow color. This returns
the value of

getSecondary1()

.

getControlInfo

```java
public
ColorUIResource
getControlInfo()
```

Returns the control info color. This returns
the value of

getBlack()

.

**Returns:** the control info color

---

#### getControlInfo

public

ColorUIResource

getControlInfo()

Returns the control info color. This returns
the value of

getBlack()

.

getControlHighlight

```java
public
ColorUIResource
getControlHighlight()
```

Returns the control highlight color. This returns
the value of

getWhite()

.

**Returns:** the control highlight color

---

#### getControlHighlight

public

ColorUIResource

getControlHighlight()

Returns the control highlight color. This returns
the value of

getWhite()

.

getControlDisabled

```java
public
ColorUIResource
getControlDisabled()
```

Returns the control disabled color. This returns
the value of

getSecondary2()

.

**Returns:** the control disabled color

---

#### getControlDisabled

public

ColorUIResource

getControlDisabled()

Returns the control disabled color. This returns
the value of

getSecondary2()

.

getPrimaryControl

```java
public
ColorUIResource
getPrimaryControl()
```

Returns the primary control color. This returns
the value of

getPrimary3()

.

**Returns:** the primary control color

---

#### getPrimaryControl

public

ColorUIResource

getPrimaryControl()

Returns the primary control color. This returns
the value of

getPrimary3()

.

getPrimaryControlShadow

```java
public
ColorUIResource
getPrimaryControlShadow()
```

Returns the primary control shadow color. This returns
the value of

getPrimary2()

.

**Returns:** the primary control shadow color

---

#### getPrimaryControlShadow

public

ColorUIResource

getPrimaryControlShadow()

Returns the primary control shadow color. This returns
the value of

getPrimary2()

.

getPrimaryControlDarkShadow

```java
public
ColorUIResource
getPrimaryControlDarkShadow()
```

Returns the primary control dark shadow color. This
returns the value of

getPrimary1()

.

**Returns:** the primary control dark shadow color

---

#### getPrimaryControlDarkShadow

public

ColorUIResource

getPrimaryControlDarkShadow()

Returns the primary control dark shadow color. This
returns the value of

getPrimary1()

.

getPrimaryControlInfo

```java
public
ColorUIResource
getPrimaryControlInfo()
```

Returns the primary control info color. This
returns the value of

getBlack()

.

**Returns:** the primary control info color

---

#### getPrimaryControlInfo

public

ColorUIResource

getPrimaryControlInfo()

Returns the primary control info color. This
returns the value of

getBlack()

.

getPrimaryControlHighlight

```java
public
ColorUIResource
getPrimaryControlHighlight()
```

Returns the primary control highlight color. This
returns the value of

getWhite()

.

**Returns:** the primary control highlight color

---

#### getPrimaryControlHighlight

public

ColorUIResource

getPrimaryControlHighlight()

Returns the primary control highlight color. This
returns the value of

getWhite()

.

getSystemTextColor

```java
public
ColorUIResource
getSystemTextColor()
```

Returns the system text color. This returns the value of

getBlack()

.

**Returns:** the system text color

---

#### getSystemTextColor

public

ColorUIResource

getSystemTextColor()

Returns the system text color. This returns the value of

getBlack()

.

getControlTextColor

```java
public
ColorUIResource
getControlTextColor()
```

Returns the control text color. This returns the value of

getControlInfo()

.

**Returns:** the control text color

---

#### getControlTextColor

public

ColorUIResource

getControlTextColor()

Returns the control text color. This returns the value of

getControlInfo()

.

getInactiveControlTextColor

```java
public
ColorUIResource
getInactiveControlTextColor()
```

Returns the inactive control text color. This returns the value of

getControlDisabled()

.

**Returns:** the inactive control text color

---

#### getInactiveControlTextColor

public

ColorUIResource

getInactiveControlTextColor()

Returns the inactive control text color. This returns the value of

getControlDisabled()

.

getInactiveSystemTextColor

```java
public
ColorUIResource
getInactiveSystemTextColor()
```

Returns the inactive system text color. This returns the value of

getSecondary2()

.

**Returns:** the inactive system text color

---

#### getInactiveSystemTextColor

public

ColorUIResource

getInactiveSystemTextColor()

Returns the inactive system text color. This returns the value of

getSecondary2()

.

getUserTextColor

```java
public
ColorUIResource
getUserTextColor()
```

Returns the user text color. This returns the value of

getBlack()

.

**Returns:** the user text color

---

#### getUserTextColor

public

ColorUIResource

getUserTextColor()

Returns the user text color. This returns the value of

getBlack()

.

getTextHighlightColor

```java
public
ColorUIResource
getTextHighlightColor()
```

Returns the text highlight color. This returns the value of

getPrimary3()

.

**Returns:** the text highlight color

---

#### getTextHighlightColor

public

ColorUIResource

getTextHighlightColor()

Returns the text highlight color. This returns the value of

getPrimary3()

.

getHighlightedTextColor

```java
public
ColorUIResource
getHighlightedTextColor()
```

Returns the highlighted text color. This returns the value of

getControlTextColor()

.

**Returns:** the highlighted text color

---

#### getHighlightedTextColor

public

ColorUIResource

getHighlightedTextColor()

Returns the highlighted text color. This returns the value of

getControlTextColor()

.

getWindowBackground

```java
public
ColorUIResource
getWindowBackground()
```

Returns the window background color. This returns the value of

getWhite()

.

**Returns:** the window background color

---

#### getWindowBackground

public

ColorUIResource

getWindowBackground()

Returns the window background color. This returns the value of

getWhite()

.

getWindowTitleBackground

```java
public
ColorUIResource
getWindowTitleBackground()
```

Returns the window title background color. This returns the value of

getPrimary3()

.

**Returns:** the window title background color

---

#### getWindowTitleBackground

public

ColorUIResource

getWindowTitleBackground()

Returns the window title background color. This returns the value of

getPrimary3()

.

getWindowTitleForeground

```java
public
ColorUIResource
getWindowTitleForeground()
```

Returns the window title foreground color. This returns the value of

getBlack()

.

**Returns:** the window title foreground color

---

#### getWindowTitleForeground

public

ColorUIResource

getWindowTitleForeground()

Returns the window title foreground color. This returns the value of

getBlack()

.

getWindowTitleInactiveBackground

```java
public
ColorUIResource
getWindowTitleInactiveBackground()
```

Returns the window title inactive background color. This
returns the value of

getSecondary3()

.

**Returns:** the window title inactive background color

---

#### getWindowTitleInactiveBackground

public

ColorUIResource

getWindowTitleInactiveBackground()

Returns the window title inactive background color. This
returns the value of

getSecondary3()

.

getWindowTitleInactiveForeground

```java
public
ColorUIResource
getWindowTitleInactiveForeground()
```

Returns the window title inactive foreground color. This
returns the value of

getBlack()

.

**Returns:** the window title inactive foreground color

---

#### getWindowTitleInactiveForeground

public

ColorUIResource

getWindowTitleInactiveForeground()

Returns the window title inactive foreground color. This
returns the value of

getBlack()

.

getMenuBackground

```java
public
ColorUIResource
getMenuBackground()
```

Returns the menu background color. This
returns the value of

getSecondary3()

.

**Returns:** the menu background color

---

#### getMenuBackground

public

ColorUIResource

getMenuBackground()

Returns the menu background color. This
returns the value of

getSecondary3()

.

getMenuForeground

```java
public
ColorUIResource
getMenuForeground()
```

Returns the menu foreground color. This
returns the value of

getBlack()

.

**Returns:** the menu foreground color

---

#### getMenuForeground

public

ColorUIResource

getMenuForeground()

Returns the menu foreground color. This
returns the value of

getBlack()

.

getMenuSelectedBackground

```java
public
ColorUIResource
getMenuSelectedBackground()
```

Returns the menu selected background color. This
returns the value of

getPrimary2()

.

**Returns:** the menu selected background color

---

#### getMenuSelectedBackground

public

ColorUIResource

getMenuSelectedBackground()

Returns the menu selected background color. This
returns the value of

getPrimary2()

.

getMenuSelectedForeground

```java
public
ColorUIResource
getMenuSelectedForeground()
```

Returns the menu selected foreground color. This
returns the value of

getBlack()

.

**Returns:** the menu selected foreground color

---

#### getMenuSelectedForeground

public

ColorUIResource

getMenuSelectedForeground()

Returns the menu selected foreground color. This
returns the value of

getBlack()

.

getMenuDisabledForeground

```java
public
ColorUIResource
getMenuDisabledForeground()
```

Returns the menu disabled foreground color. This
returns the value of

getSecondary2()

.

**Returns:** the menu disabled foreground color

---

#### getMenuDisabledForeground

public

ColorUIResource

getMenuDisabledForeground()

Returns the menu disabled foreground color. This
returns the value of

getSecondary2()

.

getSeparatorBackground

```java
public
ColorUIResource
getSeparatorBackground()
```

Returns the separator background color. This
returns the value of

getWhite()

.

**Returns:** the separator background color

---

#### getSeparatorBackground

public

ColorUIResource

getSeparatorBackground()

Returns the separator background color. This
returns the value of

getWhite()

.

getSeparatorForeground

```java
public
ColorUIResource
getSeparatorForeground()
```

Returns the separator foreground color. This
returns the value of

getPrimary1()

.

**Returns:** the separator foreground color

---

#### getSeparatorForeground

public

ColorUIResource

getSeparatorForeground()

Returns the separator foreground color. This
returns the value of

getPrimary1()

.

getAcceleratorForeground

```java
public
ColorUIResource
getAcceleratorForeground()
```

Returns the accelerator foreground color. This
returns the value of

getPrimary1()

.

**Returns:** the accelerator foreground color

---

#### getAcceleratorForeground

public

ColorUIResource

getAcceleratorForeground()

Returns the accelerator foreground color. This
returns the value of

getPrimary1()

.

getAcceleratorSelectedForeground

```java
public
ColorUIResource
getAcceleratorSelectedForeground()
```

Returns the accelerator selected foreground color. This
returns the value of

getBlack()

.

**Returns:** the accelerator selected foreground color

---

#### getAcceleratorSelectedForeground

public

ColorUIResource

getAcceleratorSelectedForeground()

Returns the accelerator selected foreground color. This
returns the value of

getBlack()

.

addCustomEntriesToTable

```java
public void addCustomEntriesToTable​(
UIDefaults
table)
```

Adds values specific to this theme to the defaults table. This method
is invoked when the look and feel defaults are obtained from

MetalLookAndFeel

.

This implementation does nothing; it is provided for subclasses
that wish to customize the defaults table.

**Parameters:** table

- the

UIDefaults

to add the values to
**See Also:** MetalLookAndFeel.getDefaults()

---

#### addCustomEntriesToTable

public void addCustomEntriesToTable​(

UIDefaults

table)

Adds values specific to this theme to the defaults table. This method
is invoked when the look and feel defaults are obtained from

MetalLookAndFeel

.

This implementation does nothing; it is provided for subclasses
that wish to customize the defaults table.

This implementation does nothing; it is provided for subclasses
that wish to customize the defaults table.

---

