# Class SynthLookAndFeel

**Source:** `java.desktop\javax\swing\plaf\synth\SynthLookAndFeel.html`

### Class Description

```java
public class
SynthLookAndFeel

extends
BasicLookAndFeel
```

SynthLookAndFeel provides the basis for creating a customized look and
feel. SynthLookAndFeel does not directly provide a look, all painting is
delegated.
You need to either provide a configuration file, by way of the

load(java.io.InputStream, java.lang.Class<?>)

method, or provide your own

SynthStyleFactory

to

setStyleFactory(javax.swing.plaf.synth.SynthStyleFactory)

. Refer to the

package summary

for an example of
loading a file, and

SynthStyleFactory

for
an example of providing your own

SynthStyleFactory

to

setStyleFactory

.

SynthIcon

interface provides

paintIcon(synthContext, graphics, x, y, width, height)

method that
allows to draw the icon with the given

SynthContext

.

Warning:

This class implements

Serializable

as a side effect of it
extending

BasicLookAndFeel

. It is not intended to be serialized.
An attempt to serialize it will
result in

NotSerializableException

.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public SynthLookAndFeel()

Creates a SynthLookAndFeel.

For the returned

SynthLookAndFeel

to be useful you need to
invoke

load

to specify the set of

SynthStyle

s, or invoke

setStyleFactory

.

**See Also:**
- load(java.io.InputStream, java.lang.Class<?>)

,

setStyleFactory(javax.swing.plaf.synth.SynthStyleFactory)

---

### Method Details

#### public static void setStyleFactory​(
SynthStyleFactory
cache)

Sets the SynthStyleFactory that the UI classes provided by
synth will use to obtain a SynthStyle.

**Parameters:**
- cache

- SynthStyleFactory the UIs should use.

---

#### public static
SynthStyleFactory
getStyleFactory()

Returns the current SynthStyleFactory.

**Returns:**
- SynthStyleFactory

---

#### public static
SynthStyle
getStyle​(
JComponent
c,

Region
region)

Gets a SynthStyle for the specified region of the specified component.
This is not for general consumption, only custom UIs should call this
method.

**Parameters:**
- c

- JComponent to get the SynthStyle for
- region

- Identifies the region of the specified component

**Returns:**
- SynthStyle to use.

---

#### public static void updateStyles​(
Component
c)

Updates the style associated with

c

, and all its children.
This is a lighter version of

SwingUtilities.updateComponentTreeUI

.

**Parameters:**
- c

- Component to update style for.

---

#### public static
Region
getRegion​(
JComponent
c)

Returns the Region for the JComponent

c

.

**Parameters:**
- c

- JComponent to fetch the Region for

**Returns:**
- Region corresponding to

c

---

#### public static
ComponentUI
createUI​(
JComponent
c)

Creates the Synth look and feel

ComponentUI

for
the passed in

JComponent

.

**Parameters:**
- c

- JComponent to create the

ComponentUI

for

**Returns:**
- ComponentUI to use for

c

---

#### public void load​(
InputStream
input,

Class
<?> resourceBase)
throws
ParseException

Loads the set of

SynthStyle

s that will be used by
this

SynthLookAndFeel

.

resourceBase

is
used to resolve any path based resources, for example an

Image

would be resolved by

resourceBase.getResource(path)

. Refer to

Synth File Format

for more information.

**Parameters:**
- input

- InputStream to load from
- resourceBase

- used to resolve any images or other resources

**Throws:**
- ParseException

- if there is an error in parsing
- IllegalArgumentException

- if input or resourceBase is

null

---

#### public void load​(
URL
url)
throws
ParseException
,

IOException

Loads the set of

SynthStyle

s that will be used by
this

SynthLookAndFeel

. Path based resources are resolved
relatively to the specified

URL

of the style. For example
an

Image

would be resolved by

new URL(synthFile, path)

. Refer to

Synth File Format

for more
information.

Whilst this API may be safe for loading local resources that are
delivered with a

LookAndFeel

or application, and so have an
equal level of trust with application code, using it to load from
remote resources, particularly any which may have a lower level of
trust, is strongly discouraged.
The alternative mechanisms to load styles from an

InputStream

load(InputStream, Class)

using resources co-located with the application or by providing a

SynthStyleFactory

to

setStyleFactory(SynthStyleFactory)

are preferred.

**Parameters:**
- url

- the

URL

to load the set of

SynthStyle

from

**Throws:**
- ParseException

