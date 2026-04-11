# Class SystemColor

**Source:** `java.desktop\java\awt\SystemColor.html`

### Class Description

```java
public final class
SystemColor

extends
Color

implements
Serializable
```

A class to encapsulate symbolic colors representing the color of
native GUI objects on a system. For systems which support the dynamic
update of the system colors (when the user changes the colors)
the actual RGB values of these symbolic colors will also change
dynamically. In order to compare the "current" RGB value of a

SystemColor

object with a non-symbolic Color object,

getRGB

should be used rather than

equals

.

Note that the way in which these system colors are applied to GUI objects
may vary slightly from platform to platform since GUI objects may be
rendered differently on each platform.

System color values may also be available through the

getDesktopProperty

method on

java.awt.Toolkit

.

**All Implemented Interfaces:** Paint

,

Transparency

,

Serializable

---

### Field Details

#### @Native

public static final int DESKTOP

The array index for the

desktop

system color.

**See Also:**
- desktop

,

Constant Field Values

---

#### @Native

public static final int ACTIVE_CAPTION

The array index for the

activeCaption

system color.

**See Also:**
- activeCaption

,

Constant Field Values

---

#### @Native

public static final int ACTIVE_CAPTION_TEXT

The array index for the

activeCaptionText

system color.

**See Also:**
- activeCaptionText

,

Constant Field Values

---

#### @Native

public static final int ACTIVE_CAPTION_BORDER

The array index for the

activeCaptionBorder

system color.

**See Also:**
- activeCaptionBorder

,

Constant Field Values

---

#### @Native

public static final int INACTIVE_CAPTION

The array index for the

inactiveCaption

system color.

**See Also:**
- inactiveCaption

,

Constant Field Values

---

#### @Native

public static final int INACTIVE_CAPTION_TEXT

The array index for the

inactiveCaptionText

system color.

**See Also:**
- inactiveCaptionText

,

Constant Field Values

---

#### @Native

public static final int INACTIVE_CAPTION_BORDER

The array index for the

inactiveCaptionBorder

system color.

**See Also:**
- inactiveCaptionBorder

,

Constant Field Values

---

#### @Native

public static final int WINDOW

The array index for the

window

system color.

**See Also:**
- window

,

Constant Field Values

---

#### @Native

public static final int WINDOW_BORDER

The array index for the

windowBorder

system color.

**See Also:**
- windowBorder

,

Constant Field Values

---

#### @Native

public static final int WINDOW_TEXT

The array index for the

windowText

system color.

**See Also:**
- windowText

,

Constant Field Values

---

#### @Native

public static final int MENU

The array index for the

menu

system color.

**See Also:**
- menu

,

Constant Field Values

---

#### @Native

public static final int MENU_TEXT

The array index for the

menuText

system color.

**See Also:**
- menuText

,

Constant Field Values

---

#### @Native

public static final int TEXT

The array index for the

text

system color.

**See Also:**
- text

,

Constant Field Values

---

#### @Native

public static final int TEXT_TEXT

The array index for the

textText

system color.

**See Also:**
- textText

,

Constant Field Values

---

#### @Native

public static final int TEXT_HIGHLIGHT

The array index for the

textHighlight

system color.

**See Also:**
- textHighlight

,

Constant Field Values

---

#### @Native

public static final int TEXT_HIGHLIGHT_TEXT

The array index for the

textHighlightText

system color.

**See Also:**
- textHighlightText

,

Constant Field Values

---

#### @Native

public static final int TEXT_INACTIVE_TEXT

The array index for the

textInactiveText

system color.

**See Also:**
- textInactiveText

,

Constant Field Values

---

#### @Native

public static final int CONTROL

The array index for the

control

system color.

**See Also:**
- control

,

Constant Field Values

---

#### @Native

public static final int CONTROL_TEXT

The array index for the

controlText

system color.

**See Also:**
- controlText

,

Constant Field Values

---

#### @Native

public static final int CONTROL_HIGHLIGHT

The array index for the

controlHighlight

system color.

**See Also:**
- controlHighlight

,

Constant Field Values

---

#### @Native

public static final int CONTROL_LT_HIGHLIGHT

The array index for the

controlLtHighlight

system color.

**See Also:**
- controlLtHighlight

,

Constant Field Values

---

#### @Native

public static final int CONTROL_SHADOW

The array index for the

controlShadow

system color.

**See Also:**
- controlShadow

,

Constant Field Values

---

#### @Native

public static final int CONTROL_DK_SHADOW

The array index for the

controlDkShadow

system color.

**See Also:**
- controlDkShadow

,

Constant Field Values

---

#### @Native

public static final int SCROLLBAR

The array index for the

scrollbar

system color.

**See Also:**
- scrollbar

,

Constant Field Values

---

#### @Native

public static final int INFO

The array index for the

info

system color.

**See Also:**
- info

,

Constant Field Values

---

#### @Native

public static final int INFO_TEXT

The array index for the

infoText

system color.

**See Also:**
- infoText

,

Constant Field Values

---

#### @Native

public static final int NUM_COLORS

The number of system colors in the array.

**See Also:**
- Constant Field Values

---

#### public static final
SystemColor
desktop

The color rendered for the background of the desktop.

---

#### public static final
SystemColor
activeCaption

The color rendered for the window-title background of the currently active window.

---

#### public static final
SystemColor
activeCaptionText

The color rendered for the window-title text of the currently active window.

---

#### public static final
SystemColor
activeCaptionBorder

The color rendered for the border around the currently active window.

---

#### public static final
SystemColor
inactiveCaption

The color rendered for the window-title background of inactive windows.

---

#### public static final
SystemColor
inactiveCaptionText

The color rendered for the window-title text of inactive windows.

---

#### public static final
SystemColor
inactiveCaptionBorder

The color rendered for the border around inactive windows.

---

#### public static final
SystemColor
window

The color rendered for the background of interior regions inside windows.

---

#### public static final
SystemColor
windowBorder

The color rendered for the border around interior regions inside windows.

---

#### public static final
SystemColor
windowText

The color rendered for text of interior regions inside windows.

---

#### public static final
SystemColor
menu

The color rendered for the background of menus.

---

#### public static final
SystemColor
menuText

The color rendered for the text of menus.

---

#### public static final
SystemColor
text

The color rendered for the background of text control objects, such as
textfields and comboboxes.

---

#### public static final
SystemColor
textText

The color rendered for the text of text control objects, such as textfields
and comboboxes.

---

#### public static final
SystemColor
textHighlight

The color rendered for the background of selected items, such as in menus,
comboboxes, and text.

---

#### public static final
SystemColor
textHighlightText

The color rendered for the text of selected items, such as in menus, comboboxes,
and text.

---

#### public static final
SystemColor
textInactiveText

The color rendered for the text of inactive items, such as in menus.

---

#### public static final
SystemColor
control

The color rendered for the background of control panels and control objects,
such as pushbuttons.

---

#### public static final
SystemColor
controlText

The color rendered for the text of control panels and control objects,
such as pushbuttons.

---

#### public static final
SystemColor
controlHighlight

The color rendered for light areas of 3D control objects, such as pushbuttons.
This color is typically derived from the

control

background color
to provide a 3D effect.

---

#### public static final
SystemColor
controlLtHighlight

The color rendered for highlight areas of 3D control objects, such as pushbuttons.
This color is typically derived from the

