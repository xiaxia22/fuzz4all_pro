# Class NimbusLookAndFeel

**Source:** `java.desktop\javax\swing\plaf\nimbus\NimbusLookAndFeel.html`

### Class Description

```java
public class
NimbusLookAndFeel

extends
SynthLookAndFeel
```

The NimbusLookAndFeel class.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public NimbusLookAndFeel()

Create a new NimbusLookAndFeel.

---

### Method Details

#### public void initialize()

Called by UIManager when this look and feel is installed.

**Overrides:**
- initialize

in class

SynthLookAndFeel

**See Also:**
- LookAndFeel.uninitialize()

,

UIManager.setLookAndFeel(javax.swing.LookAndFeel)

---

#### public void uninitialize()

Called by UIManager when this look and feel is uninstalled.

**Overrides:**
- uninitialize

in class

SynthLookAndFeel

**See Also:**
- LookAndFeel.initialize()

,

UIManager.setLookAndFeel(javax.swing.LookAndFeel)

---

#### public static
NimbusStyle
getStyle​(
JComponent
c,

Region
r)

Gets the style associated with the given component and region. This
will never return null. If an appropriate component and region cannot
be determined, then a default style is returned.

**Parameters:**
- c

- a non-null reference to a JComponent
- r

- a non-null reference to the region of the component c

**Returns:**
- a non-null reference to a NimbusStyle.

---

#### public
String
getName()

Return a short string that identifies this look and feel. This
String will be the unquoted String "Nimbus".

**Overrides:**
- getName

in class

SynthLookAndFeel

**Returns:**
- a short string identifying this look and feel.

---

#### public
String
getID()

Return a string that identifies this look and feel. This String will
be the unquoted String "Nimbus".

**Overrides:**
- getID

in class

SynthLookAndFeel

**Returns:**
- a short string identifying this look and feel.

---

#### public
String
getDescription()

Returns a textual description of this look and feel.

**Overrides:**
- getDescription

in class

SynthLookAndFeel

**Returns:**
- textual description of this look and feel.

---

#### public boolean shouldUpdateStyleOnAncestorChanged()

Returns whether or not the UIs should update their

SynthStyles

from the

SynthStyleFactory

when the ancestor of the

JComponent

changes. A subclass
that provided a

SynthStyleFactory

that based the
return value from

getStyle

off the containment hierarchy
would override this method to return true.

**Overrides:**
- shouldUpdateStyleOnAncestorChanged

in class

SynthLookAndFeel

**Returns:**
- true

---

#### protected boolean shouldUpdateStyleOnEvent​(
PropertyChangeEvent
ev)

Returns whether or not the UIs should update their styles when a
particular event occurs.

Overridden to return

true

when one of the following
properties change:

- "Nimbus.Overrides"

"Nimbus.Overrides.InheritDefaults"

"JComponent.sizeVariant"

**Overrides:**
- shouldUpdateStyleOnEvent

in class

SynthLookAndFeel

**Parameters:**
- ev

- a

PropertyChangeEvent

**Returns:**
- whether or not the UIs should update their styles

**Since:**
- 1.7

---

#### public void register​(
Region
region,

String
prefix)

Registers a third party component with the NimbusLookAndFeel.

Regions represent Components and areas within Components that act as
independent painting areas. Once registered with the NimbusLookAndFeel,
NimbusStyles for these Regions can be retrieved via the

getStyle

method.

The NimbusLookAndFeel uses a standard naming scheme for entries in the
UIDefaults table. The key for each property, state, painter, and other
default registered in UIDefaults for a specific Region will begin with
the specified

prefix

For example, suppose I had a component named JFoo. Suppose I then registered
this component with the NimbusLookAndFeel in this manner:

```java
laf.register(NimbusFooUI.FOO_REGION, "Foo");
```

In this case, I could then register properties for this component with
UIDefaults in the following manner:

```java
UIManager.put("Foo.background", new ColorUIResource(Color.BLACK));
UIManager.put("Foo.Enabled.backgroundPainter", new FooBackgroundPainter());
```

It is also possible to register a named component with Nimbus.
For example, suppose you wanted to style the background of a JPanel
named "MyPanel" differently from other JPanels. You could accomplish this
by doing the following:

```java
laf.register(Region.PANEL, "\"MyPanel\"");
UIManager.put("\"MyPanel\".background", new ColorUIResource(Color.RED));
```

**Parameters:**
- region

- The Synth Region that is being registered. Such as Button, or
ScrollBarThumb, or NimbusFooUI.FOO_REGION.
- prefix

- The UIDefault prefix. For example, could be ComboBox, or if
a named components, "MyComboBox", or even something like
ToolBar."MyComboBox"."ComboBox.arrowButton"

---

#### public
Color
getDerivedColor​(
String
uiDefaultParentName,
float hOffset,
float sOffset,
float bOffset,
int aOffset,
boolean uiResource)