- if there is an error in parsing
- IllegalArgumentException

- if synthSet is

null
- IOException

- if synthSet cannot be opened as an

InputStream

**Since:**
- 1.6

---

#### public void initialize()

Called by UIManager when this look and feel is installed.

**Overrides:**
- initialize

in class

LookAndFeel

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

LookAndFeel

**See Also:**
- LookAndFeel.initialize()

,

UIManager.setLookAndFeel(javax.swing.LookAndFeel)

---

#### public
UIDefaults
getDefaults()

Returns the defaults for this SynthLookAndFeel.

**Overrides:**
- getDefaults

in class

BasicLookAndFeel

**Returns:**
- Defaults table.

**See Also:**
- BasicLookAndFeel.initClassDefaults(javax.swing.UIDefaults)

,

BasicLookAndFeel.initSystemColorDefaults(javax.swing.UIDefaults)

,

BasicLookAndFeel.initComponentDefaults(javax.swing.UIDefaults)

---

#### public boolean isSupportedLookAndFeel()

Returns true, SynthLookAndFeel is always supported.

**Specified by:**
- isSupportedLookAndFeel

in class

LookAndFeel

**Returns:**
- true.

**See Also:**
- UIManager.setLookAndFeel(javax.swing.LookAndFeel)

---

#### public boolean isNativeLookAndFeel()

Returns false, SynthLookAndFeel is not a native look and feel.

**Specified by:**
- isNativeLookAndFeel

in class

LookAndFeel

**Returns:**
- false

---

#### public
String
getDescription()

Returns a textual description of SynthLookAndFeel.

**Specified by:**
- getDescription

in class

LookAndFeel

**Returns:**
- textual description of synth.

---

#### public
String
getName()

Return a short string that identifies this look and feel.

**Specified by:**
- getName

in class

LookAndFeel

**Returns:**
- a short string identifying this look and feel.

---

#### public
String
getID()

Return a string that identifies this look and feel.

**Specified by:**
- getID

in class

LookAndFeel

**Returns:**
- a short string identifying this look and feel.

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

**Returns:**
- whether or not the UIs should update their

SynthStyles

from the

SynthStyleFactory

when the ancestor changed.

---

#### protected boolean shouldUpdateStyleOnEvent​(
PropertyChangeEvent
ev)

Returns whether or not the UIs should update their styles when a
particular event occurs.

**Parameters:**
- ev

- a

PropertyChangeEvent

**Returns:**
- whether or not the UIs should update their styles

**Since:**
- 1.7

---

### Additional Sections

#### Class SynthLookAndFeel

java.lang.Object

- javax.swing.LookAndFeel
- - javax.swing.plaf.basic.BasicLookAndFeel
- - javax.swing.plaf.synth.SynthLookAndFeel

javax.swing.LookAndFeel

- javax.swing.plaf.basic.BasicLookAndFeel
- - javax.swing.plaf.synth.SynthLookAndFeel

javax.swing.plaf.basic.BasicLookAndFeel

- javax.swing.plaf.synth.SynthLookAndFeel

javax.swing.plaf.synth.SynthLookAndFeel

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** NimbusLookAndFeel

```java
public class
SynthLookAndFeel

extends
BasicLookAndFeel
```

SynthLookAndFeel provides the basis for creating a customized look and
feel. SynthLookAndFeel does not directly provide a look, all painting is
delegated.
You need to either provide a configuration file, by way of the

load(java.io.InputStream, java.lang.Class<?>)

method, or provide your own

SynthStyleFactory

to

setStyleFactory(javax.swing.plaf.synth.SynthStyleFactory)

. Refer to the

package summary

for an example of
loading a file, and

SynthStyleFactory

for
an example of providing your own

SynthStyleFactory

to

setStyleFactory

.

SynthIcon

interface provides

paintIcon(synthContext, graphics, x, y, width, height)

method that
allows to draw the icon with the given

SynthContext

.

Warning:

This class implements

Serializable

as a side effect of it
extending

BasicLookAndFeel

. It is not intended to be serialized.
An attempt to serialize it will
result in

NotSerializableException

.

**Since:** 1.5

public class

SynthLookAndFeel

extends

BasicLookAndFeel

SynthLookAndFeel provides the basis for creating a customized look and
feel. SynthLookAndFeel does not directly provide a look, all painting is
delegated.
You need to either provide a configuration file, by way of the

load(java.io.InputStream, java.lang.Class<?>)

method, or provide your own

