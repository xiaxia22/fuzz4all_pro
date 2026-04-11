# Class SynthStyle

**Source:** `java.desktop\javax\swing\plaf\synth\SynthStyle.html`

### Class Description

```java
public abstract class
SynthStyle

extends
Object
```

SynthStyle

is a set of style properties.
Each

SynthUI

references at least one

SynthStyle

that is obtained using a

SynthStyleFactory

. You typically don't need to interact with
this class directly, rather you will load a

Synth File Format file

into

SynthLookAndFeel

that will create a set of SynthStyles.

**Direct Known Subclasses:** NimbusStyle

---

### Field Details

*No entries found.*

### Constructor Details

#### public SynthStyle()

Constructs a SynthStyle.

---

### Method Details

#### public
SynthGraphicsUtils
getGraphicsUtils​(
SynthContext
context)

Returns the

SynthGraphicUtils

for the specified context.

**Parameters:**
- context

- SynthContext identifying requester

**Returns:**
- SynthGraphicsUtils

---

#### public
Color
getColor​(
SynthContext
context,

ColorType
type)

Returns the color for the specified state. This gives precedence to
foreground and background of the

JComponent

. If the

Color

from the

JComponent

is not appropriate,
or not used, this will invoke

getColorForState

. Subclasses
should generally not have to override this, instead override

getColorForState(javax.swing.plaf.synth.SynthContext, javax.swing.plaf.synth.ColorType)

.

**Parameters:**
- context

- SynthContext identifying requester
- type

- Type of color being requested.

**Returns:**
- Color

---

#### protected abstract
Color
getColorForState​(
SynthContext
context,

ColorType
type)

Returns the color for the specified state. This should NOT call any
methods on the

JComponent

.

**Parameters:**
- context

- SynthContext identifying requester
- type

- Type of color being requested.

**Returns:**
- Color to render with

---

#### public
Font
getFont​(
SynthContext
context)

Returns the Font for the specified state. This redirects to the

JComponent

from the

context

as necessary.
If this does not redirect
to the JComponent

getFontForState(javax.swing.plaf.synth.SynthContext)

is invoked.

**Parameters:**
- context

- SynthContext identifying requester

**Returns:**
- Font to render with

---

#### protected abstract
Font
getFontForState​(
SynthContext
context)

Returns the font for the specified state. This should NOT call any
method on the

JComponent

.

**Parameters:**
- context

- SynthContext identifying requester

**Returns:**
- Font to render with

---

#### public
Insets
getInsets​(
SynthContext
context,

Insets
insets)

Returns the Insets that are used to calculate sizing information.

**Parameters:**
- context

- SynthContext identifying requester
- insets

- Insets to place return value in.

**Returns:**
- Sizing Insets.

---

#### public
SynthPainter
getPainter​(
SynthContext
context)

Returns the

SynthPainter

that will be used for painting.
This may return null.

**Parameters:**
- context

- SynthContext identifying requester

**Returns:**
- SynthPainter to use

---

#### public boolean isOpaque​(
SynthContext
context)

Returns true if the region is opaque.

**Parameters:**
- context

- SynthContext identifying requester

**Returns:**
- true if region is opaque.

---

#### public
Object
get​(
SynthContext
context,

Object
key)

Getter for a region specific style property.

**Parameters:**
- context

- SynthContext identifying requester
- key

- Property being requested.

**Returns:**
- Value of the named property

---

#### public void installDefaults​(
SynthContext
context)

Installs the necessary state from this Style on the

JComponent

from

context

.

**Parameters:**
- context

- SynthContext identifying component to install properties
to.

---

#### public void uninstallDefaults​(
SynthContext
context)

Uninstalls any state that this style installed on
the

JComponent

from

context

.

Styles should NOT depend upon this being called, in certain cases
it may never be called.

**Parameters:**
- context

- SynthContext identifying component to install properties
to.

---

#### public int getInt​(
SynthContext
context,

Object
key,
int defaultValue)

Convenience method to get a specific style property whose value is
a

Number

. If the value is a

Number

,

intValue

is returned, otherwise

defaultValue