Get a derived color, derived colors are shared instances and is color
value will change when its parent UIDefault color changes.

**Parameters:**
- uiDefaultParentName

- The parent UIDefault key
- hOffset

- The hue offset
- sOffset

- The saturation offset
- bOffset

- The brightness offset
- aOffset

- The alpha offset
- uiResource

- True if the derived color should be a
UIResource, false if it should not be

**Returns:**
- The stored derived color

---

#### protected final
Color
getDerivedColor​(
Color
color1,

Color
color2,
float midPoint,
boolean uiResource)

Decodes and returns a color, which is derived from an offset between two
other colors.

**Parameters:**
- color1

- The first color
- color2

- The second color
- midPoint

- The offset between color 1 and color 2, a value of 0.0 is
color 1 and 1.0 is color 2;
- uiResource

- True if the derived color should be a UIResource

**Returns:**
- The derived color

---

#### protected final
Color
getDerivedColor​(
Color
color1,

Color
color2,
float midPoint)

Decodes and returns a color, which is derived from a offset between two
other colors.

**Parameters:**
- color1

- The first color
- color2

- The second color
- midPoint

- The offset between color 1 and color 2, a value of 0.0 is
color 1 and 1.0 is color 2;

**Returns:**
- The derived color, which will be a UIResource

---

### Additional Sections

#### Class NimbusLookAndFeel

java.lang.Object

- javax.swing.LookAndFeel
- - javax.swing.plaf.basic.BasicLookAndFeel
- - javax.swing.plaf.synth.SynthLookAndFeel
- - javax.swing.plaf.nimbus.NimbusLookAndFeel

javax.swing.LookAndFeel

- javax.swing.plaf.basic.BasicLookAndFeel
- - javax.swing.plaf.synth.SynthLookAndFeel
- - javax.swing.plaf.nimbus.NimbusLookAndFeel

javax.swing.plaf.basic.BasicLookAndFeel

- javax.swing.plaf.synth.SynthLookAndFeel
- - javax.swing.plaf.nimbus.NimbusLookAndFeel

javax.swing.plaf.synth.SynthLookAndFeel

- javax.swing.plaf.nimbus.NimbusLookAndFeel

javax.swing.plaf.nimbus.NimbusLookAndFeel

**All Implemented Interfaces:** Serializable

```java
public class
NimbusLookAndFeel

extends
SynthLookAndFeel
```

The NimbusLookAndFeel class.

**See Also:** Serialized Form

public class

NimbusLookAndFeel

extends

SynthLookAndFeel

The NimbusLookAndFeel class.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

NimbusLookAndFeel

()

Create a new NimbusLookAndFeel.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

Color

getDerivedColor

​(

Color

color1,

Color

color2,
float midPoint)

Decodes and returns a color, which is derived from a offset between two
other colors.

protected

Color

getDerivedColor

​(

Color

color1,

Color

color2,
float midPoint,
boolean uiResource)

Decodes and returns a color, which is derived from an offset between two
other colors.

Color

getDerivedColor

​(

String

uiDefaultParentName,
float hOffset,
float sOffset,
float bOffset,
int aOffset,
boolean uiResource)

Get a derived color, derived colors are shared instances and is color
value will change when its parent UIDefault color changes.

String

getDescription

()

Returns a textual description of this look and feel.

String

getID

()

Return a string that identifies this look and feel.

String

getName

()

Return a short string that identifies this look and feel.

static

NimbusStyle

getStyle

​(

JComponent

c,

Region

r)

Gets the style associated with the given component and region.

void

initialize

()

Called by UIManager when this look and feel is installed.

void

register

​(

Region

region,

String

prefix)

Registers a third party component with the NimbusLookAndFeel.

boolean

shouldUpdateStyleOnAncestorChanged

()

Returns whether or not the UIs should update their

SynthStyles

from the

SynthStyleFactory

when the ancestor of the

JComponent

changes.

protected boolean

shouldUpdateStyleOnEvent

​(

PropertyChangeEvent

ev)

Returns whether or not the UIs should update their styles when a
particular event occurs.

void

uninitialize

()

Called by UIManager when this look and feel is uninstalled.

- Methods declared in class javax.swing.plaf.synth.

SynthLookAndFeel

createUI

,

getDefaults

,

getRegion

,

getStyleFactory

,

isNativeLookAndFeel

,

isSupportedLookAndFeel

,

load

,

load

,

setStyleFactory

,

updateStyles

- Methods declared in class javax.swing.plaf.basic.

BasicLookAndFeel

createAudioAction

,

getAudioActionMap

,

initClassDefaults

,

initComponentDefaults

,

initSystemColorDefaults

,

loadSystemColors

,

playSound

- Methods declared in class javax.swing.

LookAndFeel

getDesktopPropertyValue

,