SynthStyleFactory

to

setStyleFactory(javax.swing.plaf.synth.SynthStyleFactory)

. Refer to the

package summary

for an example of
loading a file, and

SynthStyleFactory

for
an example of providing your own

SynthStyleFactory

to

setStyleFactory

.

SynthIcon

interface provides

paintIcon(synthContext, graphics, x, y, width, height)

method that
allows to draw the icon with the given

SynthContext

.

Warning:

This class implements

Serializable

as a side effect of it
extending

BasicLookAndFeel

. It is not intended to be serialized.
An attempt to serialize it will
result in

NotSerializableException

.

SynthIcon

interface provides

paintIcon(synthContext, graphics, x, y, width, height)

method that
allows to draw the icon with the given

SynthContext

.

Warning:

This class implements

Serializable

as a side effect of it
extending

BasicLookAndFeel

. It is not intended to be serialized.
An attempt to serialize it will
result in

NotSerializableException

.

Warning:

This class implements

Serializable

as a side effect of it
extending

BasicLookAndFeel

. It is not intended to be serialized.
An attempt to serialize it will
result in

NotSerializableException

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SynthLookAndFeel

()

Creates a SynthLookAndFeel.

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

Creates the Synth look and feel

ComponentUI

for
the passed in

JComponent

.

UIDefaults

getDefaults

()

Returns the defaults for this SynthLookAndFeel.

String

getDescription

()

Returns a textual description of SynthLookAndFeel.

String

getID

()

Return a string that identifies this look and feel.

String

getName

()

Return a short string that identifies this look and feel.

static

Region

getRegion

​(

JComponent

c)

Returns the Region for the JComponent

c

.

static

SynthStyle

getStyle

​(

JComponent

c,

Region

region)

Gets a SynthStyle for the specified region of the specified component.

static

SynthStyleFactory

getStyleFactory

()

Returns the current SynthStyleFactory.

void

initialize

()

Called by UIManager when this look and feel is installed.

boolean

isNativeLookAndFeel

()

Returns false, SynthLookAndFeel is not a native look and feel.

boolean

isSupportedLookAndFeel

()

Returns true, SynthLookAndFeel is always supported.

void

load

​(

InputStream

input,

Class

<?> resourceBase)

Loads the set of

SynthStyle

s that will be used by
this

SynthLookAndFeel

.

void

load

​(

URL

url)

Loads the set of

SynthStyle

s that will be used by
this

SynthLookAndFeel

.

static void

setStyleFactory

​(

SynthStyleFactory

cache)

Sets the SynthStyleFactory that the UI classes provided by
synth will use to obtain a SynthStyle.

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

static void

updateStyles

​(

Component

c)

Updates the style associated with

c

, and all its children.

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

SynthLookAndFeel

()

Creates a SynthLookAndFeel.

---

#### Constructor Summary

Creates a SynthLookAndFeel.

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

Creates the Synth look and feel

ComponentUI

for
the passed in

JComponent

.

UIDefaults

getDefaults

()

Returns the defaults for this SynthLookAndFeel.

String

getDescription

()

Returns a textual description of SynthLookAndFeel.

String

getID

()

Return a string that identifies this look and feel.

String

getName

()

Return a short string that identifies this look and feel.

static

Region

getRegion

​(

JComponent

c)

Returns the Region for the JComponent

c

.

static

SynthStyle

getStyle

​(

JComponent

c,

Region

region)

Gets a SynthStyle for the specified region of the specified component.

static

SynthStyleFactory

getStyleFactory

()

Returns the current SynthStyleFactory.

void

initialize

()

Called by UIManager when this look and feel is installed.

boolean

isNativeLookAndFeel

()

Returns false, SynthLookAndFeel is not a native look and feel.

boolean

isSupportedLookAndFeel

()

Returns true, SynthLookAndFeel is always supported.

void

load

​(

InputStream

input,

Class

<?> resourceBase)

Loads the set of

SynthStyle

s that will be used by
this

SynthLookAndFeel

.

void

load

​(

URL

url)

Loads the set of

SynthStyle

s that will be used by
this

SynthLookAndFeel

.

static void

setStyleFactory

​(

SynthStyleFactory

cache)

Sets the SynthStyleFactory that the UI classes provided by
synth will use to obtain a SynthStyle.

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

static void

updateStyles

​(

Component

c)

Updates the style associated with

c

, and all its children.

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

Creates the Synth look and feel

ComponentUI

for
the passed in