control

background color
to provide a 3D effect.

---

#### public static final
SystemColor
controlShadow

The color rendered for shadow areas of 3D control objects, such as pushbuttons.
This color is typically derived from the

control

background color
to provide a 3D effect.

---

#### public static final
SystemColor
controlDkShadow

The color rendered for dark shadow areas on 3D control objects, such as pushbuttons.
This color is typically derived from the

control

background color
to provide a 3D effect.

---

#### public static final
SystemColor
scrollbar

The color rendered for the background of scrollbars.

---

#### public static final
SystemColor
info

The color rendered for the background of tooltips or spot help.

---

#### public static final
SystemColor
infoText

The color rendered for the text of tooltips or spot help.

---

### Constructor Details

*No entries found.*

### Method Details

#### public
String
toString()

Returns a string representation of this

Color

's values.
This method is intended to be used only for debugging purposes,
and the content and format of the returned string may vary between
implementations.
The returned string may be empty but may not be

null

.

**Overrides:**
- toString

in class

Color

**Returns:**
- a string representation of this

Color

---

### Additional Sections

#### Class SystemColor

java.lang.Object

- java.awt.Color
- - java.awt.SystemColor

java.awt.Color

- java.awt.SystemColor

java.awt.SystemColor

**All Implemented Interfaces:** Paint

,

Transparency

,

Serializable

```java
public final class
SystemColor

extends
Color

implements
Serializable
```

A class to encapsulate symbolic colors representing the color of
native GUI objects on a system. For systems which support the dynamic
update of the system colors (when the user changes the colors)
the actual RGB values of these symbolic colors will also change
dynamically. In order to compare the "current" RGB value of a

SystemColor

object with a non-symbolic Color object,

getRGB

should be used rather than

equals

.

Note that the way in which these system colors are applied to GUI objects
may vary slightly from platform to platform since GUI objects may be
rendered differently on each platform.

System color values may also be available through the

getDesktopProperty

method on

java.awt.Toolkit

.

**See Also:** Toolkit.getDesktopProperty(java.lang.String)

,

Serialized Form

public final class

SystemColor

extends

Color

implements

Serializable

A class to encapsulate symbolic colors representing the color of
native GUI objects on a system. For systems which support the dynamic
update of the system colors (when the user changes the colors)
the actual RGB values of these symbolic colors will also change
dynamically. In order to compare the "current" RGB value of a

SystemColor

object with a non-symbolic Color object,

getRGB

should be used rather than

equals

.

Note that the way in which these system colors are applied to GUI objects
may vary slightly from platform to platform since GUI objects may be
rendered differently on each platform.

System color values may also be available through the

getDesktopProperty

method on

java.awt.Toolkit

.

Note that the way in which these system colors are applied to GUI objects
may vary slightly from platform to platform since GUI objects may be
rendered differently on each platform.

System color values may also be available through the

getDesktopProperty

method on

java.awt.Toolkit

.

System color values may also be available through the

getDesktopProperty

method on

java.awt.Toolkit

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

ACTIVE_CAPTION

The array index for the

activeCaption

system color.

static int

ACTIVE_CAPTION_BORDER

The array index for the

activeCaptionBorder

system color.

static int

ACTIVE_CAPTION_TEXT

The array index for the

activeCaptionText

system color.

static

SystemColor

activeCaption

The color rendered for the window-title background of the currently active window.

static

SystemColor

activeCaptionBorder

The color rendered for the border around the currently active window.

static

SystemColor

activeCaptionText

The color rendered for the window-title text of the currently active window.

static

SystemColor

control

The color rendered for the background of control panels and control objects,
such as pushbuttons.

static int

CONTROL

The array index for the

control

system color.

static int

CONTROL_DK_SHADOW

The array index for the

controlDkShadow

system color.

static int

CONTROL_HIGHLIGHT

The array index for the

controlHighlight

system color.

static int

CONTROL_LT_HIGHLIGHT

The array index for the

controlLtHighlight

system color.

static int

CONTROL_SHADOW

The array index for the

controlShadow

system color.

static int

CONTROL_TEXT

The array index for the

controlText

system color.

static

SystemColor

controlDkShadow

The color rendered for dark shadow areas on 3D control objects, such as pushbuttons.

static

SystemColor

controlHighlight

The color rendered for light areas of 3D control objects, such as pushbuttons.

static

SystemColor

controlLtHighlight

The color rendered for highlight areas of 3D control objects, such as pushbuttons.

static

SystemColor

controlShadow

The color rendered for shadow areas of 3D control objects, such as pushbuttons.

static

SystemColor

controlText

The color rendered for the text of control panels and control objects,
such as pushbuttons.

static

SystemColor

desktop

The color rendered for the background of the desktop.

static int

DESKTOP

The array index for the

desktop

system color.

static int

INACTIVE_CAPTION

The array index for the

inactiveCaption

system color.

static int

INACTIVE_CAPTION_BORDER

The array index for the

inactiveCaptionBorder

system color.

static int

INACTIVE_CAPTION_TEXT

The array index for the

inactiveCaptionText

system color.

static

SystemColor

inactiveCaption

The color rendered for the window-title background of inactive windows.

static

SystemColor

inactiveCaptionBorder

The color rendered for the border around inactive windows.

static

SystemColor

inactiveCaptionText

The color rendered for the window-title text of inactive windows.

static

SystemColor

info

The color rendered for the background of tooltips or spot help.

static int

INFO

The array index for the

info

system color.

static int

INFO_TEXT

The array index for the

infoText

system color.

static

SystemColor

infoText

The color rendered for the text of tooltips or spot help.

static

SystemColor

menu

The color rendered for the background of menus.

static int

MENU

The array index for the

menu

system color.

static int

MENU_TEXT

The array index for the

menuText

system color.

static

SystemColor

menuText

The color rendered for the text of menus.

static int

NUM_COLORS

The number of system colors in the array.

static

SystemColor

scrollbar

The color rendered for the background of scrollbars.

static int

SCROLLBAR

The array index for the

scrollbar

system color.

static

SystemColor

text

The color rendered for the background of text control objects, such as
textfields and comboboxes.

static int

TEXT

The array index for the

text

system color.

static int

TEXT_HIGHLIGHT

The array index for the

textHighlight

system color.

static int

TEXT_HIGHLIGHT_TEXT

The array index for the

textHighlightText

system color.

static int

TEXT_INACTIVE_TEXT

The array index for the

textInactiveText

system color.

static int

TEXT_TEXT

The array index for the

textText

system color.

static

SystemColor

textHighlight

The color rendered for the background of selected items, such as in menus,
comboboxes, and text.

static

SystemColor

textHighlightText

The color rendered for the text of selected items, such as in menus, comboboxes,
and text.

static

SystemColor

textInactiveText

The color rendered for the text of inactive items, such as in menus.

static

SystemColor

textText

The color rendered for the text of text control objects, such as textfields
and comboboxes.

static

SystemColor

window

The color rendered for the background of interior regions inside windows.

static int

WINDOW

The array index for the

window

system color.

static int

WINDOW_BORDER

The array index for the

windowBorder

system color.

static int

WINDOW_TEXT

The array index for the

windowText

system color.

static

SystemColor

windowBorder

The color rendered for the border around interior regions inside windows.

static

SystemColor

windowText