getDisabledIcon

,

getDisabledSelectedIcon

,

getLayoutStyle

,

getSupportsWindowDecorations

,

installBorder

,

installColors

,

installColorsAndFont

,

installProperty

,

loadKeyBindings

,

makeComponentInputMap

,

makeIcon

,

makeInputMap

,

makeKeyBindings

,

provideErrorFeedback

,

toString

,

uninstallBorder

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

Constructor Summary

Constructors

Constructor

Description

NimbusLookAndFeel

()

Create a new NimbusLookAndFeel.

---

#### Constructor Summary

Create a new NimbusLookAndFeel.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

Color

getDerivedColor

​(

Color

color1,

Color

color2,
float midPoint)

Decodes and returns a color, which is derived from a offset between two
other colors.

protected

Color

getDerivedColor

​(

Color

color1,

Color

color2,
float midPoint,
boolean uiResource)

Decodes and returns a color, which is derived from an offset between two
other colors.

Color

getDerivedColor

​(

String

uiDefaultParentName,
float hOffset,
float sOffset,
float bOffset,
int aOffset,
boolean uiResource)

Get a derived color, derived colors are shared instances and is color
value will change when its parent UIDefault color changes.

String

getDescription

()

Returns a textual description of this look and feel.

String

getID

()

Return a string that identifies this look and feel.

String

getName

()

Return a short string that identifies this look and feel.

static

NimbusStyle

getStyle

​(

JComponent

c,

Region

r)

Gets the style associated with the given component and region.

void

initialize

()

Called by UIManager when this look and feel is installed.

void

register

​(

Region

region,

String

prefix)

Registers a third party component with the NimbusLookAndFeel.

boolean

shouldUpdateStyleOnAncestorChanged

()

Returns whether or not the UIs should update their

SynthStyles

from the

SynthStyleFactory

when the ancestor of the

JComponent

changes.

protected boolean

shouldUpdateStyleOnEvent

​(

PropertyChangeEvent

ev)

Returns whether or not the UIs should update their styles when a
particular event occurs.

void

uninitialize

()

Called by UIManager when this look and feel is uninstalled.

- Methods declared in class javax.swing.plaf.synth.

SynthLookAndFeel

createUI

,

getDefaults

,

getRegion

,

getStyleFactory

,

isNativeLookAndFeel

,

isSupportedLookAndFeel

,

load

,

load

,

setStyleFactory

,

updateStyles

- Methods declared in class javax.swing.plaf.basic.

BasicLookAndFeel

createAudioAction

,

getAudioActionMap

,

initClassDefaults

,

initComponentDefaults

,

initSystemColorDefaults

,

loadSystemColors

,

playSound

- Methods declared in class javax.swing.

LookAndFeel

getDesktopPropertyValue

,

getDisabledIcon

,

getDisabledSelectedIcon

,

getLayoutStyle

,

getSupportsWindowDecorations

,

installBorder

,

installColors

,

installColorsAndFont

,

installProperty

,

loadKeyBindings

,

makeComponentInputMap

,

makeIcon

,

makeInputMap

,

makeKeyBindings

,

provideErrorFeedback

,

toString

,

uninstallBorder

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

Decodes and returns a color, which is derived from a offset between two
other colors.

Decodes and returns a color, which is derived from an offset between two
other colors.

Get a derived color, derived colors are shared instances and is color
value will change when its parent UIDefault color changes.

Returns a textual description of this look and feel.

Return a string that identifies this look and feel.

Return a short string that identifies this look and feel.

Gets the style associated with the given component and region.

Called by UIManager when this look and feel is installed.

Registers a third party component with the NimbusLookAndFeel.

Returns whether or not the UIs should update their

SynthStyles

from the

SynthStyleFactory

when the ancestor of the

JComponent

changes.

Returns whether or not the UIs should update their styles when a
particular event occurs.

Called by UIManager when this look and feel is uninstalled.

Methods declared in class javax.swing.plaf.synth.

SynthLookAndFeel

createUI

,

getDefaults

,

getRegion

,

getStyleFactory

,

isNativeLookAndFeel

,

isSupportedLookAndFeel

,

load

,

load

,

setStyleFactory

,

updateStyles

---

#### Methods declared in class javax.swing.plaf.synth. SynthLookAndFeel

Methods declared in class javax.swing.plaf.basic.

BasicLookAndFeel

createAudioAction

,

getAudioActionMap

,

initClassDefaults

,

initComponentDefaults

,

initSystemColorDefaults

,

loadSystemColors

,

playSound

---

#### Methods declared in class javax.swing.plaf.basic. BasicLookAndFeel

Methods declared in class javax.swing.

LookAndFeel

getDesktopPropertyValue

,

getDisabledIcon

,

getDisabledSelectedIcon

,

getLayoutStyle

,

getSupportsWindowDecorations

,