is returned.

**Parameters:**
- context

- SynthContext identifying requester
- key

- Property being requested.
- defaultValue

- Value to return if the property has not been
specified, or is not a Number

**Returns:**
- Value of the named property

---

#### public boolean getBoolean​(
SynthContext
context,

Object
key,
boolean defaultValue)

Convenience method to get a specific style property whose value is
an Boolean.

**Parameters:**
- context

- SynthContext identifying requester
- key

- Property being requested.
- defaultValue

- Value to return if the property has not been
specified, or is not a Boolean

**Returns:**
- Value of the named property

---

#### public
Icon
getIcon​(
SynthContext
context,

Object
key)

Convenience method to get a specific style property whose value is
an Icon.

**Parameters:**
- context

- SynthContext identifying requester
- key

- Property being requested.

**Returns:**
- Value of the named property, or null if not specified

---

#### public
String
getString​(
SynthContext
context,

Object
key,

String
defaultValue)

Convenience method to get a specific style property whose value is
a String.

**Parameters:**
- context

- SynthContext identifying requester
- key

- Property being requested.
- defaultValue

- Value to return if the property has not been
specified, or is not a String

**Returns:**
- Value of the named property

---

### Additional Sections

#### Class SynthStyle

java.lang.Object

- javax.swing.plaf.synth.SynthStyle

javax.swing.plaf.synth.SynthStyle

**Direct Known Subclasses:** NimbusStyle

```java
public abstract class
SynthStyle

extends
Object
```

SynthStyle

is a set of style properties.
Each

SynthUI

references at least one

SynthStyle

that is obtained using a

SynthStyleFactory

. You typically don't need to interact with
this class directly, rather you will load a

Synth File Format file

into

SynthLookAndFeel

that will create a set of SynthStyles.

**Since:** 1.5
**See Also:** SynthLookAndFeel

,

SynthStyleFactory

public abstract class

SynthStyle

extends

Object

SynthStyle

is a set of style properties.
Each

SynthUI

references at least one

SynthStyle

that is obtained using a

SynthStyleFactory

. You typically don't need to interact with
this class directly, rather you will load a

Synth File Format file

into

SynthLookAndFeel

that will create a set of SynthStyles.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SynthStyle

()

Constructs a SynthStyle.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

Object

get

​(

SynthContext

context,

Object

key)

Getter for a region specific style property.

boolean

getBoolean

​(

SynthContext

context,

Object

key,
boolean defaultValue)

Convenience method to get a specific style property whose value is
an Boolean.

Color

getColor

​(

SynthContext

context,

ColorType

type)

Returns the color for the specified state.

protected abstract

Color

getColorForState

​(

SynthContext

context,

ColorType

type)

Returns the color for the specified state.

Font

getFont

​(

SynthContext

context)

Returns the Font for the specified state.

protected abstract

Font

getFontForState

​(

SynthContext

context)

Returns the font for the specified state.

SynthGraphicsUtils

getGraphicsUtils

​(

SynthContext

context)

Returns the

SynthGraphicUtils

for the specified context.

Icon

getIcon

​(

SynthContext

context,

Object

key)

Convenience method to get a specific style property whose value is
an Icon.

Insets

getInsets

​(

SynthContext

context,

Insets

insets)

Returns the Insets that are used to calculate sizing information.

int

getInt

​(

SynthContext

context,

Object

key,
int defaultValue)

Convenience method to get a specific style property whose value is
a

Number

.

SynthPainter

getPainter

​(

SynthContext

context)

Returns the

SynthPainter

that will be used for painting.

String

getString

​(

SynthContext

context,

Object

key,

String

defaultValue)

Convenience method to get a specific style property whose value is
a String.

void

installDefaults

​(

SynthContext

context)

Installs the necessary state from this Style on the

JComponent

from

context

.

boolean

isOpaque

​(

SynthContext

context)

Returns true if the region is opaque.

void

uninstallDefaults

​(

SynthContext

context)

Uninstalls any state that this style installed on
the

JComponent

from

context

.

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

SynthStyle

()

Constructs a SynthStyle.

---