The color rendered for text of interior regions inside windows.

- Fields declared in class java.awt.

Color

black

,

BLACK

,

blue

,

BLUE

,

cyan

,

CYAN

,

DARK_GRAY

,

darkGray

,

gray

,

GRAY

,

green

,

GREEN

,

LIGHT_GRAY

,

lightGray

,

magenta

,

MAGENTA

,

orange

,

ORANGE

,

pink

,

PINK

,

red

,

RED

,

white

,

WHITE

,

yellow

,

YELLOW

- Fields declared in interface java.awt.

Transparency

BITMASK

,

OPAQUE

,

TRANSLUCENT

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

toString

()

Returns a string representation of this

Color

's values.

- Methods declared in class java.awt.

Color

brighter

,

createContext

,

darker

,

decode

,

equals

,

getAlpha

,

getBlue

,

getColor

,

getColor

,

getColor

,

getColorComponents

,

getColorComponents

,

getColorSpace

,

getComponents

,

getComponents

,

getGreen

,

getHSBColor

,

getRed

,

getRGB

,

getRGBColorComponents

,

getRGBComponents

,

getTransparency

,

hashCode

,

HSBtoRGB

,

RGBtoHSB

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

static int

ACTIVE_CAPTION

The array index for the

activeCaption

system color.

static int

ACTIVE_CAPTION_BORDER

The array index for the

activeCaptionBorder

system color.

static int

ACTIVE_CAPTION_TEXT

The array index for the

activeCaptionText

system color.

static

SystemColor

activeCaption

The color rendered for the window-title background of the currently active window.

static

SystemColor

activeCaptionBorder

The color rendered for the border around the currently active window.

static

SystemColor

activeCaptionText

The color rendered for the window-title text of the currently active window.

static

SystemColor

control

The color rendered for the background of control panels and control objects,
such as pushbuttons.

static int

CONTROL

The array index for the

control

system color.

static int

CONTROL_DK_SHADOW

The array index for the

controlDkShadow

system color.

static int

CONTROL_HIGHLIGHT

The array index for the

controlHighlight

system color.

static int

CONTROL_LT_HIGHLIGHT

The array index for the

controlLtHighlight

system color.

static int

CONTROL_SHADOW

The array index for the

controlShadow

system color.

static int

CONTROL_TEXT

The array index for the

controlText

system color.

static

SystemColor

controlDkShadow

The color rendered for dark shadow areas on 3D control objects, such as pushbuttons.

static

SystemColor

controlHighlight

The color rendered for light areas of 3D control objects, such as pushbuttons.

static

SystemColor

controlLtHighlight

The color rendered for highlight areas of 3D control objects, such as pushbuttons.

static

SystemColor

controlShadow

The color rendered for shadow areas of 3D control objects, such as pushbuttons.

static

SystemColor

controlText

The color rendered for the text of control panels and control objects,
such as pushbuttons.

static

SystemColor

desktop

The color rendered for the background of the desktop.

static int

DESKTOP

The array index for the

desktop

system color.

static int

INACTIVE_CAPTION

The array index for the

inactiveCaption

system color.

static int

INACTIVE_CAPTION_BORDER

The array index for the

inactiveCaptionBorder

system color.

static int

INACTIVE_CAPTION_TEXT

The array index for the

inactiveCaptionText

system color.

static

SystemColor

inactiveCaption

The color rendered for the window-title background of inactive windows.

static

SystemColor

inactiveCaptionBorder

The color rendered for the border around inactive windows.

static

SystemColor

inactiveCaptionText

The color rendered for the window-title text of inactive windows.

static

SystemColor

info

The color rendered for the background of tooltips or spot help.

static int

INFO

The array index for the

info

system color.

static int

INFO_TEXT

The array index for the

infoText

system color.

static

SystemColor

infoText

The color rendered for the text of tooltips or spot help.

static

SystemColor

menu

The color rendered for the background of menus.

static int

MENU

The array index for the

menu

system color.

static int

MENU_TEXT

The array index for the

menuText

system color.

static

SystemColor

menuText

The color rendered for the text of menus.

static int

NUM_COLORS

The number of system colors in the array.

static

SystemColor

scrollbar

The color rendered for the background of scrollbars.

static int

SCROLLBAR

The array index for the

scrollbar

system color.

static

SystemColor

text

The color rendered for the background of text control objects, such as
textfields and comboboxes.

static int

TEXT

The array index for the

text

system color.

static int

TEXT_HIGHLIGHT

The array index for the

textHighlight

system color.

static int

TEXT_HIGHLIGHT_TEXT

The array index for the

textHighlightText

system color.

static int

TEXT_INACTIVE_TEXT

The array index for the

textInactiveText

system color.

static int

TEXT_TEXT

The array index for the

textText

system color.

static

SystemColor

textHighlight

The color rendered for the background of selected items, such as in menus,
comboboxes, and text.

static

SystemColor

textHighlightText

The color rendered for the text of selected items, such as in menus, comboboxes,
and text.

static

SystemColor

textInactiveText

The color rendered for the text of inactive items, such as in menus.

static

SystemColor

textText

The color rendered for the text of text control objects, such as textfields
and comboboxes.

static

SystemColor

window

The color rendered for the background of interior regions inside windows.

static int

WINDOW

The array index for the

window

system color.

static int

WINDOW_BORDER

The array index for the

windowBorder

system color.

static int

WINDOW_TEXT

The array index for the

windowText

system color.

static

SystemColor

windowBorder

The color rendered for the border around interior regions inside windows.

static

SystemColor

windowText

The color rendered for text of interior regions inside windows.

- Fields declared in class java.awt.

Color

black

,

BLACK

,

blue

,

BLUE

,

cyan

,

CYAN

,

DARK_GRAY

,

darkGray

,

gray

,

GRAY

,

green

,

GREEN

,

LIGHT_GRAY

,

lightGray

,

magenta

,

MAGENTA

,

orange

,

ORANGE

,

pink

,

PINK

,

red

,

RED

,

white

,

WHITE

,

yellow

,

YELLOW

- Fields declared in interface java.awt.

Transparency

BITMASK

,

OPAQUE

,

TRANSLUCENT

---

#### Field Summary

The array index for the

activeCaption

system color.

The array index for the

activeCaptionBorder

system color.

The array index for the

activeCaptionText

system color.

The color rendered for the window-title background of the currently active window.

The color rendered for the border around the currently active window.

The color rendered for the window-title text of the currently active window.

The color rendered for the background of control panels and control objects,
such as pushbuttons.

The array index for the

control

system color.

The array index for the

controlDkShadow

system color.

The array index for the

controlHighlight

system color.

The array index for the

controlLtHighlight

system color.

The array index for the

controlShadow

system color.

The array index for the

controlText

system color.

The color rendered for dark shadow areas on 3D control objects, such as pushbuttons.

The color rendered for light areas of 3D control objects, such as pushbuttons.

The color rendered for highlight areas of 3D control objects, such as pushbuttons.

The color rendered for shadow areas of 3D control objects, such as pushbuttons.

The color rendered for the text of control panels and control objects,
such as pushbuttons.

The color rendered for the background of the desktop.

The array index for the

desktop

system color.

The array index for the

inactiveCaption

system color.

The array index for the

inactiveCaptionBorder

system color.

The array index for the

inactiveCaptionText

system color.