JComponent

.

Returns the defaults for this SynthLookAndFeel.

Returns a textual description of SynthLookAndFeel.

Return a string that identifies this look and feel.

Return a short string that identifies this look and feel.

Returns the Region for the JComponent

c

.

Gets a SynthStyle for the specified region of the specified component.

Returns the current SynthStyleFactory.

Called by UIManager when this look and feel is installed.

Returns false, SynthLookAndFeel is not a native look and feel.

Returns true, SynthLookAndFeel is always supported.

Loads the set of

SynthStyle

s that will be used by
this

SynthLookAndFeel

.

Sets the SynthStyleFactory that the UI classes provided by
synth will use to obtain a SynthStyle.

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

Updates the style associated with

c

, and all its children.

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

- SynthLookAndFeel

```java
public SynthLookAndFeel()
```

Creates a SynthLookAndFeel.

For the returned

SynthLookAndFeel

to be useful you need to
invoke

load

to specify the set of

SynthStyle

s, or invoke

setStyleFactory

.

**See Also:** load(java.io.InputStream, java.lang.Class<?>)

,

setStyleFactory(javax.swing.plaf.synth.SynthStyleFactory)

============ METHOD DETAIL ==========

- Method Detail

- setStyleFactory

```java
public static void setStyleFactory​(
SynthStyleFactory
cache)
```

Sets the SynthStyleFactory that the UI classes provided by
synth will use to obtain a SynthStyle.

**Parameters:** cache

- SynthStyleFactory the UIs should use.

- getStyleFactory

```java
public static
SynthStyleFactory
getStyleFactory()
```

Returns the current SynthStyleFactory.

**Returns:** SynthStyleFactory

- getStyle

```java
public static
SynthStyle
getStyle​(
JComponent
c,

Region
region)
```

Gets a SynthStyle for the specified region of the specified component.
This is not for general consumption, only custom UIs should call this
method.

**Parameters:** c

- JComponent to get the SynthStyle for
**Parameters:** region

- Identifies the region of the specified component
**Returns:** SynthStyle to use.

- updateStyles

```java
public static void updateStyles​(
Component
c)
```

Updates the style associated with

c

, and all its children.
This is a lighter version of

SwingUtilities.updateComponentTreeUI

.

**Parameters:** c

- Component to update style for.

- getRegion

```java
public static
Region
getRegion​(
JComponent
c)
```

Returns the Region for the JComponent

c

.

**Parameters:** c

- JComponent to fetch the Region for
**Returns:** Region corresponding to

c

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Creates the Synth look and feel

ComponentUI

for
the passed in

JComponent

.

**Parameters:** c

- JComponent to create the

ComponentUI

for
**Returns:** ComponentUI to use for

c

- load

```java
public void load​(
InputStream
input,

Class
<?> resourceBase)
throws
ParseException
```

Loads the set of

SynthStyle

s that will be used by
this

SynthLookAndFeel

.

resourceBase

is
used to resolve any path based resources, for example an

Image

would be resolved by

resourceBase.getResource(path)

. Refer to

Synth File Format

for more information.

**Parameters:** input

- InputStream to load from
**Parameters:** resourceBase

- used to resolve any images or other resources
**Throws:** ParseException

- if there is an error in parsing
**Throws:** IllegalArgumentException

- if input or resourceBase is

null

- load

```java
public void load​(
URL
url)
throws
ParseException
,

IOException
```

Loads the set of

SynthStyle

s that will be used by
this

SynthLookAndFeel

. Path based resources are resolved
relatively to the specified

URL

of the style. For example
an

Image

would be resolved by

new URL(synthFile, path)

. Refer to

Synth File Format

for more
information.

Whilst this API may be safe for loading local resources that are
delivered with a

LookAndFeel

or application, and so have an
equal level of trust with application code, using it to load from
remote resources, particularly any which may have a lower level of
trust, is strongly discouraged.
The alternative mechanisms to load styles from an

InputStream

load(InputStream, Class)

using resources co-located with the application or by providing a

SynthStyleFactory

to

setStyleFactory(SynthStyleFactory)

are preferred.

**Parameters:** url

- the

URL

to load the set of

SynthStyle

from
**Throws:** ParseException

- if there is an error in parsing
**Throws:** IllegalArgumentException

- if synthSet is

null
**Throws:** IOException

- if synthSet cannot be opened as an

InputStream
**Since:** 1.6

- initialize

```java
public void initialize()
```