installBorder

,

installColors

,

installColorsAndFont

,

installProperty

,

loadKeyBindings

,

makeComponentInputMap

,

makeIcon

,

makeInputMap

,

makeKeyBindings

,

provideErrorFeedback

,

toString

,

uninstallBorder

---

#### Methods declared in class javax.swing. LookAndFeel

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- NimbusLookAndFeel

```java
public NimbusLookAndFeel()
```

Create a new NimbusLookAndFeel.

============ METHOD DETAIL ==========

- Method Detail

- initialize

```java
public void initialize()
```

Called by UIManager when this look and feel is installed.

**Overrides:** initialize

in class

SynthLookAndFeel
**See Also:** LookAndFeel.uninitialize()

,

UIManager.setLookAndFeel(javax.swing.LookAndFeel)

- uninitialize

```java
public void uninitialize()
```

Called by UIManager when this look and feel is uninstalled.

**Overrides:** uninitialize

in class

SynthLookAndFeel
**See Also:** LookAndFeel.initialize()

,

UIManager.setLookAndFeel(javax.swing.LookAndFeel)

- getStyle

```java
public static
NimbusStyle
getStyle​(
JComponent
c,

Region
r)
```

Gets the style associated with the given component and region. This
will never return null. If an appropriate component and region cannot
be determined, then a default style is returned.

**Parameters:** c

- a non-null reference to a JComponent
**Parameters:** r

- a non-null reference to the region of the component c
**Returns:** a non-null reference to a NimbusStyle.

- getName

```java
public
String
getName()
```

Return a short string that identifies this look and feel. This
String will be the unquoted String "Nimbus".

**Overrides:** getName

in class

SynthLookAndFeel
**Returns:** a short string identifying this look and feel.

- getID

```java
public
String
getID()
```

Return a string that identifies this look and feel. This String will
be the unquoted String "Nimbus".

**Overrides:** getID

in class

SynthLookAndFeel
**Returns:** a short string identifying this look and feel.

- getDescription

```java
public
String
getDescription()
```

Returns a textual description of this look and feel.

**Overrides:** getDescription

in class

SynthLookAndFeel
**Returns:** textual description of this look and feel.

- shouldUpdateStyleOnAncestorChanged

```java
public boolean shouldUpdateStyleOnAncestorChanged()
```

Returns whether or not the UIs should update their

SynthStyles

from the

SynthStyleFactory

when the ancestor of the

JComponent

changes. A subclass
that provided a

SynthStyleFactory

that based the
return value from

getStyle

off the containment hierarchy
would override this method to return true.

**Overrides:** shouldUpdateStyleOnAncestorChanged

in class

SynthLookAndFeel
**Returns:** true

- shouldUpdateStyleOnEvent

```java
protected boolean shouldUpdateStyleOnEvent​(
PropertyChangeEvent
ev)
```

Returns whether or not the UIs should update their styles when a
particular event occurs.

Overridden to return

true

when one of the following
properties change:

- "Nimbus.Overrides"

"Nimbus.Overrides.InheritDefaults"

"JComponent.sizeVariant"

**Overrides:** shouldUpdateStyleOnEvent

in class

SynthLookAndFeel
**Parameters:** ev

- a

PropertyChangeEvent
**Returns:** whether or not the UIs should update their styles
**Since:** 1.7

- register

```java
public void register​(
Region
region,

String
prefix)
```

Registers a third party component with the NimbusLookAndFeel.

Regions represent Components and areas within Components that act as
independent painting areas. Once registered with the NimbusLookAndFeel,
NimbusStyles for these Regions can be retrieved via the

getStyle

method.

The NimbusLookAndFeel uses a standard naming scheme for entries in the
UIDefaults table. The key for each property, state, painter, and other
default registered in UIDefaults for a specific Region will begin with
the specified

prefix

For example, suppose I had a component named JFoo. Suppose I then registered
this component with the NimbusLookAndFeel in this manner:

```java
laf.register(NimbusFooUI.FOO_REGION, "Foo");
```

In this case, I could then register properties for this component with
UIDefaults in the following manner:

```java
UIManager.put("Foo.background", new ColorUIResource(Color.BLACK));
UIManager.put("Foo.Enabled.backgroundPainter", new FooBackgroundPainter());
```

It is also possible to register a named component with Nimbus.
For example, suppose you wanted to style the background of a JPanel
named "MyPanel" differently from other JPanels. You could accomplish this
by doing the following:

```java
laf.register(Region.PANEL, "\"MyPanel\"");
UIManager.put("\"MyPanel\".background", new ColorUIResource(Color.RED));
```

**Parameters:** region

- The Synth Region that is being registered. Such as Button, or
ScrollBarThumb, or NimbusFooUI.FOO_REGION.
**Parameters:** prefix

