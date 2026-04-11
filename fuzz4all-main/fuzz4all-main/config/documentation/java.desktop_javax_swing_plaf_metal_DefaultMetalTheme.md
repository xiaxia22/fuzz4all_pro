# Class DefaultMetalTheme

**Source:** `java.desktop\javax\swing\plaf\metal\DefaultMetalTheme.html`

### Class Description

```java
public class
DefaultMetalTheme

extends
MetalTheme
```

A concrete implementation of

MetalTheme

providing
the original look of the Java Look and Feel, code-named "Steel". Refer
to

MetalLookAndFeel.setCurrentTheme(javax.swing.plaf.metal.MetalTheme)

for details on changing
the default theme.

All colors returned by

DefaultMetalTheme

are completely
opaque.

Font Style

DefaultMetalTheme

uses bold fonts for many controls. To make all
controls (with the exception of the internal frame title bars and
client decorated frame title bars) use plain fonts you can do either of
the following:

- Set the system property

swing.boldMetal

to

false

. For example,

java -Dswing.boldMetal=false MyApp

.

Set the defaults property

swing.boldMetal

to

Boolean.FALSE

. For example:

UIManager.put("swing.boldMetal", Boolean.FALSE);

The defaults property

swing.boldMetal

, if set,
takes precedence over the system property of the same name. After
setting this defaults property you need to re-install

MetalLookAndFeel

, as well as update the UI
of any previously created widgets. Otherwise the results are undefined.
The following illustrates how to do this:

```java
// turn off bold fonts
UIManager.put("swing.boldMetal", Boolean.FALSE);

// re-install the Metal Look and Feel
UIManager.setLookAndFeel(new MetalLookAndFeel());

// Update the ComponentUIs for all Components. This
// needs to be invoked for all windows.
SwingUtilities.updateComponentTreeUI(rootComponent);
```

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

**Direct Known Subclasses:** OceanTheme

---

### Field Details

*No entries found.*

### Constructor Details

#### public DefaultMetalTheme()

Creates and returns an instance of

DefaultMetalTheme

.

---

### Method Details

#### public
String
getName()

Returns the name of this theme. This returns

"Steel"

.

**Specified by:**
- getName

in class

MetalTheme

**Returns:**
- the name of this theme.

---

#### protected
ColorUIResource
getPrimary1()

Returns the primary 1 color. This returns a color with rgb values
of 102, 102, and 153, respectively.

**Specified by:**
- getPrimary1

in class

MetalTheme

**Returns:**
- the primary 1 color

---

#### protected
ColorUIResource
getPrimary2()

Returns the primary 2 color. This returns a color with rgb values
of 153, 153, 204, respectively.

**Specified by:**
- getPrimary2

in class

MetalTheme

**Returns:**
- the primary 2 color

---

#### protected
ColorUIResource
getPrimary3()

Returns the primary 3 color. This returns a color with rgb values
204, 204, 255, respectively.

**Specified by:**
- getPrimary3

in class

MetalTheme

**Returns:**
- the primary 3 color

---

#### protected
ColorUIResource
getSecondary1()

Returns the secondary 1 color. This returns a color with rgb values
102, 102, and 102, respectively.

**Specified by:**
- getSecondary1

in class

MetalTheme

**Returns:**
- the secondary 1 color

---

#### protected
ColorUIResource
getSecondary2()

Returns the secondary 2 color. This returns a color with rgb values
153, 153, and 153, respectively.

**Specified by:**
- getSecondary2

in class

MetalTheme

**Returns:**
- the secondary 2 color

---

#### protected
ColorUIResource
getSecondary3()

Returns the secondary 3 color. This returns a color with rgb values
204, 204, and 204, respectively.

**Specified by:**
- getSecondary3

in class

MetalTheme

**Returns:**
- the secondary 3 color

---

#### public
FontUIResource
getControlTextFont()

Returns the control text font. This returns Dialog, 12pt. If
plain fonts have been enabled as described in

font style

, the font style is plain. Otherwise the font style is
bold.

**Specified by:**
- getControlTextFont

in class

MetalTheme

**Returns:**
- the control text font

---

#### public
FontUIResource
getSystemTextFont()

Returns the system text font. This returns Dialog, 12pt, plain.

**Specified by:**
- getSystemTextFont