Called by UIManager when this look and feel is installed.

**Overrides:** initialize

in class

LookAndFeel
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

LookAndFeel
**See Also:** LookAndFeel.initialize()

,

UIManager.setLookAndFeel(javax.swing.LookAndFeel)

- getDefaults

```java
public
UIDefaults
getDefaults()
```

Returns the defaults for this SynthLookAndFeel.

**Overrides:** getDefaults

in class

BasicLookAndFeel
**Returns:** Defaults table.
**See Also:** BasicLookAndFeel.initClassDefaults(javax.swing.UIDefaults)

,

BasicLookAndFeel.initSystemColorDefaults(javax.swing.UIDefaults)

,

BasicLookAndFeel.initComponentDefaults(javax.swing.UIDefaults)

- isSupportedLookAndFeel

```java
public boolean isSupportedLookAndFeel()
```

Returns true, SynthLookAndFeel is always supported.

**Specified by:** isSupportedLookAndFeel

in class

LookAndFeel
**Returns:** true.
**See Also:** UIManager.setLookAndFeel(javax.swing.LookAndFeel)

- isNativeLookAndFeel

```java
public boolean isNativeLookAndFeel()
```

Returns false, SynthLookAndFeel is not a native look and feel.

**Specified by:** isNativeLookAndFeel

in class

LookAndFeel
**Returns:** false

- getDescription

```java
public
String
getDescription()
```

Returns a textual description of SynthLookAndFeel.

**Specified by:** getDescription

in class

LookAndFeel
**Returns:** textual description of synth.

- getName

```java
public
String
getName()
```

Return a short string that identifies this look and feel.

**Specified by:** getName

in class

LookAndFeel
**Returns:** a short string identifying this look and feel.

- getID

```java
public
String
getID()
```

Return a string that identifies this look and feel.

**Specified by:** getID

in class

LookAndFeel
**Returns:** a short string identifying this look and feel.

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

**Returns:** whether or not the UIs should update their

SynthStyles

from the

SynthStyleFactory

when the ancestor changed.

- shouldUpdateStyleOnEvent

```java
protected boolean shouldUpdateStyleOnEvent​(
PropertyChangeEvent
ev)
```

Returns whether or not the UIs should update their styles when a
particular event occurs.

**Parameters:** ev

- a

PropertyChangeEvent
**Returns:** whether or not the UIs should update their styles
**Since:** 1.7

Constructor Detail

- SynthLookAndFeel

```java
public SynthLookAndFeel()
```

Creates a SynthLookAndFeel.

For the returned

SynthLookAndFeel

to be useful you need to
invoke

load

to specify the set of

SynthStyle

s, or invoke

setStyleFactory

.

**See Also:** load(java.io.InputStream, java.lang.Class<?>)

,

setStyleFactory(javax.swing.plaf.synth.SynthStyleFactory)

---

#### Constructor Detail

SynthLookAndFeel

```java
public SynthLookAndFeel()
```

Creates a SynthLookAndFeel.

For the returned

SynthLookAndFeel

to be useful you need to
invoke

load

to specify the set of

SynthStyle

s, or invoke

setStyleFactory

.

**See Also:** load(java.io.InputStream, java.lang.Class<?>)

,

setStyleFactory(javax.swing.plaf.synth.SynthStyleFactory)

---

#### SynthLookAndFeel

public SynthLookAndFeel()

Creates a SynthLookAndFeel.

For the returned

SynthLookAndFeel

to be useful you need to
invoke

load

to specify the set of

SynthStyle

s, or invoke

setStyleFactory

.

For the returned

SynthLookAndFeel

to be useful you need to
invoke

load

to specify the set of

SynthStyle

s, or invoke

setStyleFactory

.

Method Detail

- setStyleFactory

```java
public static void setStyleFactory​(
SynthStyleFactory
cache)
```

Sets the SynthStyleFactory that the UI classes provided by
synth will use to obtain a SynthStyle.

**Parameters:** cache

- SynthStyleFactory the UIs should use.

- getStyleFactory

```java
public static
SynthStyleFactory
getStyleFactory()
```

Returns the current SynthStyleFactory.

**Returns:** SynthStyleFactory

- getStyle

```java
public static
SynthStyle
getStyle​(
JComponent
c,

Region
region)
```

Gets a SynthStyle for the specified region of the specified component.
This is not for general consumption, only custom UIs should call this
method.

**Parameters:** c

- JComponent to get the SynthStyle for
**Parameters:** region