The color rendered for the window-title background of inactive windows.

The color rendered for the border around inactive windows.

The color rendered for the window-title text of inactive windows.

The color rendered for the background of tooltips or spot help.

The array index for the

info

system color.

The array index for the

infoText

system color.

The color rendered for the text of tooltips or spot help.

The color rendered for the background of menus.

The array index for the

menu

system color.

The array index for the

menuText

system color.

The color rendered for the text of menus.

The number of system colors in the array.

The color rendered for the background of scrollbars.

The array index for the

scrollbar

system color.

The color rendered for the background of text control objects, such as
textfields and comboboxes.

The array index for the

text

system color.

The array index for the

textHighlight

system color.

The array index for the

textHighlightText

system color.

The array index for the

textInactiveText

system color.

The array index for the

textText

system color.

The color rendered for the background of selected items, such as in menus,
comboboxes, and text.

The color rendered for the text of selected items, such as in menus, comboboxes,
and text.

The color rendered for the text of inactive items, such as in menus.

The color rendered for the text of text control objects, such as textfields
and comboboxes.

The color rendered for the background of interior regions inside windows.

The array index for the

window

system color.

The array index for the

windowBorder

system color.

The array index for the

windowText

system color.

The color rendered for the border around interior regions inside windows.

The color rendered for text of interior regions inside windows.

Fields declared in class java.awt.

Color

black

,

BLACK

,

blue

,

BLUE

,

cyan

,

CYAN

,

DARK_GRAY

,

darkGray

,

gray

,

GRAY

,

green

,

GREEN

,

LIGHT_GRAY

,

lightGray

,

magenta

,

MAGENTA

,

orange

,

ORANGE

,

pink

,

PINK

,

red

,

RED

,

white

,

WHITE

,

yellow

,

YELLOW

---

#### Fields declared in class java.awt. Color

Fields declared in interface java.awt.

Transparency

BITMASK

,

OPAQUE

,

TRANSLUCENT

---

#### Fields declared in interface java.awt. Transparency

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

toString

()

Returns a string representation of this

Color

's values.

- Methods declared in class java.awt.

Color

brighter

,

createContext

,

darker

,

decode

,

equals

,

getAlpha

,

getBlue

,

getColor

,

getColor

,

getColor

,

getColorComponents

,

getColorComponents

,

getColorSpace

,

getComponents

,

getComponents

,

getGreen

,

getHSBColor

,

getRed

,

getRGB

,

getRGBColorComponents

,

getRGBComponents

,

getTransparency

,

hashCode

,

HSBtoRGB

,

RGBtoHSB

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

Returns a string representation of this

Color

's values.

Methods declared in class java.awt.

Color

brighter

,

createContext

,

darker

,

decode

,

equals

,

getAlpha

,

getBlue

,

getColor

,

getColor

,

getColor

,

getColorComponents

,

getColorComponents

,

getColorSpace

,

getComponents

,

getComponents

,

getGreen

,

getHSBColor

,

getRed

,

getRGB

,

getRGBColorComponents

,

getRGBComponents

,

getTransparency

,

hashCode

,

HSBtoRGB

,

RGBtoHSB

---

#### Methods declared in class java.awt. Color

Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

- DESKTOP

```java
@Native

public static final int DESKTOP
```

The array index for the

desktop

system color.

**See Also:** desktop

,

Constant Field Values

- ACTIVE_CAPTION

```java
@Native

public static final int ACTIVE_CAPTION
```

The array index for the

activeCaption

system color.

**See Also:** activeCaption

,

Constant Field Values

- ACTIVE_CAPTION_TEXT

```java
@Native

public static final int ACTIVE_CAPTION_TEXT
```

The array index for the

activeCaptionText

system color.

**See Also:** activeCaptionText

,

Constant Field Values

- ACTIVE_CAPTION_BORDER

```java
@Native

public static final int ACTIVE_CAPTION_BORDER
```

The array index for the

activeCaptionBorder

system color.

**See Also:** activeCaptionBorder

,

Constant Field Values

- INACTIVE_CAPTION

```java
@Native

public static final int INACTIVE_CAPTION
```

The array index for the

inactiveCaption

system color.

**See Also:** inactiveCaption

,

Constant Field Values

- INACTIVE_CAPTION_TEXT

```java
@Native

public static final int INACTIVE_CAPTION_TEXT
```

The array index for the

inactiveCaptionText

system color.

**See Also:** inactiveCaptionText

,

Constant Field Values

- INACTIVE_CAPTION_BORDER

```java
@Native

public static final int INACTIVE_CAPTION_BORDER
```

The array index for the

inactiveCaptionBorder

system color.

**See Also:** inactiveCaptionBorder

,

Constant Field Values

- WINDOW

```java
@Native

public static final int WINDOW
```

The array index for the

window

system color.

**See Also:** window

,

Constant Field Values

- WINDOW_BORDER

```java
@Native

public static final int WINDOW_BORDER
```

The array index for the

windowBorder

system color.

**See Also:** windowBorder

,

Constant Field Values

- WINDOW_TEXT

```java
@Native

public static final int WINDOW_TEXT
```

The array index for the

windowText

system color.

**See Also:** windowText

,

Constant Field Values

- MENU

```java
@Native

public static final int MENU
```

The array index for the

menu

system color.

**See Also:** menu

,

Constant Field Values

- MENU_TEXT

```java
@Native

public static final int MENU_TEXT
```

The array index for the

menuText

system color.

**See Also:** menuText

,

Constant Field Values

- TEXT

```java
@Native

public static final int TEXT
```

The array index for the

text

system color.

**See Also:** text

,

Constant Field Values

- TEXT_TEXT

```java
@Native

public static final int TEXT_TEXT
```

The array index for the

textText

system color.

**See Also:** textText

,

Constant Field Values

- TEXT_HIGHLIGHT

```java
@Native

public static final int TEXT_HIGHLIGHT
```

The array index for the

textHighlight

system color.

**See Also:** textHighlight

,

Constant Field Values

- TEXT_HIGHLIGHT_TEXT

```java
@Native

public static final int TEXT_HIGHLIGHT_TEXT
```

The array index for the

textHighlightText

system color.

**See Also:** textHighlightText

,

Constant Field Values

- TEXT_INACTIVE_TEXT

```java
@Native

public static final int TEXT_INACTIVE_TEXT
```

The array index for the

textInactiveText

system color.

**See Also:** textInactiveText

,

Constant Field Values

- CONTROL

```java
@Native

public static final int CONTROL
```

The array index for the

control

system color.

**See Also:** control

,

Constant Field Values

- CONTROL_TEXT

```java
@Native

public static final int CONTROL_TEXT
```

The array index for the

controlText

system color.

**See Also:** controlText

,

Constant Field Values

- CONTROL_HIGHLIGHT

```java
@Native

public static final int CONTROL_HIGHLIGHT
```

The array index for the

controlHighlight

system color.

**See Also:** controlHighlight

,

Constant Field Values

- CONTROL_LT_HIGHLIGHT

```java
@Native

public static final int CONTROL_LT_HIGHLIGHT
```

The array index for the

controlLtHighlight

system color.

**See Also:** controlLtHighlight

,

Constant Field Values

- CONTROL_SHADOW

```java
@Native

public static final int CONTROL_SHADOW
```

The array index for the

controlShadow

system color.