in class

MetalTheme

**Returns:**
- the system text font

---

#### public
FontUIResource
getUserTextFont()

Returns the user text font. This returns Dialog, 12pt, plain.

**Specified by:**
- getUserTextFont

in class

MetalTheme

**Returns:**
- the user text font

---

#### public
FontUIResource
getMenuTextFont()

Returns the menu text font. This returns Dialog, 12pt. If
plain fonts have been enabled as described in

font style

, the font style is plain. Otherwise the font style is
bold.

**Specified by:**
- getMenuTextFont

in class

MetalTheme

**Returns:**
- the menu text font

---

#### public
FontUIResource
getWindowTitleFont()

Returns the window title font. This returns Dialog, 12pt, bold.

**Specified by:**
- getWindowTitleFont

in class

MetalTheme

**Returns:**
- the window title font

---

#### public
FontUIResource
getSubTextFont()

Returns the sub-text font. This returns Dialog, 10pt, plain.

**Specified by:**
- getSubTextFont

in class

MetalTheme

**Returns:**
- the sub-text font

---

### Additional Sections

#### Class DefaultMetalTheme

java.lang.Object

- javax.swing.plaf.metal.MetalTheme
- - javax.swing.plaf.metal.DefaultMetalTheme

javax.swing.plaf.metal.MetalTheme

- javax.swing.plaf.metal.DefaultMetalTheme

javax.swing.plaf.metal.DefaultMetalTheme

**Direct Known Subclasses:** OceanTheme

```java
public class
DefaultMetalTheme

extends
MetalTheme
```

A concrete implementation of

MetalTheme

providing
the original look of the Java Look and Feel, code-named "Steel". Refer
to

MetalLookAndFeel.setCurrentTheme(javax.swing.plaf.metal.MetalTheme)

for details on changing
the default theme.

All colors returned by

DefaultMetalTheme

are completely
opaque.

Font Style

DefaultMetalTheme

uses bold fonts for many controls. To make all
controls (with the exception of the internal frame title bars and
client decorated frame title bars) use plain fonts you can do either of
the following:

- Set the system property

swing.boldMetal

to

false

. For example,

java -Dswing.boldMetal=false MyApp

.

Set the defaults property

swing.boldMetal

to

Boolean.FALSE

. For example:

UIManager.put("swing.boldMetal", Boolean.FALSE);

The defaults property

swing.boldMetal

, if set,
takes precedence over the system property of the same name. After
setting this defaults property you need to re-install

MetalLookAndFeel

, as well as update the UI
of any previously created widgets. Otherwise the results are undefined.
The following illustrates how to do this:

```java
// turn off bold fonts
UIManager.put("swing.boldMetal", Boolean.FALSE);

// re-install the Metal Look and Feel
UIManager.setLookAndFeel(new MetalLookAndFeel());

// Update the ComponentUIs for all Components. This
// needs to be invoked for all windows.
SwingUtilities.updateComponentTreeUI(rootComponent);
```

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

**See Also:** MetalLookAndFeel

,

MetalLookAndFeel.setCurrentTheme(javax.swing.plaf.metal.MetalTheme)

public class

DefaultMetalTheme

extends

MetalTheme

A concrete implementation of

MetalTheme

providing
the original look of the Java Look and Feel, code-named "Steel". Refer
to

MetalLookAndFeel.setCurrentTheme(javax.swing.plaf.metal.MetalTheme)

for details on changing
the default theme.

All colors returned by

DefaultMetalTheme

are completely
opaque.

Font Style

DefaultMetalTheme

uses bold fonts for many controls. To make all
controls (with the exception of the internal frame title bars and
client decorated frame title bars) use plain fonts you can do either of
the following:

- Set the system property

swing.boldMetal

to

false

. For example,

java -Dswing.boldMetal=false MyApp

.

Set the defaults property

swing.boldMetal

to

Boolean.FALSE

. For example:

UIManager.put("swing.boldMetal", Boolean.FALSE);

The defaults property

swing.boldMetal

, if set,
takes precedence over the system property of the same name. After
setting this defaults property you need to re-install

MetalLookAndFeel

, as well as update the UI
of any previously created widgets. Otherwise the results are undefined.
The following illustrates how to do this:

```java
// turn off bold fonts
UIManager.put("swing.boldMetal", Boolean.FALSE);

// re-install the Metal Look and Feel
UIManager.setLookAndFeel(new MetalLookAndFeel());

// Update the ComponentUIs for all Components. This
// needs to be invoked for all windows.
SwingUtilities.updateComponentTreeUI(rootComponent);
```

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

All colors returned by

DefaultMetalTheme

are completely
opaque.

Font Style

DefaultMetalTheme

uses bold fonts for many controls. To make all
controls (with the exception of the internal frame title bars and
client decorated frame title bars) use plain fonts you can do either of
the following:

- Set the system property

swing.boldMetal

to

false

. For example,

java -Dswing.boldMetal=false MyApp

.

Set the defaults property

swing.boldMetal

to

Boolean.FALSE

. For example:

UIManager.put("swing.boldMetal", Boolean.FALSE);

The defaults property

swing.boldMetal

, if set,
takes precedence over the system property of the same name. After
setting this defaults property you need to re-install

MetalLookAndFeel

, as well as update the UI
of any previously created widgets. Otherwise the results are undefined.
The following illustrates how to do this:

```java
// turn off bold fonts
UIManager.put("swing.boldMetal", Boolean.FALSE);

// re-install the Metal Look and Feel
UIManager.setLookAndFeel(new MetalLookAndFeel());

// Update the ComponentUIs for all Components. This
// needs to be invoked for all windows.
SwingUtilities.updateComponentTreeUI(rootComponent);
```

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

---

#### Font Style

Set the system property

swing.boldMetal

to

false

. For example,

java -Dswing.boldMetal=false MyApp

.

Set the defaults property

swing.boldMetal

to

Boolean.FALSE

. For example:

UIManager.put("swing.boldMetal", Boolean.FALSE);

// turn off bold fonts
UIManager.put("swing.boldMetal", Boolean.FALSE);

// re-install the Metal Look and Feel
UIManager.setLookAndFeel(new MetalLookAndFeel());

// Update the ComponentUIs for all Components. This
// needs to be invoked for all windows.
SwingUtilities.updateComponentTreeUI(rootComponent);

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

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DefaultMetalTheme

()

Creates and returns an instance of

DefaultMetalTheme

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

FontUIResource

getControlTextFont

()

Returns the control text font.

FontUIResource

getMenuTextFont

()

Returns the menu text font.

String

getName

()

Returns the name of this theme.

protected

ColorUIResource

getPrimary1

()

Returns the primary 1 color.

protected

ColorUIResource

getPrimary2

()

Returns the primary 2 color.

protected

ColorUIResource

getPrimary3

()

Returns the primary 3 color.

protected

ColorUIResource

getSecondary1

()

Returns the secondary 1 color.

protected

ColorUIResource

getSecondary2

()

Returns the secondary 2 color.

protected

ColorUIResource

getSecondary3

()

Returns the secondary 3 color.

FontUIResource

getSubTextFont

()

Returns the sub-text font.

FontUIResource

getSystemTextFont

()

Returns the system text font.

FontUIResource

getUserTextFont

()

Returns the user text font.

FontUIResource

getWindowTitleFont

()

Returns the window title font.

- Methods declared in class javax.swing.plaf.metal.

MetalTheme

addCustomEntriesToTable

,

getAcceleratorForeground

,

getAcceleratorSelectedForeground

,

getBlack

,

getControl

,

getControlDarkShadow

,

getControlDisabled

,

getControlHighlight

,

getControlInfo

,

getControlShadow

,

getControlTextColor

,

getDesktopColor

,

getFocusColor

,

getHighlightedTextColor

,

getInactiveControlTextColor

,

getInactiveSystemTextColor

,

getMenuBackground

,

getMenuDisabledForeground

,

getMenuForeground

,

getMenuSelectedBackground

,

getMenuSelectedForeground

,

getPrimaryControl

,

getPrimaryControlDarkShadow

,

getPrimaryControlHighlight

,

getPrimaryControlInfo

,

getPrimaryControlShadow

,

getSeparatorBackground

,

getSeparatorForeground

,

getSystemTextColor

,

getTextHighlightColor

,

getUserTextColor

,

getWhite

,

getWindowBackground

,

getWindowTitleBackground

,

getWindowTitleForeground

,