- The UIDefault prefix. For example, could be ComboBox, or if
a named components, "MyComboBox", or even something like
ToolBar."MyComboBox"."ComboBox.arrowButton"

- getDerivedColor

```java
public
Color
getDerivedColor​(
String
uiDefaultParentName,
float hOffset,
float sOffset,
float bOffset,
int aOffset,
boolean uiResource)
```

Get a derived color, derived colors are shared instances and is color
value will change when its parent UIDefault color changes.

**Parameters:** uiDefaultParentName

- The parent UIDefault key
**Parameters:** hOffset

- The hue offset
**Parameters:** sOffset

- The saturation offset
**Parameters:** bOffset

- The brightness offset
**Parameters:** aOffset

- The alpha offset
**Parameters:** uiResource

- True if the derived color should be a
UIResource, false if it should not be
**Returns:** The stored derived color

- getDerivedColor

```java
protected final
Color
getDerivedColor​(
Color
color1,

Color
color2,
float midPoint,
boolean uiResource)
```

Decodes and returns a color, which is derived from an offset between two
other colors.

**Parameters:** color1

- The first color
**Parameters:** color2

- The second color
**Parameters:** midPoint

- The offset between color 1 and color 2, a value of 0.0 is
color 1 and 1.0 is color 2;
**Parameters:** uiResource

- True if the derived color should be a UIResource
**Returns:** The derived color

- getDerivedColor

```java
protected final
Color
getDerivedColor​(
Color
color1,

Color
color2,
float midPoint)
```

Decodes and returns a color, which is derived from a offset between two
other colors.

**Parameters:** color1

- The first color
**Parameters:** color2

- The second color
**Parameters:** midPoint

- The offset between color 1 and color 2, a value of 0.0 is
color 1 and 1.0 is color 2;
**Returns:** The derived color, which will be a UIResource

Constructor Detail

- NimbusLookAndFeel

```java
public NimbusLookAndFeel()
```

Create a new NimbusLookAndFeel.

---

#### Constructor Detail

NimbusLookAndFeel

```java
public NimbusLookAndFeel()
```

Create a new NimbusLookAndFeel.

---

#### NimbusLookAndFeel

public NimbusLookAndFeel()

Create a new NimbusLookAndFeel.

Method Detail

- initialize

```java
public void initialize()
```

Called by UIManager when this look and feel is installed.

**Overrides:** initialize

in class

SynthLookAndFeel
**See Also:** LookAndFeel.uninitialize()

,

UIManager.setLookAndFeel(javax.swing.LookAndFeel)

- uninitialize

```java
public void uninitialize()
```

Called by UIManager when this look and feel is uninstalled.

**Overrides:** uninitialize

in class

SynthLookAndFeel
**See Also:** LookAndFeel.initialize()

,

UIManager.setLookAndFeel(javax.swing.LookAndFeel)

- getStyle

```java
public static
NimbusStyle
getStyle​(
JComponent
c,

Region
r)
```

Gets the style associated with the given component and region. This
will never return null. If an appropriate component and region cannot
be determined, then a default style is returned.

**Parameters:** c

- a non-null reference to a JComponent
**Parameters:** r

- a non-null reference to the region of the component c
**Returns:** a non-null reference to a NimbusStyle.

- getName

```java
public
String
getName()
```

Return a short string that identifies this look and feel. This
String will be the unquoted String "Nimbus".

**Overrides:** getName

in class

SynthLookAndFeel
**Returns:** a short string identifying this look and feel.

- getID

```java
public
String
getID()
```

Return a string that identifies this look and feel. This String will
be the unquoted String "Nimbus".

**Overrides:** getID

in class

SynthLookAndFeel
**Returns:** a short string identifying this look and feel.

- getDescription

```java
public
String
getDescription()
```

Returns a textual description of this look and feel.

**Overrides:** getDescription

in class

SynthLookAndFeel
**Returns:** textual description of this look and feel.

- shouldUpdateStyleOnAncestorChanged

```java
public boolean shouldUpdateStyleOnAncestorChanged()
```

Returns whether or not the UIs should update their

SynthStyles

from the

SynthStyleFactory

when the ancestor of the

JComponent

changes. A subclass
that provided a

SynthStyleFactory

that based the
return value from

getStyle

off the containment hierarchy
would override this method to return true.

**Overrides:** shouldUpdateStyleOnAncestorChanged

in class

SynthLookAndFeel
**Returns:** true

- shouldUpdateStyleOnEvent

```java
protected boolean shouldUpdateStyleOnEvent​(
PropertyChangeEvent
ev)
```

Returns whether or not the UIs should update their styles when a
particular event occurs.

Overridden to return

true

when one of the following
properties change:

- "Nimbus.Overrides"

"Nimbus.Overrides.InheritDefaults"

"JComponent.sizeVariant"

**Overrides:** shouldUpdateStyleOnEvent

in class