#### Constructor Summary

Constructs a SynthStyle.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

Object

get

​(

SynthContext

context,

Object

key)

Getter for a region specific style property.

boolean

getBoolean

​(

SynthContext

context,

Object

key,
boolean defaultValue)

Convenience method to get a specific style property whose value is
an Boolean.

Color

getColor

​(

SynthContext

context,

ColorType

type)

Returns the color for the specified state.

protected abstract

Color

getColorForState

​(

SynthContext

context,

ColorType

type)

Returns the color for the specified state.

Font

getFont

​(

SynthContext

context)

Returns the Font for the specified state.

protected abstract

Font

getFontForState

​(

SynthContext

context)

Returns the font for the specified state.

SynthGraphicsUtils

getGraphicsUtils

​(

SynthContext

context)

Returns the

SynthGraphicUtils

for the specified context.

Icon

getIcon

​(

SynthContext

context,

Object

key)

Convenience method to get a specific style property whose value is
an Icon.

Insets

getInsets

​(

SynthContext

context,

Insets

insets)

Returns the Insets that are used to calculate sizing information.

int

getInt

​(

SynthContext

context,

Object

key,
int defaultValue)

Convenience method to get a specific style property whose value is
a

Number

.

SynthPainter

getPainter

​(

SynthContext

context)

Returns the

SynthPainter

that will be used for painting.

String

getString

​(

SynthContext

context,

Object

key,

String

defaultValue)

Convenience method to get a specific style property whose value is
a String.

void

installDefaults

​(

SynthContext

context)

Installs the necessary state from this Style on the

JComponent

from

context

.

boolean

isOpaque

​(

SynthContext

context)

Returns true if the region is opaque.

void

uninstallDefaults

​(

SynthContext

context)

Uninstalls any state that this style installed on
the

JComponent

from

context

.

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

Getter for a region specific style property.

Convenience method to get a specific style property whose value is
an Boolean.

Returns the color for the specified state.

Returns the Font for the specified state.

Returns the font for the specified state.

Returns the

SynthGraphicUtils

for the specified context.

Convenience method to get a specific style property whose value is
an Icon.

Returns the Insets that are used to calculate sizing information.

Convenience method to get a specific style property whose value is
a

Number

.

Returns the

SynthPainter

that will be used for painting.

Convenience method to get a specific style property whose value is
a String.

Installs the necessary state from this Style on the

JComponent

from

context

.

Returns true if the region is opaque.

Uninstalls any state that this style installed on
the

JComponent

from

context

.

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

- SynthStyle

```java
public SynthStyle()
```

Constructs a SynthStyle.

============ METHOD DETAIL ==========

- Method Detail

- getGraphicsUtils

```java
public
SynthGraphicsUtils
getGraphicsUtils​(
SynthContext
context)
```

Returns the

SynthGraphicUtils

for the specified context.

**Parameters:** context

- SynthContext identifying requester
**Returns:** SynthGraphicsUtils

- getColor

```java
public
Color
getColor​(
SynthContext
context,

ColorType
type)
```

Returns the color for the specified state. This gives precedence to
foreground and background of the

JComponent

. If the

Color

from the

JComponent

is not appropriate,
or not used, this will invoke

getColorForState

. Subclasses
should generally not have to override this, instead override

getColorForState(javax.swing.plaf.synth.SynthContext, javax.swing.plaf.synth.ColorType)

.

**Parameters:** context

- SynthContext identifying requester
**Parameters:** type

- Type of color being requested.
**Returns:** Color

- getColorForState

```java
protected abstract
Color
getColorForState​(
SynthContext
context,

ColorType
type)
```

Returns the color for the specified state. This should NOT call any
methods on the

JComponent

.

**Parameters:** context

- SynthContext identifying requester
**Parameters:** type

- Type of color being requested.
**Returns:** Color to render with

- getFont

```java
public
Font
getFont​(
SynthContext
context)
```

Returns the Font for the specified state. This redirects to the

JComponent

from the

context

as necessary.
If this does not redirect
to the JComponent

getFontForState(javax.swing.plaf.synth.SynthContext)