getWindowTitleInactiveBackground

,

getWindowTitleInactiveForeground

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

DefaultMetalTheme

()

Creates and returns an instance of

DefaultMetalTheme

.

---

#### Constructor Summary

Creates and returns an instance of

DefaultMetalTheme

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

FontUIResource

getControlTextFont

()

Returns the control text font.

FontUIResource

getMenuTextFont

()

Returns the menu text font.

String

getName

()

Returns the name of this theme.

protected

ColorUIResource

getPrimary1

()

Returns the primary 1 color.

protected

ColorUIResource

getPrimary2

()

Returns the primary 2 color.

protected

ColorUIResource

getPrimary3

()

Returns the primary 3 color.

protected

ColorUIResource

getSecondary1

()

Returns the secondary 1 color.

protected

ColorUIResource

getSecondary2

()

Returns the secondary 2 color.

protected

ColorUIResource

getSecondary3

()

Returns the secondary 3 color.

FontUIResource

getSubTextFont

()

Returns the sub-text font.

FontUIResource

getSystemTextFont

()

Returns the system text font.

FontUIResource

getUserTextFont

()

Returns the user text font.

FontUIResource

getWindowTitleFont

()

Returns the window title font.

- Methods declared in class javax.swing.plaf.metal.

MetalTheme

addCustomEntriesToTable

,

getAcceleratorForeground

,

getAcceleratorSelectedForeground

,

getBlack

,

getControl

,

getControlDarkShadow

,

getControlDisabled

,

getControlHighlight

,

getControlInfo

,

getControlShadow

,

getControlTextColor

,

getDesktopColor

,

getFocusColor

,

getHighlightedTextColor

,

getInactiveControlTextColor

,

getInactiveSystemTextColor

,

getMenuBackground

,

getMenuDisabledForeground

,

getMenuForeground

,

getMenuSelectedBackground

,

getMenuSelectedForeground

,

getPrimaryControl

,

getPrimaryControlDarkShadow

,

getPrimaryControlHighlight

,

getPrimaryControlInfo

,

getPrimaryControlShadow

,

getSeparatorBackground

,

getSeparatorForeground

,

getSystemTextColor

,

getTextHighlightColor

,

getUserTextColor

,

getWhite

,

getWindowBackground

,

getWindowTitleBackground

,

getWindowTitleForeground

,

getWindowTitleInactiveBackground

,

getWindowTitleInactiveForeground

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

Returns the control text font.

Returns the menu text font.

Returns the name of this theme.

Returns the primary 1 color.

Returns the primary 2 color.

Returns the primary 3 color.

Returns the secondary 1 color.

Returns the secondary 2 color.

Returns the secondary 3 color.

Returns the sub-text font.

Returns the system text font.

Returns the user text font.

Returns the window title font.

Methods declared in class javax.swing.plaf.metal.

MetalTheme

addCustomEntriesToTable

,

getAcceleratorForeground

,

getAcceleratorSelectedForeground

,

getBlack

,

getControl

,

getControlDarkShadow

,

getControlDisabled

,

getControlHighlight

,

getControlInfo

,

getControlShadow

,

getControlTextColor

,

getDesktopColor

,

getFocusColor

,

getHighlightedTextColor

,

getInactiveControlTextColor

,

getInactiveSystemTextColor

,

getMenuBackground

,

getMenuDisabledForeground

,

getMenuForeground

,

getMenuSelectedBackground

,

getMenuSelectedForeground

,

getPrimaryControl

,

getPrimaryControlDarkShadow

,

getPrimaryControlHighlight

,

getPrimaryControlInfo

,

getPrimaryControlShadow

,

getSeparatorBackground

,

getSeparatorForeground

,

getSystemTextColor

,

getTextHighlightColor

,

getUserTextColor

,

getWhite

,

getWindowBackground

,

getWindowTitleBackground

,

getWindowTitleForeground

,

getWindowTitleInactiveBackground

,

getWindowTitleInactiveForeground

---

#### Methods declared in class javax.swing.plaf.metal. MetalTheme

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

- DefaultMetalTheme

```java
public DefaultMetalTheme()
```

Creates and returns an instance of

DefaultMetalTheme