SynthLookAndFeel
**Parameters:** ev

- a

PropertyChangeEvent
**Returns:** whether or not the UIs should update their styles
**Since:** 1.7

- register

```java
public void register​(
Region
region,

String
prefix)
```

Registers a third party component with the NimbusLookAndFeel.

Regions represent Components and areas within Components that act as
independent painting areas. Once registered with the NimbusLookAndFeel,
NimbusStyles for these Regions can be retrieved via the

getStyle

method.

The NimbusLookAndFeel uses a standard naming scheme for entries in the
UIDefaults table. The key for each property, state, painter, and other
default registered in UIDefaults for a specific Region will begin with
the specified

prefix

For example, suppose I had a component named JFoo. Suppose I then registered
this component with the NimbusLookAndFeel in this manner:

```java
laf.register(NimbusFooUI.FOO_REGION, "Foo");
```

In this case, I could then register properties for this component with
UIDefaults in the following manner:

```java
UIManager.put("Foo.background", new ColorUIResource(Color.BLACK));
UIManager.put("Foo.Enabled.backgroundPainter", new FooBackgroundPainter());
```

It is also possible to register a named component with Nimbus.
For example, suppose you wanted to style the background of a JPanel
named "MyPanel" differently from other JPanels. You could accomplish this
by doing the following:

```java
laf.register(Region.PANEL, "\"MyPanel\"");
UIManager.put("\"MyPanel\".background", new ColorUIResource(Color.RED));
```

**Parameters:** region

- The Synth Region that is being registered. Such as Button, or
ScrollBarThumb, or NimbusFooUI.FOO_REGION.
**Parameters:** prefix

- The UIDefault prefix. For example, could be ComboBox, or if
a named components, "MyComboBox", or even something like
ToolBar."MyComboBox"."ComboBox.arrowButton"

- getDerivedColor

```java
public
Color
getDerivedColor​(
String
uiDefaultParentName,
float hOffset,
float sOffset,
float bOffset,
int aOffset,
boolean uiResource)
```

Get a derived color, derived colors are shared instances and is color
value will change when its parent UIDefault color changes.

**Parameters:** uiDefaultParentName

- The parent UIDefault key
**Parameters:** hOffset

- The hue offset
**Parameters:** sOffset

- The saturation offset
**Parameters:** bOffset

- The brightness offset
**Parameters:** aOffset

- The alpha offset
**Parameters:** uiResource

- True if the derived color should be a
UIResource, false if it should not be
**Returns:** The stored derived color

- getDerivedColor

```java
protected final
Color
getDerivedColor​(
Color
color1,

Color
color2,
float midPoint,
boolean uiResource)
```

Decodes and returns a color, which is derived from an offset between two
other colors.

**Parameters:** color1

- The first color
**Parameters:** color2

- The second color
**Parameters:** midPoint

- The offset between color 1 and color 2, a value of 0.0 is
color 1 and 1.0 is color 2;
**Parameters:** uiResource

- True if the derived color should be a UIResource
**Returns:** The derived color

- getDerivedColor

```java
protected final
Color
getDerivedColor​(
Color
color1,

Color
color2,
float midPoint)
```

Decodes and returns a color, which is derived from a offset between two
other colors.

**Parameters:** color1

- The first color
**Parameters:** color2

- The second color
**Parameters:** midPoint

- The offset between color 1 and color 2, a value of 0.0 is
color 1 and 1.0 is color 2;
**Returns:** The derived color, which will be a UIResource

---

#### Method Detail

initialize

```java
public void initialize()
```

Called by UIManager when this look and feel is installed.

**Overrides:** initialize

in class

SynthLookAndFeel
**See Also:** LookAndFeel.uninitialize()

,

UIManager.setLookAndFeel(javax.swing.LookAndFeel)

---

#### initialize

public void initialize()

Called by UIManager when this look and feel is installed.

uninitialize

```java
public void uninitialize()
```

Called by UIManager when this look and feel is uninstalled.

**Overrides:** uninitialize

in class

SynthLookAndFeel
**See Also:** LookAndFeel.initialize()

,

UIManager.setLookAndFeel(javax.swing.LookAndFeel)

---

#### uninitialize

public void uninitialize()

Called by UIManager when this look and feel is uninstalled.

getStyle

```java
public static
NimbusStyle
getStyle​(
JComponent
c,

Region
r)
```

Gets the style associated with the given component and region. This
will never return null. If an appropriate component and region cannot
be determined, then a default style is returned.

**Parameters:** c

- a non-null reference to a JComponent
**Parameters:** r

- a non-null reference to the region of the component c
**Returns:** a non-null reference to a NimbusStyle.

---

#### getStyle

public static

NimbusStyle

getStyle​(

JComponent

c,

Region

r)

Gets the style associated with the given component and region. This
will never return null. If an appropriate component and region cannot
be determined, then a default style is returned.