is invoked.

**Parameters:** context

- SynthContext identifying requester
**Returns:** Font to render with

- getFontForState

```java
protected abstract
Font
getFontForState​(
SynthContext
context)
```

Returns the font for the specified state. This should NOT call any
method on the

JComponent

.

**Parameters:** context

- SynthContext identifying requester
**Returns:** Font to render with

- getInsets

```java
public
Insets
getInsets​(
SynthContext
context,

Insets
insets)
```

Returns the Insets that are used to calculate sizing information.

**Parameters:** context

- SynthContext identifying requester
**Parameters:** insets

- Insets to place return value in.
**Returns:** Sizing Insets.

- getPainter

```java
public
SynthPainter
getPainter​(
SynthContext
context)
```

Returns the

SynthPainter

that will be used for painting.
This may return null.

**Parameters:** context

- SynthContext identifying requester
**Returns:** SynthPainter to use

- isOpaque

```java
public boolean isOpaque​(
SynthContext
context)
```

Returns true if the region is opaque.

**Parameters:** context

- SynthContext identifying requester
**Returns:** true if region is opaque.

- get

```java
public
Object
get​(
SynthContext
context,

Object
key)
```

Getter for a region specific style property.

**Parameters:** context

- SynthContext identifying requester
**Parameters:** key

- Property being requested.
**Returns:** Value of the named property

- installDefaults

```java
public void installDefaults​(
SynthContext
context)
```

Installs the necessary state from this Style on the

JComponent

from

context

.

**Parameters:** context

- SynthContext identifying component to install properties
to.

- uninstallDefaults

```java
public void uninstallDefaults​(
SynthContext
context)
```

Uninstalls any state that this style installed on
the

JComponent

from

context

.

Styles should NOT depend upon this being called, in certain cases
it may never be called.

**Parameters:** context

- SynthContext identifying component to install properties
to.

- getInt

```java
public int getInt​(
SynthContext
context,

Object
key,
int defaultValue)
```

Convenience method to get a specific style property whose value is
a

Number

. If the value is a

Number

,

intValue

is returned, otherwise

defaultValue

is returned.

**Parameters:** context

- SynthContext identifying requester
**Parameters:** key

- Property being requested.
**Parameters:** defaultValue

- Value to return if the property has not been
specified, or is not a Number
**Returns:** Value of the named property

- getBoolean

```java
public boolean getBoolean​(
SynthContext
context,

Object
key,
boolean defaultValue)
```

Convenience method to get a specific style property whose value is
an Boolean.

**Parameters:** context

- SynthContext identifying requester
**Parameters:** key

- Property being requested.
**Parameters:** defaultValue

- Value to return if the property has not been
specified, or is not a Boolean
**Returns:** Value of the named property

- getIcon

```java
public
Icon
getIcon​(
SynthContext
context,

Object
key)
```

Convenience method to get a specific style property whose value is
an Icon.

**Parameters:** context

- SynthContext identifying requester
**Parameters:** key

- Property being requested.
**Returns:** Value of the named property, or null if not specified

- getString

```java
public
String
getString​(
SynthContext
context,

Object
key,

String
defaultValue)
```

Convenience method to get a specific style property whose value is
a String.

**Parameters:** context

- SynthContext identifying requester
**Parameters:** key

- Property being requested.
**Parameters:** defaultValue

- Value to return if the property has not been
specified, or is not a String
**Returns:** Value of the named property

Constructor Detail

- SynthStyle

```java
public SynthStyle()
```

Constructs a SynthStyle.

---

#### Constructor Detail

SynthStyle

```java
public SynthStyle()
```

Constructs a SynthStyle.

---

#### SynthStyle

public SynthStyle()

Constructs a SynthStyle.

Method Detail

- getGraphicsUtils

```java
public
SynthGraphicsUtils
getGraphicsUtils​(
SynthContext
context)
```

Returns the

SynthGraphicUtils

for the specified context.

**Parameters:** context

- SynthContext identifying requester
**Returns:** SynthGraphicsUtils

- getColor

```java
public
Color
getColor​(
SynthContext
context,

ColorType
type)
```