- Identifies the region of the specified component
**Returns:** SynthStyle to use.

- updateStyles

```java
public static void updateStyles​(
Component
c)
```

Updates the style associated with

c

, and all its children.
This is a lighter version of

SwingUtilities.updateComponentTreeUI

.

**Parameters:** c

- Component to update style for.

- getRegion

```java
public static
Region
getRegion​(
JComponent
c)
```

Returns the Region for the JComponent

c

.

**Parameters:** c

- JComponent to fetch the Region for
**Returns:** Region corresponding to

c

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Creates the Synth look and feel

ComponentUI

for
the passed in

JComponent

.

**Parameters:** c

- JComponent to create the

ComponentUI

for
**Returns:** ComponentUI to use for

c

- load

```java
public void load​(
InputStream
input,

Class
<?> resourceBase)
throws
ParseException
```

Loads the set of

SynthStyle

s that will be used by
this

SynthLookAndFeel

.

resourceBase

is
used to resolve any path based resources, for example an

Image

would be resolved by

resourceBase.getResource(path)

. Refer to

Synth File Format

for more information.

**Parameters:** input

- InputStream to load from
**Parameters:** resourceBase

- used to resolve any images or other resources
**Throws:** ParseException

- if there is an error in parsing
**Throws:** IllegalArgumentException

- if input or resourceBase is

null

- load

```java
public void load​(
URL
url)
throws
ParseException
,

IOException
```

Loads the set of

SynthStyle

s that will be used by
this

SynthLookAndFeel

. Path based resources are resolved
relatively to the specified

URL

of the style. For example
an

Image

would be resolved by

new URL(synthFile, path)

. Refer to

Synth File Format

for more
information.

Whilst this API may be safe for loading local resources that are
delivered with a

LookAndFeel

or application, and so have an
equal level of trust with application code, using it to load from
remote resources, particularly any which may have a lower level of
trust, is strongly discouraged.
The alternative mechanisms to load styles from an

InputStream

load(InputStream, Class)

using resources co-located with the application or by providing a

SynthStyleFactory

to

setStyleFactory(SynthStyleFactory)

are preferred.

**Parameters:** url

- the

URL

to load the set of

SynthStyle

from
**Throws:** ParseException

- if there is an error in parsing
**Throws:** IllegalArgumentException

- if synthSet is

null
**Throws:** IOException

- if synthSet cannot be opened as an

InputStream
**Since:** 1.6

- initialize

```java
public void initialize()
```

Called by UIManager when this look and feel is installed.

**Overrides:** initialize

in class

LookAndFeel
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

LookAndFeel
**See Also:** LookAndFeel.initialize()

,

UIManager.setLookAndFeel(javax.swing.LookAndFeel)

- getDefaults

```java
public
UIDefaults
getDefaults()
```

Returns the defaults for this SynthLookAndFeel.

**Overrides:** getDefaults

in class

BasicLookAndFeel
**Returns:** Defaults table.
**See Also:** BasicLookAndFeel.initClassDefaults(javax.swing.UIDefaults)

,

BasicLookAndFeel.initSystemColorDefaults(javax.swing.UIDefaults)

,

BasicLookAndFeel.initComponentDefaults(javax.swing.UIDefaults)

- isSupportedLookAndFeel

```java
public boolean isSupportedLookAndFeel()
```

Returns true, SynthLookAndFeel is always supported.

**Specified by:** isSupportedLookAndFeel

in class

LookAndFeel
**Returns:** true.
**See Also:** UIManager.setLookAndFeel(javax.swing.LookAndFeel)

- isNativeLookAndFeel

```java
public boolean isNativeLookAndFeel()
```

Returns false, SynthLookAndFeel is not a native look and feel.

**Specified by:** isNativeLookAndFeel

in class

LookAndFeel
**Returns:** false

- getDescription

```java
public
String
getDescription()
```

Returns a textual description of SynthLookAndFeel.

**Specified by:** getDescription

in class

LookAndFeel
**Returns:** textual description of synth.

- getName

```java
public
String
getName()
```

Return a short string that identifies this look and feel.

**Specified by:** getName

in class

LookAndFeel
**Returns:** a short string identifying this look and feel.

- getID

```java
public
String
getID()
```

Return a string that identifies this look and feel.

**Specified by:** getID

in class

LookAndFeel
**Returns:** a short string identifying this look and feel.

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

**Returns:** whether or not the UIs should update their

SynthStyles

from the