getName

```java
public
String
getName()
```

Return a short string that identifies this look and feel. This
String will be the unquoted String "Nimbus".

**Overrides:** getName

in class

SynthLookAndFeel
**Returns:** a short string identifying this look and feel.

---

#### getName

public

String

getName()

Return a short string that identifies this look and feel. This
String will be the unquoted String "Nimbus".

getID

```java
public
String
getID()
```

Return a string that identifies this look and feel. This String will
be the unquoted String "Nimbus".

**Overrides:** getID

in class

SynthLookAndFeel
**Returns:** a short string identifying this look and feel.

---

#### getID

public

String

getID()

Return a string that identifies this look and feel. This String will
be the unquoted String "Nimbus".

getDescription

```java
public
String
getDescription()
```

Returns a textual description of this look and feel.

**Overrides:** getDescription

in class

SynthLookAndFeel
**Returns:** textual description of this look and feel.

---

#### getDescription

public

String

getDescription()

Returns a textual description of this look and feel.

shouldUpdateStyleOnAncestorChanged

```java
public boolean shouldUpdateStyleOnAncestorChanged()
```

Returns whether or not the UIs should update their

SynthStyles

from the

SynthStyleFactory

when the ancestor of the

JComponent

changes. A subclass
that provided a

SynthStyleFactory

that based the
return value from

getStyle

off the containment hierarchy
would override this method to return true.

**Overrides:** shouldUpdateStyleOnAncestorChanged

in class

SynthLookAndFeel
**Returns:** true

---

#### shouldUpdateStyleOnAncestorChanged

public boolean shouldUpdateStyleOnAncestorChanged()

Returns whether or not the UIs should update their

SynthStyles

from the

SynthStyleFactory

when the ancestor of the

JComponent

changes. A subclass
that provided a

SynthStyleFactory

that based the
return value from

getStyle

off the containment hierarchy
would override this method to return true.

shouldUpdateStyleOnEvent

```java
protected boolean shouldUpdateStyleOnEvent​(
PropertyChangeEvent
ev)
```

Returns whether or not the UIs should update their styles when a
particular event occurs.

Overridden to return

true

when one of the following
properties change:

- "Nimbus.Overrides"

"Nimbus.Overrides.InheritDefaults"

"JComponent.sizeVariant"

**Overrides:** shouldUpdateStyleOnEvent

in class

SynthLookAndFeel
**Parameters:** ev

- a

PropertyChangeEvent
**Returns:** whether or not the UIs should update their styles
**Since:** 1.7

---

#### shouldUpdateStyleOnEvent

protected boolean shouldUpdateStyleOnEvent​(

PropertyChangeEvent

ev)

Returns whether or not the UIs should update their styles when a
particular event occurs.

Overridden to return

true

when one of the following
properties change:

- "Nimbus.Overrides"

"Nimbus.Overrides.InheritDefaults"

"JComponent.sizeVariant"

Overridden to return

true

when one of the following
properties change:

- "Nimbus.Overrides"

"Nimbus.Overrides.InheritDefaults"

"JComponent.sizeVariant"

"Nimbus.Overrides"

"Nimbus.Overrides.InheritDefaults"

"JComponent.sizeVariant"

register

```java
public void register​(
Region
region,

String
prefix)
```

Registers a third party component with the NimbusLookAndFeel.

Regions represent Components and areas within Components that act as
independent painting areas. Once registered with the NimbusLookAndFeel,
NimbusStyles for these Regions can be retrieved via the

getStyle

method.

The NimbusLookAndFeel uses a standard naming scheme for entries in the
UIDefaults table. The key for each property, state, painter, and other
default registered in UIDefaults for a specific Region will begin with
the specified

prefix

For example, suppose I had a component named JFoo. Suppose I then registered
this component with the NimbusLookAndFeel in this manner:

```java
laf.register(NimbusFooUI.FOO_REGION, "Foo");
```

In this case, I could then register properties for this component with
UIDefaults in the following manner:

```java
UIManager.put("Foo.background", new ColorUIResource(Color.BLACK));
UIManager.put("Foo.Enabled.backgroundPainter", new FooBackgroundPainter());
```

It is also possible to register a named component with Nimbus.
For example, suppose you wanted to style the background of a JPanel
named "MyPanel" differently from other JPanels. You could accomplish this
by doing the following:

```java
laf.register(Region.PANEL, "\"MyPanel\"");
UIManager.put("\"MyPanel\".background", new ColorUIResource(Color.RED));
```

**Parameters:** region

- The Synth Region that is being registered. Such as Button, or
ScrollBarThumb, or NimbusFooUI.FOO_REGION.
**Parameters:** prefix

- The UIDefault prefix. For example, could be ComboBox, or if
a named components, "MyComboBox", or even something like
ToolBar."MyComboBox"."ComboBox.arrowButton"