**See Also:** controlShadow

,

Constant Field Values

- CONTROL_DK_SHADOW

```java
@Native

public static final int CONTROL_DK_SHADOW
```

The array index for the

controlDkShadow

system color.

**See Also:** controlDkShadow

,

Constant Field Values

- SCROLLBAR

```java
@Native

public static final int SCROLLBAR
```

The array index for the

scrollbar

system color.

**See Also:** scrollbar

,

Constant Field Values

- INFO

```java
@Native

public static final int INFO
```

The array index for the

info

system color.

**See Also:** info

,

Constant Field Values

- INFO_TEXT

```java
@Native

public static final int INFO_TEXT
```

The array index for the

infoText

system color.

**See Also:** infoText

,

Constant Field Values

- NUM_COLORS

```java
@Native

public static final int NUM_COLORS
```

The number of system colors in the array.

**See Also:** Constant Field Values

- desktop

```java
public static final
SystemColor
desktop
```

The color rendered for the background of the desktop.

- activeCaption

```java
public static final
SystemColor
activeCaption
```

The color rendered for the window-title background of the currently active window.

- activeCaptionText

```java
public static final
SystemColor
activeCaptionText
```

The color rendered for the window-title text of the currently active window.

- activeCaptionBorder

```java
public static final
SystemColor
activeCaptionBorder
```

The color rendered for the border around the currently active window.

- inactiveCaption

```java
public static final
SystemColor
inactiveCaption
```

The color rendered for the window-title background of inactive windows.

- inactiveCaptionText

```java
public static final
SystemColor
inactiveCaptionText
```

The color rendered for the window-title text of inactive windows.

- inactiveCaptionBorder

```java
public static final
SystemColor
inactiveCaptionBorder
```

The color rendered for the border around inactive windows.

- window

```java
public static final
SystemColor
window
```

The color rendered for the background of interior regions inside windows.

- windowBorder

```java
public static final
SystemColor
windowBorder
```

The color rendered for the border around interior regions inside windows.

- windowText

```java
public static final
SystemColor
windowText
```

The color rendered for text of interior regions inside windows.

- menu

```java
public static final
SystemColor
menu
```

The color rendered for the background of menus.

- menuText

```java
public static final
SystemColor
menuText
```

The color rendered for the text of menus.

- text

```java
public static final
SystemColor
text
```

The color rendered for the background of text control objects, such as
textfields and comboboxes.

- textText

```java
public static final
SystemColor
textText
```

The color rendered for the text of text control objects, such as textfields
and comboboxes.

- textHighlight

```java
public static final
SystemColor
textHighlight
```

The color rendered for the background of selected items, such as in menus,
comboboxes, and text.

- textHighlightText

```java
public static final
SystemColor
textHighlightText
```

The color rendered for the text of selected items, such as in menus, comboboxes,
and text.

- textInactiveText

```java
public static final
SystemColor
textInactiveText
```

The color rendered for the text of inactive items, such as in menus.

- control

```java
public static final
SystemColor
control
```

The color rendered for the background of control panels and control objects,
such as pushbuttons.

- controlText

```java
public static final
SystemColor
controlText
```

The color rendered for the text of control panels and control objects,
such as pushbuttons.

- controlHighlight

```java
public static final
SystemColor
controlHighlight
```

The color rendered for light areas of 3D control objects, such as pushbuttons.
This color is typically derived from the

control

background color
to provide a 3D effect.

- controlLtHighlight

```java
public static final
SystemColor
controlLtHighlight
```

The color rendered for highlight areas of 3D control objects, such as pushbuttons.
This color is typically derived from the

control

background color
to provide a 3D effect.

- controlShadow

```java
public static final
SystemColor
controlShadow
```

The color rendered for shadow areas of 3D control objects, such as pushbuttons.
This color is typically derived from the

control

background color
to provide a 3D effect.

- controlDkShadow

```java
public static final
SystemColor
controlDkShadow
```

The color rendered for dark shadow areas on 3D control objects, such as pushbuttons.
This color is typically derived from the

control

background color
to provide a 3D effect.

- scrollbar

```java
public static final
SystemColor
scrollbar
```

The color rendered for the background of scrollbars.

- info

```java
public static final
SystemColor
info
```

The color rendered for the background of tooltips or spot help.

- infoText

```java
public static final
SystemColor
infoText
```

The color rendered for the text of tooltips or spot help.

============ METHOD DETAIL ==========

- Method Detail

- toString

```java
public
String
toString()
```

Returns a string representation of this

Color

's values.
This method is intended to be used only for debugging purposes,
and the content and format of the returned string may vary between
implementations.
The returned string may be empty but may not be

null

.

**Overrides:** toString

in class

Color
**Returns:** a string representation of this

Color

Field Detail

- DESKTOP

```java
@Native

public static final int DESKTOP
```

The array index for the

desktop

system color.

**See Also:** desktop

,

Constant Field Values

- ACTIVE_CAPTION

```java
@Native

public static final int ACTIVE_CAPTION
```

The array index for the

activeCaption

system color.

**See Also:** activeCaption

,

Constant Field Values

- ACTIVE_CAPTION_TEXT

```java
@Native

public static final int ACTIVE_CAPTION_TEXT
```

The array index for the

activeCaptionText

system color.

**See Also:** activeCaptionText

,

Constant Field Values

- ACTIVE_CAPTION_BORDER

```java
@Native

public static final int ACTIVE_CAPTION_BORDER
```

The array index for the

activeCaptionBorder

system color.

**See Also:** activeCaptionBorder

,

Constant Field Values

- INACTIVE_CAPTION

```java
@Native

public static final int INACTIVE_CAPTION
```

The array index for the

inactiveCaption

system color.

**See Also:** inactiveCaption

,

Constant Field Values

- INACTIVE_CAPTION_TEXT

```java
@Native

public static final int INACTIVE_CAPTION_TEXT
```

The array index for the

inactiveCaptionText

system color.

**See Also:** inactiveCaptionText

,

Constant Field Values

- INACTIVE_CAPTION_BORDER

```java
@Native

public static final int INACTIVE_CAPTION_BORDER
```

The array index for the

inactiveCaptionBorder

system color.

**See Also:** inactiveCaptionBorder

,

Constant Field Values

- WINDOW

```java
@Native

public static final int WINDOW
```

The array index for the

window

system color.

**See Also:** window

,

Constant Field Values

- WINDOW_BORDER

```java
@Native

public static final int WINDOW_BORDER
```

The array index for the

windowBorder

system color.

**See Also:** windowBorder

,

Constant Field Values

- WINDOW_TEXT

```java
@Native

public static final int WINDOW_TEXT
```

The array index for the

windowText

system color.

**See Also:** windowText

,

Constant Field Values

- MENU

```java
@Native

public static final int MENU
```

The array index for the

menu

system color.

**See Also:** menu

,

Constant Field Values

- MENU_TEXT

```java
@Native

public static final int MENU_TEXT
```

The array index for the

menuText

system color.

**See Also:** menuText

,

Constant Field Values

- TEXT

```java
@Native

public static final int TEXT
```

The array index for the

text

system color.

**See Also:** text

,

Constant Field Values

- TEXT_TEXT

```java
@Native

public static final int TEXT_TEXT
```

The array index for the

textText

system color.

**See Also:** textText

,

Constant Field Values