SynthStyleFactory

when the ancestor changed.

- shouldUpdateStyleOnEvent

```java
protected boolean shouldUpdateStyleOnEvent​(
PropertyChangeEvent
ev)
```

Returns whether or not the UIs should update their styles when a
particular event occurs.

**Parameters:** ev

- a

PropertyChangeEvent
**Returns:** whether or not the UIs should update their styles
**Since:** 1.7

---

#### Method Detail

setStyleFactory

```java
public static void setStyleFactory​(
SynthStyleFactory
cache)
```

Sets the SynthStyleFactory that the UI classes provided by
synth will use to obtain a SynthStyle.

**Parameters:** cache

- SynthStyleFactory the UIs should use.

---

#### setStyleFactory

public static void setStyleFactory​(

SynthStyleFactory

cache)

Sets the SynthStyleFactory that the UI classes provided by
synth will use to obtain a SynthStyle.

getStyleFactory

```java
public static
SynthStyleFactory
getStyleFactory()
```

Returns the current SynthStyleFactory.

**Returns:** SynthStyleFactory

---

#### getStyleFactory

public static

SynthStyleFactory

getStyleFactory()

Returns the current SynthStyleFactory.

getStyle

```java
public static
SynthStyle
getStyle​(
JComponent
c,

Region
region)
```

Gets a SynthStyle for the specified region of the specified component.
This is not for general consumption, only custom UIs should call this
method.

**Parameters:** c

- JComponent to get the SynthStyle for
**Parameters:** region

- Identifies the region of the specified component
**Returns:** SynthStyle to use.

---

#### getStyle

public static

SynthStyle

getStyle​(

JComponent

c,

Region

region)

Gets a SynthStyle for the specified region of the specified component.
This is not for general consumption, only custom UIs should call this
method.

updateStyles

```java
public static void updateStyles​(
Component
c)
```

Updates the style associated with

c

, and all its children.
This is a lighter version of

SwingUtilities.updateComponentTreeUI

.

**Parameters:** c

- Component to update style for.

---

#### updateStyles

public static void updateStyles​(

Component

c)

Updates the style associated with

c

, and all its children.
This is a lighter version of

SwingUtilities.updateComponentTreeUI

.

getRegion

```java
public static
Region
getRegion​(
JComponent
c)
```

Returns the Region for the JComponent

c

.

**Parameters:** c

- JComponent to fetch the Region for
**Returns:** Region corresponding to

c

---

#### getRegion

public static

Region

getRegion​(

JComponent

c)

Returns the Region for the JComponent

c

.

createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Creates the Synth look and feel

ComponentUI

for
the passed in

JComponent

.

**Parameters:** c

- JComponent to create the

ComponentUI

for
**Returns:** ComponentUI to use for

c

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

c)

Creates the Synth look and feel

ComponentUI

for
the passed in

JComponent

.

load

```java
public void load​(
InputStream
input,

Class
<?> resourceBase)
throws
ParseException
```

Loads the set of

SynthStyle

s that will be used by
this

SynthLookAndFeel

.

resourceBase

is
used to resolve any path based resources, for example an

Image

would be resolved by

resourceBase.getResource(path)

. Refer to

Synth File Format

for more information.

**Parameters:** input

- InputStream to load from
**Parameters:** resourceBase

- used to resolve any images or other resources
**Throws:** ParseException

- if there is an error in parsing
**Throws:** IllegalArgumentException

- if input or resourceBase is

null

---

#### load

public void load​(

InputStream

input,

Class

<?> resourceBase)
throws

ParseException

Loads the set of

SynthStyle

s that will be used by
this

SynthLookAndFeel

.

resourceBase

is
used to resolve any path based resources, for example an

Image

would be resolved by

resourceBase.getResource(path)

. Refer to

Synth File Format

for more information.

load

```java
public void load​(
URL
url)
throws
ParseException
,

IOException
```

Loads the set of

SynthStyle

s that will be used by
this

SynthLookAndFeel

. Path based resources are resolved
relatively to the specified

URL

of the style. For example
an

Image

would be resolved by

new URL(synthFile, path)

. Refer to

Synth File Format

for more
information.

Whilst this API may be safe for loading local resources that are
delivered with a

LookAndFeel

or application, and so have an
equal level of trust with application code, using it to load from
remote resources, particularly any which may have a lower level of
trust, is strongly discouraged.
The alternative mechanisms to load styles from an

InputStream

load(InputStream, Class)