Returns the color for the specified state. This gives precedence to
foreground and background of the

JComponent

. If the

Color

from the

JComponent

is not appropriate,
or not used, this will invoke

getColorForState

. Subclasses
should generally not have to override this, instead override

getColorForState(javax.swing.plaf.synth.SynthContext, javax.swing.plaf.synth.ColorType)

.

**Parameters:** context

- SynthContext identifying requester
**Parameters:** type

- Type of color being requested.
**Returns:** Color

- getColorForState

```java
protected abstract
Color
getColorForState​(
SynthContext
context,

ColorType
type)
```

Returns the color for the specified state. This should NOT call any
methods on the

JComponent

.

**Parameters:** context

- SynthContext identifying requester
**Parameters:** type

- Type of color being requested.
**Returns:** Color to render with

- getFont

```java
public
Font
getFont​(
SynthContext
context)
```

Returns the Font for the specified state. This redirects to the

JComponent

from the

context

as necessary.
If this does not redirect
to the JComponent

getFontForState(javax.swing.plaf.synth.SynthContext)

is invoked.

**Parameters:** context

- SynthContext identifying requester
**Returns:** Font to render with

- getFontForState

```java
protected abstract
Font
getFontForState​(
SynthContext
context)
```

Returns the font for the specified state. This should NOT call any
method on the

JComponent

.

**Parameters:** context

- SynthContext identifying requester
**Returns:** Font to render with

- getInsets

```java
public
Insets
getInsets​(
SynthContext
context,

Insets
insets)
```

Returns the Insets that are used to calculate sizing information.

**Parameters:** context

- SynthContext identifying requester
**Parameters:** insets

- Insets to place return value in.
**Returns:** Sizing Insets.

- getPainter

```java
public
SynthPainter
getPainter​(
SynthContext
context)
```

Returns the

SynthPainter

that will be used for painting.
This may return null.

**Parameters:** context

- SynthContext identifying requester
**Returns:** SynthPainter to use

- isOpaque

```java
public boolean isOpaque​(
SynthContext
context)
```

Returns true if the region is opaque.

**Parameters:** context

- SynthContext identifying requester
**Returns:** true if region is opaque.

- get

```java
public
Object
get​(
SynthContext
context,

Object
key)
```

Getter for a region specific style property.

**Parameters:** context

- SynthContext identifying requester
**Parameters:** key

- Property being requested.
**Returns:** Value of the named property

- installDefaults

```java
public void installDefaults​(
SynthContext
context)
```

Installs the necessary state from this Style on the

JComponent

from

context

.

**Parameters:** context

- SynthContext identifying component to install properties
to.

- uninstallDefaults

```java
public void uninstallDefaults​(
SynthContext
context)
```

Uninstalls any state that this style installed on
the

JComponent

from

context

.

Styles should NOT depend upon this being called, in certain cases
it may never be called.

**Parameters:** context

- SynthContext identifying component to install properties
to.

- getInt

```java
public int getInt​(
SynthContext
context,

Object
key,
int defaultValue)
```

Convenience method to get a specific style property whose value is
a

Number

. If the value is a

Number

,

intValue

is returned, otherwise

defaultValue

is returned.

**Parameters:** context

- SynthContext identifying requester
**Parameters:** key

- Property being requested.
**Parameters:** defaultValue

- Value to return if the property has not been
specified, or is not a Number
**Returns:** Value of the named property

- getBoolean

```java
public boolean getBoolean​(
SynthContext
context,

Object
key,
boolean defaultValue)
```

Convenience method to get a specific style property whose value is
an Boolean.

**Parameters:** context

- SynthContext identifying requester
**Parameters:** key

- Property being requested.
**Parameters:** defaultValue

- Value to return if the property has not been
specified, or is not a Boolean
**Returns:** Value of the named property

- getIcon

```java
public
Icon
getIcon​(
SynthContext
context,

Object
key)
```

Convenience method to get a specific style property whose value is
an Icon.

**Parameters:** context

- SynthContext identifying requester
**Parameters:** key

- Property being requested.
**Returns:** Value of the named property, or null if not specified