- TEXT_HIGHLIGHT

```java
@Native

public static final int TEXT_HIGHLIGHT
```

The array index for the

textHighlight

system color.

**See Also:** textHighlight

,

Constant Field Values

- TEXT_HIGHLIGHT_TEXT

```java
@Native

public static final int TEXT_HIGHLIGHT_TEXT
```

The array index for the

textHighlightText

system color.

**See Also:** textHighlightText

,

Constant Field Values

- TEXT_INACTIVE_TEXT

```java
@Native

public static final int TEXT_INACTIVE_TEXT
```

The array index for the

textInactiveText

system color.

**See Also:** textInactiveText

,

Constant Field Values

- CONTROL

```java
@Native

public static final int CONTROL
```

The array index for the

control

system color.

**See Also:** control

,

Constant Field Values

- CONTROL_TEXT

```java
@Native

public static final int CONTROL_TEXT
```

The array index for the

controlText

system color.

**See Also:** controlText

,

Constant Field Values

- CONTROL_HIGHLIGHT

```java
@Native

public static final int CONTROL_HIGHLIGHT
```

The array index for the

controlHighlight

system color.

**See Also:** controlHighlight

,

Constant Field Values

- CONTROL_LT_HIGHLIGHT

```java
@Native

public static final int CONTROL_LT_HIGHLIGHT
```

The array index for the

controlLtHighlight

system color.

**See Also:** controlLtHighlight

,

Constant Field Values

- CONTROL_SHADOW

```java
@Native

public static final int CONTROL_SHADOW
```

The array index for the

controlShadow

system color.

**See Also:** controlShadow

,

Constant Field Values

- CONTROL_DK_SHADOW

```java
@Native

public static final int CONTROL_DK_SHADOW
```

The array index for the

controlDkShadow

system color.

**See Also:** controlDkShadow

,

Constant Field Values

- SCROLLBAR

```java
@Native

public static final int SCROLLBAR
```

The array index for the

scrollbar

system color.

**See Also:** scrollbar

,

Constant Field Values

- INFO

```java
@Native

public static final int INFO
```

The array index for the

info

system color.

**See Also:** info

,

Constant Field Values

- INFO_TEXT

```java
@Native

public static final int INFO_TEXT
```

The array index for the

infoText

system color.

**See Also:** infoText

,

Constant Field Values

- NUM_COLORS

```java
@Native

public static final int NUM_COLORS
```

The number of system colors in the array.

**See Also:** Constant Field Values

- desktop

```java
public static final
SystemColor
desktop
```

The color rendered for the background of the desktop.

- activeCaption

```java
public static final
SystemColor
activeCaption
```

The color rendered for the window-title background of the currently active window.

- activeCaptionText

```java
public static final
SystemColor
activeCaptionText
```

The color rendered for the window-title text of the currently active window.

- activeCaptionBorder

```java
public static final
SystemColor
activeCaptionBorder
```

The color rendered for the border around the currently active window.

- inactiveCaption

```java
public static final
SystemColor
inactiveCaption
```

The color rendered for the window-title background of inactive windows.

- inactiveCaptionText

```java
public static final
SystemColor
inactiveCaptionText
```

The color rendered for the window-title text of inactive windows.

- inactiveCaptionBorder

```java
public static final
SystemColor
inactiveCaptionBorder
```

The color rendered for the border around inactive windows.

- window

```java
public static final
SystemColor
window
```

The color rendered for the background of interior regions inside windows.

- windowBorder

```java
public static final
SystemColor
windowBorder
```

The color rendered for the border around interior regions inside windows.

- windowText

```java
public static final
SystemColor
windowText
```

The color rendered for text of interior regions inside windows.

- menu

```java
public static final
SystemColor
menu
```

The color rendered for the background of menus.

- menuText

```java
public static final
SystemColor
menuText
```

The color rendered for the text of menus.

- text

```java
public static final
SystemColor
text
```

The color rendered for the background of text control objects, such as
textfields and comboboxes.

- textText

```java
public static final
SystemColor
textText
```

The color rendered for the text of text control objects, such as textfields
and comboboxes.

- textHighlight

```java
public static final
SystemColor
textHighlight
```

The color rendered for the background of selected items, such as in menus,
comboboxes, and text.

- textHighlightText

```java
public static final
SystemColor
textHighlightText
```

The color rendered for the text of selected items, such as in menus, comboboxes,
and text.

- textInactiveText

```java
public static final
SystemColor
textInactiveText
```

The color rendered for the text of inactive items, such as in menus.

- control

```java
public static final
SystemColor
control
```

The color rendered for the background of control panels and control objects,
such as pushbuttons.

- controlText

```java
public static final
SystemColor
controlText
```

The color rendered for the text of control panels and control objects,
such as pushbuttons.

- controlHighlight

```java
public static final
SystemColor
controlHighlight
```

The color rendered for light areas of 3D control objects, such as pushbuttons.
This color is typically derived from the

control

background color
to provide a 3D effect.

- controlLtHighlight

```java
public static final
SystemColor
controlLtHighlight
```

The color rendered for highlight areas of 3D control objects, such as pushbuttons.
This color is typically derived from the

control

background color
to provide a 3D effect.

- controlShadow

```java
public static final
SystemColor
controlShadow
```

The color rendered for shadow areas of 3D control objects, such as pushbuttons.
This color is typically derived from the

control

background color
to provide a 3D effect.

- controlDkShadow

```java
public static final
SystemColor
controlDkShadow
```

The color rendered for dark shadow areas on 3D control objects, such as pushbuttons.
This color is typically derived from the

control

background color
to provide a 3D effect.

- scrollbar

```java
public static final
SystemColor
scrollbar
```

The color rendered for the background of scrollbars.

- info

```java
public static final
SystemColor
info
```

The color rendered for the background of tooltips or spot help.

- infoText

```java
public static final
SystemColor
infoText
```

The color rendered for the text of tooltips or spot help.

---

#### Field Detail

DESKTOP

```java
@Native

public static final int DESKTOP
```

The array index for the

desktop

system color.

**See Also:** desktop

,

Constant Field Values

---

#### DESKTOP

@Native

public static final int DESKTOP

The array index for the

desktop

system color.

ACTIVE_CAPTION

```java
@Native

public static final int ACTIVE_CAPTION
```

The array index for the

activeCaption

system color.

**See Also:** activeCaption

,

Constant Field Values

---

#### ACTIVE_CAPTION

@Native

public static final int ACTIVE_CAPTION

The array index for the

activeCaption

system color.

ACTIVE_CAPTION_TEXT

```java
@Native

public static final int ACTIVE_CAPTION_TEXT
```

The array index for the

activeCaptionText

system color.

**See Also:** activeCaptionText

,

Constant Field Values

---

#### ACTIVE_CAPTION_TEXT

@Native

public static final int ACTIVE_CAPTION_TEXT

The array index for the

activeCaptionText

system color.

ACTIVE_CAPTION_BORDER

```java
@Native

public static final int ACTIVE_CAPTION_BORDER
```

The array index for the

activeCaptionBorder

system color.

**See Also:** activeCaptionBorder

,

Constant Field Values

---

#### ACTIVE_CAPTION_BORDER

@Native

public static final int ACTIVE_CAPTION_BORDER

The array index for the

activeCaptionBorder

system color.

INACTIVE_CAPTION