using resources co-located with the application or by providing a

SynthStyleFactory

to

setStyleFactory(SynthStyleFactory)

are preferred.

**Parameters:** url

- the

URL

to load the set of

SynthStyle

from
**Throws:** ParseException

- if there is an error in parsing
**Throws:** IllegalArgumentException

- if synthSet is

null
**Throws:** IOException

- if synthSet cannot be opened as an

InputStream
**Since:** 1.6

---

#### load

public void load​(

URL

url)
throws

ParseException

,

IOException

Loads the set of

SynthStyle

s that will be used by
this

SynthLookAndFeel

. Path based resources are resolved
relatively to the specified

URL

of the style. For example
an

Image

would be resolved by

new URL(synthFile, path)

. Refer to

Synth File Format

for more
information.

Whilst this API may be safe for loading local resources that are
delivered with a

LookAndFeel

or application, and so have an
equal level of trust with application code, using it to load from
remote resources, particularly any which may have a lower level of
trust, is strongly discouraged.
The alternative mechanisms to load styles from an

InputStream

load(InputStream, Class)

using resources co-located with the application or by providing a

SynthStyleFactory

to

setStyleFactory(SynthStyleFactory)

are preferred.

Whilst this API may be safe for loading local resources that are
delivered with a

LookAndFeel

or application, and so have an
equal level of trust with application code, using it to load from
remote resources, particularly any which may have a lower level of
trust, is strongly discouraged.
The alternative mechanisms to load styles from an

InputStream

load(InputStream, Class)

using resources co-located with the application or by providing a

SynthStyleFactory

to

setStyleFactory(SynthStyleFactory)

are preferred.

initialize

```java
public void initialize()
```

Called by UIManager when this look and feel is installed.

**Overrides:** initialize

in class

LookAndFeel
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

LookAndFeel
**See Also:** LookAndFeel.initialize()

,

UIManager.setLookAndFeel(javax.swing.LookAndFeel)

---

#### uninitialize

public void uninitialize()

Called by UIManager when this look and feel is uninstalled.

getDefaults

```java
public
UIDefaults
getDefaults()
```

Returns the defaults for this SynthLookAndFeel.

**Overrides:** getDefaults

in class

BasicLookAndFeel
**Returns:** Defaults table.
**See Also:** BasicLookAndFeel.initClassDefaults(javax.swing.UIDefaults)

,

BasicLookAndFeel.initSystemColorDefaults(javax.swing.UIDefaults)

,

BasicLookAndFeel.initComponentDefaults(javax.swing.UIDefaults)

---

#### getDefaults

public

UIDefaults

getDefaults()

Returns the defaults for this SynthLookAndFeel.

isSupportedLookAndFeel

```java
public boolean isSupportedLookAndFeel()
```

Returns true, SynthLookAndFeel is always supported.

**Specified by:** isSupportedLookAndFeel

in class

LookAndFeel
**Returns:** true.
**See Also:** UIManager.setLookAndFeel(javax.swing.LookAndFeel)

---

#### isSupportedLookAndFeel

public boolean isSupportedLookAndFeel()

Returns true, SynthLookAndFeel is always supported.

isNativeLookAndFeel

```java
public boolean isNativeLookAndFeel()
```

Returns false, SynthLookAndFeel is not a native look and feel.

**Specified by:** isNativeLookAndFeel

in class

LookAndFeel
**Returns:** false

---

#### isNativeLookAndFeel

public boolean isNativeLookAndFeel()

Returns false, SynthLookAndFeel is not a native look and feel.

getDescription

```java
public
String
getDescription()
```

Returns a textual description of SynthLookAndFeel.

**Specified by:** getDescription

in class

LookAndFeel
**Returns:** textual description of synth.

---

#### getDescription

public

String

getDescription()

Returns a textual description of SynthLookAndFeel.

getName

```java
public
String
getName()
```

Return a short string that identifies this look and feel.

**Specified by:** getName

in class

LookAndFeel
**Returns:** a short string identifying this look and feel.

---

#### getName

public

String

getName()

Return a short string that identifies this look and feel.

getID

```java
public
String
getID()
```

Return a string that identifies this look and feel.

**Specified by:** getID

in class

LookAndFeel
**Returns:** a short string identifying this look and feel.

---

#### getID

public

String

getID()

Return a string that identifies this look and feel.

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

**Returns:** whether or not the UIs should update their

SynthStyles

from the

SynthStyleFactory

when the ancestor changed.

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

---