- getString

```java
public
String
getString​(
SynthContext
context,

Object
key,

String
defaultValue)
```

Convenience method to get a specific style property whose value is
a String.

**Parameters:** context

- SynthContext identifying requester
**Parameters:** key

- Property being requested.
**Parameters:** defaultValue

- Value to return if the property has not been
specified, or is not a String
**Returns:** Value of the named property

---

#### Method Detail

getGraphicsUtils

```java
public
SynthGraphicsUtils
getGraphicsUtils​(
SynthContext
context)
```

Returns the

SynthGraphicUtils

for the specified context.

**Parameters:** context

- SynthContext identifying requester
**Returns:** SynthGraphicsUtils

---

#### getGraphicsUtils

public

SynthGraphicsUtils

getGraphicsUtils​(

SynthContext

context)

Returns the

SynthGraphicUtils

for the specified context.

getColor

```java
public
Color
getColor​(
SynthContext
context,

ColorType
type)
```

Returns the color for the specified state. This gives precedence to
foreground and background of the

JComponent

. If the

Color

from the

JComponent

is not appropriate,
or not used, this will invoke

getColorForState

. Subclasses
should generally not have to override this, instead override

getColorForState(javax.swing.plaf.synth.SynthContext, javax.swing.plaf.synth.ColorType)

.

**Parameters:** context

- SynthContext identifying requester
**Parameters:** type

- Type of color being requested.
**Returns:** Color

---

#### getColor

public

Color

getColor​(

SynthContext

context,

ColorType

type)

Returns the color for the specified state. This gives precedence to
foreground and background of the

JComponent

. If the

Color

from the

JComponent

is not appropriate,
or not used, this will invoke

getColorForState

. Subclasses
should generally not have to override this, instead override

getColorForState(javax.swing.plaf.synth.SynthContext, javax.swing.plaf.synth.ColorType)

.

getColorForState

```java
protected abstract
Color
getColorForState​(
SynthContext
context,

ColorType
type)
```

Returns the color for the specified state. This should NOT call any
methods on the

JComponent

.

**Parameters:** context

- SynthContext identifying requester
**Parameters:** type

- Type of color being requested.
**Returns:** Color to render with

---

#### getColorForState

protected abstract

Color

getColorForState​(

SynthContext

context,

ColorType

type)

Returns the color for the specified state. This should NOT call any
methods on the

JComponent

.

getFont

```java
public
Font
getFont​(
SynthContext
context)
```

Returns the Font for the specified state. This redirects to the

JComponent

from the

context

as necessary.
If this does not redirect
to the JComponent

getFontForState(javax.swing.plaf.synth.SynthContext)

is invoked.

**Parameters:** context

- SynthContext identifying requester
**Returns:** Font to render with

---

#### getFont

public

Font

getFont​(

SynthContext

context)

Returns the Font for the specified state. This redirects to the

JComponent

from the

context

as necessary.
If this does not redirect
to the JComponent

getFontForState(javax.swing.plaf.synth.SynthContext)

is invoked.

getFontForState

```java
protected abstract
Font
getFontForState​(
SynthContext
context)
```

Returns the font for the specified state. This should NOT call any
method on the

JComponent

.

**Parameters:** context

- SynthContext identifying requester
**Returns:** Font to render with

---

#### getFontForState

protected abstract

Font

getFontForState​(

SynthContext

context)

Returns the font for the specified state. This should NOT call any
method on the

JComponent

.

getInsets

```java
public
Insets
getInsets​(
SynthContext
context,

Insets
insets)
```

Returns the Insets that are used to calculate sizing information.

**Parameters:** context

- SynthContext identifying requester
**Parameters:** insets

- Insets to place return value in.
**Returns:** Sizing Insets.

---

#### getInsets

public

Insets

getInsets​(

SynthContext

context,

Insets

insets)

Returns the Insets that are used to calculate sizing information.

getPainter

```java
public
SynthPainter
getPainter​(
SynthContext
context)
```

Returns the

SynthPainter

that will be used for painting.
This may return null.

**Parameters:** context