```java
@Native

public static final int INACTIVE_CAPTION
```

The array index for the

inactiveCaption

system color.

**See Also:** inactiveCaption

,

Constant Field Values

---

#### INACTIVE_CAPTION

@Native

public static final int INACTIVE_CAPTION

The array index for the

inactiveCaption

system color.

INACTIVE_CAPTION_TEXT

```java
@Native

public static final int INACTIVE_CAPTION_TEXT
```

The array index for the

inactiveCaptionText

system color.

**See Also:** inactiveCaptionText

,

Constant Field Values

---

#### INACTIVE_CAPTION_TEXT

@Native

public static final int INACTIVE_CAPTION_TEXT

The array index for the

inactiveCaptionText

system color.

INACTIVE_CAPTION_BORDER

```java
@Native

public static final int INACTIVE_CAPTION_BORDER
```

The array index for the

inactiveCaptionBorder

system color.

**See Also:** inactiveCaptionBorder

,

Constant Field Values

---

#### INACTIVE_CAPTION_BORDER

@Native

public static final int INACTIVE_CAPTION_BORDER

The array index for the

inactiveCaptionBorder

system color.

WINDOW

```java
@Native

public static final int WINDOW
```

The array index for the

window

system color.

**See Also:** window

,

Constant Field Values

---

#### WINDOW

@Native

public static final int WINDOW

The array index for the

window

system color.

WINDOW_BORDER

```java
@Native

public static final int WINDOW_BORDER
```

The array index for the

windowBorder

system color.

**See Also:** windowBorder

,

Constant Field Values

---

#### WINDOW_BORDER

@Native

public static final int WINDOW_BORDER

The array index for the

windowBorder

system color.

WINDOW_TEXT

```java
@Native

public static final int WINDOW_TEXT
```

The array index for the

windowText

system color.

**See Also:** windowText

,

Constant Field Values

---

#### WINDOW_TEXT

@Native

public static final int WINDOW_TEXT

The array index for the

windowText

system color.

MENU

```java
@Native

public static final int MENU
```

The array index for the

menu

system color.

**See Also:** menu

,

Constant Field Values

---

#### MENU

@Native

public static final int MENU

The array index for the

menu

system color.

MENU_TEXT

```java
@Native

public static final int MENU_TEXT
```

The array index for the

menuText

system color.

**See Also:** menuText

,

Constant Field Values

---

#### MENU_TEXT

@Native

public static final int MENU_TEXT

The array index for the

menuText

system color.

TEXT

```java
@Native

public static final int TEXT
```

The array index for the

text

system color.

**See Also:** text

,

Constant Field Values

---

#### TEXT

@Native

public static final int TEXT

The array index for the

text

system color.

TEXT_TEXT

```java
@Native

public static final int TEXT_TEXT
```

The array index for the

textText

system color.

**See Also:** textText

,

Constant Field Values

---

#### TEXT_TEXT

@Native

public static final int TEXT_TEXT

The array index for the

textText

system color.

TEXT_HIGHLIGHT

```java
@Native

public static final int TEXT_HIGHLIGHT
```

The array index for the

textHighlight

system color.

**See Also:** textHighlight

,

Constant Field Values

---

#### TEXT_HIGHLIGHT

@Native

public static final int TEXT_HIGHLIGHT

The array index for the

textHighlight

system color.

TEXT_HIGHLIGHT_TEXT

```java
@Native

public static final int TEXT_HIGHLIGHT_TEXT
```

The array index for the

textHighlightText

system color.

**See Also:** textHighlightText

,

Constant Field Values

---

#### TEXT_HIGHLIGHT_TEXT

@Native

public static final int TEXT_HIGHLIGHT_TEXT

The array index for the

textHighlightText

system color.

TEXT_INACTIVE_TEXT

```java
@Native

public static final int TEXT_INACTIVE_TEXT
```

The array index for the

textInactiveText

system color.

**See Also:** textInactiveText

,

Constant Field Values

---

#### TEXT_INACTIVE_TEXT

@Native

public static final int TEXT_INACTIVE_TEXT

The array index for the

textInactiveText

system color.

CONTROL

```java
@Native

public static final int CONTROL
```

The array index for the

control

system color.

**See Also:** control

,

Constant Field Values

---

#### CONTROL

@Native

public static final int CONTROL

The array index for the

control

system color.

CONTROL_TEXT

```java
@Native

public static final int CONTROL_TEXT
```

The array index for the

controlText

system color.

**See Also:** controlText

,

Constant Field Values

---

#### CONTROL_TEXT

@Native

public static final int CONTROL_TEXT

The array index for the

controlText

system color.

CONTROL_HIGHLIGHT

```java
@Native

public static final int CONTROL_HIGHLIGHT
```

The array index for the

controlHighlight

system color.

**See Also:** controlHighlight

,

Constant Field Values

---

#### CONTROL_HIGHLIGHT

@Native

public static final int CONTROL_HIGHLIGHT

The array index for the

controlHighlight

system color.

CONTROL_LT_HIGHLIGHT

```java
@Native

public static final int CONTROL_LT_HIGHLIGHT
```

The array index for the

controlLtHighlight

system color.

**See Also:** controlLtHighlight

,

Constant Field Values

---

#### CONTROL_LT_HIGHLIGHT

@Native

public static final int CONTROL_LT_HIGHLIGHT

The array index for the

controlLtHighlight

system color.

CONTROL_SHADOW

```java
@Native

public static final int CONTROL_SHADOW
```

The array index for the

controlShadow

system color.

**See Also:** controlShadow

,

Constant Field Values

---

#### CONTROL_SHADOW

@Native

public static final int CONTROL_SHADOW

The array index for the

controlShadow

system color.

CONTROL_DK_SHADOW

```java
@Native

public static final int CONTROL_DK_SHADOW
```

The array index for the

controlDkShadow

system color.

**See Also:** controlDkShadow

,

Constant Field Values

---

#### CONTROL_DK_SHADOW

@Native

public static final int CONTROL_DK_SHADOW

The array index for the

controlDkShadow

system color.

SCROLLBAR

```java
@Native

public static final int SCROLLBAR
```

The array index for the

scrollbar

system color.

**See Also:** scrollbar

,

Constant Field Values

---

#### SCROLLBAR

@Native

public static final int SCROLLBAR

The array index for the

scrollbar

system color.

INFO

```java
@Native

public static final int INFO
```

The array index for the

info

system color.

**See Also:** info

,

Constant Field Values

---

#### INFO

@Native

public static final int INFO

The array index for the

info

system color.

INFO_TEXT

```java
@Native

public static final int INFO_TEXT
```

The array index for the

infoText

system color.

**See Also:** infoText

,

Constant Field Values

---

#### INFO_TEXT

@Native

public static final int INFO_TEXT

The array index for the

infoText

system color.

NUM_COLORS

```java
@Native

public static final int NUM_COLORS
```

The number of system colors in the array.

**See Also:** Constant Field Values

---

#### NUM_COLORS

@Native

public static final int NUM_COLORS

The number of system colors in the array.

desktop

```java
public static final
SystemColor
desktop
```

The color rendered for the background of the desktop.

---

#### desktop

public static final

SystemColor

desktop

The color rendered for the background of the desktop.

activeCaption

```java
public static final
SystemColor
activeCaption
```