---

#### register

public void register​(

Region

region,

String

prefix)

Registers a third party component with the NimbusLookAndFeel.

Regions represent Components and areas within Components that act as
independent painting areas. Once registered with the NimbusLookAndFeel,
NimbusStyles for these Regions can be retrieved via the

getStyle

method.

The NimbusLookAndFeel uses a standard naming scheme for entries in the
UIDefaults table. The key for each property, state, painter, and other
default registered in UIDefaults for a specific Region will begin with
the specified

prefix

For example, suppose I had a component named JFoo. Suppose I then registered
this component with the NimbusLookAndFeel in this manner:

```java
laf.register(NimbusFooUI.FOO_REGION, "Foo");
```

In this case, I could then register properties for this component with
UIDefaults in the following manner:

```java
UIManager.put("Foo.background", new ColorUIResource(Color.BLACK));
UIManager.put("Foo.Enabled.backgroundPainter", new FooBackgroundPainter());
```

It is also possible to register a named component with Nimbus.
For example, suppose you wanted to style the background of a JPanel
named "MyPanel" differently from other JPanels. You could accomplish this
by doing the following:

```java
laf.register(Region.PANEL, "\"MyPanel\"");
UIManager.put("\"MyPanel\".background", new ColorUIResource(Color.RED));
```

Registers a third party component with the NimbusLookAndFeel.

Regions represent Components and areas within Components that act as
independent painting areas. Once registered with the NimbusLookAndFeel,
NimbusStyles for these Regions can be retrieved via the

getStyle

method.

The NimbusLookAndFeel uses a standard naming scheme for entries in the
UIDefaults table. The key for each property, state, painter, and other
default registered in UIDefaults for a specific Region will begin with
the specified

prefix

For example, suppose I had a component named JFoo. Suppose I then registered
this component with the NimbusLookAndFeel in this manner:

laf.register(NimbusFooUI.FOO_REGION, "Foo");

In this case, I could then register properties for this component with
UIDefaults in the following manner:

UIManager.put("Foo.background", new ColorUIResource(Color.BLACK));
UIManager.put("Foo.Enabled.backgroundPainter", new FooBackgroundPainter());

It is also possible to register a named component with Nimbus.
For example, suppose you wanted to style the background of a JPanel
named "MyPanel" differently from other JPanels. You could accomplish this
by doing the following:

laf.register(Region.PANEL, "\"MyPanel\"");
UIManager.put("\"MyPanel\".background", new ColorUIResource(Color.RED));

getDerivedColor

```java
public
Color
getDerivedColor​(
String
uiDefaultParentName,
float hOffset,
float sOffset,
float bOffset,
int aOffset,
boolean uiResource)
```

Get a derived color, derived colors are shared instances and is color
value will change when its parent UIDefault color changes.

**Parameters:** uiDefaultParentName

- The parent UIDefault key
**Parameters:** hOffset

- The hue offset
**Parameters:** sOffset

- The saturation offset
**Parameters:** bOffset

- The brightness offset
**Parameters:** aOffset

- The alpha offset
**Parameters:** uiResource

- True if the derived color should be a
UIResource, false if it should not be
**Returns:** The stored derived color

---

#### getDerivedColor

public

Color

getDerivedColor​(

String

uiDefaultParentName,
float hOffset,
float sOffset,
float bOffset,
int aOffset,
boolean uiResource)

Get a derived color, derived colors are shared instances and is color
value will change when its parent UIDefault color changes.

getDerivedColor

```java
protected final
Color
getDerivedColor​(
Color
color1,

Color
color2,
float midPoint,
boolean uiResource)
```

Decodes and returns a color, which is derived from an offset between two
other colors.

**Parameters:** color1

- The first color
**Parameters:** color2

- The second color
**Parameters:** midPoint

- The offset between color 1 and color 2, a value of 0.0 is
color 1 and 1.0 is color 2;
**Parameters:** uiResource

- True if the derived color should be a UIResource
**Returns:** The derived color

---

#### getDerivedColor

protected final

Color

getDerivedColor​(

Color

color1,

Color

color2,
float midPoint,
boolean uiResource)

Decodes and returns a color, which is derived from an offset between two
other colors.

getDerivedColor

```java
protected final
Color
getDerivedColor​(
Color
color1,

Color
color2,
float midPoint)
```

Decodes and returns a color, which is derived from a offset between two
other colors.

**Parameters:** color1

- The first color
**Parameters:** color2

- The second color
**Parameters:** midPoint

- The offset between color 1 and color 2, a value of 0.0 is
color 1 and 1.0 is color 2;
**Returns:** The derived color, which will be a UIResource

---

#### getDerivedColor

protected final

Color

getDerivedColor​(

Color

color1,

Color

color2,
float midPoint)

Decodes and returns a color, which is derived from a offset between two
other colors.

---