.

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
public
String
getName()
```

Returns the name of this theme. This returns

"Steel"

.

**Specified by:** getName

in class

MetalTheme
**Returns:** the name of this theme.

- getPrimary1

```java
protected
ColorUIResource
getPrimary1()
```

Returns the primary 1 color. This returns a color with rgb values
of 102, 102, and 153, respectively.

**Specified by:** getPrimary1

in class

MetalTheme
**Returns:** the primary 1 color

- getPrimary2

```java
protected
ColorUIResource
getPrimary2()
```

Returns the primary 2 color. This returns a color with rgb values
of 153, 153, 204, respectively.

**Specified by:** getPrimary2

in class

MetalTheme
**Returns:** the primary 2 color

- getPrimary3

```java
protected
ColorUIResource
getPrimary3()
```

Returns the primary 3 color. This returns a color with rgb values
204, 204, 255, respectively.

**Specified by:** getPrimary3

in class

MetalTheme
**Returns:** the primary 3 color

- getSecondary1

```java
protected
ColorUIResource
getSecondary1()
```

Returns the secondary 1 color. This returns a color with rgb values
102, 102, and 102, respectively.

**Specified by:** getSecondary1

in class

MetalTheme
**Returns:** the secondary 1 color

- getSecondary2

```java
protected
ColorUIResource
getSecondary2()
```

Returns the secondary 2 color. This returns a color with rgb values
153, 153, and 153, respectively.

**Specified by:** getSecondary2

in class

MetalTheme
**Returns:** the secondary 2 color

- getSecondary3

```java
protected
ColorUIResource
getSecondary3()
```

Returns the secondary 3 color. This returns a color with rgb values
204, 204, and 204, respectively.

**Specified by:** getSecondary3

in class

MetalTheme
**Returns:** the secondary 3 color

- getControlTextFont

```java
public
FontUIResource
getControlTextFont()
```

Returns the control text font. This returns Dialog, 12pt. If
plain fonts have been enabled as described in

font style

, the font style is plain. Otherwise the font style is
bold.

**Specified by:** getControlTextFont

in class

MetalTheme
**Returns:** the control text font

- getSystemTextFont

```java
public
FontUIResource
getSystemTextFont()
```

Returns the system text font. This returns Dialog, 12pt, plain.

**Specified by:** getSystemTextFont

in class

MetalTheme
**Returns:** the system text font

- getUserTextFont

```java
public
FontUIResource
getUserTextFont()
```

Returns the user text font. This returns Dialog, 12pt, plain.

**Specified by:** getUserTextFont

in class

MetalTheme
**Returns:** the user text font

- getMenuTextFont

```java
public
FontUIResource
getMenuTextFont()
```

Returns the menu text font. This returns Dialog, 12pt. If
plain fonts have been enabled as described in

font style

, the font style is plain. Otherwise the font style is
bold.

**Specified by:** getMenuTextFont

in class

MetalTheme
**Returns:** the menu text font

- getWindowTitleFont

```java
public
FontUIResource
getWindowTitleFont()
```

Returns the window title font. This returns Dialog, 12pt, bold.

**Specified by:** getWindowTitleFont

in class

MetalTheme
**Returns:** the window title font

- getSubTextFont

```java
public
FontUIResource
getSubTextFont()
```

Returns the sub-text font. This returns Dialog, 10pt, plain.

**Specified by:** getSubTextFont

in class

MetalTheme
**Returns:** the sub-text font

Constructor Detail

- DefaultMetalTheme

```java
public DefaultMetalTheme()
```

Creates and returns an instance of

DefaultMetalTheme

.

---

#### Constructor Detail

DefaultMetalTheme

```java
public DefaultMetalTheme()
```

Creates and returns an instance of

DefaultMetalTheme

.

---

#### DefaultMetalTheme

public DefaultMetalTheme()

Creates and returns an instance of

DefaultMetalTheme

.

Method Detail

- getName

```java
public
String
getName()
```

Returns the name of this theme. This returns

"Steel"

.

**Specified by:** getName

in class

MetalTheme
**Returns:** the name of this theme.

- getPrimary1

```java
protected
ColorUIResource
getPrimary1()
```

Returns the primary 1 color. This returns a color with rgb values
of 102, 102, and 153, respectively.

**Specified by:** getPrimary1

in class

MetalTheme
**Returns:** the primary 1 color

- getPrimary2

```java
protected
ColorUIResource
getPrimary2()
```

Returns the primary 2 color. This returns a color with rgb values
of 153, 153, 204, respectively.

**Specified by:** getPrimary2

in class

MetalTheme
**Returns:** the primary 2 color

- getPrimary3

```java
protected
ColorUIResource
getPrimary3()
```

Returns the primary 3 color. This returns a color with rgb values
204, 204, 255, respectively.

**Specified by:** getPrimary3

in class

MetalTheme
**Returns:** the primary 3 color

- getSecondary1

```java
protected
ColorUIResource
getSecondary1()
```

Returns the secondary 1 color. This returns a color with rgb values
102, 102, and 102, respectively.

**Specified by:** getSecondary1

in class

MetalTheme
**Returns:** the secondary 1 color

- getSecondary2

```java
protected
ColorUIResource
getSecondary2()
```

Returns the secondary 2 color. This returns a color with rgb values
153, 153, and 153, respectively.

**Specified by:** getSecondary2

in class

MetalTheme
**Returns:** the secondary 2 color

- getSecondary3

```java
protected
ColorUIResource
getSecondary3()
```

Returns the secondary 3 color. This returns a color with rgb values
204, 204, and 204, respectively.

**Specified by:** getSecondary3

in class

MetalTheme
**Returns:** the secondary 3 color

- getControlTextFont

```java
public
FontUIResource
getControlTextFont()
```

Returns the control text font. This returns Dialog, 12pt. If
plain fonts have been enabled as described in

font style

, the font style is plain. Otherwise the font style is
bold.

**Specified by:** getControlTextFont

in class

MetalTheme
**Returns:** the control text font

- getSystemTextFont

```java
public
FontUIResource
getSystemTextFont()
```

Returns the system text font. This returns Dialog, 12pt, plain.

**Specified by:** getSystemTextFont

in class

MetalTheme
**Returns:** the system text font

- getUserTextFont

```java
public
FontUIResource
getUserTextFont()
```

Returns the user text font. This returns Dialog, 12pt, plain.

**Specified by:** getUserTextFont

in class

MetalTheme
**Returns:** the user text font

- getMenuTextFont

```java
public
FontUIResource
getMenuTextFont()
```

Returns the menu text font. This returns Dialog, 12pt. If
plain fonts have been enabled as described in

font style

, the font style is plain. Otherwise the font style is
bold.

**Specified by:** getMenuTextFont

in class

MetalTheme
**Returns:** the menu text font

- getWindowTitleFont

```java
public
FontUIResource
getWindowTitleFont()
```

Returns the window title font. This returns Dialog, 12pt, bold.

**Specified by:** getWindowTitleFont

in class

MetalTheme
**Returns:** the window title font

- getSubTextFont

```java
public
FontUIResource
getSubTextFont()
```

Returns the sub-text font. This returns Dialog, 10pt, plain.

**Specified by:** getSubTextFont

in class

MetalTheme
**Returns:** the sub-text font

---

#### Method Detail

getName

```java
public
String
getName()
```

Returns the name of this theme. This returns

"Steel"

.

**Specified by:** getName

in class

MetalTheme
**Returns:** the name of this theme.

---

#### getName

public

String

getName()

Returns the name of this theme. This returns

"Steel"

.

getPrimary1

```java
protected
ColorUIResource
getPrimary1()
```

Returns the primary 1 color. This returns a color with rgb values
of 102, 102, and 153, respectively.

**Specified by:** getPrimary1

in class

MetalTheme
**Returns:** the primary 1 color

---

#### getPrimary1

protected

ColorUIResource

getPrimary1()

Returns the primary 1 color. This returns a color with rgb values
of 102, 102, and 153, respectively.

getPrimary2

```java
protected
ColorUIResource
getPrimary2()
```

Returns the primary 2 color. This returns a color with rgb values
of 153, 153, 204, respectively.

**Specified by:** getPrimary2

in class

MetalTheme
**Returns:** the primary 2 color

---

#### getPrimary2

protected

ColorUIResource

getPrimary2()

Returns the primary 2 color. This returns a color with rgb values
of 153, 153, 204, respectively.

getPrimary3

```java
protected
ColorUIResource
getPrimary3()
```

Returns the primary 3 color. This returns a color with rgb values
204, 204, 255, respectively.

**Specified by:** getPrimary3

in class

MetalTheme
**Returns:** the primary 3 color

---

#### getPrimary3

protected

ColorUIResource

getPrimary3()

Returns the primary 3 color. This returns a color with rgb values
204, 204, 255, respectively.

getSecondary1

```java
protected
ColorUIResource
getSecondary1()
```

Returns the secondary 1 color. This returns a color with rgb values
102, 102, and 102, respectively.

**Specified by:** getSecondary1

in class

MetalTheme
**Returns:** the secondary 1 color

---

#### getSecondary1

protected

ColorUIResource

getSecondary1()

Returns the secondary 1 color. This returns a color with rgb values
102, 102, and 102, respectively.

getSecondary2

```java
protected
ColorUIResource
getSecondary2()
```

Returns the secondary 2 color. This returns a color with rgb values
153, 153, and 153, respectively.

**Specified by:** getSecondary2

in class

MetalTheme
**Returns:** the secondary 2 color

---

#### getSecondary2

protected

ColorUIResource

getSecondary2()

Returns the secondary 2 color. This returns a color with rgb values
153, 153, and 153, respectively.

getSecondary3

```java
protected
ColorUIResource
getSecondary3()
```

Returns the secondary 3 color. This returns a color with rgb values
204, 204, and 204, respectively.

**Specified by:** getSecondary3

in class

MetalTheme
**Returns:** the secondary 3 color

---

#### getSecondary3

protected

ColorUIResource

getSecondary3()

Returns the secondary 3 color. This returns a color with rgb values
204, 204, and 204, respectively.

getControlTextFont

```java
public
FontUIResource
getControlTextFont()
```

Returns the control text font. This returns Dialog, 12pt. If
plain fonts have been enabled as described in

font style

, the font style is plain. Otherwise the font style is
bold.

**Specified by:** getControlTextFont

in class

MetalTheme
**Returns:** the control text font

---

#### getControlTextFont

public

FontUIResource

getControlTextFont()

Returns the control text font. This returns Dialog, 12pt. If
plain fonts have been enabled as described in

font style

, the font style is plain. Otherwise the font style is
bold.

getSystemTextFont

```java
public
FontUIResource
getSystemTextFont()
```

Returns the system text font. This returns Dialog, 12pt, plain.

**Specified by:** getSystemTextFont

in class

MetalTheme
**Returns:** the system text font

---

#### getSystemTextFont

public

FontUIResource

getSystemTextFont()

Returns the system text font. This returns Dialog, 12pt, plain.

getUserTextFont

```java
public
FontUIResource
getUserTextFont()
```

Returns the user text font. This returns Dialog, 12pt, plain.

**Specified by:** getUserTextFont

in class

MetalTheme
**Returns:** the user text font

---

#### getUserTextFont

public

FontUIResource

getUserTextFont()

Returns the user text font. This returns Dialog, 12pt, plain.

getMenuTextFont

```java
public
FontUIResource
getMenuTextFont()
```

Returns the menu text font. This returns Dialog, 12pt. If
plain fonts have been enabled as described in

font style

, the font style is plain. Otherwise the font style is
bold.

**Specified by:** getMenuTextFont

in class

MetalTheme
**Returns:** the menu text font

---

#### getMenuTextFont

public

FontUIResource

getMenuTextFont()

Returns the menu text font. This returns Dialog, 12pt. If
plain fonts have been enabled as described in

font style

, the font style is plain. Otherwise the font style is
bold.

getWindowTitleFont

```java
public
FontUIResource
getWindowTitleFont()
```

Returns the window title font. This returns Dialog, 12pt, bold.

**Specified by:** getWindowTitleFont

in class

MetalTheme
**Returns:** the window title font

---

#### getWindowTitleFont

public

FontUIResource

getWindowTitleFont()

Returns the window title font. This returns Dialog, 12pt, bold.

getSubTextFont

```java
public
FontUIResource
getSubTextFont()
```

Returns the sub-text font. This returns Dialog, 10pt, plain.

**Specified by:** getSubTextFont

in class

MetalTheme
**Returns:** the sub-text font

---

#### getSubTextFont

public

FontUIResource

getSubTextFont()

Returns the sub-text font. This returns Dialog, 10pt, plain.

---