The color rendered for the window-title background of the currently active window.

---

#### activeCaption

public static final

SystemColor

activeCaption

The color rendered for the window-title background of the currently active window.

activeCaptionText

```java
public static final
SystemColor
activeCaptionText
```

The color rendered for the window-title text of the currently active window.

---

#### activeCaptionText

public static final

SystemColor

activeCaptionText

The color rendered for the window-title text of the currently active window.

activeCaptionBorder

```java
public static final
SystemColor
activeCaptionBorder
```

The color rendered for the border around the currently active window.

---

#### activeCaptionBorder

public static final

SystemColor

activeCaptionBorder

The color rendered for the border around the currently active window.

inactiveCaption

```java
public static final
SystemColor
inactiveCaption
```

The color rendered for the window-title background of inactive windows.

---

#### inactiveCaption

public static final

SystemColor

inactiveCaption

The color rendered for the window-title background of inactive windows.

inactiveCaptionText

```java
public static final
SystemColor
inactiveCaptionText
```

The color rendered for the window-title text of inactive windows.

---

#### inactiveCaptionText

public static final

SystemColor

inactiveCaptionText

The color rendered for the window-title text of inactive windows.

inactiveCaptionBorder

```java
public static final
SystemColor
inactiveCaptionBorder
```

The color rendered for the border around inactive windows.

---

#### inactiveCaptionBorder

public static final

SystemColor

inactiveCaptionBorder

The color rendered for the border around inactive windows.

window

```java
public static final
SystemColor
window
```

The color rendered for the background of interior regions inside windows.

---

#### window

public static final

SystemColor

window

The color rendered for the background of interior regions inside windows.

windowBorder

```java
public static final
SystemColor
windowBorder
```

The color rendered for the border around interior regions inside windows.

---

#### windowBorder

public static final

SystemColor

windowBorder

The color rendered for the border around interior regions inside windows.

windowText

```java
public static final
SystemColor
windowText
```

The color rendered for text of interior regions inside windows.

---

#### windowText

public static final

SystemColor

windowText

The color rendered for text of interior regions inside windows.

menu

```java
public static final
SystemColor
menu
```

The color rendered for the background of menus.

---

#### menu

public static final

SystemColor

menu

The color rendered for the background of menus.

menuText

```java
public static final
SystemColor
menuText
```

The color rendered for the text of menus.

---

#### menuText

public static final

SystemColor

menuText

The color rendered for the text of menus.

text

```java
public static final
SystemColor
text
```

The color rendered for the background of text control objects, such as
textfields and comboboxes.

---

#### text

public static final

SystemColor

text

The color rendered for the background of text control objects, such as
textfields and comboboxes.

textText

```java
public static final
SystemColor
textText
```

The color rendered for the text of text control objects, such as textfields
and comboboxes.

---

#### textText

public static final

SystemColor

textText

The color rendered for the text of text control objects, such as textfields
and comboboxes.

textHighlight

```java
public static final
SystemColor
textHighlight
```

The color rendered for the background of selected items, such as in menus,
comboboxes, and text.

---

#### textHighlight

public static final

SystemColor

textHighlight

The color rendered for the background of selected items, such as in menus,
comboboxes, and text.

textHighlightText

```java
public static final
SystemColor
textHighlightText
```

The color rendered for the text of selected items, such as in menus, comboboxes,
and text.

---

#### textHighlightText

public static final

SystemColor

textHighlightText

The color rendered for the text of selected items, such as in menus, comboboxes,
and text.

textInactiveText

```java
public static final
SystemColor
textInactiveText
```

The color rendered for the text of inactive items, such as in menus.

---

#### textInactiveText

public static final

SystemColor

textInactiveText

The color rendered for the text of inactive items, such as in menus.

control

```java
public static final
SystemColor
control
```

The color rendered for the background of control panels and control objects,
such as pushbuttons.

---

#### control

public static final

SystemColor

control

The color rendered for the background of control panels and control objects,
such as pushbuttons.

controlText

```java
public static final
SystemColor
controlText
```

The color rendered for the text of control panels and control objects,
such as pushbuttons.

---

#### controlText

public static final

SystemColor

controlText

The color rendered for the text of control panels and control objects,
such as pushbuttons.

controlHighlight

```java
public static final
SystemColor
controlHighlight
```

The color rendered for light areas of 3D control objects, such as pushbuttons.
This color is typically derived from the

control

background color
to provide a 3D effect.

---

#### controlHighlight

public static final

SystemColor

controlHighlight

The color rendered for light areas of 3D control objects, such as pushbuttons.
This color is typically derived from the

control

background color
to provide a 3D effect.

controlLtHighlight

```java
public static final
SystemColor
controlLtHighlight
```

The color rendered for highlight areas of 3D control objects, such as pushbuttons.
This color is typically derived from the

control

background color
to provide a 3D effect.

---

#### controlLtHighlight

public static final

SystemColor

controlLtHighlight

The color rendered for highlight areas of 3D control objects, such as pushbuttons.
This color is typically derived from the

control

background color
to provide a 3D effect.

controlShadow

```java
public static final
SystemColor
controlShadow
```

The color rendered for shadow areas of 3D control objects, such as pushbuttons.
This color is typically derived from the

control

background color
to provide a 3D effect.

---

#### controlShadow

public static final

SystemColor

controlShadow

The color rendered for shadow areas of 3D control objects, such as pushbuttons.
This color is typically derived from the

control

background color
to provide a 3D effect.

controlDkShadow

```java
public static final
SystemColor
controlDkShadow
```

The color rendered for dark shadow areas on 3D control objects, such as pushbuttons.
This color is typically derived from the

control

background color
to provide a 3D effect.

---

#### controlDkShadow

public static final

SystemColor

controlDkShadow

The color rendered for dark shadow areas on 3D control objects, such as pushbuttons.
This color is typically derived from the

control

background color
to provide a 3D effect.

scrollbar

```java
public static final
SystemColor
scrollbar
```

The color rendered for the background of scrollbars.

---

#### scrollbar

public static final

SystemColor

scrollbar

The color rendered for the background of scrollbars.

info

```java
public static final
SystemColor
info
```

The color rendered for the background of tooltips or spot help.

---

#### info

public static final

SystemColor

info

The color rendered for the background of tooltips or spot help.

infoText

```java
public static final
SystemColor
infoText
```

The color rendered for the text of tooltips or spot help.

---

#### infoText

public static final

SystemColor

infoText

The color rendered for the text of tooltips or spot help.

Method Detail

- toString

```java
public
String
toString()
```

Returns a string representation of this

Color

's values.
This method is intended to be used only for debugging purposes,
and the content and format of the returned string may vary between
implementations.
The returned string may be empty but may not be

null

.

**Overrides:** toString

in class

Color
**Returns:** a string representation of this

Color

---

#### Method Detail

toString

```java
public
String
toString()
```

Returns a string representation of this

Color

's values.
This method is intended to be used only for debugging purposes,
and the content and format of the returned string may vary between
implementations.
The returned string may be empty but may not be

null

.

**Overrides:** toString

in class

Color
**Returns:** a string representation of this

Color

---

#### toString

public

String

toString()

Returns a string representation of this

Color

's values.
This method is intended to be used only for debugging purposes,
and the content and format of the returned string may vary between
implementations.
The returned string may be empty but may not be

null

.

---