- SynthContext identifying requester
**Returns:** SynthPainter to use

---

#### getPainter

public

SynthPainter

getPainter​(

SynthContext

context)

Returns the

SynthPainter

that will be used for painting.
This may return null.

isOpaque

```java
public boolean isOpaque​(
SynthContext
context)
```

Returns true if the region is opaque.

**Parameters:** context

- SynthContext identifying requester
**Returns:** true if region is opaque.

---

#### isOpaque

public boolean isOpaque​(

SynthContext

context)

Returns true if the region is opaque.

get

```java
public
Object
get​(
SynthContext
context,

Object
key)
```

Getter for a region specific style property.

**Parameters:** context

- SynthContext identifying requester
**Parameters:** key

- Property being requested.
**Returns:** Value of the named property

---

#### get

public

Object

get​(

SynthContext

context,

Object

key)

Getter for a region specific style property.

installDefaults

```java
public void installDefaults​(
SynthContext
context)
```

Installs the necessary state from this Style on the

JComponent

from

context

.

**Parameters:** context

- SynthContext identifying component to install properties
to.

---

#### installDefaults

public void installDefaults​(

SynthContext

context)

Installs the necessary state from this Style on the

JComponent

from

context

.

uninstallDefaults

```java
public void uninstallDefaults​(
SynthContext
context)
```

Uninstalls any state that this style installed on
the

JComponent

from

context

.

Styles should NOT depend upon this being called, in certain cases
it may never be called.

**Parameters:** context

- SynthContext identifying component to install properties
to.

---

#### uninstallDefaults

public void uninstallDefaults​(

SynthContext

context)

Uninstalls any state that this style installed on
the

JComponent

from

context

.

Styles should NOT depend upon this being called, in certain cases
it may never be called.

Styles should NOT depend upon this being called, in certain cases
it may never be called.

getInt

```java
public int getInt​(
SynthContext
context,

Object
key,
int defaultValue)
```

Convenience method to get a specific style property whose value is
a

Number

. If the value is a

Number

,

intValue

is returned, otherwise

defaultValue

is returned.

**Parameters:** context

- SynthContext identifying requester
**Parameters:** key

- Property being requested.
**Parameters:** defaultValue

- Value to return if the property has not been
specified, or is not a Number
**Returns:** Value of the named property

---

#### getInt

public int getInt​(

SynthContext

context,

Object

key,
int defaultValue)

Convenience method to get a specific style property whose value is
a

Number

. If the value is a

Number

,

intValue

is returned, otherwise

defaultValue

is returned.

getBoolean

```java
public boolean getBoolean​(
SynthContext
context,

Object
key,
boolean defaultValue)
```

Convenience method to get a specific style property whose value is
an Boolean.

**Parameters:** context

- SynthContext identifying requester
**Parameters:** key

- Property being requested.
**Parameters:** defaultValue

- Value to return if the property has not been
specified, or is not a Boolean
**Returns:** Value of the named property

---

#### getBoolean

public boolean getBoolean​(

SynthContext

context,

Object

key,
boolean defaultValue)

Convenience method to get a specific style property whose value is
an Boolean.

getIcon

```java
public
Icon
getIcon​(
SynthContext
context,

Object
key)
```

Convenience method to get a specific style property whose value is
an Icon.

**Parameters:** context

- SynthContext identifying requester
**Parameters:** key

- Property being requested.
**Returns:** Value of the named property, or null if not specified

---

#### getIcon

public

Icon

getIcon​(

SynthContext

context,

Object

key)

Convenience method to get a specific style property whose value is
an Icon.

getString

```java
public
String
getString​(
SynthContext
context,

Object
key,

String
defaultValue)
```

Convenience method to get a specific style property whose value is
a String.

**Parameters:** context

- SynthContext identifying requester
**Parameters:** key

- Property being requested.
**Parameters:** defaultValue

- Value to return if the property has not been
specified, or is not a String
**Returns:** Value of the named property

---

#### getString

public

String

getString​(

SynthContext

context,

Object

key,

String

defaultValue)

Convenience method to get a specific style property whose value is
a String.

---

